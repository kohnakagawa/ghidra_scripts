import ghidra.app.util.bin
import ghidra.app.util.bin.format.pdb
import ghidra.app.util.bin.format.pe.debug
import ghidra.program.model.data
import java.lang


class DebugCodeView(object, ghidra.app.util.bin.StructConverter):
    """
    A class to represent the code view debug information.
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



    def equals(self, __a0: object) -> bool: ...

    def getClass(self) -> java.lang.Class: ...

    def getDebugDirectory(self) -> ghidra.app.util.bin.format.pe.debug.DebugDirectory:
        """
        Returns the code view debug directory.
        @return the code view debug directory
        """
        ...

    def getDotNetPdbInfo(self) -> ghidra.app.util.bin.format.pdb.PdbInfoDotNetIface: ...

    def getPdbInfo(self) -> ghidra.app.util.bin.format.pdb.PdbInfoIface:
        """
        Returns the code view .PDB info.
        @return the code view .PDB info
        """
        ...

    def getSymbolTable(self) -> ghidra.app.util.bin.format.pe.debug.DebugCodeViewSymbolTable:
        """
        Returns the code view symbol table.
        @return the code view symbol table
        """
        ...

    def hashCode(self) -> int: ...

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
    def debugDirectory(self) -> ghidra.app.util.bin.format.pe.debug.DebugDirectory: ...

    @property
    def dotNetPdbInfo(self) -> ghidra.app.util.bin.format.pdb.PdbInfoDotNetIface: ...

    @property
    def pdbInfo(self) -> ghidra.app.util.bin.format.pdb.PdbInfoIface: ...

    @property
    def symbolTable(self) -> ghidra.app.util.bin.format.pe.debug.DebugCodeViewSymbolTable: ...
