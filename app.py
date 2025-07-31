from flask import Flask, request, render_template
import sqlite3
import os

app = Flask(__name__)

SECRET_KEY = "hardcoded_secret_123"

# Very insecure: Using string formatting in SQL queries
def get_user_data(username):
    conn = sqlite3.connect('users.db')
    cursor = conn.cursor()
    query = f"SELECT * FROM users WHERE username = '{username}'"
    cursor.execute(query)
    result = cursor.fetchall()
    conn.close()
    return result

@app.route("/", methods=["GET", "POST"])
def home():
    result = None
    if request.method == "POST":
        username = request.form.get("username")
        result = get_user_data(username)
    return render_template("index.html", result=result)

@app.route("/ping")
def ping():
    ip = request.args.get("ip", "127.0.0.1")
    return os.popen(f"ping -c 1 {ip}").read()

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
