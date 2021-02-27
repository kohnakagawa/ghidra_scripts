from typing import List
import ghidra.app.util.bin
import ghidra.program.model.data
import java.lang


class PdbInfoIface(ghidra.app.util.bin.StructConverter, object):
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







    def equals(self, __a0: object) -> bool: ...

    def getAge(self) -> int: ...

    def getClass(self) -> java.lang.Class: ...

    def getMagic(self) -> List[int]: ...

    def getOffset(self) -> int: ...

    def getPdbName(self) -> unicode: ...

    def getSig(self) -> int: ...

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
    def age(self) -> int: ...

    @property
    def magic(self) -> List[int]: ...

    @property
    def offset(self) -> int: ...

    @property
    def pdbName(self) -> unicode: ...

    @property
    def sig(self) -> int: ...
