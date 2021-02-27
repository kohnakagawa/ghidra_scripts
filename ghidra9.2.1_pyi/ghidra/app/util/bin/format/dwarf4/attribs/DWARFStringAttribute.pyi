import ghidra.app.util.bin.format.dwarf4.attribs
import ghidra.app.util.bin.format.dwarf4.next
import java.lang


class DWARFStringAttribute(object, ghidra.app.util.bin.format.dwarf4.attribs.DWARFAttributeValue):
    """
    DWARF string attribute.
    """





    def __init__(self, value: unicode): ...



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
