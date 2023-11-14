from flask import Flask, Response , request, render_template 
from flask_cors import CORS
import json

app = Flask(__name__,static_url_path='/static')

CORS(app)

# /method?argumen1=value1&argumen2=value2

users = []

@app.route("/")
def main():
    return render_template ('index.html')

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
        {'name': 'Max', 'text': 'gggggg', 'timestamp':123},  {'name': 'Maxggg', 'text': 'g234234ggggg', 'timestamp':12443},
    ]
    return json.dumps(x)


if __name__ == "__main__":
    print('RABOTAEM')
    app.run(debug=True)






