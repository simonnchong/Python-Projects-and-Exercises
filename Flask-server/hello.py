from flask import Flask
app = Flask(__name__)

@app.route('/') #http://127.0.0.1:5000
def hello_world():
    return 'Hello, World!'

@app.route('/second_page') #http://127.0.0.1:5000/second_page
def hello_simon():
    return 'Hello Simon!'

if __name__ == "__main__":
    app.run()