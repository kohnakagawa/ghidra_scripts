from typing import List
import java.lang


class MergeProgressModifier(object):








    def equals(self, __a0: object) -> bool: ...

    def getClass(self) -> java.lang.Class: ...

    def hashCode(self) -> int: ...

    def notify(self) -> None: ...

    def notifyAll(self) -> None: ...

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
    def updateProgress(self, progressMessage: unicode) -> None:
        """
        Updates the current phase progress area in the default merge panel.
        @param progressMessage a message indicating what is currently occurring in this phase.
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
    def completed(self) -> None: ...  # No getter available.

    @completed.setter
    def completed(self, value: List[unicode]) -> None: ...

    @property
    def inProgress(self) -> None: ...  # No getter available.

    @inProgress.setter
    def inProgress(self, value: List[unicode]) -> None: ...
