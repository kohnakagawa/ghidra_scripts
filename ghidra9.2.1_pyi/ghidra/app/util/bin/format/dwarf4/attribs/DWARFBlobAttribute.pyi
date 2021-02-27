from typing import List
import ghidra.app.util.bin.format.dwarf4.attribs
import java.lang


class DWARFBlobAttribute(object, ghidra.app.util.bin.format.dwarf4.attribs.DWARFAttributeValue):
    """
    DWARF attribute with binary bytes.
    """





    def __init__(self, bytes: List[int]): ...



    def equals(self, __a0: object) -> bool: ...

    def getBytes(self) -> List[int]: ...

    def getClass(self) -> java.lang.Class: ...

    def getLength(self) -> int: ...

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
    def bytes(self) -> List[int]: ...

    @property
    def length(self) -> int: ...
