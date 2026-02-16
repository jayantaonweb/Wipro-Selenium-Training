# module level - runs once per module (file)
# use module level set up and tear down when you want to execute the set up and tear down once in the current file
# eg open the db connection execute all the testcases and at alst close the db connection
# setup_module - only one per file
# setup_class - only one per class
# setup_method - only one per class
# setup_module - only one per class

def set_module(module):
    print("Open the db connection")

def teardown_module(module):
    print("Closing the db connection")


def test_read():
    print("Reading the db")


# testcase 1

def test_write():
    print("testcase2 executed")


# testcase 1

def test_updating():
    print("testcase3 executed")
