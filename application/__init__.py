import os
from flask import Flask
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy

# Defining db
db = SQLAlchemy()

# with app.app_context():
#     # Create the database
#     db.create_all()
#     # Create fake data
#     test_character = FriendsCharacter(name="Test", age=0, catch_phrase="I am a test")
#     # Inject it into the database
#     db.session.add(test_character)
#     db.session.commit()
        
# Application factory
def create_app(env=None):
    # Initialisation of the app
    app = Flask(__name__)
    
    # Set up the environment variables depending on the environment
    if env == 'TEST':
        app.config['TESTING'] = True
        app.config['DEBUG'] = False
        app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite://"
    else:
        app.config['TESTING'] = False
        app.config['DEBUG'] = True
        app.config['SQLALCHEMY_DATABASE_URI'] = os.environ["DATABASE_URL"]
    
    # Connection of the db to the app
    db.init_app(app)
    
    # Making sure db is created in an application context
    app.app_context().push();
    CORS(app)
    
    from application.routes import characters
    app.register_blueprint(characters)

    return app
    