from typing import List
import ghidra.app.merge
import ghidra.app.merge.listing
import ghidra.program.model.address
import ghidra.util.task
import java.lang


class ListingMergeManager(object, ghidra.app.merge.MergeResolver, ghidra.app.merge.listing.ListingMergeConstants):
    """
    Manages program listing changes and conflicts between the latest versioned
     program (LATEST) and the modified program (MY) being checked into version control.
     Listing changes include:

     bytes
     code units [instructions and data]
     equates
     functions
     symbols
     references [memory, stack, and external]
     comments [plate, pre, end-of-line, repeatable, and post]
     properties
     bookmarks

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
        Manages listing changes and conflicts between the latest versioned
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

    def cancel(self) -> None: ...

    def equals(self, __a0: object) -> bool: ...

    def getClass(self) -> java.lang.Class: ...

    def getDescription(self) -> unicode: ...

    def getFunctionTagListingMerger(self) -> ghidra.app.merge.listing.FunctionTagListingMerger: ...

    def getMergedCodeUnits(self) -> ghidra.program.model.address.AddressSet:
        """
        Gets the address set for the code units that were changed in the result
         by the merge.
        @return the address set indicating the code units that changed in the
         result program due to the merge
        """
        ...

    def getName(self) -> unicode: ...

    def getPhases(self) -> List[unicode]:
        """
        This method returns all of the phases of the Listing Merge Manager that will be
         displayed in the Program Merge Manager.
         The first item is a phase indicator for the Listing Phase as a whole and
         the others are for each sub-phase of the Listing.
        """
        ...

    def hashCode(self) -> int: ...

    def initMergeInfo(self) -> None:
        """
        Sets up the change address sets, Diffs between the various program versions,
         and Merges from various versions to the resulting program.
        """
        ...

    def merge(self, monitor: ghidra.util.task.TaskMonitor) -> None: ...

    def notify(self) -> None: ...

    def notifyAll(self) -> None: ...

    def setShowListingPanel(self, showListingPanel: bool) -> None:
        """
        True signals to show the listing panel (default); false signals to show an empty listing (faster)
        @param showListingPanel
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
    def description(self) -> unicode: ...

    @property
    def functionTagListingMerger(self) -> ghidra.app.merge.listing.FunctionTagListingMerger: ...

    @property
    def mergedCodeUnits(self) -> ghidra.program.model.address.AddressSet: ...

    @property
    def name(self) -> unicode: ...

    @property
    def phases(self) -> List[unicode]: ...

    @property
    def showListingPanel(self) -> None: ...  # No getter available.

    @showListingPanel.setter
    def showListingPanel(self, value: bool) -> None: ...
