import pytest

class TestInput:

    def setup_class(self):
        self.expected_result = 11
        self.actual_result = 11

    def test_input_text(self):
        assert self.expected_result == self.actual_result, f'expected {self.expected_result}, got {self.actual_result}'
