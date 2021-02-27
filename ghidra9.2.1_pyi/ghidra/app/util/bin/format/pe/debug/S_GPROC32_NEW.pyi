import ghidra.app.util.bin.format.pe.debug
import java.lang


class S_GPROC32_NEW(ghidra.app.util.bin.format.pe.debug.DebugSymbol):
    """
    A class to represent the S_GPROC32_NEW data structure.
    """





    def __init__(self):
        """
        DO NOT USE THIS CONSTRUCTOR, USE create*(GenericFactory ...) FACTORY METHODS INSTEAD.
        """
        ...



    def equals(self, __a0: object) -> bool: ...

    def getClass(self) -> java.lang.Class: ...

    def getDebugEnd(self) -> int: ...

    def getDebugStart(self) -> int: ...

    def getEnd(self) -> int: ...

    def getLength(self) -> int:
        """
        Returns the length of the symbol.
        @return the length of the symbol
        """
        ...

    def getName(self) -> unicode:
        """
        Returns the name of the symbol.
        @return the name of the symbol
        """
        ...

    def getNext(self) -> int: ...

    def getOffset(self) -> int:
        """
        Returns the offset.
        @return the offset
        """
        ...

    def getParent(self) -> int: ...

    def getProcLen(self) -> int:
        """
        Returns the procedure length.
        @return the procedure length
        """
        ...

    def getProcOffset(self) -> int:
        """
        Returns the procedure offset.
        @return the procedure offset
        """
        ...

    def getProcType(self) -> int:
        """
        Returns the procedure type.
        @return the procedure type
        """
        ...

    def getSection(self) -> int:
        """
        Returns the section number.
        @return the section number
        """
        ...

    def getType(self) -> int:
        """
        Returns the type of the symbol.
        @return the type of the symbol
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
    def debugEnd(self) -> int: ...

    @property
    def debugStart(self) -> int: ...

    @property
    def end(self) -> int: ...

    @property
    def next(self) -> int: ...

    @property
    def parent(self) -> int: ...

    @property
    def procLen(self) -> int: ...

    @property
    def procOffset(self) -> int: ...

    @property
    def procType(self) -> int: ...
