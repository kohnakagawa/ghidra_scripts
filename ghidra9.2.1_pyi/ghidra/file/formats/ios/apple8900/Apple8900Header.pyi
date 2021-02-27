from typing import List
import ghidra.app.util.bin
import ghidra.program.model.data
import java.lang


class Apple8900Header(object, ghidra.app.util.bin.StructConverter):
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



    @overload
    def __init__(self, __a0: ghidra.app.util.bin.BinaryReader): ...

    @overload
    def __init__(self, __a0: ghidra.app.util.bin.ByteProvider): ...



    def equals(self, __a0: object) -> bool: ...

    def getClass(self) -> java.lang.Class: ...

    def getFooterCertificateLength(self) -> int: ...

    def getFooterCertificateOffset(self) -> int: ...

    def getFooterSignatureOffset(self) -> int: ...

    def getKey1(self) -> List[int]: ...

    def getKey2(self) -> List[int]: ...

    def getMagic(self) -> unicode: ...

    def getSizeOfData(self) -> int: ...

    def getUnknown(self, __a0: int) -> List[int]: ...

    def getVersion(self) -> unicode: ...

    def hashCode(self) -> int: ...

    def isEncrypted(self) -> bool: ...

    def notify(self) -> None: ...

    def notifyAll(self) -> None: ...

    @staticmethod
    def reverse(__a0: List[int]) -> List[int]: ...

    def toDataType(self) -> ghidra.program.model.data.DataType: ...

    def toString(self) -> unicode: ...

    @overload
    def wait(self) -> None: ...

    @overload
    def wait(self, __a0: long) -> None: ...

    @overload
    def wait(self, __a0: long, __a1: int) -> None: ...

    @property
    def encrypted(self) -> bool: ...

    @property
    def footerCertificateLength(self) -> int: ...

    @property
    def footerCertificateOffset(self) -> int: ...

    @property
    def footerSignatureOffset(self) -> int: ...

    @property
    def key1(self) -> List[int]: ...

    @property
    def key2(self) -> List[int]: ...

    @property
    def magic(self) -> unicode: ...

    @property
    def sizeOfData(self) -> int: ...

    @property
    def version(self) -> unicode: ...