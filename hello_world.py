class HelloWorld:
    def __init__(self, message, number):
        '''Initialize an object with an arbitrary message and an arbitrary number'''
        self.message = message
        self.number = number

    def say_hello(self):
        '''Return the message in all caps'''
        return self.message.upper()
    
    def say_number(self):
        '''Return the number rounded to the nearest full value as a float'''
        return float(round(self.number))