from typing import List
import ghidra.app.util.bin
import ghidra.app.util.bin.format.pe
import ghidra.app.util.importer
import ghidra.program.model.data
import ghidra.program.model.listing
import ghidra.util
import ghidra.util.task
import java.io
import java.lang


class BaseRelocationDataDirectory(ghidra.app.util.bin.format.pe.DataDirectory, ghidra.app.util.bin.ByteArrayConverter):
    """
    Points to the base relocation information.
    """





    def __init__(self):
        """
        DO NOT USE THIS CONSTRUCTOR, USE create*(GenericFactory ...) FACTORY METHODS INSTEAD.
        """
        ...



    def addBaseRelocation(self, reloc: ghidra.app.util.bin.format.pe.BaseRelocation) -> None:
        """
        Adds the specified base relocation.
        @param reloc the new base relocation
        """
        ...

    def createBaseRelocation(self, va: int) -> ghidra.app.util.bin.format.pe.BaseRelocation:
        """
        Create a new base relocation using the specified
         virtual address.
        @param va the virtual address of the new base relocation
        @return the new base relocation
        """
        ...

    def equals(self, __a0: object) -> bool: ...

    def getBaseRelocations(self) -> List[ghidra.app.util.bin.format.pe.BaseRelocation]:
        """
        Returns the array of base relocations defined in this base relocation data directory.
        @return the array of base relocations defined in this base relocation data directory
        """
        ...

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

    def markup(self, program: ghidra.program.model.listing.Program, isBinary: bool, monitor: ghidra.util.task.TaskMonitor, log: ghidra.app.util.importer.MessageLog, ntHeader: ghidra.app.util.bin.format.pe.NTHeader) -> None: ...

    def notify(self) -> None: ...

    def notifyAll(self) -> None: ...

    def parse(self) -> bool: ...

    def removeAllRelocations(self) -> None:
        """
        Removes all base relocations from this base relocation
         directory.
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

    def toBytes(self, dc: ghidra.util.DataConverter) -> List[int]:
        """
        @see ghidra.app.util.bin.ByteArrayConverter#toBytes(ghidra.util.DataConverter)
        """
        ...

    def toDataType(self) -> ghidra.program.model.data.DataType:
        """
        @see ghidra.app.util.bin.StructConverter#toDataType()
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
    def baseRelocations(self) -> List[ghidra.app.util.bin.format.pe.BaseRelocation]: ...

    @property
    def directoryName(self) -> unicode: ...
