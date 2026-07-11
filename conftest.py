import pytest


@pytest.fixture(scope="function")
def createdbconnection():
    print("Creating database connection")
    print("connected to database")
    x = 23
    yield x
    del x