import java.lang


class ResourceStringInfo(object):
    """
    A class to hold the information extracted from a
     resource data directory.

     NOTE:
     This class is simply a storage class created for
     parsing the PE header data structures.
     It does not map back to a PE data data structure.
    """





    def __init__(self, address: int, string: unicode, length: int):
        """
        Constructor.
        @param address the adjusted address where the resource exists
        @param string the resource string
        @param length the length of the resource
        """
        ...



    def equals(self, __a0: object) -> bool: ...

    def getAddress(self) -> int:
        """
        Returns the adjusted address where the resource exists.
        @return the adjusted address where the resource exists
        """
        ...

    def getClass(self) -> java.lang.Class: ...

    def getLength(self) -> int:
        """
        Returns the length of the resource.
        @return the length of the resource
        """
        ...

    def getString(self) -> unicode:
        """
        Returns the resource string.
        @return the resource string
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
    def address(self) -> int: ...

    @property
    def length(self) -> int: ...

    @property
    def string(self) -> unicode: ...
