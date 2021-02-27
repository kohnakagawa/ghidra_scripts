import java.lang


class Prime(object):
    """
    Class that provides a static nextPrime method that gives out prime numbers
     that are useful in a buffer doubling strategy with all buffer sizes being prime.
    """





    def __init__(self): ...



    def equals(self, __a0: object) -> bool: ...

    def getClass(self) -> java.lang.Class: ...

    def hashCode(self) -> int: ...

    @staticmethod
    def nextPrime(n: int) -> int:
        """
        Finds the next prime number greater than or equal to n.
        @param n the number from which to find the next higher prime number.
        """
        ...

    def notify(self) -> None: ...

    def notifyAll(self) -> None: ...

    def toString(self) -> unicode: ...

    @overload
    def wait(self) -> None: ...

    @overload
    def wait(self, __a0: long) -> None: ...

    @overload
    def wait(self, __a0: long, __a1: int) -> None: ...
