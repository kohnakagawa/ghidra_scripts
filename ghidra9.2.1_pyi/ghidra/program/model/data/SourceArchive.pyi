import ghidra.program.model.data
import ghidra.util
import java.lang


class SourceArchive(object):
    """
    DataTypeSource holds information about a single data type archive which supplied a data type
     to the program.
    """









    def equals(self, __a0: object) -> bool: ...

    def getArchiveType(self) -> ghidra.program.model.data.ArchiveType:
        """
        Gets an indicator for the type of data type archive.
         (ArchiveType.BUILT_IN, ArchiveType.PROGRAM, ArchiveType.PROJECT, ArchiveType.FILE)
        @return the type
        """
        ...

    def getClass(self) -> java.lang.Class: ...

    def getDomainFileID(self) -> unicode:
        """
        Gets the ID used to uniquely identify the domain file for the data type archive.
        @return the domain file identifier
        """
        ...

    def getLastSyncTime(self) -> long:
        """
        Returns the last time that this source archive was synchronized to the containing
         DataTypeManager.
        @return the last time that this source archive was synchronized to the containing
         DataTypeManager.
        """
        ...

    def getName(self) -> unicode:
        """
        Returns the name of the source archive
        @return the name of the source archive.
        """
        ...

    def getSourceArchiveID(self) -> ghidra.util.UniversalID:
        """
        Gets the ID that the program has associated with the data type archive.
        @return the data type archive ID
        """
        ...

    def hashCode(self) -> int: ...

    def isDirty(self) -> bool:
        """
        Returns true if at least one data type that originally came from this source archive has been
         changed.
        @return true if at least one data type that originally came from this source archive has been
         changed.
        """
        ...

    def notify(self) -> None: ...

    def notifyAll(self) -> None: ...

    def setDirtyFlag(self, dirty: bool) -> None:
        """
        Sets the dirty flag to indicate if at least one data type that originally came from the
         associated source archive has been changed since the last time the containing DataTypeManager
         was synchronized with it.
        @param dirty true means at least one data type that originally came from this source archive has been
         changed.
        """
        ...

    def setLastSyncTime(self, time: long) -> None:
        """
        Sets the last time that this source archive was synchronized to the containing
         DataTypeManager.
        @param time the last time that this source archive was synchronized to the containing
         DataTypeManager.
        """
        ...

    def setName(self, name: unicode) -> None:
        """
        Sets the name of the source archive associated with this SourceArchive object.
        @param name the name of the associated source archive.
        """
        ...

    def toString(self) -> unicode: ...

    @overload
    def wait(self) -> None: ...

    @overload
    def wait(self, __a0: long) -> None: ...

    @overload
    def wait(self, __a0: long, __a1: int) -> None: ...

    @property
    def archiveType(self) -> ghidra.program.model.data.ArchiveType: ...

    @property
    def dirty(self) -> bool: ...

    @property
    def dirtyFlag(self) -> None: ...  # No getter available.

    @dirtyFlag.setter
    def dirtyFlag(self, value: bool) -> None: ...

    @property
    def domainFileID(self) -> unicode: ...

    @property
    def lastSyncTime(self) -> long: ...

    @lastSyncTime.setter
    def lastSyncTime(self, value: long) -> None: ...

    @property
    def name(self) -> unicode: ...

    @name.setter
    def name(self, value: unicode) -> None: ...

    @property
    def sourceArchiveID(self) -> ghidra.util.UniversalID: ...
