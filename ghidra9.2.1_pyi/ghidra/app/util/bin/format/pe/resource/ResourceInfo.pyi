import ghidra.app.util.bin.format.pe.resource
import java.lang


class ResourceInfo(object, java.lang.Comparable):
    """
    A class to hold the information extracted from a
     resource data directory.

     NOTE:
     This class is simply a storage class created for
     parsing the PE header data structures.
     It does not map back to a PE data data structure.
    """





    def __init__(self, address: int, name: unicode, size: int):
        """
        Constructor.
        @param address the adjusted address where the resource exists
        @param name the name of the resource
        @param size the size of the resource
        """
        ...



    @overload
    def compareTo(self, that: ghidra.app.util.bin.format.pe.resource.ResourceInfo) -> int: ...

    @overload
    def compareTo(self, __a0: object) -> int: ...

    def equals(self, __a0: object) -> bool: ...

    def getAddress(self) -> int:
        """
        Returns the adjusted address where the resource exists.
        @return the adjusted address where the resource exists
        """
        ...

    def getClass(self) -> java.lang.Class: ...

    def getID(self) -> int:
        """
        Returns the ID of the resource.
        @return the ID of the resource
        """
        ...

    def getName(self) -> unicode:
        """
        Returns the name of the resource.
        @return the name of the resource
        """
        ...

    def getSize(self) -> int:
        """
        Returns the size of the resource.
        @return the size of the resource
        """
        ...

    def getTypeID(self) -> int:
        """
        Returns the resource type ID.
         For example, RT_CURSOR, RT_BITMAP, etc.
         Returns -1 if this is a named resource.
        """
        ...

    def hashCode(self) -> int: ...

    def notify(self) -> None: ...

    def notifyAll(self) -> None: ...

    def setID(self, id: int) -> None: ...

    def setName(self, name: unicode) -> None: ...

    def setTypeID(self, typeID: int) -> None: ...

    def toString(self) -> unicode: ...

    @overload
    def wait(self) -> None: ...

    @overload
    def wait(self, __a0: long) -> None: ...

    @overload
    def wait(self, __a0: long, __a1: int) -> None: ...

    @property
    def ID(self) -> int: ...

    @ID.setter
    def ID(self, value: int) -> None: ...

    @property
    def address(self) -> int: ...

    @property
    def name(self) -> unicode: ...

    @name.setter
    def name(self, value: unicode) -> None: ...

    @property
    def size(self) -> int: ...

    @property
    def typeID(self) -> int: ...

    @typeID.setter
    def typeID(self, value: int) -> None: ...
