from wsgiref.simple_server import make_server
from pyramid.config import Configurator
from pyramid.response import Response


def hello_world(request):
    return Response('Hello World!')


if __name__ == '__main__':
    HOST = '0.0.0.0'
    PORT = 8080

    with Configurator() as config:
        config.add_route('hello', '/')
        config.add_view(hello_world, route_name='hello')
        app = config.make_wsgi_app()
    server = make_server(HOST, PORT, app)
    print(f'Starting server at {HOST}:{PORT}')
    server.serve_forever()
