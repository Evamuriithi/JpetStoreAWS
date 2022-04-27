import unittest
import jpetstoredemo_locators as locators
import jpetstoredemo_methods as methods

class JpetstoreAppPostiveTestCases(unittest.TestCase):

    @staticmethod # signal to unittest that this is a function inside class (vs @classmethod)
    def test_main_jpetstoredemo(): # test_in the name is mandotory
        methods.setUp()
        methods.sign_up()
        methods.register()
        methods.profile_information()
        methods.tearDown()





        #setUp()
        #sign_up()
        #register()
        #profile_information()
        #tearDown()