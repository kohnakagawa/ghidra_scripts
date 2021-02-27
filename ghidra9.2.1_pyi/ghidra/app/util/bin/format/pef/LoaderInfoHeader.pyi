from typing import List
import ghidra.app.util.bin
import ghidra.app.util.bin.format.pef
import ghidra.program.model.data
import java.lang


class LoaderInfoHeader(object, ghidra.app.util.bin.StructConverter):
    """
    See Apple's -- PEFBinaryFormat.h

    """

    ASCII: ghidra.program.model.data.DataType = char
    BYTE: ghidra.program.model.data.DataType = byte
    DWORD: ghidra.program.model.data.DataType = dword
    IBO32: ghidra.program.model.data.DataType = ImageBaseOffset32
    POINTER: ghidra.program.model.data.DataType = pointer
    QWORD: ghidra.program.model.data.DataType = qword
    SIZEOF: int = 56
    STRING: ghidra.program.model.data.DataType = string
    UTF16: ghidra.program.model.data.DataType = unicode
    UTF8: ghidra.program.model.data.DataType = string-utf8
    VOID: ghidra.program.model.data.DataType = void
    WORD: ghidra.program.model.data.DataType = word







    def equals(self, __a0: object) -> bool: ...

    def findLibrary(self, symbolIndex: int) -> ghidra.app.util.bin.format.pef.ImportedLibrary:
        """
        Finds the PEF library that contains the specified imported symbol index.
        @param symbolIndex the imported symbol index
        @return PEF library that contains the specified imported symbol index
        """
        ...

    def getClass(self) -> java.lang.Class: ...

    def getExportHashOffset(self) -> int:
        """
        The exportHashOffset field (4 bytes) indicates the offset
         (in bytes) from the beginning of the loader section
         to the start of the export hash table. The hash table should be 4-byte aligned
         with padding added if necessary.
        @return offset to the export hash table
        """
        ...

    def getExportHashTablePower(self) -> int:
        """
        The exportHashTablePower field (4 bytes) indicates the
         number of hash index values (that is, the number of entries in the
         hash table). The number of entries is specified as a power of two. For example,
         a value of 0 indicates one entry, while a value of 2 indicates four entries. If
         no exports exist, the hash table still contains one entry, and the value of this
         field is 0.
        @return number of hash index values
        """
        ...

    def getExportedHashSlots(self) -> List[ghidra.app.util.bin.format.pef.ExportedSymbolHashSlot]: ...

    def getExportedSymbolCount(self) -> int:
        """
        The exportedSymbolCount field (4 bytes) indicates the number of
         symbols exported from this container.
        @return number of symbols exported from this container
        """
        ...

    def getExportedSymbolKeys(self) -> List[ghidra.app.util.bin.format.pef.ExportedSymbolKey]: ...

    def getExportedSymbols(self) -> List[ghidra.app.util.bin.format.pef.ExportedSymbol]: ...

    def getImportedLibraries(self) -> List[ghidra.app.util.bin.format.pef.ImportedLibrary]: ...

    def getImportedLibraryCount(self) -> int:
        """
        The importedLibraryCount field (4 bytes) indicates the
         number of imported libraries.
        @return number of imported libraries
        """
        ...

    def getImportedSymbols(self) -> List[ghidra.app.util.bin.format.pef.ImportedSymbol]: ...

    def getInitOffset(self) -> int:
        """
        The initOffset field (4 bytes) indicates the offset (in bytes) from the
         beginning of the section to the initialization function's transition vector.
        @return offset to initialization function's transition vector
        """
        ...

    def getInitSection(self) -> int:
        """
        The initSection field (4 bytes) contains the number of the
         section containing the initialization function's transition
         vector. If no initialization function exists, this field is set to -1.
        @return number of the section containing the initialization function's transition vector
        """
        ...

    def getLoaderStringsOffset(self) -> int:
        """
        The loaderStringsOffset field (4 bytes) indicates the offset
         (in bytes) from the beginning of the loader
         section to the start of the loader string table.
        @return offset to the loader string table
        """
        ...

    def getMainOffset(self) -> int:
        """
        The mainOffset field (4 bytes) indicates the offset (in bytes) from the
         beginning of the section to the main symbol.
        @return offset to the main symbol
        """
        ...

    def getMainSection(self) -> int:
        """
        The mainSection field (4 bytes) specifies the number
         of the section in this container that contains the main
         symbol. If the fragment does not have a main symbol,
         this field is set to -1.
        @return number of section containing main symbol
        """
        ...

    def getRelocInstrOffset(self) -> int:
        """
        The relocInstrOffset field (4 bytes) indicates the offset (in bytes) from the
         beginning of the loader section to the start of the relocations area.
        @return offset to the relocations
        """
        ...

    def getRelocSectionCount(self) -> int:
        """
        The relocSectionCount field (4 bytes) indicates the
         number of sections containing load-time relocations.
        @return number of sections containing load-time relocations
        """
        ...

    def getRelocations(self) -> List[ghidra.app.util.bin.format.pef.LoaderRelocationHeader]: ...

    def getSection(self) -> ghidra.app.util.bin.format.pef.SectionHeader:
        """
        Returns the section corresponding to this loader.
        @return the section corresponding to this loader
        """
        ...

    def getTermOffset(self) -> int:
        """
        The termOffset field (4 bytes) indicates the offset
         (in bytes) from the beginning of the section to the termination routine's
         transition vector.
        @return offset to termination routine's transition vector
        """
        ...

    def getTermSection(self) -> int:
        """
        The termSection field (4 bytes) contains the number of the section containing
         the termination routine's transition vector. If no termination routine exists,
         this field is set to -1.
        @return number of the section containing the termination routine's transition vector
        """
        ...

    def getTotalImportedSymbolCount(self) -> int:
        """
        The totalImportedSymbolCount field (4 bytes)
         indicates the total number of imported symbols.
        @return number of imported symbols
        """
        ...

    def hashCode(self) -> int: ...

    def notify(self) -> None: ...

    def notifyAll(self) -> None: ...

    def toDataType(self) -> ghidra.program.model.data.DataType: ...

    def toString(self) -> unicode: ...

    @overload
    def wait(self) -> None: ...

    @overload
    def wait(self, __a0: long) -> None: ...

    @overload
    def wait(self, __a0: long, __a1: int) -> None: ...

    @property
    def exportHashOffset(self) -> int: ...

    @property
    def exportHashTablePower(self) -> int: ...

    @property
    def exportedHashSlots(self) -> List[object]: ...

    @property
    def exportedSymbolCount(self) -> int: ...

    @property
    def exportedSymbolKeys(self) -> List[object]: ...

    @property
    def exportedSymbols(self) -> List[object]: ...

    @property
    def importedLibraries(self) -> List[object]: ...

    @property
    def importedLibraryCount(self) -> int: ...

    @property
    def importedSymbols(self) -> List[object]: ...

    @property
    def initOffset(self) -> int: ...

    @property
    def initSection(self) -> int: ...

    @property
    def loaderStringsOffset(self) -> int: ...

    @property
    def mainOffset(self) -> int: ...

    @property
    def mainSection(self) -> int: ...

    @property
    def relocInstrOffset(self) -> int: ...

    @property
    def relocSectionCount(self) -> int: ...

    @property
    def relocations(self) -> List[object]: ...

    @property
    def section(self) -> ghidra.app.util.bin.format.pef.SectionHeader: ...

    @property
    def termOffset(self) -> int: ...

    @property
    def termSection(self) -> int: ...

    @property
    def totalImportedSymbolCount(self) -> int: ...
