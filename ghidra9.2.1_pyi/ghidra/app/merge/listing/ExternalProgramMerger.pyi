from typing import List
import ghidra.app.merge
import ghidra.app.merge.listing
import ghidra.app.merge.listing.ExternalProgramMerger
import ghidra.program.model.listing
import ghidra.util.task
import java.lang


class ExternalProgramMerger(object, ghidra.app.merge.MergeResolver, ghidra.app.merge.listing.ListingMergeConstants):
    """
    Manages external program name changes and conflicts between the latest versioned
     program and the modified program being checked into version control.
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
        Manages code unit changes and conflicts between the latest versioned
         program and the modified program being checked into version control.
        @param mergeManager the top level merge manager for merging a program version.
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

    def autoMerge(self, monitor: ghidra.util.task.TaskMonitor) -> None: ...

    def cancel(self) -> None: ...

    def equals(self, __a0: object) -> bool: ...

    def getClass(self) -> java.lang.Class: ...

    def getConflictCount(self) -> int: ...

    def getConflictInfo(self, idGroup: ghidra.app.merge.listing.ExternalProgramMerger.IDGroup, conflictIndex: int, totalConflicts: int) -> unicode:
        """
        Gets the information to display at the top of the conflict window indicating
         which conflict this is of the total external program name conflicts.
        @param idGroup the symbol ID group for the external program (Library) in conflict.
        @param conflictIndex the index of the current conflict.
        @param totalConflicts the total number of conflicts.
        """
        ...

    def getConflicts(self) -> List[ghidra.app.merge.listing.ExternalProgramMerger.IDGroup]:
        """
        Returns an array of symbol ID groups for all the external programs that are in conflict.
        """
        ...

    def getDescription(self) -> unicode: ...

    def getName(self) -> unicode: ...

    def getPhases(self) -> List[unicode]: ...

    def hasConflict(self) -> bool: ...

    def hashCode(self) -> int: ...

    def init(self) -> None: ...

    def merge(self, monitor: ghidra.util.task.TaskMonitor) -> None: ...

    def mergeConflicts(self, chosenConflictOption: int, monitor: ghidra.util.task.TaskMonitor) -> None:
        """
        Performs a manual merge of external program conflicts.
        @param chosenConflictOption ASK_USER means interactively resolve conflicts.
         JUnit testing also allows setting this to LATEST, MY, or ORIGINAL to force
         selection of a particular version change.
        @param monitor task monitor for informing the user of progress.
        @throws CancelledException if the user cancels the merge.
        """
        ...

    def mergeExternalProgramName(self, program1: ghidra.program.model.listing.Program, program2: ghidra.program.model.listing.Program, idGroup: ghidra.app.merge.listing.ExternalProgramMerger.IDGroup, monitor: ghidra.util.task.TaskMonitor) -> None:
        """
        Actually merges (sets or removes) the indicated external program name in
         program1 based on the same external program name in program2
        @param program1 the program to merge into.
        @param program2 the program to get the merge information from.
        @param idGroup the symbol ID group for the external program (Library) to merge.
        @param monitor task monitor for feedback or canceling the merge.s
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
    def conflictCount(self) -> int: ...

    @property
    def conflicts(self) -> List[ghidra.app.merge.listing.ExternalProgramMerger.IDGroup]: ...

    @property
    def description(self) -> unicode: ...

    @property
    def name(self) -> unicode: ...

    @property
    def phases(self) -> List[unicode]: ...
