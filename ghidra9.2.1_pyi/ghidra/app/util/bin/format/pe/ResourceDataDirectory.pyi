from typing import List
import ghidra.app.util.bin.format.pe
import ghidra.app.util.bin.format.pe.resource
import ghidra.app.util.importer
import ghidra.program.model.data
import ghidra.program.model.listing
import ghidra.util
import ghidra.util.task
import java.io
import java.lang


class ResourceDataDirectory(ghidra.app.util.bin.format.pe.DataDirectory):
    """
    Points to the root resource directory.
    """

    IMAGE_RESOURCE_DATA_IS_DIRECTORY: int = -2147483648
    IMAGE_RESOURCE_NAME_IS_STRING: int = -2147483648
    IMAGE_SIZEOF_RESOURCE_DIRECTORY: int = 16
    IMAGE_SIZEOF_RESOURCE_DIRECTORY_ENTRY: int = 8
    PREDEFINED_RESOURCE_NAMES: List[unicode] = array(java.lang.String, [u'0', u'Cursor', u'Bitmap', u'Icon', u'Menu', u'Dialog', u'StringTable', u'FontDir', u'Font', u'Accelerator', u'RC_Data', u'MessageTable', u'GroupCursor', u'13', u'GroupIcon', u'15', u'Version', u'DialogInclude', u'18', u'PlugAndPlay', u'VXD', u'ANI_Cursor', u'ANI_Icon', u'HTML', u'Manifest'])
    RT_ACCELERATOR: int = 9
    RT_ANICURSOR: int = 21
    RT_ANIICON: int = 22
    RT_BITMAP: int = 2
    RT_CURSOR: int = 1
    RT_DIALOG: int = 5
    RT_DLGINCLUDE: int = 17
    RT_FONT: int = 8
    RT_FONTDIR: int = 7
    RT_GROUP_CURSOR: int = 12
    RT_GROUP_ICON: int = 14
    RT_HTML: int = 23
    RT_ICON: int = 3
    RT_MANIFEST: int = 24
    RT_MENU: int = 4
    RT_MESSAGETABLE: int = 11
    RT_NOTDEFINED: int = 0
    RT_PLUGPLAY: int = 19
    RT_RCDATA: int = 10
    RT_STRING: int = 6
    RT_VERSION: int = 16
    RT_VXD: int = 20
    directoryMap: java.util.Set



    def __init__(self):
        """
        DO NOT USE THIS CONSTRUCTOR, USE create*(GenericFactory ...) FACTORY METHODS INSTEAD.
        """
        ...



    def equals(self, __a0: object) -> bool: ...

    def getClass(self) -> java.lang.Class: ...

    def getDirectoryName(self) -> unicode: ...

    def getPointer(self) -> int: ...

    def getResources(self) -> List[ghidra.app.util.bin.format.pe.resource.ResourceInfo]: ...

    def getRootDirectory(self) -> ghidra.app.util.bin.format.pe.resource.ResourceDirectory: ...

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
        @see ghidra.app.util.bin.StructConverter#toDataType()
        """
        ...

    def toString(self) -> unicode: ...

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
    def resources(self) -> List[object]: ...

    @property
    def rootDirectory(self) -> ghidra.app.util.bin.format.pe.resource.ResourceDirectory: ...
