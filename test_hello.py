import pytest
from hello_world import HelloWorld

def test_message_string():
    message = "Hallo! Wie geht's?"
    greeter = HelloWorld(message,0)
    hello_message = greeter.say_hello()

    assert hello_message == message.upper(), "Test failed: not returning an all caps message"
