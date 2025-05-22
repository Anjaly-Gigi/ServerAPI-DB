# Implementation of Server API with Database

## Technologies:
- Flask (Python)
- MySQL (via XAMPP)
- HTML, CSS, JavaScript
- RESTful API

### Instruction
* Install XAMPP and start **Apache** and **MySQL** in the control panel  
* Go to `http://localhost/phpmyadmin` and create a new database `user_db`  
* Run the create and insert sql query to create a table and insert values to the tables.
* Create a Python Flask Backend which initialize a Flask app. This Flask app connect to a MySql database and set up API routes for login and user data retrieval.
   - Login API (/login) accepts POST requests with JSON (username and password) Verifies 
     credentials using an SQL query and returns user data if successful otherwise, returns an 
     error.
   - User Data API (/userdata) accepts GET requests with username as a query parameter and 
     fetches and returns the user's details (username, email, full name)
  
  





