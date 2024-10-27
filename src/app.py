from flask import Flask

app = Flask(__name__)

@app.post("/user")
def hello_world():
    return {
        "status":"200 OK",
    }