from htmldoom import elements as e

from .layout import Layout


class Template(Layout):
    """Hello view renderer"""

    @property
    def content(self):
        return e.Div()(
            e.H3()(self["data"]),
            e.A(href="/")("Home"),
            e.Br(),
            e.A(href="/jinja2")("Jinja2"),
        )
