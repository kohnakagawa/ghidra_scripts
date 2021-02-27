import ghidra.app.util.bin.format.pdb2.pdbreader
import ghidra.app.util.importer
import ghidra.app.util.pdb
import ghidra.program.model.listing
import ghidra.util.task
import java.io
import java.lang


class PdbLocator(object):
    DEFAULT_SYMBOLS_DIR: java.io.File = /Users/konakagawa.ffri/Symbols
    PDB_SYMBOLS_DIR_PREFERENCE: unicode = u'PDB Storage Directory'
    WINDOWS_SYMBOLS_DIR: java.io.File = None
    onWindows: bool = False



    def __init__(self, __a0: java.io.File): ...



    def equals(self, __a0: object) -> bool: ...

    def findPdb(self, __a0: ghidra.program.model.listing.Program, __a1: ghidra.app.util.pdb.PdbProgramAttributes, __a2: bool, __a3: bool, __a4: ghidra.util.task.TaskMonitor, __a5: ghidra.app.util.importer.MessageLog, __a6: unicode) -> unicode: ...

    @overload
    @staticmethod
    def formatPdbIdentifiers(__a0: ghidra.app.util.pdb.PdbProgramAttributes) -> java.lang.StringBuilder: ...

    @overload
    @staticmethod
    def formatPdbIdentifiers(__a0: unicode, __a1: ghidra.app.util.bin.format.pdb2.pdbreader.PdbIdentifiers) -> java.lang.StringBuilder: ...

    def getClass(self) -> java.lang.Class: ...

    @staticmethod
    def getDefaultPdbSymbolsDir() -> java.io.File: ...

    def hashCode(self) -> int: ...

    def notify(self) -> None: ...

    def notifyAll(self) -> None: ...

    @staticmethod
    def setDefaultPdbSymbolsDir(__a0: java.io.File) -> None: ...

    def toString(self) -> unicode: ...

    @staticmethod
    def verifyPdbSignature(__a0: ghidra.app.util.pdb.PdbProgramAttributes, __a1: ghidra.app.util.bin.format.pdb2.pdbreader.PdbIdentifiers) -> bool: ...

    @overload
    def wait(self) -> None: ...

    @overload
    def wait(self, __a0: long) -> None: ...

    @overload
    def wait(self, __a0: long, __a1: int) -> None: ...
