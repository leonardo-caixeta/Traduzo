from flask import Flask

from controllers.admin_controller import admin_controller
from src.controllers.language_controller import language_controller
from src.controllers.history_controller import history_controller

from os import environ
from waitress import serve


app = Flask(__name__)
app.template_folder = "views/templates"
app.static_folder = "views/static"

app.register_blueprint(admin_controller, url_prefix="/admin")
app.register_blueprint(language_controller, url_prefix="/")
app.register_blueprint(history_controller, url_prefix="/history")


def start_server(host="0.0.0.0", port=8000):
    if environ.get("FLASK_ENV") != "production":
        return app.run(debug=True, host=host, port=port)
    else:
        serve(app, host=host, port=port)


if __name__ == "__main__":
    start_server()
