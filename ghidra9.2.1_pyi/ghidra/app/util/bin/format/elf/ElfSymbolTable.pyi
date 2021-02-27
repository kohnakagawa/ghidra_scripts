from typing import List
import ghidra.app.util.bin
import ghidra.app.util.bin.format.elf
import ghidra.program.model.data
import ghidra.util
import java.lang


class ElfSymbolTable(object, ghidra.app.util.bin.format.elf.ElfFileSection, ghidra.app.util.bin.ByteArrayConverter):
    """
    A container class to hold ELF symbols.
    """

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



    def addSymbol(self, symbol: ghidra.app.util.bin.format.elf.ElfSymbol) -> None:
        """
        Adds the specified symbol into this symbol table.
        @param symbol the new symbol to add
        """
        ...

    def equals(self, __a0: object) -> bool: ...

    def getAddressOffset(self) -> long: ...

    def getClass(self) -> java.lang.Class: ...

    def getEntrySize(self) -> int: ...

    def getFileOffset(self) -> long: ...

    def getGlobalSymbols(self) -> List[ghidra.app.util.bin.format.elf.ElfSymbol]:
        """
        Returns all of the global symbols.
        @return all of the global symbols
        """
        ...

    def getLength(self) -> long: ...

    def getSourceFiles(self) -> List[unicode]:
        """
        Returns all of the sources file names.
        @return all of the sources file names
        """
        ...

    def getStringTable(self) -> ghidra.app.util.bin.format.elf.ElfStringTable:
        """
        Returns the associated string table section.
        @return the associated string table section
        """
        ...

    def getSymbolAt(self, addr: long) -> ghidra.app.util.bin.format.elf.ElfSymbol:
        """
        Returns the symbol at the specified address.
        @param addr the symbol address
        @return the symbol at the specified address
        """
        ...

    def getSymbolCount(self) -> int:
        """
        @return number of symbols
        """
        ...

    def getSymbolIndex(self, symbol: ghidra.app.util.bin.format.elf.ElfSymbol) -> int:
        """
        Returns the index of the specified symbol in this
         symbol table.
        @param symbol the symbol
        @return the index of the specified symbol
        """
        ...

    def getSymbols(self) -> List[ghidra.app.util.bin.format.elf.ElfSymbol]:
        """
        Returns all of the symbols defined in this symbol table.
        @return all of the symbols defined in this symbol table
        """
        ...

    def getTableSectionHeader(self) -> ghidra.app.util.bin.format.elf.ElfSectionHeader:
        """
        Get the section header which corresponds to this table, or null
         if only associated with a dynamic table entry
        @return symbol table section header or null
        """
        ...

    def hashCode(self) -> int: ...

    def isDynamic(self) -> bool:
        """
        Returns true if this is the dynamic symbol table
        @return true if this is the dynamic symbol table
        """
        ...

    def notify(self) -> None: ...

    def notifyAll(self) -> None: ...

    def toBytes(self, dc: ghidra.util.DataConverter) -> List[int]:
        """
        @see ghidra.app.util.bin.ByteArrayConverter#toBytes(ghidra.util.DataConverter)
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
    def dynamic(self) -> bool: ...

    @property
    def entrySize(self) -> int: ...

    @property
    def fileOffset(self) -> long: ...

    @property
    def globalSymbols(self) -> List[ghidra.app.util.bin.format.elf.ElfSymbol]: ...

    @property
    def length(self) -> long: ...

    @property
    def sourceFiles(self) -> List[unicode]: ...

    @property
    def stringTable(self) -> ghidra.app.util.bin.format.elf.ElfStringTable: ...

    @property
    def symbolCount(self) -> int: ...

    @property
    def symbols(self) -> List[ghidra.app.util.bin.format.elf.ElfSymbol]: ...

    @property
    def tableSectionHeader(self) -> ghidra.app.util.bin.format.elf.ElfSectionHeader: ...
