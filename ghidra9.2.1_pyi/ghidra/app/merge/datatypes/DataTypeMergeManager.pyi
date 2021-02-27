from typing import List
import ghidra.app.merge
import ghidra.util.task
import java.lang


class DataTypeMergeManager(object, ghidra.app.merge.MergeResolver):
    """
    Manager for merging category and data type changes
    """





    def __init__(self, mergeManager: ghidra.framework.data.DomainObjectMergeManager, resultDomainObject: ghidra.program.model.data.DataTypeManagerDomainObject, myDomainObject: ghidra.program.model.data.DataTypeManagerDomainObject, originalDomainObject: ghidra.program.model.data.DataTypeManagerDomainObject, latestDomainObject: ghidra.program.model.data.DataTypeManagerDomainObject, latestChanges: ghidra.program.model.listing.DataTypeChangeSet, myChanges: ghidra.program.model.listing.DataTypeChangeSet):
        """
        Manager for merging the data types using the four programs.
        @param mergeManager overall merge manager for domain object
        @param resultDomainObject the program to be updated with the result of the merge.
         This is the program that will actually get checked in.
        @param myDomainObject the program requesting to be checked in.
        @param originalDomainObject the program that was checked out.
        @param latestDomainObject the latest checked-in version of the program.
        @param latestChanges the address set of changes between original and latest versioned program.
        @param myChanges the address set of changes between original and my modified program.
        """
        ...



    def apply(self) -> None: ...

    def cancel(self) -> None: ...

    def equals(self, __a0: object) -> bool: ...

    def getClass(self) -> java.lang.Class: ...

    def getDescription(self) -> unicode: ...

    def getName(self) -> unicode: ...

    def getPhases(self) -> List[unicode]: ...

    def hashCode(self) -> int: ...

    def merge(self, monitor: ghidra.util.task.TaskMonitor) -> None:
        """
        Merge the data types using the four programs.
        @param monitor merge task monitor
        @see MergeConstants
        """
        ...

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
    def description(self) -> unicode: ...

    @property
    def name(self) -> unicode: ...

    @property
    def phases(self) -> List[unicode]: ...
