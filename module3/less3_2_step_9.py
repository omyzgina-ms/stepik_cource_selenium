import pytest

class TestStrings:

    def setup_class(self):
        print('Get variables for testing')
        self.full_string = '11'
        self.substring = '1'

    def test_substring(self):
        print('Check variables')
        assert self.substring in self.full_string, f"expected '{self.substring}' to be substring of '{self.full_string}'"
