from typing import List
import ghidra.app.util.bin.format.dwarf4
import java.lang


class DWARFLocation(object):




    def __init__(self, addressRange: ghidra.app.util.bin.format.dwarf4.DWARFRange, location: List[int]):
        """
        Create a Location given an address range and location expression.
        @param addressRange memory range of this location
        @param location byte array holding location expression
        """
        ...



    def equals(self, __a0: object) -> bool: ...

    def getClass(self) -> java.lang.Class: ...

    def getLocation(self) -> List[int]: ...

    def getRange(self) -> ghidra.app.util.bin.format.dwarf4.DWARFRange: ...

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
    def location(self) -> List[int]: ...

    @property
    def range(self) -> ghidra.app.util.bin.format.dwarf4.DWARFRange: ...
