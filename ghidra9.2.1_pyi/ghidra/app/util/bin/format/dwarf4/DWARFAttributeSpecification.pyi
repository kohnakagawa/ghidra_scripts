import ghidra.app.util.bin
import ghidra.app.util.bin.format.dwarf4
import ghidra.app.util.bin.format.dwarf4.encoding
import java.lang


class DWARFAttributeSpecification(object):
    """
    Information about a single DWARF attribute.
    """





    def __init__(self, attribute: int, attributeForm: ghidra.app.util.bin.format.dwarf4.encoding.DWARFForm): ...



    def equals(self, obj: object) -> bool: ...

    def getAttribute(self) -> int:
        """
        Get the attribute of the attribute specification.
        @return the attribute value
        """
        ...

    def getAttributeForm(self) -> ghidra.app.util.bin.format.dwarf4.encoding.DWARFForm:
        """
        Get the form of the attribute specification.
        @return the form value
        """
        ...

    def getClass(self) -> java.lang.Class: ...

    def hashCode(self) -> int: ...

    def notify(self) -> None: ...

    def notifyAll(self) -> None: ...

    @staticmethod
    def read(reader: ghidra.app.util.bin.BinaryReader) -> ghidra.app.util.bin.format.dwarf4.DWARFAttributeSpecification:
        """
        Reads a {@link DWARFAttributeSpecification} instance from the {@link BinaryReader reader}.
         <p>
         Returns a null if its a end-of-list marker.
         <p>
        @param reader
        @return
        @throws IOException
        """
        ...

    def toString(self) -> unicode: ...

    @overload
    def wait(self) -> None: ...

    @overload
    def wait(self, __a0: long) -> None: ...

    @overload
    def wait(self, __a0: long, __a1: int) -> None: ...

    @property
    def attribute(self) -> int: ...

    @property
    def attributeForm(self) -> ghidra.app.util.bin.format.dwarf4.encoding.DWARFForm: ...
