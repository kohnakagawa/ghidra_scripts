from typing import List
import ghidra.app.util.bin
import ghidra.app.util.bin.format.pe.resource
import ghidra.program.model.data
import java.lang


class ResourceDirectoryEntry(object, ghidra.app.util.bin.StructConverter):
    """

     typedef struct _IMAGE_RESOURCE_DIRECTORY_ENTRY {
         union {
             struct {
                 DWORD NameOffset:31;
                 DWORD NameIsString:1;
             };
             DWORD   Name;
             WORD    Id;
         };
         union {
             DWORD   OffsetToData;
             struct {
                 DWORD   OffsetToDirectory:31;
                 DWORD   DataIsDirectory:1;
             };
         };
     };

    """

    ASCII: ghidra.program.model.data.DataType = char
    BYTE: ghidra.program.model.data.DataType = byte
    DWORD: ghidra.program.model.data.DataType = dword
    IBO32: ghidra.program.model.data.DataType = ImageBaseOffset32
    POINTER: ghidra.program.model.data.DataType = pointer
    QWORD: ghidra.program.model.data.DataType = qword
    SIZEOF: int = 8
    STRING: ghidra.program.model.data.DataType = string
    UTF16: ghidra.program.model.data.DataType = unicode
    UTF8: ghidra.program.model.data.DataType = string-utf8
    VOID: ghidra.program.model.data.DataType = void
    WORD: ghidra.program.model.data.DataType = word



    def __init__(self, reader: ghidra.app.util.bin.format.FactoryBundledWithBinaryReader, index: int, resourceBase: int, isNameEntry: bool, isFirstLevel: bool, ntHeader: ghidra.app.util.bin.format.pe.NTHeader):
        """
        Constructor.
        @param reader the binary reader
        @param index the index where this directory begins
        """
        ...



    def equals(self, __a0: object) -> bool: ...

    def getClass(self) -> java.lang.Class: ...

    def getData(self) -> ghidra.app.util.bin.format.pe.resource.ResourceDataEntry: ...

    def getDataIsDirectory(self) -> bool:
        """
        Returns a pointer to information about a specific resource instance.
        @return a pointer to information about a specific resource instance
        @see #getOffsetToData()
        """
        ...

    def getDirectoryString(self) -> ghidra.app.util.bin.format.pe.resource.ResourceDirectoryStringU: ...

    def getId(self) -> int:
        """
        Returns a resource ID.
        @return a resource ID
        @see #getName()
        """
        ...

    def getName(self) -> int:
        """
        @return either an integer ID or a pointer to a structure that contains a string name
        """
        ...

    def getNameIsString(self) -> bool:
        """
        Returns the ID of the name of this resource.
        @return the ID of the name of this resource
        @see #getName()
        """
        ...

    def getNameOffset(self) -> int:
        """
        Returns the offset to the name of this resource.
        @return the offset to the name of this resource
        @see #getName()
        """
        ...

    def getOffsetToData(self) -> int:
        """
        @return either an offset to another resource directory
                 or a pointer to information about a specific resource instance
        """
        ...

    def getOffsetToDirectory(self) -> int:
        """
        Returns an offset to another resource directory.
        @return an offset to another resource directory
        @see #getOffsetToData()
        """
        ...

    def getResources(self, level: int) -> List[ghidra.app.util.bin.format.pe.resource.ResourceInfo]: ...

    def getSubDirectory(self) -> ghidra.app.util.bin.format.pe.resource.ResourceDirectory: ...

    def hashCode(self) -> int: ...

    def isNameEntry(self) -> bool:
        """
        Returns true if the parent resource directory is named,
         false indicates an ID.
        """
        ...

    def isValid(self) -> bool: ...

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
    def data(self) -> ghidra.app.util.bin.format.pe.resource.ResourceDataEntry: ...

    @property
    def dataIsDirectory(self) -> bool: ...

    @property
    def directoryString(self) -> ghidra.app.util.bin.format.pe.resource.ResourceDirectoryStringU: ...

    @property
    def id(self) -> int: ...

    @property
    def name(self) -> int: ...

    @property
    def nameEntry(self) -> bool: ...

    @property
    def nameIsString(self) -> bool: ...

    @property
    def nameOffset(self) -> int: ...

    @property
    def offsetToData(self) -> int: ...

    @property
    def offsetToDirectory(self) -> int: ...

    @property
    def subDirectory(self) -> ghidra.app.util.bin.format.pe.resource.ResourceDirectory: ...

    @property
    def valid(self) -> bool: ...
