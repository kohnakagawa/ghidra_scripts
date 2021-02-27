import java.lang


class DebugSymbol(object):
    """
    A base class for Object Module Format (OMF) symbols.
    """









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
    def length(self) -> int: ...

    @property
    def name(self) -> unicode: ...

    @property
    def offset(self) -> int: ...

    @property
    def section(self) -> int: ...

    @property
    def type(self) -> int: ...
