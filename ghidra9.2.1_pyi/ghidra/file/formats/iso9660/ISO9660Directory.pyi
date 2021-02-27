from typing import List
import ghidra.app.util.bin
import ghidra.file.formats.iso9660
import ghidra.program.model.data
import java.io
import java.lang


class ISO9660Directory(object, ghidra.app.util.bin.StructConverter):
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
    def __init__(self, __a0: ghidra.app.util.bin.BinaryReader, __a1: ghidra.file.formats.iso9660.ISO9660Directory): ...



    def equals(self, __a0: object) -> bool: ...

    def getClass(self) -> java.lang.Class: ...

    def getDataBytes(self, __a0: ghidra.app.util.bin.ByteProvider, __a1: long) -> java.io.InputStream: ...

    def getDataLengthBE(self) -> int: ...

    def getDataLengthLE(self) -> int: ...

    def getDirectoryRecordLength(self) -> int: ...

    def getExtendedAttributeRecordLen(self) -> int: ...

    def getFileFlag(self) -> int: ...

    def getFileIdentLength(self) -> int: ...

    def getFileIdentifier(self) -> List[int]: ...

    def getFileUnitSize(self) -> int: ...

    def getInterleaveGapSize(self) -> int: ...

    def getLocationOfExtentBE(self) -> int: ...

    def getLocationOfExtentLE(self) -> int: ...

    def getName(self) -> unicode: ...

    def getPaddingField(self) -> int: ...

    def getParentDirectory(self) -> ghidra.file.formats.iso9660.ISO9660Directory: ...

    def getRecordingDateTime(self) -> List[int]: ...

    def getVolumeIndex(self) -> long: ...

    def getVolumeSequenceNumberBE(self) -> int: ...

    def getVolumeSequenceNumberLE(self) -> int: ...

    def hashCode(self) -> int: ...

    def isDirectoryFlagSet(self) -> bool: ...

    def isPaddingFieldPresent(self) -> bool: ...

    def notify(self) -> None: ...

    def notifyAll(self) -> None: ...

    def setName(self, __a0: unicode) -> None: ...

    def setParentDirectory(self, __a0: ghidra.file.formats.iso9660.ISO9660Directory) -> None: ...

    def toDataType(self) -> ghidra.program.model.data.DataType: ...

    def toString(self) -> unicode: ...

    @overload
    def wait(self) -> None: ...

    @overload
    def wait(self, __a0: long) -> None: ...

    @overload
    def wait(self, __a0: long, __a1: int) -> None: ...

    @property
    def dataLengthBE(self) -> int: ...

    @property
    def dataLengthLE(self) -> int: ...

    @property
    def directoryFlagSet(self) -> bool: ...

    @property
    def directoryRecordLength(self) -> int: ...

    @property
    def extendedAttributeRecordLen(self) -> int: ...

    @property
    def fileFlag(self) -> int: ...

    @property
    def fileIdentLength(self) -> int: ...

    @property
    def fileIdentifier(self) -> List[int]: ...

    @property
    def fileUnitSize(self) -> int: ...

    @property
    def interleaveGapSize(self) -> int: ...

    @property
    def locationOfExtentBE(self) -> int: ...

    @property
    def locationOfExtentLE(self) -> int: ...

    @property
    def name(self) -> unicode: ...

    @name.setter
    def name(self, value: unicode) -> None: ...

    @property
    def paddingField(self) -> int: ...

    @property
    def paddingFieldPresent(self) -> bool: ...

    @property
    def parentDirectory(self) -> ghidra.file.formats.iso9660.ISO9660Directory: ...

    @parentDirectory.setter
    def parentDirectory(self, value: ghidra.file.formats.iso9660.ISO9660Directory) -> None: ...

    @property
    def recordingDateTime(self) -> List[int]: ...

    @property
    def volumeIndex(self) -> long: ...

    @property
    def volumeSequenceNumberBE(self) -> int: ...

    @property
    def volumeSequenceNumberLE(self) -> int: ...