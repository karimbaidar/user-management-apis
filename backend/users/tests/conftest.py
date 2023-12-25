import pytest
from django.test import Client
from users.models import User

@pytest.fixture
def client_fixture():
    return Client()


@pytest.fixture
def create_user():
    User.objects.create(email='karimbaidar@test.com', 
                        first_name='Test', 
                        last_name='User', 
                        avatar='https://reqres.in/img/faces/7-image.jpg')
    return User.objects.get(email='karimbaidar@test.com')
