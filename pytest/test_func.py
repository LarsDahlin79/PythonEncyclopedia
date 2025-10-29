
import pytest

"""
Install pytest
pip install pytest

Run the tests
pytest
"""

def test_add():
    assert 2 + 3 == 5

@pytest.fixture
def my_fixture():
    yield 3

def test_my_fixture(my_fixture):
    assert 0 < my_fixture and my_fixture <= 5

@pytest.mark.parametrize("my_param", (1,2,3,4,5))
def test_add(my_param):
    assert my_param + 1 > 0

