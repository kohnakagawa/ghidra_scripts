from typing import List
import ghidra.app.util.bin.format.ne
import java.lang


class ResourceTable(object):
    """
    A class for storing the new-executable resource table.
     A resource table contains all of the supported types
     of resources.
    """









    def equals(self, __a0: object) -> bool: ...

    def getAlignmentShiftCount(self) -> int:
        """
        Returns the alignment shift count.
         Some resources offsets and lengths are stored bit shifted.
        @return the alignment shift count
        """
        ...

    def getClass(self) -> java.lang.Class: ...

    def getIndex(self) -> int:
        """
        Returns the byte index where the resource table begins,
         relative to the beginning of the file.
        @return the byte index where the resource table begins
        """
        ...

    def getResourceNames(self) -> List[ghidra.app.util.bin.format.ne.ResourceName]:
        """
        Returns the array of resources names.
        @return the array of resources names
        """
        ...

    def getResourceTypes(self) -> List[ghidra.app.util.bin.format.ne.ResourceType]:
        """
        Returns the array of resource types.
        @return the array of resource types
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
    def alignmentShiftCount(self) -> int: ...

    @property
    def index(self) -> int: ...

    @property
    def resourceNames(self) -> List[ghidra.app.util.bin.format.ne.ResourceName]: ...

    @property
    def resourceTypes(self) -> List[ghidra.app.util.bin.format.ne.ResourceType]: ...
