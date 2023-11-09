# File where you will setup the test environment as well as anything that needs to be called before every test
# Fixture

import pytest
from application import create_app, db
from application.models import FriendsCharacter


# Fixture 
@pytest.fixture
def client():
    env = "TEST"
    # Initialise a test app
    app = create_app(env)
    
    # Create a test client to which we can make requests
    client = app.test_client()
    
    with app.app_context():
        db.session.rollback()
        db.drop_all()
        
    # Create a test database with some test data
    with app.app_context():
        # Create the database
        db.create_all()
        # Create fake data
        test_character = FriendsCharacter(name="Test", age=0, catch_phrase="I am a test")
        # Inject it into the database
        db.session.add(test_character)
        db.session.commit()

    return client

   
