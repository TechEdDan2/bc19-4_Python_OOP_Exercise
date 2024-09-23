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

    def __init__(self, start=0):
        """ Initialize a new SerialGenerator, starting at the start"""
        self.start = start
        self.count = self.start

    def __repr__(self):
        """ Display the representation of the object """
        return f"<SerialGenerator start={self.start} count={self.count}"

    def generate(self):
        """ Generate returns the next number in the increased count """
        self.count += 1
        return self.count

    def reset(self):
        """ Return to the starting number """
        self.count = self.start


