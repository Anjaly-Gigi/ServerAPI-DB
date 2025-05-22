# Implementation of Server API with Database

## Technologies:
- Flask (Python)
- MySQL (via XAMPP)
- HTML, CSS, JavaScript
- RESTful API

### Instruction
* Install XAMPP and start **Apache** and **MySQL** in the control panel.
  
* Go to `http://localhost/phpmyadmin` and create a new database `user_db`
  
* Run the create and insert sql query to create a table and insert values to the tables.
  
* Installed flask and mysql-connector-python using pip to handle server logic and connect to the 
  MySQL database.
           pip install flask mysql-connector-python

* Create a Python Flask Backend which initialize a Flask app. This Flask app connect to a MySql 
  database and set up API routes for login and user data retrieval.
  
   - `Login API (/login)` accepts POST requests with JSON (username and password) Verifies 
     credentials using an SQL query and returns user data if successful otherwise, returns an 
     error.
   - `User Data API (/userdata)` accepts GET requests with username as a query parameter and 
     fetches and returns the user's details (username, email, full name).
     
* Created `index.html` (login page) and `home.html` (home page) using basic HTML structure and 
  forms.
    
* Wrote a pure CSS file to style the login and home pages.
  
* Used JavaScript (Fetch API) in `index.html` to send login credentials to the Flask API and 
  handle responses and added a button in `home.html` that uses JavaScript to call the API and 
  display user data after login.
  
* Ran the Flask app on localhost and tested the full login flow and data retrieval functionality.
  

  
  





