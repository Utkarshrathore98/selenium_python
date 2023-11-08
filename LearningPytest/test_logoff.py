import pytest


@pytest.mark.sanity
def testLogoff():
    print("Logoff Successfully !")


@pytest.mark.xfail
def testCalculation():
    assert 2 + 2 == 5
