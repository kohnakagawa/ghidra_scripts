from typing import List
import ghidra.app.util.bin
import ghidra.app.util.bin.format.pef
import ghidra.program.model.data
import ghidra.util.task
import java.io
import java.lang


class SectionHeader(object, ghidra.app.util.bin.StructConverter):
    """
    See Apple's -- PEFBinaryFormat

     struct PEFSectionHeader {
         SInt32   nameOffset;             // Offset of name within the section name table, -1 = none.
         UInt32   defaultAddress;         // Default address, affects relocations.
         UInt32   totalLength;            // Fully expanded size in bytes of the section contents.
         UInt32   unpackedLength;         // Size in bytes of the "initialized" part of the contents.
         UInt32   containerLength;        // Size in bytes of the raw data in the container.
         UInt32   containerOffset;        // Offset of section's raw data.
         UInt8    sectionKind;            // Kind of section contents/usage.
         UInt8    shareKind;              // Sharing level, if a writeable section.
         UInt8    alignment;              // Preferred alignment, expressed as log 2.
         UInt8    reservedA;              // Reserved, must be zero.
     };

    """

    ASCII: ghidra.program.model.data.DataType = char
    BYTE: ghidra.program.model.data.DataType = byte
    DWORD: ghidra.program.model.data.DataType = dword
    IBO32: ghidra.program.model.data.DataType = ImageBaseOffset32
    NO_NAME_OFFSET: int = -1
    POINTER: ghidra.program.model.data.DataType = pointer
    QWORD: ghidra.program.model.data.DataType = qword
    STRING: ghidra.program.model.data.DataType = string
    UTF16: ghidra.program.model.data.DataType = unicode
    UTF8: ghidra.program.model.data.DataType = string-utf8
    VOID: ghidra.program.model.data.DataType = void
    WORD: ghidra.program.model.data.DataType = word







    def equals(self, __a0: object) -> bool: ...

    def getAlignment(self) -> int: ...

    def getClass(self) -> java.lang.Class: ...

    def getContainerLength(self) -> int:
        """
        Returns the size in bytes of the raw data in the container.
        @return the size in bytes of the raw data in the container
        """
        ...

    def getContainerOffset(self) -> int: ...

    def getData(self) -> java.io.InputStream:
        """
        Returns an input stream to underlying bytes of this section.
        @return an input stream to underlying bytes of this section
        @throws IOException if an i/o error occurs.
        """
        ...

    def getDefaultAddress(self) -> int:
        """
        Returns the preferred address of this section.
        @return the preferred address of this section
        """
        ...

    def getName(self) -> unicode:
        """
        Returns the name of this section.
        @return the name of this section
        """
        ...

    def getNameOffset(self) -> int:
        """
        The offset from the start of the section name table
         to the name of this section.
         A value of -1 indicates an unnamed section.
        @return the offset from the start of the section name table
        """
        ...

    def getReservedA(self) -> int:
        """
        Reserved!
        @return Reserved!
        """
        ...

    def getSectionKind(self) -> ghidra.app.util.bin.format.pef.SectionKind: ...

    def getShareKind(self) -> ghidra.app.util.bin.format.pef.SectionShareKind: ...

    def getTotalLength(self) -> int: ...

    def getUnpackedData(self, monitor: ghidra.util.task.TaskMonitor) -> List[int]:
        """
        Unpack the data in a packed section.
         Calling this method is only valid on a packed section.
        @param monitor the task monitor
        @return the unpacked data
        @throws IOException if an i/o error occurs or the section is not packed.
        """
        ...

    def getUnpackedLength(self) -> int:
        """
        Returns the size in bytes of the "initialized" part of the contents.
        @return the size in bytes of the "initialized" part of the contents
        """
        ...

    def hashCode(self) -> int: ...

    def isExecute(self) -> bool:
        """
        Returns true if this section has execute permissions.
        @return true if this section has execute permissions
        """
        ...

    def isRead(self) -> bool:
        """
        Returns true if this section has read permissions.
        @return true if this section has read permissions
        """
        ...

    def isWrite(self) -> bool:
        """
        Returns true if this section has write permissions.
        @return true if this section has write permissions
        """
        ...

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
    def alignment(self) -> int: ...

    @property
    def containerLength(self) -> int: ...

    @property
    def containerOffset(self) -> int: ...

    @property
    def data(self) -> java.io.InputStream: ...

    @property
    def defaultAddress(self) -> int: ...

    @property
    def execute(self) -> bool: ...

    @property
    def name(self) -> unicode: ...

    @property
    def nameOffset(self) -> int: ...

    @property
    def read(self) -> bool: ...

    @property
    def reservedA(self) -> int: ...

    @property
    def sectionKind(self) -> ghidra.app.util.bin.format.pef.SectionKind: ...

    @property
    def shareKind(self) -> ghidra.app.util.bin.format.pef.SectionShareKind: ...

    @property
    def totalLength(self) -> int: ...

    @property
    def unpackedLength(self) -> int: ...

    @property
    def write(self) -> bool: ...
