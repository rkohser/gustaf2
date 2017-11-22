from flask import Flask, request, Response
from fs.gustaffs import refresh as fs_refresh

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
    xspf = pg.generate()
    
    return Response(xspf,
                    mimetype='text/xspf',
                    headers={
                        "Content-disposition":"attachement;filename=playlist.xspf"
                    })


if __name__ == "__main__":
    gustafrest.run(port=5000, debug=True)