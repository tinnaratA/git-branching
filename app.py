from flask import Flask
app = Flask(__name__)


@app.route('/')
def hello():
    return "Hello World!"

@app.route('/version')
def version():
    return "App.Version=1.0"

if __name__ == '__main__':
    app.run()
