import ghidra.app.util.bin
import ghidra.app.util.bin.format.dwarf4
import ghidra.app.util.bin.format.dwarf4.encoding
import java.lang


class DWARFCompileUnit(object):
    """
    DWARFCompileUnit hold some values retrieved from a DWARF DW_TAG_compile_unit DIE.

    """





    def __init__(self, name: unicode, producer: unicode, comp_dir: unicode, low_pc: java.lang.Number, high_pc: java.lang.Number, language: java.lang.Number, stmt_list: java.lang.Number, identifier_case: ghidra.app.util.bin.format.dwarf4.encoding.DWARFIdentifierCase, hasDWO: bool, line: ghidra.app.util.bin.format.dwarf4.DWARFLine): ...



    def equals(self, __a0: object) -> bool: ...

    def getClass(self) -> java.lang.Class: ...

    def getCompileDirectory(self) -> unicode:
        """
        Get the compile directory of the compile unit
        @return the compile directory of the compile unit
        """
        ...

    def getFileByIndex(self, index: int) -> unicode:
        """
        Get a file name based on a file index.
        @param index index of the file
        @return file name or null if line information does not exist
        @throws IllegalArgumentException if a negative or invalid file index is given
        """
        ...

    def getFileName(self) -> unicode:
        """
        Get the filename of the compile unit
        @return the filename of the compile unit
        """
        ...

    def getFullFileByIndex(self, index: int) -> unicode:
        """
        Get a file name with the full path included based on a file index.
        @param index index of the file
        @return file name with full path or null if line information does not exist
        @throws IllegalArgumentException if a negative or invalid file index is given
        """
        ...

    def getHighPC(self) -> java.lang.Number:
        """
        Get the high PC value of the compile unit
        @return the high PC value of the compile unit
        """
        ...

    def getIdentifierCase(self) -> ghidra.app.util.bin.format.dwarf4.encoding.DWARFIdentifierCase:
        """
        Get the identifier case of the compile unit
        @return the identifier case of the compile unit
        """
        ...

    def getLanguage(self) -> int:
        """
        Get the source language of the compile unit.
        @return the source language of the compile unit
        """
        ...

    def getLowPC(self) -> java.lang.Number:
        """
        Get the low PC value of the compile unit
        @return the low PC value of the compile unit
        """
        ...

    def getName(self) -> unicode:
        """
        Get the name of the compile unit
        @return the name of the compile unit
        """
        ...

    def getProducer(self) -> unicode:
        """
        Get the producer of the compile unit
        @return the producer of the compile unit
        """
        ...

    def getStatementList(self) -> int:
        """
        Get the statement list of the compile unit.
        @return the statement list of the compile unit
        """
        ...

    def hasDWO(self) -> bool: ...

    def hashCode(self) -> int: ...

    def notify(self) -> None: ...

    def notifyAll(self) -> None: ...

    @staticmethod
    def read(diea: ghidra.app.util.bin.format.dwarf4.DIEAggregate, lineReader: ghidra.app.util.bin.BinaryReader) -> ghidra.app.util.bin.format.dwarf4.DWARFCompileUnit: ...

    def toString(self) -> unicode: ...

    @overload
    def wait(self) -> None: ...

    @overload
    def wait(self, __a0: long) -> None: ...

    @overload
    def wait(self, __a0: long, __a1: int) -> None: ...

    @property
    def compileDirectory(self) -> unicode: ...

    @property
    def fileName(self) -> unicode: ...

    @property
    def highPC(self) -> java.lang.Number: ...

    @property
    def identifierCase(self) -> ghidra.app.util.bin.format.dwarf4.encoding.DWARFIdentifierCase: ...

    @property
    def language(self) -> int: ...

    @property
    def lowPC(self) -> java.lang.Number: ...

    @property
    def name(self) -> unicode: ...

    @property
    def producer(self) -> unicode: ...

    @property
    def statementList(self) -> int: ...
