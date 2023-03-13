class HelloWorld:
    def __init__(self, message, number):
        '''Initialize an object with an arbitrary message and an arbitrary number'''
        self.message = message
        self.number = number

    def say_hello(self):
        '''Return the message in all caps'''
        return self.message
    
    def say_number(self):
        '''Return the number rounded down to the nearest int'''
        return self.number