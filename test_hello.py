import pytest
from hello_world import HelloWorld

def test_message_string():
    message = "Hallo! Wie geht's?"
    greeter = HelloWorld(message,0)
    hello_message = greeter.say_hello()

    assert hello_message == message.upper(), "Test failed: not returning an all caps message"

def test_number_is_int():
    greeter = HelloWorld('message', 13.2)
    num = greeter.say_number

    assert type(num) == int, "Test failed: not returning an integer"

def test_rounding():
    greeter = HelloWorld('message', 13.9)
    num = greeter.say_number

    assert num == 13, "Test failed: not rounding down correctly"
