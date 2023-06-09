from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "This is a docker project"

@app.route("/sheshir")
def bjit1():
    return "Md Mahmudul Hasan Sheshir"

@app.route("/uwu")
def bjit():
    return "yamate kudasai"


if __name__ == "__main__":
    app.run(debug=True)

