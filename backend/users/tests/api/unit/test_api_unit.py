import pytest
from users.models import User


@pytest.mark.django_db
def test_user_list(client):
    response = client.get('/api/users/')
    assert response.status_code == 200
    assert isinstance(response.json(), list)
    assert all(isinstance(item, dict) for item in response.json())


@pytest.mark.django_db
@pytest.mark.parametrize('data, expected_status', [
    ({ 
        'email': 'newuser@e.com',
        'first_name': 'New',
        'last_name': 'User',
        'avatar': 'https://reqres.in/img/faces/7-image.jpg'
    }, 201),
    ({
        'first_name': 'Incomplete',
        'last_name': 'User',
        'avatar': 'https://reqres.in/img/faces/7-image.jpg'
    }, 400)
])
def test_create_user(client, data, expected_status):
    response = client.post('/api/users/create/', data, content_type='application/json')
    assert response.status_code == expected_status
    if expected_status == 201:
        assert User.objects.get(email=data['email'])



@pytest.mark.django_db
@pytest.mark.parametrize('expected_status', [200])
def test_user_detail(client, create_user, expected_status):
    response = client.get(f'/api/users/{create_user.id}/')
    assert response.status_code == expected_status
    if expected_status == 200:
        assert response.json()['email'] == 'karimbaidar@test.com'



@pytest.mark.django_db
@pytest.mark.parametrize('expected_status', [400])
def test_duplicate_user_creation(client, expected_status):
    """
    Testing duplicate entry
    """
    user_data = {
        'email': 'karimbaidar@test.com',
        'first_name': 'Test',
        'last_name': 'User',
        'avatar': 'https://reqres.in/img/faces/7-image.jpg'
    }
    response = client.post('/api/users/create/', user_data, content_type='application/json')
    assert response.status_code == 201

    duplicate_user_data = {
        'email': 'karimbaidar@test.com',
        'first_name': 'Duplicate',
        'last_name': 'User',
        'avatar': 'https://reqres.in/img/faces/7-image-duplicate.jpg'
    }
    duplicate_response = client.post('/api/users/create/', duplicate_user_data, content_type='application/json')
    assert duplicate_response.status_code == expected_status



@pytest.mark.django_db
@pytest.mark.parametrize('expected_status', [400])
def test_create_user_with_missing_fields(client, expected_status):
    """
    Test user creation with missing fields.
    """
    user_data = {
        'first_name': 'Incomplete',
        'last_name': 'User',
        'avatar': 'https://reqres.in/img/faces/7-image.jpg'
    }
    response = client.post('/api/users/create/', user_data, content_type='application/json')
    assert response.status_code == expected_status

    

@pytest.mark.django_db
@pytest.mark.parametrize('expected_status', [404])
def test_get_non_existent_user(client, expected_status):
    non_existent_user_id = 999
    response = client.get(f'/api/users/{non_existent_user_id}/')
    assert response.status_code == expected_status
