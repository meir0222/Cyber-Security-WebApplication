from django.shortcuts import render,redirect
from django.urls import reverse_lazy
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from django.views.generic.edit import CreateView
from .forms import UserRegistrationForm,LoginForm
from django.core.mail import send_mail
from django.core.mail import EmailMultiAlternatives
from django.template.loader import get_template
from .forms import SetPasswordForm
from django.http import HttpRequest,HttpResponse,JsonResponse
from django.template.loader import render_to_string
from django.contrib.sites.shortcuts import get_current_site
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.utils.encoding import force_bytes, force_str
from .tokens import account_activation_token
from users.models import Customer
from users.forms import CustomerForm,ValidationForm,User
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.decorators import login_required
from django.db import connection
from django.contrib import messages
from django.contrib.auth.hashers import make_password
from django.contrib.auth import authenticate, login
import datetime
import sqlite3
import hashlib
import random
from django.core.mail import EmailMessage
from django.conf import settings
from django.utils.crypto import get_random_string




# Create your views here.
def is_ajax():
     return HttpRequest.headers.get('x-requested-with') == 'XMLHttpRequest' 

def home(request):
    return render(request,"users/home.html")

#protected signup function
# class SignUp(CreateView):
#     request = HttpRequest
#     form_class = UserRegistrationForm
#     success_url = reverse_lazy("login")
#     template_name = "registration/signup.html"

#protected signup function
def SignUp(request):
    if request.method=="POST":
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            # taking care of input sanitizations.
            username = form.cleaned_data["username"]
            first_name = form.cleaned_data["first_name"]
            last_name = form.cleaned_data["last_name"]
            email = form.cleaned_data["email"]
            password =form.cleaned_data["password1"]
            hashed_pass = make_password(password)
            date_joined = datetime.datetime.now()
            # user = form_class.save()
            # Direct SQL Queries         
            cursor = connection.cursor()
            query = "INSERT INTO auth_user (username, first_name, last_name,email,password,date_joined,is_superuser,is_staff,is_active,last_login) VALUES ('%s', '%s', '%s','%s','%s','%s','0','0','1',NULL)" % (
                username, first_name,last_name,email,hashed_pass,date_joined)           
            cursor.execute(query)           
            return redirect("users:home")

        messages.error(request, "Unsuccessful registration. Invalid information.")    
        # success_url = reverse_lazy("login")
        # template_name = "registration/signup.html"
    form = UserRegistrationForm()
    return render (request=request, template_name="registration/signup.html", context={"register_form":form})    


#sql injection vulnerable register function 
# def SignUp(request):
#     if request.method=="POST":
#         form = UserRegistrationForm(request.POST)
#         username = request.POST['username']
#         first_name = request.POST['first_name']
#         last_name = request.POST['last_name']
#         email = request.POST['email']
#         password =request.POST['password1']
#         hashed_pass = make_password(password)
#         date_joined = datetime.datetime.now()
#         # user = form_class.save()
#         # Direct SQL Queries - the wrong way        
#         db = sqlite3.connect('db.sqlite3')
#         cursor = db.cursor()
#         query = "INSERT INTO auth_user (username, first_name, last_name,email,password,date_joined,is_superuser,is_staff,is_active,last_login) VALUES ('%s', '%s', '%s','%s','%s','%s','0','0','1',NULL)" % (
#             username, first_name,last_name,email,hashed_pass,date_joined)           
#         cursor.executescript(query)           
#         return redirect("users:home")
#     form = UserRegistrationForm()
#     return render (request=request, template_name="registration/signup.html", context={"register_form":form})  


#  sql injection vulnerable login function ---> '; DELETE FROM users_customer; --
# def Login(request):         
#     if request.method == "POST":
#         form = AuthenticationForm(request, data=request.POST)
#         # if form.is_valid():
#         # username = form.cleaned_data.get('username')
#         # password = form.cleaned_data.get('password')
#         username =  form.request.POST.get('username')
#         password =  form.request.POST.get('password')
#         searchName = request.POST['username']
#         searchPass = request.POST['password']
#         print(searchName)
#         db = sqlite3.connect('db.sqlite3')
#         cursor = db.cursor()
#         query = "SELECT * FROM auth_user WHERE username='%s' AND password='%s';" % (searchName,searchPass)
#         cursor.executescript(query)
#         user = authenticate(request,username=username, password=password)
#         if user is not None:
#             login(request, user)
#             return redirect("/")
#         else:
#                 messages.error(request,"Invalid username or password.")
#     else:
#         messages.error(request,"Invalid username or password.")
#     form = AuthenticationForm()
#     return render(request=request, template_name="registration/login.html", context={"login_form":form})

#protected Login form
def Login(request):         
    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            # sanitization
            username= form.cleaned_data.get('username')
            password= form.cleaned_data.get('password')
            user = authenticate(request,username=username, password=password)
            if user is not None:
                login(request,user)
                return redirect("/")
            else:
                    messages.error(request,"Invalid username or password.")
        else:
            messages.error(request,"Invalid username or password.")
    form = AuthenticationForm()
    return render(request=request, template_name="registration/login.html", context={"login_form":form})

def send_email(request):
    if request.method=="POST":
        # get email address
        email_received = request.POST.get('email')
        original_number = random.randint(1, 1000000)
        # hash the  random number
        hashed_number = hashlib.sha1(str(original_number).encode()).hexdigest()
        # send the hashed number to the email address
        send_mail(
            'Password Reset Request - Validation Code',
            f'Please use this code to enter reset page: {hashed_number}',
            settings.EMAIL_HOST_USER,
            [email_received],
            fail_silently=False,
        )
        # store the original number for validation
        request.session['validation_number'] = hashed_number
        return redirect('users:validate_email')
    return render(request, 'users/email_form.html')

def validate_email(request):
    if request.method == 'POST':
        form = ValidationForm(request.POST)
        if form.is_valid():
            # Get the user input
            user_input = form.cleaned_data['validation_number']
            # Get the original hash from the session (assuming it was stored there after sending the email)
            original_hash = request.session.get('validation_number')
            # Compare the user input with the original hash
            if user_input == original_hash:
                print("Correct valid code - proceeding to password reset page.")
                return redirect('password_reset')
            else:
                print("wrong valid number - try again.")
                return render(request, 'users/validation.html', {'form': form})
    else:
        form = ValidationForm()
    return render(request, 'users/validation.html', {'form': form})

def password_change(request):
    user = request.user
    form = SetPasswordForm(user)
    return render(request, 'users/password_reset_confirm.html', {'form': form})

@login_required
def customers(request):
    if request.method == "POST":
        cust_id = request.POST.get("cust_id")
        cust_name = request.POST.get("cust_name")
        cust_email = request.POST.get("cust_email")
        cust_contact = request.POST.get("cust_contact")

        # Saving to DB using Django ORM - the best way
        Customer.objects.create(cust_id=cust_id, cust_name=cust_name, cust_email=cust_email
        ,cust_contact=cust_contact)

        # # Direct SQL Queries - wrong way
        # db = sqlite3.connect('db.sqlite3')
        # cursor = db.cursor()
        # query = "INSERT INTO users_customer (cust_id, cust_name, cust_email, cust_contact) VALUES ('%s', '%s', '%s', '%s')" % (cust_id, cust_name, cust_email, cust_contact)
        # cursor.executescript(query)

        return redirect("users:customers")
    else:
        # Fetch all customers  using Django ORM
        customers = Customer.objects.all()
        return render(request, 'users/customers.html',
        {"customers":customers})


@login_required
@csrf_exempt
def search_customers(request):
    ajax_check = request.headers.get('x-requested-with') == 'XMLHttpRequest' 
    if ajax_check:
        search_term = request.POST.get('searchTerm')
        search_term = "%"+search_term+"%"
        # Searching Customer using Django ORM - best way
        customers = Customer.objects.filter(cust_name__icontains=search_term)
        
        #  raw() / direct SQL queries - wrong way
        # db = sqlite3.connect('db.sqlite3')
        # cursor = db.cursor()
        # query = "SELECT * FROM users_customer WHERE cust_name LIKE '%s';" % search_term        
        # cursor.executescript(query) 
        # customers = Customer.objects.raw(query)

        # raw() - correct way
        # customers = Customer.objects.raw('SELECT * FROM users_customer WHERE cust_name LIKE %s;',[search_term])

        # extra() - wrong way
        # customers = Customer.objects.extra(where=["cust_name LIKE '%s'" % search_term])

        # extra() - correct way params
        # customers = Customer.objects.extra(where=['cust_name LIKE %s'], params=[search_term])

        # return HttpResponse(html)
        return render(request,'users/search_customers.html',{'customers':customers})






