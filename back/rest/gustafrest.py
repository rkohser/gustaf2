from flask import Flask
from fs.gustaffs import refresh as fs_refresh


gustafrest = Flask(__name__)

@gustafrest.route("/refresh")
def refresh():

    fs_refresh.delay()

    return "Hello World!"


if __name__ == "__main__":
    gustafrest.run(port=5000, debug=True)