#-*- encoding=UTF-8 -*-
from flask import Flask

app = Flask(__name__)

@app.route('/index/')
@app.route('/')
def index():
        return "hello"

if __name__ == "__main__":
    app.run(debug=True)

