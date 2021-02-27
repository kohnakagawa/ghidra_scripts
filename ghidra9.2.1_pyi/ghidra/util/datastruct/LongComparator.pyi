import java.lang


class LongComparator(object):
    """
    Interface that defines a method for comparing two long values.
    """









    def compare(self, a: long, b: long) -> int:
        """
        Compares the long values a and b.
        @param a the first value
        @param b the second value
        @return 0 if a equals b; a number greater than 0 if a is greater than b;
         a number less than 0 if a is less than b.
        """
        ...

    def equals(self, __a0: object) -> bool: ...

    def getClass(self) -> java.lang.Class: ...

    def hashCode(self) -> int: ...

    def notify(self) -> None: ...

    def notifyAll(self) -> None: ...

    def toString(self) -> unicode: ...

    @overload
    def wait(self) -> None: ...

    @overload
    def wait(self, __a0: long) -> None: ...

    @overload
    def wait(self, __a0: long, __a1: int) -> None: ...
