# Any pytest file should start with test_ or end with _test
# pytest method names should start with test
# Any code should be wrapped in method only
# Method name should have sense
# [CMD] -k stands for method names execution, -s logs in output, -v stands for more info metadata
# [CMD] py.test -v -s
# you can run spesific file with py.test <filename.py>
# You can mark (tag) tests @pytest.mark.smoke and then run with py.test -m smoke -v -s
# @pytest.mark.xfail
# fixtures are used as setup and tear down methods for test cases- conftest file to generalize fixture
# fixture and make it available to all test cases
# datadriven and parameterization can be done with return statements in tuple format
# when you define fixture scope to calss only, it will run once before class is initiate and at the end

import pytest

@pytest.mark.smoke
@pytest.mark.skip
def test_firstProgram():
    msg = "Hello" # Operations
    assert msg == "Hi", "Test failed because strings do not match"

def test_secondCreditCard():
    a = 4
    b = 6
    assert a+2 == 6, "Addition do not match"