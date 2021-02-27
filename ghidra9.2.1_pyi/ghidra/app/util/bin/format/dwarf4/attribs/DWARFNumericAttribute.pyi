import ghidra.app.util.bin.format.dwarf4.attribs
import java.lang


class DWARFNumericAttribute(object, ghidra.app.util.bin.format.dwarf4.attribs.DWARFAttributeValue):
    """
    DWARF numeric attribute.

     Use this class instead of DWARFAmbigNumericAttribute when the signed-ness
     of the raw value is known when deserializing the attribute from a stream.

     Use DWARFAmbigNumericAttribute when the signed-ness of the raw value is only know
     to the code that is using the attribute value.
    """





    def __init__(self, value: long): ...



    def equals(self, __a0: object) -> bool: ...

    def getClass(self) -> java.lang.Class: ...

    def getUnsignedValue(self) -> long: ...

    def getValue(self) -> long: ...

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
    def unsignedValue(self) -> long: ...

    @property
    def value(self) -> long: ...
