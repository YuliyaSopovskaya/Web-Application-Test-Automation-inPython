import pytest 

@pytest.fixture()
def good():
    return "Молоко"

@pytest.fixture()
def bad():
    return "Малоко"
