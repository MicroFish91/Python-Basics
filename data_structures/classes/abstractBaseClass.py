# Since we don't ever want to create a stream object directly,
# only use it to set up as a template for other classes
# we can set it up as an abstract base class
from abc import ABC, abstractmethod


class InvalidOperationError(Exception):
    pass


class Stream(ABC):
    def __init__(self):
        self.opened = False

    def open(self):
        if self.opened:
            raise InvalidOperationError("Stream is already open.")
        self.opened = True

    def closed(self):
        if not self.opened:
            raise InvalidOperationError("Stream is already closed.")
        self.opened = False

    @abstractmethod
    def read(self):
        pass


class FileStream(Stream):
    def read(self):
        print("Reading data from a file.")


class NetworkStream(Stream):
    def read(self):
        print("Reading data from a network")


class MemoryStream(Stream):
    # pass
    def read(self):
        print("Reading data from memory stream")


# stream = Stream()  # TypeError can't instantiate abstract class with abstract method
# MemoryStream will not work if we just "pass" as we inherit the ABC
# Need to set definitive read method to create a concrete class
