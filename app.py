# flask app
from flask import Flask

app = Flask(__name__)

def home():
    return "Hello, User!"
if __name__ == "__main__":
    app.run(debug=True)

#app.py
