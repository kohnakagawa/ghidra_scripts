from typing import List
import ghidra.app.merge
import ghidra.util
import ghidra.util.task
import java.lang
import javax.swing


class DomainObjectMergeManager(ghidra.app.merge.MergeProgressModifier, object):
    """
    An interface to allow merging of domain objects.
    """









    def clearStatusText(self) -> None:
        """
        Clear the status text on the merge dialog.
        """
        ...

    def equals(self, __a0: object) -> bool: ...

    def getClass(self) -> java.lang.Class: ...

    def hashCode(self) -> int: ...

    def merge(self, monitor: ghidra.util.task.TaskMonitor) -> bool:
        """
        Merge domain objects and resolve any conflicts.
        @return true if the merge process completed successfully
        @throws CancelledException if the user canceled the merge process
        """
        ...

    def notify(self) -> None: ...

    def notifyAll(self) -> None: ...

    def setApplyEnabled(self, enabled: bool) -> None:
        """
        Enable the apply button according to the "enabled" parameter.
        """
        ...

    def setCompleted(self, __a0: List[unicode]) -> None: ...

    def setInProgress(self, __a0: List[unicode]) -> None: ...

    def setResolveInformation(self, infoType: unicode, infoObject: object) -> None:
        """
        Sets the resolve information object for the indicated standardized name.
         This is how information is passed between merge managers.
        @param infoType the string indicating the type of resolve information
        @param infoObject the object for the named string. This information is
         determined by the merge manager that creates it.
        @see ghidra.app.merge.MergeManager#getResolveInformation(String) MergeManager.getResolveInformation(String)
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

    def toString(self) -> unicode: ...

    @overload
    def updateProgress(self, __a0: int) -> None: ...

    @overload
    def updateProgress(self, __a0: unicode) -> None: ...

    @overload
    def updateProgress(self, __a0: int, __a1: unicode) -> None: ...

    @overload
    def wait(self) -> None: ...

    @overload
    def wait(self, __a0: long) -> None: ...

    @overload
    def wait(self, __a0: long, __a1: int) -> None: ...

    @property
    def applyEnabled(self) -> None: ...  # No getter available.

    @applyEnabled.setter
    def applyEnabled(self, value: bool) -> None: ...

    @property
    def completed(self) -> None: ...  # No getter available.

    @completed.setter
    def completed(self, value: List[unicode]) -> None: ...

    @property
    def inProgress(self) -> None: ...  # No getter available.

    @inProgress.setter
    def inProgress(self, value: List[unicode]) -> None: ...

    @property
    def statusText(self) -> None: ...  # No getter available.

    @statusText.setter
    def statusText(self, value: unicode) -> None: ...
