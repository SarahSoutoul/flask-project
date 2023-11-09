from application.models import FriendsCharacter

def test_new_character():
    character = FriendsCharacter("Joe", 12, "I AM A GREAT PERSON")
    
    assert character.name == 'Joe'
    assert character.age == 12
    assert character.catch_phrase == "I AM A GREAT PERSON"
    
    
    
    
    