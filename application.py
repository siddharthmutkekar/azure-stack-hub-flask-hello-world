from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return "Hello Sidd Updated World!"

if __name__ == '__main__':
    app.run()
