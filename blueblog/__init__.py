import os
import click

from flask import Flask
from flask import render_template, request

from settings import config
from blueprints.blog import blog_bp
from blueprints.admin import admin_bp
from blueprints.auth import auth_bp
from .extensions import db, csrf, ckeditor, bootstrap, debug_toolbar, moment, login_manager, migrate


base_dir = os.path.abspath(os.path.dirname(os.path.dirname(__file__)))


def create_app(config_name=None):
    if config_name is None:
        config_name = os.getenv("FLASK_APP", "development")

    app = Flask("blueblog")
    app.config.from_object(config[config_name])

    app.register_blueprint(blog_bp)
    app.register_blueprint(admin_bp, url_prefix="/admin")
    app.register_blueprint(auth_bp, url_prefix="/auth")

    db.init_app(app)
    csrf.init_app(app)
    ckeditor.init_app(app)
    bootstrap.init_app(app)
    debug_toolbar.init_app(app)
    moment.init_app(app)
    login_manager.init_app(app)
    migrate.init_app(app)
