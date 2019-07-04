pyramid_htmldoom
================
[htmldoom](https://github.com/sayanarijit/htmldoom) rendering library plugin for Pyramid

Checkout the **[live demo](https://htmldoom-pyramid-example.herokuapp.com/)** with **[performance debugging](http://htmldoom-pyramid-example.herokuapp.com/_debug_toolbar/)**

Usage
----
### Install

```bash
pip install pyramid_htmldoom
```

### Plug into Pyramid

#### app.py

```python
from wsgiref.simple_server import make_server
from pyramid.config import Configurator
from pyramid.response import Response
from pyramid.view import view_config

@view_config(route_name="hello_htmldoom", renderer="templates.hello.py")
def hello_htmldoom_view(request):
    """htmldoom rendered view"""
    return {"data": "Hello htmldoom"}


if __name__ == "__main__":
    with Configurator() as config:
        config.scan()

        config.include("pyramid_htmldoom")
        config.add_route("hello_htmldoom", "/")

        app = config.make_wsgi_app()
    server = make_server("localhost", 8080, app)
    server.serve_forever()
```

#### templates/hello.py

```python
from htmldoom import elements as e
from htmldoom import renders

from .layout import render_document


@renders(
    e.body()(
        e.h3()("{contents}"),
        e.a(href="/")("Home"),
    )
)
def render_body(data):
    return {"contents": data["data"]}


def render(data):
    return render_document(data, body_renderer=render_body)
```

#### templates/layout.py

```python
from htmldoom import base as b
from htmldoom import elements as e
from htmldoom import render as _render
from htmldoom import renders

doctype = _render(b.doctype("html"))


@renders(e.title()("{doctitle}"))
def render_title(doctitle):
    return {"doctitle": doctitle}


@renders(e.body()("{content}"))
def render_body(data):
    raise NotImplementedError("You are trying to render a layout.")


@renders("{doctype}", e.html()(e.head()("{title}"), "{body}"))
def render_document(
    data,
    title_renderer=render_title,
    body_renderer=render_body,
):
    return {
        "doctype": doctype,
        "title": title_renderer(doctitle=data["data"]),
        "body": body_renderer(data=data),
    }


def render(data):
    return render_document(data=data)
```

Examples
--------
[Find demo and examples here](https://github.com/sayanarijit/pyramid_htmldoom/blob/master/examples)

### Deploy examples on heroku:

```bash
git push heroku $(git subtree split --prefix examples/2_hackernews master):master
```
