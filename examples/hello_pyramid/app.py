from wsgiref.simple_server import make_server

from htmldoom import elements as e
from pyramid.config import Configurator
from pyramid.response import Response
from pyramid.view import view_config


@view_config(route_name="home")
def home(request):
    """Index page - without renderer"""
    return Response(
        str(
            e.HTML()(
                e.Head()(e.Title()("Pyramid template engine demo")),
                e.Body()(
                    e.H1()("Home page"),
                    e.A(href="/jinja2")("Jinja2"),
                    e.Br(),
                    e.A(href="/htmldoom")("htmldoom"),
                ),
            )
        )
    )


@view_config(route_name="hello_jinja2", renderer="templates/hello.jinja2")
def hello_jinja2_view(request):
    """Jinja2 rendered view"""
    return {"data": "Hello Jinja2"}


@view_config(route_name="hello_htmldoom", renderer="templates.hello.py")
def hello_htmldoom_view(request):
    """htmldoom rendered view"""
    return {"data": "Hello htmldoom"}


if __name__ == "__main__":
    with Configurator() as config:
        config.scan()
        config.add_route("home", "/")

        # Jinja2 view
        config.include("pyramid_jinja2")
        config.add_route("hello_jinja2", "/jinja2")

        # htmldoo view
        config.include("pyramid_htmldoom")
        config.add_route("hello_htmldoom", "/htmldoom")

        app = config.make_wsgi_app()
    server = make_server("localhost", 8080, app)
    server.serve_forever()
