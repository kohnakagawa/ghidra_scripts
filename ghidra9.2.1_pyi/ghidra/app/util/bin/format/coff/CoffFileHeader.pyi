from typing import List
import ghidra.app.util.bin
import ghidra.app.util.bin.format.coff
import ghidra.program.model.data
import ghidra.util.task
import java.lang


class CoffFileHeader(object, ghidra.app.util.bin.StructConverter):
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



    def __init__(self, provider: ghidra.app.util.bin.ByteProvider): ...



    def equals(self, __a0: object) -> bool: ...

    def getClass(self) -> java.lang.Class: ...

    def getFlags(self) -> int:
        """
        Returns the flags about this COFF.
        @return the flags about this COFF
        """
        ...

    def getImageBase(self, isWindowsPlatform: bool) -> long:
        """
        Returns the image base.
        @return the image base
        """
        ...

    def getMachine(self) -> int: ...

    def getMachineName(self) -> unicode:
        """
        Returns the machine name.
        @return the machine name
        """
        ...

    def getMagic(self) -> int:
        """
        Returns the magic COFF file identifier.
        @return the magic COFF file identifier
        """
        ...

    def getOptionalHeader(self) -> ghidra.app.util.bin.format.coff.AoutHeader:
        """
        Returns the a.out optional header.
         This return value may be null.
        @return the a.out optional header
        """
        ...

    def getOptionalHeaderSize(self) -> int:
        """
        Returns the size in bytes of the optional header.
         The optional header immediately follows the file header
         and immediately proceeds the sections headers.
        @return the size in bytes of the optional header
        """
        ...

    def getSectionCount(self) -> int:
        """
        Returns the number of sections in this COFF file.
        @return the number of sections in this COFF file
        """
        ...

    def getSections(self) -> List[ghidra.app.util.bin.format.coff.CoffSectionHeader]:
        """
        Returns the sections in this COFF header.
        @return the sections in this COFF header
        """
        ...

    def getSymbolAtIndex(self, index: long) -> ghidra.app.util.bin.format.coff.CoffSymbol: ...

    def getSymbolTableEntries(self) -> int:
        """
        Returns the number of symbols in the symbol table.
        @return the number of symbols in the symbol table
        """
        ...

    def getSymbolTablePointer(self) -> int:
        """
        Returns the file offset to the symbol table.
        @return the file offset to the symbol table
        """
        ...

    def getSymbols(self) -> List[ghidra.app.util.bin.format.coff.CoffSymbol]:
        """
        Returns the symbols in this COFF header.
        @return the symbols in this COFF header
        """
        ...

    def getTargetID(self) -> int:
        """
        Returns the specific target id
        @return the specific target id
        """
        ...

    def getTimestamp(self) -> int:
        """
        Returns the time stamp of when this file was created.
        @return the time stamp of when this file was created
        """
        ...

    def hashCode(self) -> int: ...

    def notify(self) -> None: ...

    def notifyAll(self) -> None: ...

    def parse(self, provider: ghidra.app.util.bin.ByteProvider, monitor: ghidra.util.task.TaskMonitor) -> None:
        """
        Finishes the parsing of this file header.
        @param monitor the task monitor
        @throws IOException if an i/o error occurs
        """
        ...

    def parseSectionHeaders(self, provider: ghidra.app.util.bin.ByteProvider) -> None:
        """
        Read just the section headers, not including line numbers and relocations
        @param provider
        @throws IOException
        """
        ...

    def sizeof(self) -> int:
        """
        Returns the size (in bytes) of this COFF file header.
        @return the size (in bytes) of this COFF file header
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
    def flags(self) -> int: ...

    @property
    def machine(self) -> int: ...

    @property
    def machineName(self) -> unicode: ...

    @property
    def magic(self) -> int: ...

    @property
    def optionalHeader(self) -> ghidra.app.util.bin.format.coff.AoutHeader: ...

    @property
    def optionalHeaderSize(self) -> int: ...

    @property
    def sectionCount(self) -> int: ...

    @property
    def sections(self) -> List[object]: ...

    @property
    def symbolTableEntries(self) -> int: ...

    @property
    def symbolTablePointer(self) -> int: ...

    @property
    def symbols(self) -> List[object]: ...

    @property
    def targetID(self) -> int: ...

    @property
    def timestamp(self) -> int: ...
