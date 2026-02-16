#used inside the class
# used inside the class
# runs before and after the test methods inside the class
#in case of inheritance it will be executed

class Testclass:
    # class level set up
    def setup_class(cls):
        print("API Authorization needed with username and password")
    def teardown_class(cls):
        print("API Authorization closed")

    def setup_method(method):

        print("opening the browser")

    def teardown_method(method):
        print("closing the browser")

    def testcase1(self):
        print("testcase1 executed")


    def testcase2(self):
        print("testcase2 executed")


    def test_case3(self):
        print("testcase3 executed")

class Testclass2(Testclass):
    def testcase1(self):
        print("testcase1 executed")


    def testcase2(self):
        print("testcase2 executed")

    def test_case3(self):
        print("testcase3 executed")