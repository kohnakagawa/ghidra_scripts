from typing import List
import ghidra.util
import java.lang


class ByteArrayConverter(object):
    """
    An interface to convert from a object to a
     byte array.
    """









    def equals(self, __a0: object) -> bool: ...

    def getClass(self) -> java.lang.Class: ...

    def hashCode(self) -> int: ...

    def notify(self) -> None: ...

    def notifyAll(self) -> None: ...

    def toBytes(self, dc: ghidra.util.DataConverter) -> List[int]:
        """
        Returns a byte array representing this implementor
         of this interface.
        @param dc the data converter to use
        @return a byte array representing this object
        """
        ...

    def toString(self) -> unicode: ...

    @overload
    def wait(self) -> None: ...

    @overload
    def wait(self, __a0: long) -> None: ...

    @overload
    def wait(self, __a0: long, __a1: int) -> None: ...
