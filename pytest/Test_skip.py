# skip - if defects are there
# skip - if the testcases are absolute
# windows , mobile -OS dependnecy
# browsers - FF , IE , chrome

import pytest

# testcase 1

def testcase1():
    print("testcase1 executed")

@pytest.mark.skip
# testcase 1

def testcase2():
    print("testcase2 executed")


# testcase 1

def test_case3():
    print("testcase3 executed")
