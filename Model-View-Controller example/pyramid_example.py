from wsgiref.simple_server import make_server
from pyramid.config import Configurator
from pyramid.response import Response
from pyramid.static import static_view


if __name__=='__main__':
    config = Configurator()
    config.add_route('index', '/')
    config.scan(package='views')
    config.add_static_view(name='static', path='static')
    app = config.make_wsgi_app()
    server = make_server('0.0.0.0', 8080, app)
    server.serve_forever()

