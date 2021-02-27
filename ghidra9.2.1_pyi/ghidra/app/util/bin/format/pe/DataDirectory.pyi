import ghidra.app.util.bin
import ghidra.app.util.bin.format.pe
import ghidra.app.util.importer
import ghidra.program.model.data
import ghidra.program.model.listing
import ghidra.util
import ghidra.util.task
import java.io
import java.lang


class DataDirectory(object, ghidra.app.util.bin.StructConverter, ghidra.app.util.bin.format.pe.PeMarkupable):
    """
    An abstract base class to represent the
     IMAGE_DATA_DIRECTORY
     data structure defined in winnt.h.

     typedef struct _IMAGE_DATA_DIRECTORY {
         DWORD   VirtualAddress;
         DWORD   Size;
     } IMAGE_DATA_DIRECTORY, *PIMAGE_DATA_DIRECTORY; {

    """

    ASCII: ghidra.program.model.data.DataType = char
    BYTE: ghidra.program.model.data.DataType = byte
    DWORD: ghidra.program.model.data.DataType = dword
    IBO32: ghidra.program.model.data.DataType = ImageBaseOffset32
    IMAGE_SIZEOF_IMAGE_DIRECTORY_ENTRY: int = 8
    POINTER: ghidra.program.model.data.DataType = pointer
    QWORD: ghidra.program.model.data.DataType = qword
    STRING: ghidra.program.model.data.DataType = string
    UTF16: ghidra.program.model.data.DataType = unicode
    UTF8: ghidra.program.model.data.DataType = string-utf8
    VOID: ghidra.program.model.data.DataType = void
    WORD: ghidra.program.model.data.DataType = word



    def __init__(self): ...



    def equals(self, __a0: object) -> bool: ...

    def getClass(self) -> java.lang.Class: ...

    def getDirectoryName(self) -> unicode: ...

    def getPointer(self) -> int: ...

    def getSize(self) -> int:
        """
        Returns the size of this data directory.
        @return the size of this data directory
        """
        ...

    def getVirtualAddress(self) -> int:
        """
        Returns the relative virtual address of this data directory.
        @return the relative virtual address of this data directory
        """
        ...

    def hasParsedCorrectly(self) -> bool: ...

    def hashCode(self) -> int: ...

    def markup(self, __a0: ghidra.program.model.listing.Program, __a1: bool, __a2: ghidra.util.task.TaskMonitor, __a3: ghidra.app.util.importer.MessageLog, __a4: ghidra.app.util.bin.format.pe.NTHeader) -> None: ...

    def notify(self) -> None: ...

    def notifyAll(self) -> None: ...

    def parse(self) -> bool:
        """
        Parses this data directory.
        @return True if parsing completed successfully; otherwise, false.
        @throws IOException If there was an IO problem while parsing.
        """
        ...

    def setSize(self, size: int) -> None:
        """
        Sets the size of this data directory.
        @param size the new size of this data directory
        """
        ...

    def setVirtualAddress(self, addr: int) -> None:
        """
        Sets the relative virtual address of this data directory.
        @param addr the new relative virtual address
        """
        ...

    def toDataType(self) -> ghidra.program.model.data.DataType:
        """
        This method should return a datatype representing the data stored
         in this directory.
        """
        ...

    def toString(self) -> unicode:
        """
        @see java.lang.Object#toString()
        """
        ...

    @overload
    def wait(self) -> None: ...

    @overload
    def wait(self, __a0: long) -> None: ...

    @overload
    def wait(self, __a0: long, __a1: int) -> None: ...

    def writeBytes(self, raf: java.io.RandomAccessFile, dc: ghidra.util.DataConverter, template: ghidra.app.util.bin.format.pe.PortableExecutable) -> None:
        """
        Directories that are not contained inside of sections
         should override this method to write their bytes into the
         specified file.
        @param raf the random access file used for output
        @param dc the data converter for endianness
        @param template the original unadulterated PE
        @throws IOException if an I/O error occurs
        """
        ...

    @property
    def directoryName(self) -> unicode: ...

    @property
    def pointer(self) -> int: ...

    @property
    def size(self) -> int: ...

    @size.setter
    def size(self, value: int) -> None: ...

    @property
    def virtualAddress(self) -> int: ...

    @virtualAddress.setter
    def virtualAddress(self, value: int) -> None: ...
