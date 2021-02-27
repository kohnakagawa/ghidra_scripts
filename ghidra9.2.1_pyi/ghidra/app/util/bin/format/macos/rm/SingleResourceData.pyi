from typing import List
import java.lang


class SingleResourceData(object):
    """
    Format of resource data for a single resource.
    """





    def __init__(self, reader: ghidra.app.util.bin.BinaryReader): ...



    def equals(self, __a0: object) -> bool: ...

    def getClass(self) -> java.lang.Class: ...

    def getData(self) -> List[int]:
        """
        Returns the resource data for this resource.
        @return the resource data for this resource
        """
        ...

    def getLength(self) -> int:
        """
        Returns the length of the following resource.
        @return the length of the following resource
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
    def data(self) -> List[int]: ...

    @property
    def length(self) -> int: ...
