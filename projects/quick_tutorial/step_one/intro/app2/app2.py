from wsgiref.simple_server import make_server
from pyramid.config import Configurator
from pyramid.view import view_config


@view_config(
    route_name="home",
    renderer="json"
)
def home(request):
    return {"a": 1, "b": 2}


if __name__ == '__main__':
    HOST = '0.0.0.0'
    PORT = 8080

    with Configurator() as config:
        config.add_route('home', '/')
        config.scan()
        app = config.make_wsgi_app()
    server = make_server(HOST, PORT, app)
    print(f'Starting server at {HOST}:{PORT}')
    server.serve_forever()
