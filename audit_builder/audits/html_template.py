"""html_template.py
--
Generate HTML templates for the audit reports.
"""
from audit_builder.utils import getpath

from datetime import datetime
from htmlBuilder import tags
from htmlBuilder.attributes import Id, Class, Style, Rel, Href, Src, Type
from htmlBuilder.tags import Link
from weasyprint import HTML, CSS


def html_head():
    """Construct the HTML head section to link styles, etc."""
    styles_path = getpath.styles

    return tags.Head(
        [],
        Link([Rel("preconnect"), Href("https://fonts.gstatic.com")]),
        Link([Rel("preconnect"), Href("https://fonts.googleapis.com")]),
        Link(
            [
                Rel("stylesheet"),
                Href(
                    "https://fonts.googleapis.com/css2?family=Share+Tech&display=swap"
                ),
            ]
        ),
    )


def logo_block(audit_data: str = None) -> str:
    """Generate the title page for the TestMachine audit."""
    logo = tags.Img([Class("logo"), Src(f"file://{getpath.images}/logo.png")])
    title = tags.H1([Class("title-font")], "TestMachine.ai")
    return tags.Section([Class("title-section")], logo, title)


def version_and_timestamp():
    """Generate the version and timestamp of the audit."""
    timestamp = datetime.now().strftime("%Y-%m-%d | %I:%M%p")
    audit_title = tags.H1([Class("medium-font tech-font")], "Audit Report")
    time_line = tags.H1([Class("version-font")], timestamp)
    return tags.Section([Class("stack")], audit_title, time_line)


def assemble_report() -> str:
    """Assemble the whole report now."""
    with open(getpath.styles, "r") as f:
        styles = f.read()
    html = tags.Html(
        [], html_head(), tags.Main([], logo_block(), version_and_timestamp())
    )
    return html.render(pretty=True)


if __name__ == "__main__":
    html_string = assemble_report()
    html = HTML(string=html_string)
    css = CSS(url=f"file://{getpath.styles}")
    html.write_pdf("test.pdf", stylesheets=[css])
    with open("test.html", "w") as f:
        f.write(html_string)
