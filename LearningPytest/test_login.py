import pytest


@pytest.mark.regression
def testLogin():
    print("Login Successfully !")


@pytest.mark.sanity
def testCalculation():
    assert 2 + 2 == 4


@pytest.mark.skip
def testSkip():
    assert 2 + 2 == 4
