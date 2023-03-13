import pytest
from hello_world import HelloWorld

def test_number_is_int():
    greeter = HelloWorld('message', 13.2)
    num = greeter.say_number()

    assert type(num) == float, "Test failed: not returning a float"

