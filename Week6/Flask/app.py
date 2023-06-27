from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "Hello World"

@app.route("/hello1")
def hello_world1():
    return "Hello World1"

@app.route("/hello2")
def hello_world2():
    return "Hello World2"

if __name__ == "__main__":
    app.run(host="0.0.0.0")