import java.lang


class EntryPoint(object):
    """
    A class to represent a new-executable entry point.
    """

    EXPORTED: int = 1
    GLOBAL: int = 2







    def equals(self, __a0: object) -> bool: ...

    def getClass(self) -> java.lang.Class: ...

    def getFlagword(self) -> int:
        """
        Returns the flagword.
        @return the flagword
        """
        ...

    def getInstruction(self) -> int:
        """
        Returns the instruction.
        @return the instruction
        """
        ...

    def getOffset(self) -> int:
        """
        Returns the offset.
        @return the offset
        """
        ...

    def getSegment(self) -> int:
        """
        Returns the segment.
        @return the segment
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

    @property
    def flagword(self) -> int: ...

    @property
    def instruction(self) -> int: ...

    @property
    def offset(self) -> int: ...

    @property
    def segment(self) -> int: ...
