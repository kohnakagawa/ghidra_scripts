from typing import List
import ghidra.app.util.bin.format.pe
import ghidra.program.model.data
import ghidra.program.model.listing
import ghidra.util
import ghidra.util.task
import java.io
import java.lang


class OptionalHeaderImpl(object, ghidra.app.util.bin.format.pe.OptionalHeader):
    """

     typedef struct _IMAGE_OPTIONAL_HEADER {
         WORD    Magic;									// MANDATORY
         BYTE    MajorLinkerVersion;
         BYTE    MinorLinkerVersion;
         DWORD   SizeOfCode;
         DWORD   SizeOfInitializedData;
         DWORD   SizeOfUninitializedData;
         DWORD   AddressOfEntryPoint;						// MANDATORY
         DWORD   BaseOfCode;
         DWORD   BaseOfData;
         DWORD   ImageBase;								// MANDATORY
         DWORD   SectionAlignment;						// MANDATORY
         DWORD   FileAlignment;							// MANDATORY
         WORD    MajorOperatingSystemVersion;				// MANDATORY
         WORD    MinorOperatingSystemVersion;
         WORD    MajorImageVersion;
         WORD    MinorImageVersion;
         WORD    MajorSubsystemVersion;
         WORD    MinorSubsystemVersion;
         DWORD   Win32VersionValue;
         DWORD   SizeOfImage;								// MANDATORY
         DWORD   SizeOfHeaders;							// MANDATORY
         DWORD   CheckSum;
         WORD    Subsystem;								// MANDATORY
         WORD    DllCharacteristics;
         DWORD   SizeOfStackReserve;
         DWORD   SizeOfStackCommit;
         DWORD   SizeOfHeapReserve;
         DWORD   SizeOfHeapCommit;
         DWORD   LoaderFlags;
         DWORD   NumberOfRvaAndSizes;						// USED
         IMAGE_DATA_DIRECTORY DataDirectory[IMAGE_NUMBEROF_DIRECTORY_ENTRIES];
     };



     typedef struct _IMAGE_OPTIONAL_HEADER64 {
         WORD        Magic;
         BYTE        MajorLinkerVersion;
         BYTE        MinorLinkerVersion;
         DWORD       SizeOfCode;
         DWORD       SizeOfInitializedData;
         DWORD       SizeOfUninitializedData;
         DWORD       AddressOfEntryPoint;
         DWORD       BaseOfCode;
         ULONGLONG   ImageBase;
         DWORD       SectionAlignment;
         DWORD       FileAlignment;
         WORD        MajorOperatingSystemVersion;
         WORD        MinorOperatingSystemVersion;
         WORD        MajorImageVersion;
         WORD        MinorImageVersion;
         WORD        MajorSubsystemVersion;
         WORD        MinorSubsystemVersion;
         DWORD       Win32VersionValue;
         DWORD       SizeOfImage;
         DWORD       SizeOfHeaders;
         DWORD       CheckSum;
         WORD        Subsystem;
         WORD        DllCharacteristics;
         ULONGLONG   SizeOfStackReserve;
         ULONGLONG   SizeOfStackCommit;
         ULONGLONG   SizeOfHeapReserve;
         ULONGLONG   SizeOfHeapCommit;
         DWORD       LoaderFlags;
         DWORD       NumberOfRvaAndSizes;
         IMAGE_DATA_DIRECTORY DataDirectory[IMAGE_NUMBEROF_DIRECTORY_ENTRIES];
     };

    """

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



    def __init__(self):
        """
        DO NOT USE THIS CONSTRUCTOR, USE create*(GenericFactory ...) FACTORY METHODS INSTEAD.
        """
        ...



    def equals(self, __a0: object) -> bool: ...

    def getAddressOfEntryPoint(self) -> long: ...

    def getBaseOfCode(self) -> long: ...

    def getBaseOfData(self) -> long: ...

    def getChecksum(self) -> int: ...

    def getClass(self) -> java.lang.Class: ...

    def getDataDirectories(self) -> List[ghidra.app.util.bin.format.pe.DataDirectory]: ...

    def getDllCharacteristics(self) -> int: ...

    def getFileAlignment(self) -> int: ...

    def getImageBase(self) -> long: ...

    def getLoaderFlags(self) -> int: ...

    def getMajorImageVersion(self) -> int: ...

    def getMajorLinkerVersion(self) -> int: ...

    def getMajorOperatingSystemVersion(self) -> int: ...

    def getMajorSubsystemVersion(self) -> int: ...

    def getMinorImageVersion(self) -> int: ...

    def getMinorLinkerVersion(self) -> int: ...

    def getMinorOperatingSystemVersion(self) -> int: ...

    def getMinorSubsystemVersion(self) -> int: ...

    def getNumberOfRvaAndSizes(self) -> long: ...

    def getOriginalImageBase(self) -> long: ...

    def getSectionAlignment(self) -> int: ...

    def getSizeOfCode(self) -> long: ...

    def getSizeOfHeaders(self) -> long: ...

    def getSizeOfHeapCommit(self) -> long: ...

    def getSizeOfHeapReserve(self) -> long: ...

    def getSizeOfImage(self) -> long: ...

    def getSizeOfInitializedData(self) -> long: ...

    def getSizeOfStackCommit(self) -> long: ...

    def getSizeOfStackReserve(self) -> long: ...

    def getSizeOfUninitializedData(self) -> long: ...

    def getSubsystem(self) -> int: ...

    def getWin32VersionValue(self) -> int: ...

    def hashCode(self) -> int: ...

    def is64bit(self) -> bool: ...

    def isCLI(self) -> bool: ...

    def notify(self) -> None: ...

    def notifyAll(self) -> None: ...

    def processDataDirectories(self, monitor: ghidra.util.task.TaskMonitor) -> None: ...

    def setSizeOfCode(self, size: long) -> None: ...

    def setSizeOfHeaders(self, size: long) -> None: ...

    def setSizeOfImage(self, size: long) -> None: ...

    def setSizeOfInitializedData(self, size: long) -> None: ...

    def setSizeOfUninitializedData(self, size: long) -> None: ...

    def toDataType(self) -> ghidra.program.model.data.DataType:
        """
        @see ghidra.app.util.bin.StructConverter#toDataType()
        """
        ...

    def toString(self) -> unicode: ...

    def validateDataDirectories(self, program: ghidra.program.model.listing.Program) -> None: ...

    @overload
    def wait(self) -> None: ...

    @overload
    def wait(self, __a0: long) -> None: ...

    @overload
    def wait(self, __a0: long, __a1: int) -> None: ...

    def wasRebased(self) -> bool: ...

    def writeHeader(self, raf: java.io.RandomAccessFile, dc: ghidra.util.DataConverter) -> None: ...

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
