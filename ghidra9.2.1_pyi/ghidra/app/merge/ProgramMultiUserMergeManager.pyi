from typing import List
import ghidra.app.merge
import ghidra.app.merge.tool
import ghidra.framework.model
import ghidra.framework.plugintool
import ghidra.program.model.address
import ghidra.program.model.listing
import ghidra.util
import ghidra.util.task
import java.lang
import javax.swing


class ProgramMultiUserMergeManager(ghidra.app.merge.MergeManager):
    """
    Top level object that manages each step of the merge/resolve conflicts
     process.
    """





    @overload
    def __init__(self, resultProgram: ghidra.program.model.listing.Program, myProgram: ghidra.program.model.listing.Program, originalProgram: ghidra.program.model.listing.Program, latestProgram: ghidra.program.model.listing.Program, latestChangeSet: ghidra.program.model.listing.ProgramChangeSet, myChangeSet: ghidra.program.model.listing.ProgramChangeSet): ...

    @overload
    def __init__(self, resultProgram: ghidra.program.model.listing.Program, myProgram: ghidra.program.model.listing.Program, originalProgram: ghidra.program.model.listing.Program, latestProgram: ghidra.program.model.listing.Program, latestChangeSet: ghidra.program.model.listing.ProgramChangeSet, myChangeSet: ghidra.program.model.listing.ProgramChangeSet, showListingPanels: bool): ...



    def clearStatusText(self) -> None:
        """
        Clear the status text on the merge dialog.
        """
        ...

    @staticmethod
    def displayErrorAndWait(originator: object, title: unicode, msg: unicode) -> None:
        """
        Display error message dialog in a blocking fashion.
        @param originator message originator
        @param title dialog title
        @param msg dialog message
        """
        ...

    def equals(self, __a0: object) -> bool: ...

    def getClass(self) -> java.lang.Class: ...

    def getDomainObject(self, version: int) -> ghidra.framework.model.UndoableDomainObject:
        """
        Returns one of the four programs involved in the merge as indicated by the version.
        @param version the program version to return. (LATEST, MY, ORIGINAL, or RESULT).
        @return the indicated program version or null if a valid version isn't specified.
        @see MergeConstants
        """
        ...

    def getListingMergePanel(self) -> ghidra.app.merge.tool.ListingMergePanel:
        """
        Returns the listing merge panel. This is the panel containing the four
         listing windows: result, latest, my, and original. The four listings are
         the center component of JPanel with a BorderLayout.
        """
        ...

    def getMergeProgressPanel(self) -> ghidra.app.merge.MergeProgressPanel:
        """
        gets the default merge progress panel that indicates all the phases and their current status.
        @return the merge panel that indicates progress.
        """
        ...

    def getMergeResolverByName(self, name: unicode) -> ghidra.app.merge.MergeResolver:
        """
        Returns the named merge resolver from the ones used directly by the MergeManager.
        @param name the name of the desired merge resolver
        @return the merge resolver or null.
        """
        ...

    def getMergeTool(self) -> ghidra.framework.plugintool.PluginTool:
        """
        For Junit tests
        @return the merge tool
        """
        ...

    def getMonitorComponent(self) -> javax.swing.JComponent:
        """
        Gets the TaskMonitor component that is displayed at the bottom of the merge tool.
        @return the task monitor component.
        """
        ...

    def getProgram(self, version: int) -> ghidra.program.model.listing.Program:
        """
        Returns one of the four programs involved in the merge as indicated by the version.
        @param version the program version to return. (LATEST, MY, ORIGINAL, or RESULT).
        @return the indicated program version or null if a valid version isn't specified.
        @see MergeConstants
        """
        ...

    def getResolveInformation(self, infoType: unicode) -> object:
        """
        Gets the resolve information object for the indicated standardized name.
         This is how information is passed between merge managers.
         <br>For example:
         <br>the data type merger knows what data type in the result is equivalent
         to a given data type from my checked out program. The code unit and
         function mergers need to be able to get this information so they
         don't unknowingly re-introduce a data type that was already eliminated
         by a data type conflict.
        @param infoType the string indicating the type of resolve information
        @return the object for the named string or null
        """
        ...

    def hashCode(self) -> int: ...

    def isMergeToolVisible(self) -> bool:
        """
        Determines if the modal merge tool is currently displayed on the screen.
        @return true if the merge tool is displayed.
        """
        ...

    def isPromptingUser(self) -> bool:
        """
        Determines whether or not the user is being prompted to resolve a conflict.
        @return true if the user is being prompted for input.
        """
        ...

    def isShowingListingMergePanel(self) -> bool:
        """
        Determines if the four program Listing merge panel is currently displayed in the merge tool.
        @return true if the Listing merge panel is displayed.
        """
        ...

    @overload
    def merge(self) -> bool:
        """
        Convenience method for Junit tests.
        """
        ...

    @overload
    def merge(self, taskMonitor: ghidra.util.task.TaskMonitor) -> bool: ...

    def notify(self) -> None: ...

    def notifyAll(self) -> None: ...

    def processingCompleted(self) -> bool:
        """
        Return whether the merge process has completed. (Needed for Junit testing
         only.)
        """
        ...

    def refreshListingMergePanel(self, resultAddress: ghidra.program.model.address.Address, latestAddress: ghidra.program.model.address.Address, myAddress: ghidra.program.model.address.Address, originalAddress: ghidra.program.model.address.Address) -> None:
        """
        Show the listing merge panel with each listing positioned to the indicated address.
         A null can be passed for any address to indicate that listing should be empty.
        @param resultAddress the address for positioning the Result program's listing.
        @param latestAddress the address for positioning the Latest program's listing.
        @param myAddress the address for positioning the My program's listing.
        @param originalAddress the address for positioning the Original program's listing.
        """
        ...

    def removeComponent(self, comp: javax.swing.JComponent) -> None:
        """
        Removes the component that is used to resolve conflicts. This method
         is called by the MergeResolvers when user input is no longer required
         using the specified component.
        @param comp component to show; if component is null, show the
         default component and do not block
        """
        ...

    def removeListingMergePanel(self) -> None:
        """
        Remove the listing merge panel from the merge manager.
        """
        ...

    def setApplyEnabled(self, enabled: bool) -> None:
        """
        Enable the apply button according to the "enabled" parameter.
        """
        ...

    def setCompleted(self, mergePhase: List[unicode]) -> None:
        """
        The manager (MergeResolver) for a particular merge phase should call this when its phase or sub-phase completes.
         The string array should match one that the returned by MergeResolver.getPhases().
        @param mergePhase identifier for the merge phase to change to completed status.
        @see MergeResolver
        """
        ...

    def setInProgress(self, mergePhase: List[unicode]) -> None:
        """
        The manager (MergeResolver) for a particular merge phase should call this when its phase or sub-phase begins.
         The string array should match one that the returned by MergeResolver.getPhases().
        @param mergePhase identifier for the merge phase to change to in progress status.
        @see MergeResolver
        """
        ...

    def setResolveInformation(self, infoType: unicode, infoObject: object) -> None:
        """
        Sets the resolve information object for the indicated standardized name.
         This is how information is passed between merge managers.
        @param infoType the string indicating the type of resolve information
        @param infoObject the object for the named string. This information is
         determined by the merge manager that creates it.
        @see getResolveInformation(String)
        """
        ...

    def setStatusText(self, msg: unicode) -> None:
        """
        Set the status text on the merge dialog.
        """
        ...

    def showComponent(self, comp: javax.swing.JComponent, componentID: unicode, helpLoc: ghidra.util.HelpLocation) -> None:
        """
        Show the component that is used to resolve conflicts. This method
         is called by the MergeResolvers when user input is required. If the
         component is not null, this method blocks until the user either
         cancels the merge process or resolves a conflict. If comp is null,
         then the default component is displayed, and the method does not
         wait for user input.
        @param comp component to show; if component is null, show the
         default component and do not block
        @param componentID id or name for the component
        """
        ...

    def showDefaultMergePanel(self, description: unicode) -> None:
        """
        Show the default merge panel. The default merge panel now shows the status of each phase
         of the merge and also the progress in the current phase.
        @param description description of current merge process near the top of the merge tool.
        """
        ...

    @overload
    def showListingMergePanel(self, goToAddress: ghidra.program.model.address.Address) -> None:
        """
        Show the listing merge panel.
        @param goToAddress the address to goto.
        """
        ...

    @overload
    def showListingMergePanel(self, resultAddress: ghidra.program.model.address.Address, latestAddress: ghidra.program.model.address.Address, myAddress: ghidra.program.model.address.Address, originalAddress: ghidra.program.model.address.Address) -> None:
        """
        Show the listing merge panel with each listing positioned to the indicated address.
         A null can be passed for any address to indicate that listing should be empty.
        @param resultAddress the address for positioning the Result program's listing.
        @param latestAddress the address for positioning the Latest program's listing.
        @param myAddress the address for positioning the My program's listing.
        @param originalAddress the address for positioning the Original program's listing.
        """
        ...

    def showMonitorComponent(self, show: bool) -> None:
        """
        Shows/hides the monitor component at the bottom of the merge tool.
        @param show true means to show the task monitor at the bottom of the merge tool.
        """
        ...

    def showProgressIcon(self, show: bool) -> None:
        """
        Shows/hides the progress icon (spinning globe) at the bottom of the merge tool.
        @param show true means to show the icon.
        """
        ...

    def toString(self) -> unicode: ...

    @overload
    def updateProgress(self, currentProgressPercentage: int) -> None:
        """
        Updates the current phase progress area in the default merge panel.
        @param currentProgressPercentage the progress percentage completed for the current phase.
         This should be a value from 0 to 100.
        """
        ...

    @overload
    def updateProgress(self, description: unicode) -> None:
        """
        Updates the current phase progress area in the default merge panel.
        @param description a message describing what is currently occurring in this phase.
         Null indicates to use the default message.
        """
        ...

    @overload
    def updateProgress(self, currentProgressPercentage: int, progressMessage: unicode) -> None:
        """
        Updates the current phase progress area in the default merge panel.
        @param currentProgressPercentage the progress percentage completed for the current phase.
         This should be a value from 0 to 100.
        @param progressMessage a message indicating what is currently occurring in this phase.
        """
        ...

    @overload
    def wait(self) -> None: ...

    @overload
    def wait(self, __a0: long) -> None: ...

    @overload
    def wait(self, __a0: long, __a1: int) -> None: ...

    @property
    def listingMergePanel(self) -> ghidra.app.merge.tool.ListingMergePanel: ...

    @property
    def mergeToolVisible(self) -> bool: ...

    @property
    def showingListingMergePanel(self) -> bool: ...
