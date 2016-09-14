from flask import Flask


def load_config(app, config=None):
    config = config or 'config'
    app.config.from_object(config)


def load_blueprints(app):
    from core import core as core_bp
    app.register_blueprint(core_bp, url_prefix='/')


def create_app(config=None):
    app = Flask('texaco')
    load_config(app, config)
    load_blueprints(app)
    return app
