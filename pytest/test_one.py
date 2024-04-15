# lesson 1.1
# a = True
# def test_a():
#     assert a == True
#     print("yeah")

import pytest

@pytest.fixture
def variable():
    return "hi"

def test_00(variable):
    assert variable == "hi"