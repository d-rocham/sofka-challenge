import os

from app import create_app, db
from app.models import Answers, Level, Questions

app = create_app(os.getenv("FLASK_CONFIG") or "default")


@app.shell_context_processor
def make_shell_context_processor():
    """Provides shell access to any variable when executing `flask shell`

    Args:
        None

    Returns:
        `dictionary` containing any data to be used inside the shell

    """
    return dict(
        config=app.config,
        Answers=Answers,
        Level=Level,
        Questions=Questions,
        db=db,
    )


@app.cli.command()
def test():
    import unittest

    tests = unittest.TestLoader().discover("tests")
    unittest.TextTestRunner(verbosity=2).run(tests)
