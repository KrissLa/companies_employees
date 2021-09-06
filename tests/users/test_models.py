import pytest

from backend.apps.users.models import User


@pytest.mark.django_db
def test_user_model():
    user = User.objects.create(username='test_username', password='test_password')
    assert user.username == 'test_username'
    assert user.check_password('test_password')
    assert not user.first_name
    assert not user.last_name
    assert not user.email
    assert not user.patronymic
    assert not user.age
    assert not user.is_staff
    assert user.is_active
    assert user.date_joined
    assert user.created_at
    assert user.updated_at
    assert str(user) == user.username
