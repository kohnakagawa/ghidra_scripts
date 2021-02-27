import ghidra.app.util.bin
import ghidra.program.model.data
import java.lang


class AoutHeader(object, ghidra.app.util.bin.StructConverter):
    ASCII: ghidra.program.model.data.DataType = char
    BYTE: ghidra.program.model.data.DataType = byte
    DWORD: ghidra.program.model.data.DataType = dword
    IBO32: ghidra.program.model.data.DataType = ImageBaseOffset32
    POINTER: ghidra.program.model.data.DataType = pointer
    QWORD: ghidra.program.model.data.DataType = qword
    SIZEOF: int = 28
    STRING: ghidra.program.model.data.DataType = string
    UTF16: ghidra.program.model.data.DataType = unicode
    UTF8: ghidra.program.model.data.DataType = string-utf8
    VOID: ghidra.program.model.data.DataType = void
    WORD: ghidra.program.model.data.DataType = word







    def equals(self, __a0: object) -> bool: ...

    def getClass(self) -> java.lang.Class: ...

    def getEntry(self) -> int: ...

    def getInitializedDataSize(self) -> int: ...

    def getInitializedDataStart(self) -> int: ...

    def getMagic(self) -> int: ...

    def getTextSize(self) -> int: ...

    def getTextStart(self) -> int: ...

    def getUninitializedDataSize(self) -> int: ...

    def getVersionStamp(self) -> int: ...

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
    def entry(self) -> int: ...

    @property
    def initializedDataSize(self) -> int: ...

    @property
    def initializedDataStart(self) -> int: ...

    @property
    def magic(self) -> int: ...

    @property
    def textSize(self) -> int: ...

    @property
    def textStart(self) -> int: ...

    @property
    def uninitializedDataSize(self) -> int: ...

    @property
    def versionStamp(self) -> int: ...
