import pytest
from src.my_package import my_module


class TestMyModule:
    def setup_method(self):
        """Assemble common resources to be acted upon"""

    def test_do_thing(self):
        expected = my_module.do_thing()
        assert expected.unwrap() == "Hello world!"
