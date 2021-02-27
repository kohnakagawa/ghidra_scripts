from typing import List
import ghidra.app.util.bin
import ghidra.app.util.bin.format.pe.resource
import ghidra.program.model.data
import java.lang


class VS_VERSION_INFO(object, ghidra.app.util.bin.StructConverter):
    """
    A class to represent the VS_VERSION_INFO data structure.
    """

    ASCII: ghidra.program.model.data.DataType = char
    BYTE: ghidra.program.model.data.DataType = byte
    DWORD: ghidra.program.model.data.DataType = dword
    IBO32: ghidra.program.model.data.DataType = ImageBaseOffset32
    NAME: unicode = u'VS_VERSION_INFO'
    POINTER: ghidra.program.model.data.DataType = pointer
    QWORD: ghidra.program.model.data.DataType = qword
    SIZEOF: int = 92
    STRING: ghidra.program.model.data.DataType = string
    UTF16: ghidra.program.model.data.DataType = unicode
    UTF8: ghidra.program.model.data.DataType = string-utf8
    VOID: ghidra.program.model.data.DataType = void
    WORD: ghidra.program.model.data.DataType = word



    def __init__(self, reader: ghidra.app.util.bin.format.FactoryBundledWithBinaryReader, index: int):
        """
        Constructs a new VS_VERSION_INFO object.
        @param reader the binary reader
        @param index the index where the VS_VERSION_INFO begins
        @throws IOException if an I/O error occurs
        """
        ...



    def equals(self, __a0: object) -> bool: ...

    def getChildren(self) -> List[ghidra.app.util.bin.format.pe.resource.VS_VERSION_CHILD]:
        """
        Returns the array of VS_VERSION_CHILD defined in this VS_VERSION_INFO object.
        @return the array of VS_VERSION_CHILD defined in this VS_VERSION_INFO object
        """
        ...

    def getClass(self) -> java.lang.Class: ...

    def getFileFlags(self) -> int:
        """
        Returns the file flags.
        @return the file flags
        """
        ...

    def getFileFlagsMask(self) -> unicode:
        """
        Returns the file flags mask.
        @return the file flags mask
        """
        ...

    def getFileOS(self) -> int:
        """
        Returns the file OS.
        @return the file OS
        """
        ...

    def getFileSubtype(self) -> int:
        """
        Returns the file sub-type.
        @return the file sub-type
        """
        ...

    def getFileTimestamp(self) -> int:
        """
        Returns the file timestamp.
        @return the file timestamp
        """
        ...

    def getFileType(self) -> int:
        """
        Returns the file type.
        @return the file type
        """
        ...

    def getFileVersion(self) -> unicode:
        """
        Returns the file version.
        @return the file version
        """
        ...

    def getInfo(self) -> unicode:
        """
        Returns the info.
        @return the info
        """
        ...

    def getKeys(self) -> List[unicode]:
        """
        Returns the array of keys in this version child.
        @return the array of keys in this version child
        """
        ...

    def getProductVersion(self) -> unicode:
        """
        Returns the product version.
        @return the product version
        """
        ...

    def getSignature(self) -> int:
        """
        Returns the signature.
        @return the signature
        """
        ...

    def getStructLength(self) -> int:
        """
        Returns the structure length.
        @return the structure length
        """
        ...

    def getStructType(self) -> int:
        """
        Returns the structure type.
        @return the structure type
        """
        ...

    def getStructVersion(self) -> unicode:
        """
        Returns the structure version.
        @return the structure version
        """
        ...

    def getValue(self, key: unicode) -> unicode:
        """
        Returns the value for the specified key.
        @param key the key
        @return the value for the specified key
        """
        ...

    def getValueLength(self) -> int:
        """
        Returns the value length.
        @return the value length
        """
        ...

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
    def children(self) -> List[ghidra.app.util.bin.format.pe.resource.VS_VERSION_CHILD]: ...

    @property
    def fileFlags(self) -> int: ...

    @property
    def fileFlagsMask(self) -> unicode: ...

    @property
    def fileOS(self) -> int: ...

    @property
    def fileSubtype(self) -> int: ...

    @property
    def fileTimestamp(self) -> int: ...

    @property
    def fileType(self) -> int: ...

    @property
    def fileVersion(self) -> unicode: ...

    @property
    def info(self) -> unicode: ...

    @property
    def keys(self) -> List[unicode]: ...

    @property
    def productVersion(self) -> unicode: ...

    @property
    def signature(self) -> int: ...

    @property
    def structLength(self) -> int: ...

    @property
    def structType(self) -> int: ...

    @property
    def structVersion(self) -> unicode: ...

    @property
    def valueLength(self) -> int: ...
