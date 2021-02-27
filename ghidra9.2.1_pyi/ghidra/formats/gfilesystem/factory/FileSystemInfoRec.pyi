import ghidra.formats.gfilesystem.factory
import java.lang


class FileSystemInfoRec(object):
    """
    Holds information read from a FileSystemInfo annotation.

    """

    BY_PRIORITY: java.util.Comparator = ghidra.formats.gfilesystem.factory.FileSystemInfoRec$$Lambda$1117/0x00000008014c6440@49c19e87







    def equals(self, __a0: object) -> bool: ...

    @staticmethod
    def fromClass(fsClazz: java.lang.Class) -> ghidra.formats.gfilesystem.factory.FileSystemInfoRec:
        """
        Instantiate a new {@link FileSystemInfoRec} from the information found in the
         {@link FileSystemInfo} annotation attached to the specified Class.
        @param fsClazz class to query for file system info.
        @return new {@link FileSystemInfoRec}, or null if the class doesn't have
         valid file system meta data.
        """
        ...

    def getClass(self) -> java.lang.Class: ...

    def getDescription(self) -> unicode:
        """
        Filesystem description, ie. "XYZ Vendor Filesystem Type 1"
        @return description string
        """
        ...

    def getFSClass(self) -> java.lang.Class:
        """
        The {@link Class} of the filesystem implementation.
        @return {@link GFileSystem} derived class.
        """
        ...

    def getFactory(self) -> ghidra.formats.gfilesystem.factory.GFileSystemFactory:
        """
        The {@link GFileSystemFactory} instance that will create new filesystem
         instances when needed.
        @return {@link GFileSystemFactory} for this filesystem
        """
        ...

    def getPriority(self) -> int:
        """
        Filesystem relative priority.
         <p>
         See {@link FileSystemInfo#priority()}.
        @return priority int
        """
        ...

    def getType(self) -> unicode:
        """
        Filesystem 'type', ie. "file", or "zip", etc.
        @return type string
        """
        ...

    def hashCode(self) -> int: ...

    def notify(self) -> None: ...

    def notifyAll(self) -> None: ...

    def toString(self) -> unicode: ...

    @overload
    def wait(self) -> None: ...

    @overload
    def wait(self, __a0: long) -> None: ...

    @overload
    def wait(self, __a0: long, __a1: int) -> None: ...

    @property
    def FSClass(self) -> java.lang.Class: ...

    @property
    def description(self) -> unicode: ...

    @property
    def factory(self) -> ghidra.formats.gfilesystem.factory.GFileSystemFactory: ...

    @property
    def priority(self) -> int: ...

    @property
    def type(self) -> unicode: ...
