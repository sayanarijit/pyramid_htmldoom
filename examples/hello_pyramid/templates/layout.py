from htmldoom import elements as e
from htmldoom.layouts import BaseLayout


class Layout(BaseLayout):
    @property
    def title(self):
        return e.Title()(self["data"])

    @property
    def body(self):
        return e.Body()(e.Div(**{"id": "main"})(self.content))

    @property
    def content(self):
        """To be implemented by renderers."""
        raise NotImplementedError()
