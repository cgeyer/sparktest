from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello():
    username = request.args.get('user')
	if (str(username) != '')
	    return "Hello " + str(username)
	else
        return "Hello everyone!"


if __name__ == "__main__":
    app.run(debug=True,host='0.0.0.0')
