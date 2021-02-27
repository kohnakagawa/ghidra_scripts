from typing import List
import ghidra.app.util.bin
import ghidra.program.model.data
import java.lang


class BootImage(object, ghidra.app.util.bin.StructConverter):
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

    def getCommandLine(self) -> unicode: ...

    def getId(self) -> List[int]: ...

    def getKernelAddress(self) -> int: ...

    def getKernelOffset(self) -> int: ...

    def getKernelSize(self) -> int: ...

    def getKernelSizePageAligned(self) -> int: ...

    def getMagic(self) -> unicode: ...

    def getName(self) -> unicode: ...

    def getPageSize(self) -> int: ...

    def getRamDiskAddress(self) -> int: ...

    def getRamDiskOffset(self) -> int: ...

    def getRamDiskSize(self) -> int: ...

    def getRamDiskSizePageAligned(self) -> int: ...

    def getSecondStageAddress(self) -> int: ...

    def getSecondStageOffset(self) -> int: ...

    def getSecondStageSize(self) -> int: ...

    def getSecondStageSizePageAligned(self) -> int: ...

    def getTagsAddress(self) -> int: ...

    def getUnused(self) -> List[int]: ...

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
    def commandLine(self) -> unicode: ...

    @property
    def id(self) -> List[int]: ...

    @property
    def kernelAddress(self) -> int: ...

    @property
    def kernelOffset(self) -> int: ...

    @property
    def kernelSize(self) -> int: ...

    @property
    def kernelSizePageAligned(self) -> int: ...

    @property
    def magic(self) -> unicode: ...

    @property
    def name(self) -> unicode: ...

    @property
    def pageSize(self) -> int: ...

    @property
    def ramDiskAddress(self) -> int: ...

    @property
    def ramDiskOffset(self) -> int: ...

    @property
    def ramDiskSize(self) -> int: ...

    @property
    def ramDiskSizePageAligned(self) -> int: ...

    @property
    def secondStageAddress(self) -> int: ...

    @property
    def secondStageOffset(self) -> int: ...

    @property
    def secondStageSize(self) -> int: ...

    @property
    def secondStageSizePageAligned(self) -> int: ...

    @property
    def tagsAddress(self) -> int: ...

    @property
    def unused(self) -> List[int]: ...
