from typing import List
import ghidra.util.task
import java.lang


class MergeResolver(object):
    """
    Interface for resolving domain object merge conflicts.
    """









    def apply(self) -> None:
        """
        Notification that the apply button was hit.
        """
        ...

    def cancel(self) -> None:
        """
        Notification that the merge process was canceled.
        """
        ...

    def equals(self, __a0: object) -> bool: ...

    def getClass(self) -> java.lang.Class: ...

    def getDescription(self) -> unicode:
        """
        Get the description of what this MergeResolver does.
        """
        ...

    def getName(self) -> unicode:
        """
        Get the name of this MergeResolver.
        """
        ...

    def getPhases(self) -> List[unicode]:
        """
        Gets identifiers for the merge phases handled by this MergeResolver.
         If the merge has no sub-phases then return an array with a single string array.
         Each inner String array indicates a path for a single merge phase.
         Each outer array element represents a phase whose progress we wish to indicate.
         <br>Examples:
         <br>So for a simple phase which has no sub-phases return
         <code>
         new String[][] {new String[] {"Phase A"}}
         </code>
         <br>So for a phase with 2 sub-phases return
         <code>
         new String[][] { new String[] {"Phase A"},
                          new String[] {"Phase A", "Sub-Phase 1},
                          new String[] {"Phase A", "Sub-Phase 2} }
         </code>.
        @return an array of phases.
        """
        ...

    def hashCode(self) -> int: ...

    def merge(self, monitor: ghidra.util.task.TaskMonitor) -> None:
        """
        Perform the merge process.
        @param monitor monitor that allows the user to cancel the merge
         operation
        @throws Exception if the merge encounters an error and the merge process
         should not continue.
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
