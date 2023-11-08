import pytest


@pytest.fixture(scope="session", autouse=True)
# if you are using older version, you can use @pytest.yield_fixture(). If autouse = True , you do not have to mention
# the module name (tc_setup) in the module parameter. .i.e in test_conftestLearning.py. If we don't mention the scope
# then by default scope will be function. If scope ="session" then tier down will only execute once all the modules
# are executed.
def tc_setUp():
    print("Launch browser")
    print("Login")
    print("Browse Products")
    yield """It will help in tier down, so before yield it will run all the above lines and in place of yield 
    AddItemsToCart will run and then last two lines will be run."""
    print("Logoff")
    print("Close Browser")
