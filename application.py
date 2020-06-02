import bottle
from bottle import route, run, Response


app = bottle.default_app()

@route('/')
def index():
    """Returns standard text response."""
    return Response("my bottle app is up and running!")

if __name__ == "__main__":
    run(host="0.0.0.0", port=5000, debug=False, reloader=True)

