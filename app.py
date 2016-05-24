from flask import Flask
from flask import request

app = Flask(__name__)

@app.route("/")
def hello():
    username = request.args.get('user')
    if (username != None and str(username) != ''):
        return "Hello " + str(username)
    else:
        return "Hello everyone!"


if __name__ == "__main__":
    #app.run(debug=True,host='0.0.0.0')
