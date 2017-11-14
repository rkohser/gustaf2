from flask import Flask, request
from fs.gustaffs import refresh as fs_refresh
from flask.helpers import send_file

from rest.playlistgenerator import PlaylistGenerator


gustafrest = Flask(__name__)

@gustafrest.route("/refresh")
def refresh():

    fs_refresh.delay()

    return "Hello World!"

@gustafrest.route("/playlist")
def playlist():
    
    show = request.args.get('show')
    
    pg = PlaylistGenerator(show)
    pg.generate();
    
    return send_file(r'E:\workspace\gustaf2\xspfplaylist.xspf', as_attachment=True)


if __name__ == "__main__":
    gustafrest.run(port=5000, debug=True)