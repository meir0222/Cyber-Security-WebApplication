# Cyber Security WebApplication
This project focuses on creating a robust authentication system using the Django framework. The objective is to develop a secure web application by deliberately introducing vulnerabilities, such as SQL injection and cross-site scripting (XSS), and then applying secure development principles to mitigate these vulnerabilities.

## Features

* Authentication System: The application includes a secure authentication system that allows users to register, log in, and manage their accounts.
* Deliberate Vulnerability Implementation: The web application deliberately introduces vulnerabilities, such as SQL injection and cross-site scripting (XSS), to simulate real-world security risks and demonstrate the importance of secure development.
* Secure Development Practices: The project emphasizes the application of secure development principles to mitigate vulnerabilities. It includes input validation, output encoding, secure session management, and the use of secure hashing algorithms(HMAC) with salt to protect user passwords.
* TLS 1.2 Implementation: The application is configured to use TLS 1.2 to enable HTTPS on localhost.

## Getting Started
Prerequisites

  * Python 3.x
  * Django

1.Installation

    Clone the repository:
    git clone https://github.com/meir0222/Cyber-Security-WebApplication.git

2.Navigate to the project directory:

    cd Cyber-Security-WebApplication
    Install the dependencies:
    pip install -r requirements.txt

3.Configuration

    Set up the database:

        Configure the database settings in the settings.py file, such as database type, host, port, username, and password.

        Migrate the database schema:
        python manage.py migrate

4.Run the development server:

    to run http server:
    python manage.py runserver

    or to run https server:
    python manage.py runserver_plus --cert-file cert.pem --key-file key.pem
    
    Access the application in your web browser at https://localhost:8000.

Usage:

    Create a new user account by navigating to the registration page and providing the required information.
    Log in to the system using your credentials.
    Explore the application and access different features to test the secure development practices and vulnerability mitigation.
    Note: Some files have been removed from the repository for safety purposes, so the code may not fully work as expected.

## Acknowledgments

This project was developed to showcase the importance of secure development practices in web applications. It combines authentication, deliberate vulnerability implementation, and secure development principles to provide a comprehensive learning experience in the field of cyber security.
