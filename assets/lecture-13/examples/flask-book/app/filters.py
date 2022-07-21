from . import app

from markdown import markdown


@app.template_filter('markdown')
def render_markdown(value):
    return markdown(value)
