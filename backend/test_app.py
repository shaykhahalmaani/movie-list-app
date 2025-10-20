import pytest
from app import app

@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

def test_get_movies(client):
    response = client.get('/movies')
    assert response.status_code == 200
    data = response.get_json()
    assert 'movies' in data
    assert len(data['movies']) == 4

def test_get_movie_by_id(client):
    response = client.get('/movies/123')
    assert response.status_code == 200
    data = response.get_json()
    assert 'movie' in data
    assert data['movie']['title'] == 'Top Gun: Maverick'

def test_get_nonexistent_movie(client):
    response = client.get('/movies/999')
    assert response.status_code == 200
    data = response.get_json()
    assert 'movie' in data
