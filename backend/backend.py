import os

from app import create_app

app = create_app(os.getenv("FLASK_CONFIG") or "default")


@app.shell_context_processor
def make_shell_context_processor():
    """Provides shell access to any variable when executing `flask shell`

    Args:
        None

    Returns:
        `dictionary` containing any data to be used inside the shell

    """
    return dict(config=app.config)
