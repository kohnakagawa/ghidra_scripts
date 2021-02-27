import ghidra.pcode.floatformat
import java.lang


class FloatFormatFactory(object):




    def __init__(self): ...



    def equals(self, __a0: object) -> bool: ...

    def getClass(self) -> java.lang.Class: ...

    @staticmethod
    def getFloatFormat(size: int) -> ghidra.pcode.floatformat.FloatFormat:
        """
        Get float format
        @param size format storage size in bytes
        @return float format or null if size is not supported
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
