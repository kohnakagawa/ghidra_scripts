from typing import List
import ghidra.app.util.bin.format.ne
import java.lang


class ResourceType(object):
    """
    An implementation of the TTYPEINFO structure.
    """

    RT_ACCELERATOR: int = 9
    RT_BITMAP: int = 2
    RT_CURSOR: int = 1
    RT_DIALOG: int = 5
    RT_FONT: int = 8
    RT_FONTDIR: int = 7
    RT_GROUP_CURSOR: int = 12
    RT_GROUP_ICON: int = 14
    RT_ICON: int = 3
    RT_MENU: int = 4
    RT_MESSAGETABLE: int = 11
    RT_RCDATA: int = 10
    RT_STRING: int = 6
    RT_VERSION: int = 16







    def equals(self, __a0: object) -> bool: ...

    def getClass(self) -> java.lang.Class: ...

    def getCount(self) -> int:
        """
        Returns the number of resources of this type.
        @return the number of resources of this type
        """
        ...

    def getReserved(self) -> int:
        """
        Returns the reserved value (purpose is unknown).
        @return the reserved value
        """
        ...

    def getResources(self) -> List[ghidra.app.util.bin.format.ne.Resource]:
        """
        Returns the array of resources of this type.
        @return the array of resources of this type
        """
        ...

    def getTypeID(self) -> int:
        """
        Returns the resource type ID.
        @return the resource type ID
        """
        ...

    def hashCode(self) -> int: ...

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
    def count(self) -> int: ...

    @property
    def reserved(self) -> int: ...

    @property
    def resources(self) -> List[ghidra.app.util.bin.format.ne.Resource]: ...

    @property
    def typeID(self) -> int: ...
