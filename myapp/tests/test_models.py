import pytest
from myapp.models import Item

@pytest.mark.django_db
def test_create_item():
    item = Item.objects.create(name='Test Item', description='This is a test item.')
    assert item.name == 'Test Item'
    assert item.description == 'This is a test item.'
