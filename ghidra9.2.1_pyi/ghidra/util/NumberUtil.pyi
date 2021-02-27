import java.lang


class NumberUtil(object):
    UNSIGNED_BYTE_MASK: int = 255
    UNSIGNED_INT_MASK: long = 0xffffffffL
    UNSIGNED_SHORT_MASK: int = 65535



    def __init__(self): ...



    def equals(self, __a0: object) -> bool: ...

    @staticmethod
    def equalsMaxUnsignedValue(value: java.lang.Number) -> bool:
        """
        Compare to the maximum unsigned value that the current number is holding.
        @param value the value stored in a signed number
        @return true if equal to the maximum and false otherwise
        """
        ...

    def getClass(self) -> java.lang.Class: ...

    @staticmethod
    def getUnsignedValue(value: java.lang.Number) -> java.lang.Number:
        """
        Get the unsigned value of a number.
        @param value the value stored in a signed number
        @return the unsigned value of the number
        """
        ...

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
