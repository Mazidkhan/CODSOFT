# conftest.py

import pytest

@pytest.fixture
def setup_data():
    data = {'key': 'value'}
    return data

# test_sample.py

def test_data(setup_data):
    assert setup_data['key'] == 'value'