from typing import List
import ghidra.formats.gfilesystem
import ghidra.plugins.importer.batch
import ghidra.util.task
import java.lang


class BatchInfo(object):
    """
    This is the main state of a batch import task, containing the segregated groupings of
     applications.

     This class also handles populating the batch groups by recursively descending into files
     and the contents of those files.
    """

    MAXDEPTH_DEFAULT: int = 2
    MAXDEPTH_UNLIMITED: int = -1



    @overload
    def __init__(self):
        """
        Creates a new BatchInfo object with a default {@link #maxDepth}.
        """
        ...

    @overload
    def __init__(self, maxDepth: int):
        """
        Creates a new BatchInfo object using the specified maxDepth.
        @param maxDepth see {@link #maxDepth}.
        """
        ...



    def addFile(self, fsrl: ghidra.formats.gfilesystem.FSRL, taskMonitor: ghidra.util.task.TaskMonitor) -> bool:
        """
        Adds a file to this batch as the direct result of a user action.
         <p>
         If the file is a container for other files, this method will iterate through those
         child files and recursively try to add them using this method.
         <p>
        @param fsrl {@link FSRL} of the file to add.
        @param taskMonitor {@link TaskMonitor} to watch and update with progress.
        @return boolean true if something in the the file produced something to import.
        @throws IOException if io error when reading files.
        @throws CancelledException if user cancels.
        """
        ...

    def equals(self, __a0: object) -> bool: ...

    def getClass(self) -> java.lang.Class: ...

    def getEnabledCount(self) -> int:
        """
        Returns the count of applications in enabled {@link BatchGroup}s... in other
         words, the number of objects that would be imported during this batch.
        @return count of enabled applications.
        """
        ...

    def getGroups(self) -> List[ghidra.plugins.importer.batch.BatchGroup]:
        """
        Returns a list of the {@link BatchGroup}s that have been found when processing
         the added files.
        @return {@link List} of {@link BatchGroup}s.
        """
        ...

    def getMaxDepth(self) -> int:
        """
        Maximum depth of containers (ie. filesystems) to recurse into when processing
         a file added by the user
        @return the current maximum depth of containers (ie. filesystems) to recurse into when processing
         a file added by the user.
        """
        ...

    def getTotalCount(self) -> int:
        """
        Returns the count of how many importable objects (ie. {@link LoadSpec}s) were found.
        @return count of importable objects.
        """
        ...

    def getTotalRawCount(self) -> int:
        """
        Returns the count of how many files were found while processing the source files.
        @return count of files found while processing source files.
        """
        ...

    def getUserAddedSources(self) -> List[ghidra.plugins.importer.batch.UserAddedSourceInfo]:
        """
        Returns the {@link List} of files added via {@link #addFile(FSRL, TaskMonitor)}.
        @return {@link List} of files added via {@link #addFile(FSRL, TaskMonitor)}.
        """
        ...

    def hashCode(self) -> int: ...

    def isSingleApp(self) -> bool:
        """
        Checks the found applications and returns true if only a single binary was found,
         even if multiple loaders claim it.
        @return true if single binary and batch is probably not correct importer.
        """
        ...

    def notify(self) -> None: ...

    def notifyAll(self) -> None: ...

    def remove(self, fsrl: ghidra.formats.gfilesystem.FSRL) -> None:
        """
        Removes a user-added source file (and all the embedded files inside it) from this
         batch.
        @param fsrl {@link FSRL} of the file to remove.
        """
        ...

    def setMaxDepth(self, newMaxDepth: int) -> None:
        """
        Sets a new max container recursive depth limit for this batch import
         <p>
         Doing this requires rescanning all original user-added source files and stopping
         at the new max depth.
         <p>
        @param newMaxDepth new value for the max depth
        """
        ...

    def toString(self) -> unicode: ...

    @overload
    def wait(self) -> None: ...

    @overload
    def wait(self, __a0: long) -> None: ...

    @overload
    def wait(self, __a0: long, __a1: int) -> None: ...

    def wasRecurseTerminatedEarly(self) -> bool:
        """
        Returns true if any of the user source files had containers that were not
         recursed into because of the {@link #maxDepth} limit.
        @return true if any of the user source files had containers that were not
         recursed into because of the {@link #maxDepth} limit.
        """
        ...

    @property
    def enabledCount(self) -> int: ...

    @property
    def groups(self) -> List[object]: ...

    @property
    def maxDepth(self) -> int: ...

    @maxDepth.setter
    def maxDepth(self, value: int) -> None: ...

    @property
    def singleApp(self) -> bool: ...

    @property
    def totalCount(self) -> int: ...

    @property
    def totalRawCount(self) -> int: ...

    @property
    def userAddedSources(self) -> List[object]: ...
