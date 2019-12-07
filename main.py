from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def home():
    return render_template("home.html")


@app.route('/user/<nome>')
def user(nome):
	return '<h1>Hello, {}!</h1>'.format(nome)


if __name__ == "__main__":
    app.run(debug=True)