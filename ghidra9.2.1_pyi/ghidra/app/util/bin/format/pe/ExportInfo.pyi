import java.lang


class ExportInfo(object):
    """
    A class to hold the information extracted from a
     export data directory.

     NOTE:
     This class is simply a storage class created for
     parsing the PE header data structures.
     It does not map back to a PE data data structure.
    """









    def equals(self, __a0: object) -> bool: ...

    def getAddress(self) -> long:
        """
        Returns the adjusted address where the export occurs.
        @return the adjusted address where the export occurs
        """
        ...

    def getClass(self) -> java.lang.Class: ...

    def getComment(self) -> unicode:
        """
        Returns a comment string containing extra information about the export.
        @return a comment string containing extra information about the export
        """
        ...

    def getName(self) -> unicode:
        """
        Returns the name of the export.
        @return the name of the export
        """
        ...

    def getOrdinal(self) -> int:
        """
        Returns the ordinal value of the export.
        @return the ordinal value of the export
        """
        ...

    def hashCode(self) -> int: ...

    def isForwarded(self) -> bool:
        """
        Returns true of this export is going to be forwarded.
         Generally, a forwarded export just through another export.
        @return true of this export is going to be forwarded
        """
        ...

    def notify(self) -> None: ...

    def notifyAll(self) -> None: ...

    def toString(self) -> unicode:
        """
        @see java.lang.Object#toString()
        """
        ...

    @overload
    def wait(self) -> None: ...

    @overload
    def wait(self, __a0: long) -> None: ...

    @overload
    def wait(self, __a0: long, __a1: int) -> None: ...

    @property
    def address(self) -> long: ...

    @property
    def comment(self) -> unicode: ...

    @property
    def forwarded(self) -> bool: ...

    @property
    def name(self) -> unicode: ...

    @property
    def ordinal(self) -> int: ...
