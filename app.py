from flask import Flask
app = Flask(__name__)

def hello():
    return "Hello Docker!"

if __name__ == '__main__':
    app.run(host='0.0.0.0')