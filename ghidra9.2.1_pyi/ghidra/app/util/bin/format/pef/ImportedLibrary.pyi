import ghidra.app.util.bin
import ghidra.program.model.data
import java.lang


class ImportedLibrary(object, ghidra.app.util.bin.StructConverter):
    """
    Imported Libraries

     See Apple's -- PEFBinaryFormat.h

     struct PEFImportedLibrary {
       UInt32              nameOffset;             // Loader string table offset of library's name.
       UInt32              oldImpVersion;          // Oldest compatible implementation version.
       UInt32              currentVersion;         // Current version at build time.
       UInt32              importedSymbolCount;    // Imported symbol count for this library.
       UInt32              firstImportedSymbol;    // Index of first imported symbol from this library.
       UInt8               options;                // Option bits for this library.
       UInt8               reservedA;              // Reserved, must be zero.
       UInt16              reservedB;              // Reserved, must be zero.
     };

    """

    ASCII: ghidra.program.model.data.DataType = char
    BYTE: ghidra.program.model.data.DataType = byte
    DWORD: ghidra.program.model.data.DataType = dword
    IBO32: ghidra.program.model.data.DataType = ImageBaseOffset32
    OPTION_kPEFInitLibBeforeMask: int = 128
    OPTION_kPEFWeakImportLibMask: int = 64
    POINTER: ghidra.program.model.data.DataType = pointer
    QWORD: ghidra.program.model.data.DataType = qword
    SIZEOF: int = 24
    STRING: ghidra.program.model.data.DataType = string
    UTF16: ghidra.program.model.data.DataType = unicode
    UTF8: ghidra.program.model.data.DataType = string-utf8
    VOID: ghidra.program.model.data.DataType = void
    WORD: ghidra.program.model.data.DataType = word







    def equals(self, __a0: object) -> bool: ...

    def getClass(self) -> java.lang.Class: ...

    def getCurrentVersion(self) -> int:
        """
        The oldImpVersion and currentVersion fields (4 bytes each) provide version
         information for checking the compatibility of the imported library.
        @return current version at build time
        """
        ...

    def getFirstImportedSymbol(self) -> int:
        """
        The firstImportedSymbol field (4 bytes) holds the (zero-based) index of the
         first entry in the imported symbol table for this library.
        @return index of first imported symbol from this library
        """
        ...

    def getImportedSymbolCount(self) -> int:
        """
        The importedSymbolCount field (4 bytes) indicates the number of symbols
         imported from this library.
        @return imported symbol count for this library
        """
        ...

    def getName(self) -> unicode:
        """
        Returns the name of the library being imported.
        @return the name of the library being imported
        """
        ...

    def getNameOffset(self) -> int:
        """
        The nameOffset field (4 bytes) indicates the offset (in bytes) from the beginning
         of the loader string table to the start of the null-terminated library name.
        @return loader string table offset of library's name.
        """
        ...

    def getOldImpVersion(self) -> int:
        """
        The oldImpVersion and currentVersion fields (4 bytes each) provide version
         information for checking the compatibility of the imported library.
        @return oldest compatible implementation version
        """
        ...

    def getOptions(self) -> int:
        """
        The options byte contains bit flag information as follows:
         <p>
         The high-order bit (mask 0x80) controls the order that the import libraries
         are initialized. If set to 0, the default initialization order is used, which
         specifies that the Code Fragment Manager should try to initialize the
         import library before the fragment that imports it. When set to 1, the import
         library must be initialized before the client fragment.
         <p>
         The next bit (mask 0x40) controls whether the import library is weak.
         When set to 1 (weak import), the Code Fragment Manager continues
         preparation of the client fragment (and does not generate an error) even if
         the import library cannot be found. If the import library is not found, all
         imported symbols from that library have their addresses set to 0. You can
         use this information to determine whether a weak import library is actually
         present.
        @return option bits for this library
        """
        ...

    def getReservedA(self) -> int:
        """
        Reserved, must be set to zero (0).
        @return reserved, must be set to zero (0)
        """
        ...

    def getReservedB(self) -> int:
        """
        Reserved, must be set to zero (0).
        @return reserved, must be set to zero (0)
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
    def currentVersion(self) -> int: ...

    @property
    def firstImportedSymbol(self) -> int: ...

    @property
    def importedSymbolCount(self) -> int: ...

    @property
    def name(self) -> unicode: ...

    @property
    def nameOffset(self) -> int: ...

    @property
    def oldImpVersion(self) -> int: ...

    @property
    def options(self) -> int: ...

    @property
    def reservedA(self) -> int: ...

    @property
    def reservedB(self) -> int: ...
