from typing import List
import ghidra.app.util.bin
import ghidra.app.util.bin.format
import ghidra.app.util.bin.format.pe.debug
import ghidra.program.model.data
import java.lang


class DebugCodeViewSymbolTable(object, ghidra.app.util.bin.StructConverter):
    """
    A class to represent the Object Module Format (OMF)
     code view symbol table.
    """

    ASCII: ghidra.program.model.data.DataType = char
    BYTE: ghidra.program.model.data.DataType = byte
    DWORD: ghidra.program.model.data.DataType = dword
    IBO32: ghidra.program.model.data.DataType = ImageBaseOffset32
    MAGIC_N1_12: int = 1311846720
    MAGIC_N1_13: int = 1311846640
    MAGIC_NB_09: int = 1312960569
    MAGIC_NB_11: int = 1312960817
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



    def equals(self, __a0: object) -> bool: ...

    def getClass(self) -> java.lang.Class: ...

    def getMagic(self) -> List[int]: ...

    def getOMFAlignSym(self) -> List[ghidra.app.util.bin.format.pe.debug.OMFAlignSym]:
        """
        Returns the OMF Align Symbols.
        @return the OMF Align Symbols
        """
        ...

    def getOMFDirectoryEntries(self) -> List[ghidra.app.util.bin.format.pe.debug.OMFDirEntry]:
        """
        Returns the OMF directory entries.
        @return the OMF directory entries
        """
        ...

    def getOMFFiles(self) -> List[ghidra.app.util.bin.format.pe.debug.OMFFileIndex]:
        """
        Returns the OMF Source Files.
        @return the OMF Source Files
        """
        ...

    def getOMFGlobals(self) -> List[ghidra.app.util.bin.format.pe.debug.OMFGlobal]:
        """
        Returns the OMF globals.
        @return the OMF globals
        """
        ...

    def getOMFLibrary(self) -> ghidra.app.util.bin.format.pe.debug.OMFLibrary: ...

    def getOMFModules(self) -> List[ghidra.app.util.bin.format.pe.debug.OMFModule]:
        """
        Returns the OMF modules.
        @return the OMF modules
        """
        ...

    def getOMFSegMaps(self) -> List[ghidra.app.util.bin.format.pe.debug.OMFSegMap]:
        """
        Returns the OMF segment maps.
        @return the OMF segment maps
        """
        ...

    def getOMFSrcModules(self) -> List[ghidra.app.util.bin.format.pe.debug.OMFSrcModule]:
        """
        Returns the OMF Source Modules.
        @return the OMF Source Modules
        """
        ...

    def hashCode(self) -> int: ...

    @staticmethod
    def isMatch(reader: ghidra.app.util.bin.format.FactoryBundledWithBinaryReader, ptr: int) -> bool: ...

    def notify(self) -> None: ...

    def notifyAll(self) -> None: ...

    def toDataType(self) -> ghidra.program.model.data.DataType:
        """
        @see ghidra.app.util.bin.StructConverter#toDataType()
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
    def OMFAlignSym(self) -> List[object]: ...

    @property
    def OMFDirectoryEntries(self) -> List[object]: ...

    @property
    def OMFFiles(self) -> List[object]: ...

    @property
    def OMFGlobals(self) -> List[object]: ...

    @property
    def OMFLibrary(self) -> ghidra.app.util.bin.format.pe.debug.OMFLibrary: ...

    @property
    def OMFModules(self) -> List[object]: ...

    @property
    def OMFSegMaps(self) -> List[object]: ...

    @property
    def OMFSrcModules(self) -> List[object]: ...

    @property
    def magic(self) -> List[int]: ...
