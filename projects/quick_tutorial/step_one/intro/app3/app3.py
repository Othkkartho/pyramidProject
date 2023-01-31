from wsgiref.simple_server import make_server
from pyramid.config import Configurator
from pyramid.view import view_config


@view_config(
    route_name='hello',
    renderer="/templates/home.jinja2"
)
def home(request):
    return {"greet": 'welcome', 'name': 'Tut Ankh Amun'}


if __name__ == '__main__':
    HOST = '0.0.0.0'
    PORT = 8080

    with Configurator() as config:
        config.include('pyramid_jinja2')
        config.include('pyramid_debugtoolbar')
        config.add_static_view(name='static', path='static')
        config.add_route('hello', '/')
        config.scan()
        app = config.make_wsgi_app()
    server = make_server(HOST, PORT, app)
    print(f'Starting server at {HOST}:{PORT}')
    server.serve_forever()
