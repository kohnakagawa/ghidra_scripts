import java.lang


class ImportInfo(object):








    def equals(self, __a0: object) -> bool: ...

    def getAddress(self) -> int:
        """
        Returns the adjusted address where the import occurs.
        @return the adjusted address where the import occurs
        """
        ...

    def getClass(self) -> java.lang.Class: ...

    def getComment(self) -> unicode:
        """
        Returns a comment string containing extra information about the import.
        @return a comment string containing extra information about the import
        """
        ...

    def getDLL(self) -> unicode:
        """
        Returns the name of the imported DLL.
        @return the name of the imported DLL
        """
        ...

    def getName(self) -> unicode:
        """
        Returns the name of the imported symbol.
        @return the name of the imported symbol
        """
        ...

    def hashCode(self) -> int: ...

    def isBound(self) -> bool:
        """
        Returns true if this is a bound import.
        @return true if this is a bound import
        """
        ...

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
    def DLL(self) -> unicode: ...

    @property
    def address(self) -> int: ...

    @property
    def bound(self) -> bool: ...

    @property
    def comment(self) -> unicode: ...

    @property
    def name(self) -> unicode: ...
