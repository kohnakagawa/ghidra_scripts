import ghidra.program.model.mem
import ghidra.util.ascii
import java.lang


class PascalUtil(object):




    def __init__(self): ...



    def equals(self, __a0: object) -> bool: ...

    @staticmethod
    def findPascalSequence(buf: ghidra.program.model.mem.MemBuffer, sequence: ghidra.util.ascii.Sequence, alignment: int) -> ghidra.util.ascii.Sequence:
        """
        Looks for Pascal strings given a sequence of bytes that represent a sequence of ascii chars.
        @param buf the Memory buffer containing the bytes that make up the string.
        @param sequence the sequence that specifies the start, end, and type of ascii sequence (i.e. ascii,
         unicode16).  This method looks for both 2 byte and 1 byte leading pascal lengths both before
         and at the beginning of the given sequence.
        @return a new sequence that has been adjusted  to represent a pascal string or null if
         a pascal string was not found.
        """
        ...

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
