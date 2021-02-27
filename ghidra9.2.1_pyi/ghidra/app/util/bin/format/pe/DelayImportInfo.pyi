import java.lang


class DelayImportInfo(object):
    """
    A class to hold the information extracted from a
     delay import descriptor.

     NOTE:
     This class is simply a storage class created for
     parsing the PE header data structures.
     It does not map back to a PE data data structure.
    """









    def equals(self, __a0: object) -> bool: ...

    def getClass(self) -> java.lang.Class: ...

    def getName(self) -> unicode:
        """
        Returns the name of the imported DLL.
        @return the name of the imported DLL
        """
        ...

    def getOrdinal(self) -> long:
        """
        Returns the ordinal number of the imported DLL.
        @return the ordinal number of the imported DLL
        """
        ...

    def hasName(self) -> bool:
        """
        Returns true if the import is 'by name'.
        @return true if the import is 'by name'
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
    def name(self) -> unicode: ...

    @property
    def ordinal(self) -> long: ...
