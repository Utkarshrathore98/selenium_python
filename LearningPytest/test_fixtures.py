import pytest


@pytest.fixture()  # if you are using older version, you can use @pytest.yield_fixture()
def setUp():
    print("Launch browser")
    print("Login")
    print("Browse Products")
    yield """It will help in tier down, so before yield it will run all the above lines and in place of yield 
    AddItemsToCart will run and then last two lines will be run."""
    print("Logoff")
    print("Close Browser")


def testAddItemsToCart(setUp):
    print("Add Item Successfully !")


def testRemoveItemsToCart(setUp):
    print("Remove Item Successfully !")
