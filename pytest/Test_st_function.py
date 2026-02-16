

#function level set up and tear down
# these run before and after each test function


# set up at function level
def setup_function(function):
    print("opening the browser")

#teardown at function level
def teardown_function(function):
    print("Closing the browser")


def testcase1():
    print("testcase1 executed")


# testcase 1

def testcase2():
    print("testcase2 executed")


# testcase 1

def test_case3():
    print("testcase3 executed")
