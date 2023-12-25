import pytest


@pytest.mark.django_db
@pytest.mark.parametrize('user_data', [
    {
        'email': 'karim.baidar@test.com',
        'first_name': 'karim',
        'last_name': 'baidar',
        'avatar': 'https://reqres.in/img/faces/7-image.jpg'
    },
    {
        'email': 'baidar.karim@test.com',
        'first_name': 'baidar',
        'last_name': 'karim',
        'avatar': 'https://reqres.in/img/faces/8-image.jpg'
    }
])
def test_integration_user_management(client, user_data):
    """
    Insert User details
    Get id of the inserted user as a response
    Use the id of the response for accessing the detailed view
    """
    
    create_response = client.post('/api/users/create/', data=user_data, content_type='application/json')
    assert create_response.status_code == 201

    user_id = create_response.json()['id']
    detail_response = client.get(f'/api/users/{user_id}/')
    assert detail_response.status_code == 200

    user_info = detail_response.json()
    assert user_info['email'] == user_data['email']
    assert user_info['first_name'] == user_data['first_name']
    assert user_info['last_name'] == user_data['last_name']
    assert user_info['avatar'] == user_data['avatar']

