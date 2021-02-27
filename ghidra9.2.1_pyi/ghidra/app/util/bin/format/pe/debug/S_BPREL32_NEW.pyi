import ghidra.app.util.bin.format.pe.debug
import java.lang


class S_BPREL32_NEW(ghidra.app.util.bin.format.pe.debug.DebugSymbol):
    """
    A class to represent the S_BPREL32_NEW data structure.
    """





    def __init__(self):
        """
        DO NOT USE THIS CONSTRUCTOR, USE create*(GenericFactory ...) FACTORY METHODS INSTEAD.
        """
        ...



    def equals(self, __a0: object) -> bool: ...

    def getClass(self) -> java.lang.Class: ...

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

    def getOffset(self) -> int:
        """
        Returns the offset.
        @return the offset
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

    def getVariableType(self) -> int:
        """
        Returns the variable type.
        @return the variable type
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
    def variableType(self) -> int: ...
