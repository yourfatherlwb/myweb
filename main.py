from flask import Flask

app=Flask(__name__)

@app.route("/")
def home():
    return "hello"

app.run(host="localhost",
port=8080)
