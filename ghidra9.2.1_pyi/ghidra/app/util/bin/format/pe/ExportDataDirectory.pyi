from typing import List
import ghidra.app.util.bin.format.pe
import ghidra.app.util.importer
import ghidra.program.model.data
import ghidra.program.model.listing
import ghidra.util
import ghidra.util.task
import java.io
import java.lang


class ExportDataDirectory(ghidra.app.util.bin.format.pe.DataDirectory):
    """
    A class to represent the IMAGE_EXPORT_DIRECTORY
     data structure defined in winnt.h.

     typedef struct _IMAGE_EXPORT_DIRECTORY {
         DWORD   Characteristics;
         DWORD   TimeDateStamp;
         WORD    MajorVersion;
         WORD    MinorVersion;
         DWORD   Name;
         DWORD   Base;
         DWORD   NumberOfFunctions;
         DWORD   NumberOfNames;
         DWORD   AddressOfFunctions;     // RVA from base of image
         DWORD   AddressOfNames;         // RVA from base of image
         DWORD   AddressOfNameOrdinals;  // RVA from base of image
     };

    """

    IMAGE_SIZEOF_EXPORT_DIRECTORY: int = 40



    def __init__(self):
        """
        DO NOT USE THIS CONSTRUCTOR, USE create*(GenericFactory ...) FACTORY METHODS INSTEAD.
        """
        ...



    def equals(self, __a0: object) -> bool: ...

    def getAddressOfFunctions(self) -> int: ...

    def getAddressOfNameOrdinals(self) -> int: ...

    def getAddressOfNames(self) -> int: ...

    def getBase(self) -> int: ...

    def getCharacteristics(self) -> int: ...

    def getClass(self) -> java.lang.Class: ...

    def getDirectoryName(self) -> unicode: ...

    def getExportName(self) -> unicode: ...

    def getExports(self) -> List[ghidra.app.util.bin.format.pe.ExportInfo]:
        """
        Returns an array of the exports defined in this export data directory.
        @return an array of the exports defined in this export data directory
        """
        ...

    def getMajorVersion(self) -> int: ...

    def getMinorVersion(self) -> int: ...

    def getName(self) -> int: ...

    def getNumberOfFunctions(self) -> int: ...

    def getNumberOfNames(self) -> int: ...

    def getPointer(self) -> int: ...

    def getSize(self) -> int:
        """
        Returns the size of this data directory.
        @return the size of this data directory
        """
        ...

    def getTimeDateStamp(self) -> int: ...

    def getVirtualAddress(self) -> int:
        """
        Returns the relative virtual address of this data directory.
        @return the relative virtual address of this data directory
        """
        ...

    def hasParsedCorrectly(self) -> bool: ...

    def hashCode(self) -> int: ...

    def markup(self, program: ghidra.program.model.listing.Program, isBinary: bool, monitor: ghidra.util.task.TaskMonitor, log: ghidra.app.util.importer.MessageLog, ntHeader: ghidra.app.util.bin.format.pe.NTHeader) -> None: ...

    def notify(self) -> None: ...

    def notifyAll(self) -> None: ...

    def parse(self) -> bool: ...

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

    def toDataType(self) -> ghidra.program.model.data.DataType: ...

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
    def addressOfFunctions(self) -> int: ...

    @property
    def addressOfNameOrdinals(self) -> int: ...

    @property
    def addressOfNames(self) -> int: ...

    @property
    def base(self) -> int: ...

    @property
    def characteristics(self) -> int: ...

    @property
    def directoryName(self) -> unicode: ...

    @property
    def exportName(self) -> unicode: ...

    @property
    def exports(self) -> List[ghidra.app.util.bin.format.pe.ExportInfo]: ...

    @property
    def majorVersion(self) -> int: ...

    @property
    def minorVersion(self) -> int: ...

    @property
    def name(self) -> int: ...

    @property
    def numberOfFunctions(self) -> int: ...

    @property
    def numberOfNames(self) -> int: ...

    @property
    def timeDateStamp(self) -> int: ...
