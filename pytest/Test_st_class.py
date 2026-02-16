#used inside the class
# it will run for every class definition 0 it will run starting and ending of the class
class Testclass:
    # class level set up
    def setup_class(cls):
        print("API Authorization needed with username and password")
    def teardown_class(cls):
        print("API Authorization closed")


    def testcase1(self):
        print("testcase1 executed")


    def testcase2(self):
        print("testcase2 executed")


    def test_case3(self):
        print("testcase3 executed")

class Testclass2:
    def testcase1(self):
        print("testcase1 executed")


    def testcase2(self):
        print("testcase2 executed")

    def test_case3(self):
        print("testcase3 executed")