from typing import List
import ghidra.app.util.bin
import ghidra.app.util.bin.format.pe.resource
import ghidra.program.model.data
import java.lang


class ResourceDirectory(object, ghidra.app.util.bin.StructConverter):
    """

     typedef struct _IMAGE_RESOURCE_DIRECTORY {
         DWORD   Characteristics;
         DWORD   TimeDateStamp;
         WORD    MajorVersion;
         WORD    MinorVersion;
         WORD    NumberOfNamedEntries;
         WORD    NumberOfIdEntries;
     };

    """

    ASCII: ghidra.program.model.data.DataType = char
    BYTE: ghidra.program.model.data.DataType = byte
    DWORD: ghidra.program.model.data.DataType = dword
    IBO32: ghidra.program.model.data.DataType = ImageBaseOffset32
    NAME: unicode = u'IMAGE_RESOURCE_DIRECTORY'
    POINTER: ghidra.program.model.data.DataType = pointer
    QWORD: ghidra.program.model.data.DataType = qword
    SIZEOF: int = 16
    STRING: ghidra.program.model.data.DataType = string
    UTF16: ghidra.program.model.data.DataType = unicode
    UTF8: ghidra.program.model.data.DataType = string-utf8
    VOID: ghidra.program.model.data.DataType = void
    WORD: ghidra.program.model.data.DataType = word



    def __init__(self, reader: ghidra.app.util.bin.format.FactoryBundledWithBinaryReader, index: int, resourceBase: int, isFirstLevel: bool, ntHeader: ghidra.app.util.bin.format.pe.NTHeader): ...



    def equals(self, __a0: object) -> bool: ...

    def getCharacteristics(self) -> int:
        """
        Theoretically, this field could hold flags for the resource, but appears to always be 0.
        @return the flags for the resource
        """
        ...

    def getClass(self) -> java.lang.Class: ...

    def getEntries(self) -> List[ghidra.app.util.bin.format.pe.resource.ResourceDirectoryEntry]: ...

    def getMajorVersion(self) -> int:
        """
        Theoretically these fields would hold a version number for the resource.
         These field appear to always be set to 0.
        @return the major version number
        """
        ...

    def getMinorVersion(self) -> int:
        """
        Theoretically these fields would hold a version number for the resource.
         These field appear to always be set to 0.
        @return the minor version number
        """
        ...

    def getNumberOfIdEntries(self) -> int:
        """
        Returns the number of array elements that use integer IDs, and which follow this structure.
        @return the number of array elements that use integer IDs, and which follow this structure
        """
        ...

    def getNumberOfNamedEntries(self) -> int:
        """
        Returns the number of array elements that use names and that follow this structure.
        @return the number of array elements that use names and that follow this structure
        """
        ...

    def getTimeDataStamp(self) -> int:
        """
        Returns the time/date stamp describing the creation time of the resource.
        @return the time/date stamp describing the creation time of the resource
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
    def characteristics(self) -> int: ...

    @property
    def entries(self) -> List[object]: ...

    @property
    def majorVersion(self) -> int: ...

    @property
    def minorVersion(self) -> int: ...

    @property
    def numberOfIdEntries(self) -> int: ...

    @property
    def numberOfNamedEntries(self) -> int: ...

    @property
    def timeDataStamp(self) -> int: ...
