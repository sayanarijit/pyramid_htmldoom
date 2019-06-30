from htmldoom import base as b
from htmldoom import elements as e
from htmldoom import render as _render
from htmldoom import renders

doctype = _render(b.doctype("html"))


@renders(e.title()("{doctitle}"))
def render_title(doctitle: str) -> dict:
    return {"doctitle": doctitle}


@renders(e.body()("{content}"))
def render_body(data: dict) -> None:
    raise NotImplementedError("You are trying to render a layout.")


@renders("{doctype}", e.html()(e.head()("{title}"), "{body}"))
def render_document(
    data: dict,
    title_renderer: callable = render_title,
    body_renderer: callable = render_body,
) -> dict:
    return {
        "doctype": doctype,
        "title": title_renderer(doctitle=data["data"]),
        "body": body_renderer(data=data),
    }


def render(data: dict) -> str:
    return render_document(data=data)
