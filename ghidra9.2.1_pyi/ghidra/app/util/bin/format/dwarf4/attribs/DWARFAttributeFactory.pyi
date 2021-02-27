import ghidra.app.util.bin
import ghidra.app.util.bin.format.dwarf4
import ghidra.app.util.bin.format.dwarf4.attribs
import ghidra.app.util.bin.format.dwarf4.encoding
import java.lang


class DWARFAttributeFactory(object):
    """
    A factory for deserializing DWARFAttributeValue from
     a stream.
    """

    MAX_BLOCK4_SIZE: int = 1048576



    def __init__(self, prog: ghidra.app.util.bin.format.dwarf4.next.DWARFProgram): ...



    def equals(self, __a0: object) -> bool: ...

    def getClass(self) -> java.lang.Class: ...

    def hashCode(self) -> int: ...

    def notify(self) -> None: ...

    def notifyAll(self) -> None: ...

    def read(self, reader: ghidra.app.util.bin.BinaryReader, unit: ghidra.app.util.bin.format.dwarf4.DWARFCompilationUnit, form: ghidra.app.util.bin.format.dwarf4.encoding.DWARFForm) -> ghidra.app.util.bin.format.dwarf4.attribs.DWARFAttributeValue:
        """
        Read from the given BinaryReader based on the type of DWARFForm that is given.
        @param reader BinaryReader pointing to the value to read
        @param unit the current compilation unit
        @param form DWARFForm type defining the type of value to read
        @return Object representing the value that was read
        @throws IOException if an I/O error occurs
        """
        ...

    def toString(self) -> unicode: ...

    @overload
    def wait(self) -> None: ...

    @overload
    def wait(self, __a0: long) -> None: ...

    @overload
    def wait(self, __a0: long, __a1: int) -> None: ...
