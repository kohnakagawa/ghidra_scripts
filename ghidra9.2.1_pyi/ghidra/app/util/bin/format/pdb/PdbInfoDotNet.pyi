from typing import List
import ghidra.app.util.bin
import ghidra.app.util.bin.format.pdb
import ghidra.app.util.datatype.microsoft
import ghidra.program.model.data
import java.lang


class PdbInfoDotNet(object, ghidra.app.util.bin.format.pdb.PdbInfoDotNetIface):
    ASCII: ghidra.program.model.data.DataType = char
    BYTE: ghidra.program.model.data.DataType = byte
    DWORD: ghidra.program.model.data.DataType = dword
    IBO32: ghidra.program.model.data.DataType = ImageBaseOffset32
    MAGIC: int = 1381188691
    POINTER: ghidra.program.model.data.DataType = pointer
    QWORD: ghidra.program.model.data.DataType = qword
    STRING: ghidra.program.model.data.DataType = string
    UTF16: ghidra.program.model.data.DataType = unicode
    UTF8: ghidra.program.model.data.DataType = string-utf8
    VOID: ghidra.program.model.data.DataType = void
    WORD: ghidra.program.model.data.DataType = word



    def __init__(self, __a0: ghidra.app.util.bin.BinaryReader, __a1: int): ...



    def equals(self, __a0: object) -> bool: ...

    def getAge(self) -> int: ...

    def getClass(self) -> java.lang.Class: ...

    def getGUID(self) -> ghidra.app.util.datatype.microsoft.GUID: ...

    def getMagic(self) -> List[int]: ...

    def getPdbName(self) -> unicode: ...

    def getSignature(self) -> int: ...

    def hashCode(self) -> int: ...

    @staticmethod
    def isMatch(__a0: ghidra.app.util.bin.BinaryReader, __a1: int) -> bool: ...

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
    def GUID(self) -> ghidra.app.util.datatype.microsoft.GUID: ...

    @property
    def age(self) -> int: ...

    @property
    def magic(self) -> List[int]: ...

    @property
    def pdbName(self) -> unicode: ...

    @property
    def signature(self) -> int: ...
