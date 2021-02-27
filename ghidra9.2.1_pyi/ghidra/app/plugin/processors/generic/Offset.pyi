import ghidra.program.model.mem
import java.io
import java.lang
import java.util


class Offset(object, java.io.Serializable):




    @overload
    def __init__(self, off: int, name: unicode): ...

    @overload
    def __init__(self, off: int, rel: ghidra.app.plugin.processors.generic.Operand): ...



    def equals(self, __a0: object) -> bool: ...

    def getClass(self) -> java.lang.Class: ...

    def getOffset(self, buf: ghidra.program.model.mem.MemBuffer, off: int) -> int:
        """
        Method getOffset.
        @param buf - a MemBuffer of bytes to parse
        @param off - offset into the MemBuffer at which to start
        @return int - offset into the MemBuffer to which this Offset object points
         						given the bytes in the MemBuffer.
        """
        ...

    def hashCode(self) -> int: ...

    def notify(self) -> None: ...

    def notifyAll(self) -> None: ...

    def setRelativeOffset(self, opHash: java.util.Hashtable) -> None:
        """
        Method setRelativeOffset.
        @param opHash
        """
        ...

    def toString(self) -> unicode: ...

    @overload
    def wait(self) -> None: ...

    @overload
    def wait(self, __a0: long) -> None: ...

    @overload
    def wait(self, __a0: long, __a1: int) -> None: ...

    @property
    def relativeOffset(self) -> None: ...  # No getter available.

    @relativeOffset.setter
    def relativeOffset(self, value: java.util.Hashtable) -> None: ...
