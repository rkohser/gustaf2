from flask import Flask


gustafrest = Flask(__name__)

@gustafrest.route("/refresh")
def refresh():
    return "Hello World!"


if __name__ == "__main__":
    gustafrest.run()