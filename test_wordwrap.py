import unittest
from wordwrap import Wrapper

class TestWordWrapper(unittest.TestCase):
    def test_can_initialise_a_wrapper(self):
        wrapper = Wrapper()

    def test_can_wrapper_accept_text(self):
        wrapper = Wrapper()

        wrapper.wrap("somedata")
