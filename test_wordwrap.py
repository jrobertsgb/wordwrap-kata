import unittest
from wordwrap import Wrapper

class TestWordWrapper(unittest.TestCase):
    def setUp(self):
        self.wrapper = Wrapper()

    def test_can_initialise_a_wrapper(self):
        wrapper = Wrapper()

        assert wrapper is not None

    def test_can_wrapper_accept_text(self):
        wrapper = Wrapper()

        wrapper.wrap("somedata")

    def test_wrapper_returns_text(self):
        text = "foobar"

        wrapped = self.wrapper.wrap(text)

        assert wrapped == text
