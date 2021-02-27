import ghidra.app.util.bin.format.dwarf4.attribs
import java.lang


class DWARFBooleanAttribute(object, ghidra.app.util.bin.format.dwarf4.attribs.DWARFAttributeValue):
    """
    DWARF boolean attribute.
    """

    FALSE: ghidra.app.util.bin.format.dwarf4.attribs.DWARFBooleanAttribute = DWARFBooleanAttribute: false
    TRUE: ghidra.app.util.bin.format.dwarf4.attribs.DWARFBooleanAttribute = DWARFBooleanAttribute: true



    def __init__(self, value: bool): ...



    def equals(self, __a0: object) -> bool: ...

    @staticmethod
    def get(b: bool) -> ghidra.app.util.bin.format.dwarf4.attribs.DWARFBooleanAttribute: ...

    def getClass(self) -> java.lang.Class: ...

    def getValue(self) -> bool: ...

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
    def value(self) -> bool: ...
