import json

# Testing the overall functionality - is the route rendering the correct data?
def test_index_page(client):
    response = client.get("/")
    print(response.data)
    assert response.status_code == 200
    assert response.data == b'<p>Hello, World!</p>'
    
# GET /characters
def test_characters_page(client):
    response = client.get("/characters")
    assert response.status_code == 200
    data = json.loads(response.data)
    
    assert data['characters'][0]['name'] == 'Test'
    assert data['characters'][0]['age'] == 0
    assert data['characters'][0]['catch_phrase'] == 'I am a test'
    
# GET/:id characters
def test_character_page(client):
    response = client.get('/characters/1')
    assert response.status_code == 200
    
    data = json.loads(response.data)
    print(data)
    assert len(data) == 4
    assert data['id'] == 1
    assert data['name'] == 'Test'
    assert data['age'] == 0
    assert data['catch_phrase'] == 'I am a test'
    
