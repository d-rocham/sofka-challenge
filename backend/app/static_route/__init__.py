from flask import Blueprint
from flask.helpers import send_from_directory

static_resource_bp = Blueprint(
    "static_resource", __name__, static_folder="static", static_url_path=""
)


@static_resource_bp.route("/")
def serve_index():
    return send_from_directory(static_resource_bp.static_folder, "index.html")


@static_resource_bp.route("/static/<path>")
def serve_static(path):
    return send_from_directory(static_resource_bp.static_folder, path)
