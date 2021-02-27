from typing import List
import ghidra.app.util.bin
import ghidra.program.model.data
import ghidra.util
import java.io
import java.lang


class DebugDirectory(object, ghidra.app.util.bin.StructConverter, ghidra.app.util.bin.ByteArrayConverter):
    """
    A class to represent the Debug Directory data structure.


     typedef struct _IMAGE_DEBUG_DIRECTORY {
         DWORD   Characteristics;
         DWORD   TimeDateStamp;
         WORD    MajorVersion;
         WORD    MinorVersion;
         DWORD   Type;
         DWORD   SizeOfData;
         DWORD   AddressOfRawData;
         DWORD   PointerToRawData;
     } IMAGE_DEBUG_DIRECTORY, *PIMAGE_DEBUG_DIRECTORY;


    """

    ASCII: ghidra.program.model.data.DataType = char
    BYTE: ghidra.program.model.data.DataType = byte
    DWORD: ghidra.program.model.data.DataType = dword
    IBO32: ghidra.program.model.data.DataType = ImageBaseOffset32
    IMAGE_SIZEOF_DEBUG_DIRECTORY: int = 28
    NAME: unicode = u'IMAGE_DEBUG_DIRECTORY'
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

    def getAddressOfRawData(self) -> int:
        """
        Returns the address of the debugging information when the image is loaded, relative to the image base.
        @return the address of the debugging information when the image is loaded, relative to the image base
        """
        ...

    def getCharacteristics(self) -> int:
        """
        Reserved.
        @return reserved value
        """
        ...

    def getClass(self) -> java.lang.Class: ...

    def getDescription(self) -> unicode:
        """
        Returns a description of this debug directory.
        @return a description of this debug directory
        """
        ...

    def getMajorVersion(self) -> int:
        """
        Returns the major version number of the debugging information format.
        @return the major version number of the debugging information format
        """
        ...

    def getMinorVersion(self) -> int:
        """
        Returns the minor version number of the debugging information format.
        @return the minor version number of the debugging information format
        """
        ...

    def getPointerToRawData(self) -> int:
        """
        Returns the file pointer to the debugging information.
        @return the file pointer to the debugging information
        """
        ...

    def getSizeOfData(self) -> int:
        """
        Returns the size of the debugging information, in bytes.
         This value does not include the debug directory itself.
        @return the size of the debugging information, in bytes
        """
        ...

    def getTimeDateStamp(self) -> int:
        """
        Returns the time and date the debugging information was created.
        @return the time and date the debugging information was created
        """
        ...

    def getType(self) -> int:
        """
        Returns the format of the debugging information.
        @return the format of the debugging information
        """
        ...

    def hashCode(self) -> int: ...

    def notify(self) -> None: ...

    def notifyAll(self) -> None: ...

    def setDescription(self, desc: unicode) -> None:
        """
        Sets the description of this debug directory.
        @param desc the description of this debug directory
        """
        ...

    def toBytes(self, dc: ghidra.util.DataConverter) -> List[int]: ...

    def toDataType(self) -> ghidra.program.model.data.DataType:
        """
        @see ghidra.app.util.bin.StructConverter#toDataType()
        """
        ...

    def toString(self) -> unicode: ...

    def updatePointers(self, offset: int, postOffset: int) -> None: ...

    @overload
    def wait(self) -> None: ...

    @overload
    def wait(self, __a0: long) -> None: ...

    @overload
    def wait(self, __a0: long, __a1: int) -> None: ...

    def writeHeader(self, raf: java.io.RandomAccessFile, dc: ghidra.util.DataConverter) -> None: ...

    @property
    def addressOfRawData(self) -> int: ...

    @property
    def characteristics(self) -> int: ...

    @property
    def description(self) -> unicode: ...

    @description.setter
    def description(self, value: unicode) -> None: ...

    @property
    def majorVersion(self) -> int: ...

    @property
    def minorVersion(self) -> int: ...

    @property
    def pointerToRawData(self) -> int: ...

    @property
    def sizeOfData(self) -> int: ...

    @property
    def timeDateStamp(self) -> int: ...

    @property
    def type(self) -> int: ...
