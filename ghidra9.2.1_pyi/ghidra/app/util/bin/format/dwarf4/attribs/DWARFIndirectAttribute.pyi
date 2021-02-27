import ghidra.app.util.bin.format.dwarf4.attribs
import ghidra.app.util.bin.format.dwarf4.encoding
import java.lang


class DWARFIndirectAttribute(object, ghidra.app.util.bin.format.dwarf4.attribs.DWARFAttributeValue):
    """
    DWARF indirect attribute.

     Holds a reference to an actual DWARFAttributeValue instance and its DWARFForm.

     Used with DW_FORM_indirect attributes that encode the DWARFForm of the attribute
     value inline instead of in the DIE's DWARFAbbreviation.

    """





    def __init__(self, value: ghidra.app.util.bin.format.dwarf4.attribs.DWARFAttributeValue, form: ghidra.app.util.bin.format.dwarf4.encoding.DWARFForm): ...



    def equals(self, __a0: object) -> bool: ...

    def getClass(self) -> java.lang.Class: ...

    def getForm(self) -> ghidra.app.util.bin.format.dwarf4.encoding.DWARFForm: ...

    def getValue(self) -> ghidra.app.util.bin.format.dwarf4.attribs.DWARFAttributeValue: ...

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
    def form(self) -> ghidra.app.util.bin.format.dwarf4.encoding.DWARFForm: ...

    @property
    def value(self) -> ghidra.app.util.bin.format.dwarf4.attribs.DWARFAttributeValue: ...
