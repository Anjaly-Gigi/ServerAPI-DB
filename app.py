from flask import Flask, request, jsonify, render_template
import mysql.connector

app = Flask(__name__)

conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="user_db"
)
cursor = conn.cursor(dictionary=True)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/home")
def home():
    return render_template("home.html")

@app.route("/login", methods=["POST"])
def login():
    data = request.get_json()
    username = data.get("username")
    password = data.get("password")

    query = "SELECT username, email, full_name FROM users WHERE username=%s AND password=%s"
    cursor.execute(query, (username, password))
    user = cursor.fetchone()

    if user:
        return jsonify({"status": "success", "user": user})
    else:
        return jsonify({"status": "fail", "message": "Invalid credentials"})

@app.route("/userdata", methods=["GET"])
def get_user_data():
    username = request.args.get("username")
    cursor.execute("SELECT username, email, first_name, last_name, age FROM users WHERE username = %s", (username,))
    user = cursor.fetchone()
    if user:
        return jsonify({"status": "success", "user": user})
    else:
        return jsonify({"status": "fail", "message": "User not found"})

if __name__ == "__main__":
    app.run(debug=True)
