from typing import List
import ghidra.app.util.bin.format
import ghidra.app.util.bin.format.pe
import ghidra.app.util.bin.format.pe.debug
import java.lang


class DebugDirectoryParser(object):
    """
    A helper class to parsing different types of
     debug information from a debug directory
    """

    IMAGE_DEBUG_TYPE_BORLAND: int = 9
    IMAGE_DEBUG_TYPE_CLSID: int = 11
    IMAGE_DEBUG_TYPE_CODEVIEW: int = 2
    IMAGE_DEBUG_TYPE_COFF: int = 1
    IMAGE_DEBUG_TYPE_EXCEPTION: int = 5
    IMAGE_DEBUG_TYPE_FIXUP: int = 6
    IMAGE_DEBUG_TYPE_FPO: int = 3
    IMAGE_DEBUG_TYPE_MISC: int = 4
    IMAGE_DEBUG_TYPE_OMAP_FROM_SRC: int = 8
    IMAGE_DEBUG_TYPE_OMAP_TO_SRC: int = 7
    IMAGE_DEBUG_TYPE_RESERVED10: int = 10
    IMAGE_DEBUG_TYPE_UNKNOWN: int = 0



    def __init__(self):
        """
        DO NOT USE THIS CONSTRUCTOR, USE create*(GenericFactory ...) FACTORY METHODS INSTEAD.
        """
        ...



    @staticmethod
    def createDebugDirectoryParser(reader: ghidra.app.util.bin.format.FactoryBundledWithBinaryReader, ptr: long, size: int, validator: ghidra.app.util.bin.format.pe.OffsetValidator) -> ghidra.app.util.bin.format.pe.debug.DebugDirectoryParser:
        """
        Constructs a new debug directory parser.
        @param reader the binary reader
        @param ptr the pointer into the binary reader
        @param size the size of the directory
        @param validator the validator for the directory
        @throws IOException if an I/O error occurs
        """
        ...

    def equals(self, __a0: object) -> bool: ...

    def getClass(self) -> java.lang.Class: ...

    def getDebugCOFFSymbolsHeader(self) -> ghidra.app.util.bin.format.pe.debug.DebugCOFFSymbolsHeader:
        """
        Returns the COFF debug information, or null if it does not exists.
        @return the COFF debug information
        """
        ...

    def getDebugCodeView(self) -> ghidra.app.util.bin.format.pe.debug.DebugCodeView:
        """
        Returns the CodeView debug information, or null if it does not exists.
        @return the CodeView debug information
        """
        ...

    def getDebugDirectories(self) -> List[ghidra.app.util.bin.format.pe.debug.DebugDirectory]: ...

    def getDebugFixup(self) -> ghidra.app.util.bin.format.pe.debug.DebugFixup:
        """
        Returns the Fixup debug information, or null if it does not exists.
        @return the Fixup debug information
        """
        ...

    def getDebugMisc(self) -> ghidra.app.util.bin.format.pe.debug.DebugMisc:
        """
        Returns the miscellaneous debug information, or null if it does not exists.
        @return the miscellaneous debug information
        """
        ...

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
    def debugCOFFSymbolsHeader(self) -> ghidra.app.util.bin.format.pe.debug.DebugCOFFSymbolsHeader: ...

    @property
    def debugCodeView(self) -> ghidra.app.util.bin.format.pe.debug.DebugCodeView: ...

    @property
    def debugDirectories(self) -> List[ghidra.app.util.bin.format.pe.debug.DebugDirectory]: ...

    @property
    def debugFixup(self) -> ghidra.app.util.bin.format.pe.debug.DebugFixup: ...

    @property
    def debugMisc(self) -> ghidra.app.util.bin.format.pe.debug.DebugMisc: ...
