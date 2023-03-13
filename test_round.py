import pytest
from hello_world import HelloWorld

def test_rounding():
    greeter = HelloWorld('message', 13.9)
    num = greeter.say_number()

    assert num == 14, "Test failed: not rounding correctly"
