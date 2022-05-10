import requests
from flask import Flask
from flask import jsonify
app = Flask(__name__)


@app.route('/')
def hello():
    """Return a friendly HTTP greeting."""
    print("I am inside hello world")
    return 'Hello World! I can make change at route: /change'

@app.route('/pong')
def pong():
    return 'pong'

@app.route("/ping/<ip>")
def ping(ip):
    return requests.get(url=f"{ip}:8081/pong/").json()

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080, debug=True)
