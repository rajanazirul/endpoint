import pytest
from get_score.views import get_score
from get_score.models import Record
from django.test.client import RequestFactory

# Test fixture
@pytest.fixture
def record(db) -> Record:
    return Record.objects.create(user_id="123", input_one="2")

# Unit Test Model to get result
def test_Record_create(record):
    assert record.result == '1.60'

# Unit test View to check invalid input
@pytest.mark.django_db
def test_invalid_input():
    rf = RequestFactory()
    post_request = rf.post('/get_score/', {"user_id": "dd123", "input_one":"sa2"})
    view = get_score(post_request)
    assert view.status_code == 400

# Unit test log user Id
def test_log_user(record):
    assert record.user_id == '123'