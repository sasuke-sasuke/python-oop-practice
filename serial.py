"""Python serial number generator."""

class SerialGenerator:
    """Machine to create unique incrementing serial numbers.
    
    >>> serial = SerialGenerator(start=100)

    >>> serial.generate()
    100

    >>> serial.generate()
    101

    >>> serial.generate()
    102

    >>> serial.reset()

    >>> serial.generate()
    100
    """
    def __init__(self, start=100):
        self.start = start-1
        self.serial = self.start

    def generate(self):
        """Increments serial number by 1"""
        self.serial += 1
        return self.serial

    def reset(self):
        """Reset serial to original start"""
        self.serial = self.start



