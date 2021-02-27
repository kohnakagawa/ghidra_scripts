from typing import List
import ghidra.app.merge
import ghidra.app.merge.listing
import ghidra.util.task
import java.lang


class FunctionTagMerger(object, ghidra.app.merge.MergeResolver, ghidra.app.merge.listing.ListingMergeConstants):
    """
    Class for merging function tag changes. Most tag differences can be easily auto-merged,
     which is to say the result will be the set of all of tags from both program 1 and
     program 2. Conflicts arise when both parties have edited/deleted the same tag.

     The specific cases handled by the class are described below, where:

      - X and Y are tags
      - X(A) means to take A's version of tag X
      - ** indicates a conflict
      - NP means the situation is not possible

     		User A	|	Add X	Add Y	Delete X	Delete Y	Edit X		Edit Y
     				|
     User B		|
     ---------------------------------------------------------------------------
     Add X		|	X		X,Y			NP			X		NP			X,Y(A)
     				|
     Add Y		|	X,Y		Y			Y			NP		X(A),Y		NP
     				|
     Delete X		|	NP		Y			-			-		**			Y(A)
     				|
     Delete Y		|	X		NP			-			-		X(A)		**
     				|
     Edit X		|	NP		X(B),Y		**			X(B)	**			X(B),Y(A)
     				|
     Edit Y		|	X,Y(B)	NP			Y(B)		**		X(A),Y(B)	**
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
        Constructor.
        @param mergeManager the merge manager
        @param resultPgm the program storing the result of the merge
        @param originalPgm the state of the program before any changes
        @param latestPgm the checked in program version
        @param myPgm the checked out program version
        @param latestChanges tag changes in Latest
        @param myChanges tag changes in My
        """
        ...



    def apply(self) -> None: ...

    def cancel(self) -> None: ...

    def equals(self, __a0: object) -> bool: ...

    def getClass(self) -> java.lang.Class: ...

    def getDescription(self) -> unicode: ...

    def getName(self) -> unicode:
        """
        PUBLIC METHODS
        """
        ...

    def getPhases(self) -> List[unicode]: ...

    def hashCode(self) -> int: ...

    def merge(self, monitor: ghidra.util.task.TaskMonitor) -> None: ...

    def notify(self) -> None: ...

    def notifyAll(self) -> None: ...

    def setConflictResolution(self, option: int) -> None:
        """
        For JUnit testing only, set the option for resolving a conflict.
        @param option
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
    def conflictResolution(self) -> None: ...  # No getter available.

    @conflictResolution.setter
    def conflictResolution(self, value: int) -> None: ...

    @property
    def description(self) -> unicode: ...

    @property
    def name(self) -> unicode: ...

    @property
    def phases(self) -> List[unicode]: ...
