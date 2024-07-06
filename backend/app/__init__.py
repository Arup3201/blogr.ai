from flask import Flask
from flask_migrate import Migrate
from flask_cors import CORS
from instance.config import DevelopmentConfig, ProductionConfig
import os

def create_app(config_name=None):
    app = Flask(__name__, instance_relative_config=True)

    if config_name is None:
        config_name = os.environ.get('FLASK_ENV') or 'development'
    
    if config_name == 'development':
        app.config.from_object(DevelopmentConfig)
    else:
        app.config.from_object(ProductionConfig)

    # Build the database model
    from app.models import db
    db.init_app(app)
    with app.app_context():
        db.create_all()
    
    CORS(app)
    
    # Create migration for database in case modification in the database
    Migrate(app, db, compare_type=True)
    
    # Authentication and Blog blueprints
    from app.views import auth_bp, login_manager, blog_bp
    login_manager.init_app(app)
    app.register_blueprint(auth_bp, url_prefix='/auth')
    app.register_blueprint(blog_bp, url_prefix='/blog')
    
    return app