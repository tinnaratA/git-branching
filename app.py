from flask import Flask
app = Flask(__name__)


@app.route('/')
def hello():
    return "Greeting Message Git-Branching by Tinnarat.A!"

@app.route('/version/<v>', methods=['GET'])
def version(v):
    return str.format("App.Version={0}",v)

@app.route('/login/<username>', methods=['GET'])
def login(username):
    print(username)

if __name__ == '__main__':
    app.run()
