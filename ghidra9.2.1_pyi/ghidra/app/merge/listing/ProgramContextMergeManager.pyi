from typing import List
import ghidra.app.merge
import ghidra.app.merge.listing
import ghidra.util.task
import java.lang


class ProgramContextMergeManager(object, ghidra.app.merge.MergeResolver, ghidra.app.merge.listing.ListingMergeConstants):
    """
    ProgramContextMergeManager merges register value changes
     for multi-user program versions. It merges changes for each named register
     in the program.
     Note: If a register gets changed that is part of another register that has been set,
     then each named register will get merged independently. This means that
     when in conflict with another version the conflict would arise for each
     instead of just the larger register.
    """

    ASK_USER: int = 0
    CANCELED: int = -1
    CHECKED_OUT_BUTTON_NAME: unicode = u'CheckedOutVersionRB'
    CHECKED_OUT_CHECK_BOX_NAME: unicode = u'CheckedOutVersionCheckBox'
    CHECKED_OUT_LABEL_NAME: unicode = u'CheckedOutVersionLabel'
    CHECKED_OUT_LIST_BUTTON_NAME: unicode = u'CheckedOutListRB'
    INFO_ROW: int = 0
    KEEP_ALL: int = 7
    KEEP_BOTH: int = 6
    KEEP_LATEST: int = 2
    KEEP_MY: int = 4
    KEEP_ORIGINAL: int = 1
    KEEP_RESULT: int = 8
    LATEST_BUTTON_NAME: unicode = u'LatestVersionRB'
    LATEST_CHECK_BOX_NAME: unicode = u'LatestVersionCheckBox'
    LATEST_LABEL_NAME: unicode = u'LatestVersionLabel'
    LATEST_LIST_BUTTON_NAME: unicode = u'LatestListRB'
    LATEST_TITLE: unicode = u'Latest'
    MY_TITLE: unicode = u'Checked Out'
    ORIGINAL_BUTTON_NAME: unicode = u'OriginalVersionRB'
    ORIGINAL_CHECK_BOX_NAME: unicode = u'OriginalVersionCheckBox'
    ORIGINAL_LABEL_NAME: unicode = u'OriginalVersionLabel'
    ORIGINAL_TITLE: unicode = u'Original'
    REMOVE_CHECKED_OUT_BUTTON_NAME: unicode = u'RemoveCheckedOutRB'
    REMOVE_LATEST: int = 8
    REMOVE_LATEST_BUTTON_NAME: unicode = u'RemoveLatestRB'
    REMOVE_MY: int = 32
    RENAME_CHECKED_OUT_BUTTON_NAME: unicode = u'RenameCheckedOutRB'
    RENAME_LATEST: int = 16
    RENAME_LATEST_BUTTON_NAME: unicode = u'RenameLatestRB'
    RENAME_MY: int = 64
    RESULT_BUTTON_NAME: unicode = u'ResultVersionRB'
    RESULT_TITLE: unicode = u'Result'
    TRUNCATE_LENGTH: int = 160



    def __init__(self, mergeManager: ghidra.app.merge.ProgramMultiUserMergeManager, resultPgm: ghidra.program.model.listing.Program, originalPgm: ghidra.program.model.listing.Program, latestPgm: ghidra.program.model.listing.Program, myPgm: ghidra.program.model.listing.Program, latestChanges: ghidra.program.model.listing.ProgramChangeSet, myChanges: ghidra.program.model.listing.ProgramChangeSet):
        """
        Creates a new <code>ProgramContextMergeManager</code>.
        @param resultPgm the program to be updated with the result of the merge.
         This is the program that will actually get checked in.
        @param originalPgm the program that was checked out.
        @param latestPgm the latest checked-in version of the program.
        @param myPgm the program requesting to be checked in.
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

    def merge(self, monitor: ghidra.util.task.TaskMonitor) -> None: ...

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
