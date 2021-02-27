from typing import List
import ghidra.app.util.bin
import ghidra.app.util.bin.format.pe
import ghidra.program.model.data
import ghidra.program.model.listing
import ghidra.util
import ghidra.util.task
import java.io
import java.lang


class OptionalHeader(ghidra.app.util.bin.StructConverter, object):
    ASCII: ghidra.program.model.data.DataType = char
    BYTE: ghidra.program.model.data.DataType = byte
    DWORD: ghidra.program.model.data.DataType = dword
    IBO32: ghidra.program.model.data.DataType = ImageBaseOffset32
    IMAGE_DIRECTORY_ENTRY_ARCHITECTURE: int = 7
    IMAGE_DIRECTORY_ENTRY_BASERELOC: int = 5
    IMAGE_DIRECTORY_ENTRY_BOUND_IMPORT: int = 11
    IMAGE_DIRECTORY_ENTRY_COMHEADER: int = 14
    IMAGE_DIRECTORY_ENTRY_COM_DESCRIPTOR: int = 14
    IMAGE_DIRECTORY_ENTRY_DEBUG: int = 6
    IMAGE_DIRECTORY_ENTRY_DELAY_IMPORT: int = 13
    IMAGE_DIRECTORY_ENTRY_EXCEPTION: int = 3
    IMAGE_DIRECTORY_ENTRY_EXPORT: int = 0
    IMAGE_DIRECTORY_ENTRY_GLOBALPTR: int = 8
    IMAGE_DIRECTORY_ENTRY_IAT: int = 12
    IMAGE_DIRECTORY_ENTRY_IMPORT: int = 1
    IMAGE_DIRECTORY_ENTRY_LOAD_CONFIG: int = 10
    IMAGE_DIRECTORY_ENTRY_RESOURCE: int = 2
    IMAGE_DIRECTORY_ENTRY_SECURITY: int = 4
    IMAGE_DIRECTORY_ENTRY_TLS: int = 9
    IMAGE_NUMBEROF_DIRECTORY_ENTRIES: int = 16
    POINTER: ghidra.program.model.data.DataType = pointer
    QWORD: ghidra.program.model.data.DataType = qword
    STRING: ghidra.program.model.data.DataType = string
    UTF16: ghidra.program.model.data.DataType = unicode
    UTF8: ghidra.program.model.data.DataType = string-utf8
    VOID: ghidra.program.model.data.DataType = void
    WORD: ghidra.program.model.data.DataType = word







    def equals(self, __a0: object) -> bool: ...

    def getAddressOfEntryPoint(self) -> long:
        """
        @return the RVA of the first code byte in the file that will be executed
        """
        ...

    def getBaseOfCode(self) -> long:
        """
        Returns the RVA of the first byte of code when loaded in memory.
        @return the RVA of the first byte of code when loaded in memory
        """
        ...

    def getBaseOfData(self) -> long:
        """
        @return the RVA of the first byte of data when loaded into memory
        """
        ...

    def getChecksum(self) -> int:
        """
        Get the image file checksum.
        @return
        """
        ...

    def getClass(self) -> java.lang.Class: ...

    def getDataDirectories(self) -> List[ghidra.app.util.bin.format.pe.DataDirectory]:
        """
        Returns the array of data directories.
        @return the array of data directories
        """
        ...

    def getDllCharacteristics(self) -> int:
        """
        Return flags that describe properties of and features of this binary.
        @see ghidra.app.util.bin.format.pe.DllCharacteristics
        @return
        """
        ...

    def getFileAlignment(self) -> int:
        """
        @return the file alignment
        """
        ...

    def getImageBase(self) -> long:
        """
        @return the preferred load address of this file in memory
        """
        ...

    def getLoaderFlags(self) -> int:
        """
        Return the flags passed to the loader. Obsolete.
        @return
        """
        ...

    def getMajorImageVersion(self) -> int:
        """
        Get the major version number of the image.
        @return
        """
        ...

    def getMajorLinkerVersion(self) -> int:
        """
        Return the major version number of the linker that built this binary.
        @return
        """
        ...

    def getMajorOperatingSystemVersion(self) -> int:
        """
        Return the major version number of the required operating system.
        @return
        """
        ...

    def getMajorSubsystemVersion(self) -> int:
        """
        Get the major version number of the subsystem.
        """
        ...

    def getMinorImageVersion(self) -> int:
        """
        Get the minor version number of the image.
        @return
        """
        ...

    def getMinorLinkerVersion(self) -> int:
        """
        Return the minor version number of the linker that built this binary.
        @return
        """
        ...

    def getMinorOperatingSystemVersion(self) -> int:
        """
        Return the minor version number of the required operating system.
        @return
        """
        ...

    def getMinorSubsystemVersion(self) -> int:
        """
        Get the minor version number of the subsystem.
        @return
        """
        ...

    def getNumberOfRvaAndSizes(self) -> long: ...

    def getOriginalImageBase(self) -> long: ...

    def getSectionAlignment(self) -> int:
        """
        @return the section alignment
        """
        ...

    def getSizeOfCode(self) -> long:
        """
        Returns the combined total size of all sections with
         the <code>IMAGE_SCN_CNT_CODE</code> attribute.
        @return the combined total size of all sections with
         the <code>IMAGE_SCN_CNT_CODE</code> attribute.
        """
        ...

    def getSizeOfHeaders(self) -> long:
        """
        @return the combined size of all headers
        """
        ...

    def getSizeOfHeapCommit(self) -> long:
        """
        Return the size of the heap to commit
        @return
        """
        ...

    def getSizeOfHeapReserve(self) -> long:
        """
        Return the size of the heap reservation
        @return
        """
        ...

    def getSizeOfImage(self) -> long:
        """
        @return the RVA that would be assigned to the next section following the last section
        """
        ...

    def getSizeOfInitializedData(self) -> long:
        """
        Returns the combined size of all initialized data sections.
        @return the combined size of all initialized data sections
        """
        ...

    def getSizeOfStackCommit(self) -> long:
        """
        Return the size of the stack to commit
        @return
        """
        ...

    def getSizeOfStackReserve(self) -> long:
        """
        Return the size of the stack reservation
        @return
        """
        ...

    def getSizeOfUninitializedData(self) -> long:
        """
        Returns the size of all sections with the uninitialized
         data attributes.
        @return the size of all sections with the uninitialized data attributes
        """
        ...

    def getSubsystem(self) -> int:
        """
        Get the subsystem that is required to run this image.
        @return
        """
        ...

    def getWin32VersionValue(self) -> int:
        """
        This value is reserved, and must be 0
        """
        ...

    def hashCode(self) -> int: ...

    def is64bit(self) -> bool:
        """
        Returns true of this optional header is 64-bit.
        @return true of this optional header is 64-bit
        """
        ...

    def isCLI(self) -> bool:
        """
        @return true if the PE uses predominantly CLI code; otherwise, false.
        """
        ...

    def notify(self) -> None: ...

    def notifyAll(self) -> None: ...

    def processDataDirectories(self, monitor: ghidra.util.task.TaskMonitor) -> None:
        """
        This methods tells this optional header to process its data directories.
        """
        ...

    def setSizeOfCode(self, size: long) -> None:
        """
        @see #getSizeOfCode()
        """
        ...

    def setSizeOfHeaders(self, size: long) -> None:
        """
        @see #getSizeOfHeaders()
        """
        ...

    def setSizeOfImage(self, size: long) -> None:
        """
        @see #getSizeOfImage()
        """
        ...

    def setSizeOfInitializedData(self, size: long) -> None:
        """
        @see #getSizeOfInitializedData()
        """
        ...

    def setSizeOfUninitializedData(self, size: long) -> None:
        """
        @see #getSizeOfUninitializedData()
        """
        ...

    def toDataType(self) -> ghidra.program.model.data.DataType: ...

    def toString(self) -> unicode: ...

    def validateDataDirectories(self, program: ghidra.program.model.listing.Program) -> None: ...

    @overload
    def wait(self) -> None: ...

    @overload
    def wait(self, __a0: long) -> None: ...

    @overload
    def wait(self, __a0: long, __a1: int) -> None: ...

    def wasRebased(self) -> bool: ...

    def writeHeader(self, raf: java.io.RandomAccessFile, dc: ghidra.util.DataConverter) -> None:
        """
        Writes this optional header to the specified random access file.
        @param raf the random access file
        @param dc the data converter
        @throws IOException
        """
        ...

    @property
    def 64bit(self) -> bool: ...

    @property
    def CLI(self) -> bool: ...

    @property
    def addressOfEntryPoint(self) -> long: ...

    @property
    def baseOfCode(self) -> long: ...

    @property
    def baseOfData(self) -> long: ...

    @property
    def checksum(self) -> int: ...

    @property
    def dataDirectories(self) -> List[ghidra.app.util.bin.format.pe.DataDirectory]: ...

    @property
    def dllCharacteristics(self) -> int: ...

    @property
    def fileAlignment(self) -> int: ...

    @property
    def imageBase(self) -> long: ...

    @property
    def loaderFlags(self) -> int: ...

    @property
    def majorImageVersion(self) -> int: ...

    @property
    def majorLinkerVersion(self) -> int: ...

    @property
    def majorOperatingSystemVersion(self) -> int: ...

    @property
    def majorSubsystemVersion(self) -> int: ...

    @property
    def minorImageVersion(self) -> int: ...

    @property
    def minorLinkerVersion(self) -> int: ...

    @property
    def minorOperatingSystemVersion(self) -> int: ...

    @property
    def minorSubsystemVersion(self) -> int: ...

    @property
    def numberOfRvaAndSizes(self) -> long: ...

    @property
    def originalImageBase(self) -> long: ...

    @property
    def sectionAlignment(self) -> int: ...

    @property
    def sizeOfCode(self) -> long: ...

    @sizeOfCode.setter
    def sizeOfCode(self, value: long) -> None: ...

    @property
    def sizeOfHeaders(self) -> long: ...

    @sizeOfHeaders.setter
    def sizeOfHeaders(self, value: long) -> None: ...

    @property
    def sizeOfHeapCommit(self) -> long: ...

    @property
    def sizeOfHeapReserve(self) -> long: ...

    @property
    def sizeOfImage(self) -> long: ...

    @sizeOfImage.setter
    def sizeOfImage(self, value: long) -> None: ...

    @property
    def sizeOfInitializedData(self) -> long: ...

    @sizeOfInitializedData.setter
    def sizeOfInitializedData(self, value: long) -> None: ...

    @property
    def sizeOfStackCommit(self) -> long: ...

    @property
    def sizeOfStackReserve(self) -> long: ...

    @property
    def sizeOfUninitializedData(self) -> long: ...

    @sizeOfUninitializedData.setter
    def sizeOfUninitializedData(self, value: long) -> None: ...

    @property
    def subsystem(self) -> int: ...

    @property
    def win32VersionValue(self) -> int: ...
