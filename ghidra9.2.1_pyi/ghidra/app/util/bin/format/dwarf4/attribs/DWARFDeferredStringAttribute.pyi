import ghidra.app.util.bin.format.dwarf4.attribs
import ghidra.app.util.bin.format.dwarf4.next
import java.lang


class DWARFDeferredStringAttribute(ghidra.app.util.bin.format.dwarf4.attribs.DWARFStringAttribute):
    """
    DWARF string attribute, where getting the value from the string table is deferred
     until requested for the first time.
    """





    def __init__(self, offset: long): ...



    def equals(self, __a0: object) -> bool: ...

    def getClass(self) -> java.lang.Class: ...

    def getValue(self, stringTable: ghidra.app.util.bin.format.dwarf4.next.StringTable) -> unicode: ...

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
