import ghidra.app.util.bin
import ghidra.app.util.bin.format
import ghidra.app.util.bin.format.elf
import ghidra.program.model.data
import java.lang


class ElfStringTable(object, ghidra.app.util.bin.format.elf.ElfFileSection):
    ASCII: ghidra.program.model.data.DataType = char
    BYTE: ghidra.program.model.data.DataType = byte
    DWORD: ghidra.program.model.data.DataType = dword
    IBO32: ghidra.program.model.data.DataType = ImageBaseOffset32
    POINTER: ghidra.program.model.data.DataType = pointer
    QWORD: ghidra.program.model.data.DataType = qword
    STRING: ghidra.program.model.data.DataType = string
    UTF16: ghidra.program.model.data.DataType = unicode
    UTF8: ghidra.program.model.data.DataType = string-utf8
    VOID: ghidra.program.model.data.DataType = void
    WORD: ghidra.program.model.data.DataType = word



    def __init__(self):
        """
        DO NOT USE THIS CONSTRUCTOR, USE create*(GenericFactory ...) FACTORY METHODS INSTEAD.
        """
        ...



    @staticmethod
    def createElfStringTable(reader: ghidra.app.util.bin.format.FactoryBundledWithBinaryReader, header: ghidra.app.util.bin.format.elf.ElfHeader, stringTableSection: ghidra.app.util.bin.format.elf.ElfSectionHeader, fileOffset: long, addrOffset: long, length: long) -> ghidra.app.util.bin.format.elf.ElfStringTable:
        """
        Create and parse an Elf string table
        @param reader the binary reader containing the elf string table
        @param header elf header
        @param stringTableSection string table section header or null if associated with a dynamic table entry
        @param fileOffset symbol table file offset
        @param addrOffset memory address of symbol table (should already be adjusted for prelink)
        @param length length of symbol table in bytes of -1 if unknown
        @return Elf string table object
        @throws IOException
        """
        ...

    def equals(self, __a0: object) -> bool: ...

    def getAddressOffset(self) -> long: ...

    def getClass(self) -> java.lang.Class: ...

    def getEntrySize(self) -> int: ...

    def getFileOffset(self) -> long: ...

    def getLength(self) -> long: ...

    def getTableSectionHeader(self) -> ghidra.app.util.bin.format.elf.ElfSectionHeader:
        """
        Get section header which corresponds to this table, or null
         if only associated with a dynamic table entry
        @return string table section header or null
        """
        ...

    def hashCode(self) -> int: ...

    def notify(self) -> None: ...

    def notifyAll(self) -> None: ...

    def readString(self, reader: ghidra.app.util.bin.BinaryReader, stringOffset: long) -> unicode:
        """
        Read string from table at specified relative table offset
        @param reader
        @param stringOffset table relative string offset
        @return string or null on error
        """
        ...

    def toDataType(self) -> ghidra.program.model.data.DataType: ...

    def toString(self) -> unicode: ...

    @overload
    def wait(self) -> None: ...

    @overload
    def wait(self, __a0: long) -> None: ...

    @overload
    def wait(self, __a0: long, __a1: int) -> None: ...

    @property
    def addressOffset(self) -> long: ...

    @property
    def entrySize(self) -> int: ...

    @property
    def fileOffset(self) -> long: ...

    @property
    def length(self) -> long: ...

    @property
    def tableSectionHeader(self) -> ghidra.app.util.bin.format.elf.ElfSectionHeader: ...
