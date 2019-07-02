import os
from wsgiref.simple_server import make_server

from pyramid.config import Configurator
from pyramid.response import Response
from pyramid.view import view_config

from htmldoom import doctype
from htmldoom import elements as e
from htmldoom import render


@view_config(route_name="home")
def home(request):
    """Index page - without renderer"""
    return Response(
        render(
            doctype("html"),
            e.html()(
                e.head()(e.title()("Pyramid template engine demo")),
                e.body()(
                    e.h1()("Home page"),
                    e.a(href="/jinja2")("Jinja2"),
                    e.br(),
                    e.a(href="/htmldoom")("htmldoom"),
                ),
            ),
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
        config.include("pyramid_debugtoolbar")

        # Jinja2 view
        config.include("pyramid_jinja2")
        config.add_route("hello_jinja2", "/jinja2")

        # htmldoo view
        config.include("pyramid_htmldoom")
        config.add_route("hello_htmldoom", "/htmldoom")

        config.add_settings(
            {
                "debugtoolbar.hosts": ["0.0.0.0/0"],
                "debugtoolbar.panels": ["performance", "renderings"],
            }
        )
        app = config.make_wsgi_app()
    server = make_server("0.0.0.0", int(os.environ.get("PORT", "8080")), app)
    server.serve_forever()
