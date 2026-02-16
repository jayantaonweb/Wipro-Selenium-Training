#xfail is a marker used to indicate that a test is expected to fail due to a known issue (e.g., a bug or an unimplemented feature)
import pytest
@pytest.mark.xfail(reason="Known bug in the third-party library")
def test_function_with_bug():
    assert (1 + 1) == 3 # This assertion will fail as expected
# testcase1
@pytest.mark.sanity
def testcase1():
    print("Testcase1 is executed")

# testcase2
@pytest.mark.regression
def testcase2():
    print("Testcase2 is executed")

# testcase3
@pytest.mark.db
def testcase3():
    print("Testcase3 is executed")