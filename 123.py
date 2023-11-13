from flask import Flask, Response , request
from flask_cors import CORS




app = Flask(__name__)
CORS(app)

# /method?argumen1=value1&argumen2=value2

users = []

@app.route("/")
def main():
    return "commands: /auth, /logout, /send, /getall"

@app.route("/auth")
def auth():  
    x = request.args.get('name')
    print (x)
    return  'xxxxxxxxxxx'

@app.route("/logout")
def logout():
    return "ОК"

@app.route("/send")
def send():
    return "ОК"

@app.route("/getall")
def getall():
    x = [
        {'name': 'Max', 'message': '', 'timestamp':123},
    ]
    return "Hello, World!"


if __name__ == "__main__":
    print('RABOTAEM')
    app.run(debug=True)