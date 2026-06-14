import nox

@nox.session
def docs(session):
    """Build the documentation site as static HTML."""
    session.install("-r", "docs/requirements.txt")
    with session.chdir("docs"):
        session.run("myst", "build", "--html", "--execute")


@nox.session(name="docs-live")
def docs_live(session):
    """Serve the documentation locally with live reload."""
    session.install("-r", "docs/requirements.txt")
    with session.chdir("docs"):
        session.run("myst", "start", "--execute")
