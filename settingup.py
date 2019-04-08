from flask import Flask
app = Flask(Share)

@app.route('/')
def hello_world():
    return 'Working!!'