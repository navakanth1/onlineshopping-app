import pytest
@pytest.fixture(scope="session", autouse=True)
def setUp():
    print("open app")
    print("user login")
    yield
    print("logout")
    print("close app")
