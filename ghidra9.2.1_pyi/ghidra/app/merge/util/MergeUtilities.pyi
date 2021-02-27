import ghidra.program.model.address
import java.lang


class MergeUtilities(object):
    """
    MergeUtilities provides generic static methods for use by the
     multi-user program merge managers.
    """





    def __init__(self): ...



    @staticmethod
    def adjustSets(latestDiffs: ghidra.program.model.address.AddressSetView, myDiffs: ghidra.program.model.address.AddressSetView, autoChanges: ghidra.program.model.address.AddressSet, conflictChanges: ghidra.program.model.address.AddressSet) -> None:
        """
        Adds addresses to autoChanges where there are changes in the myDiffs set,
         but none in the latestDiffs set.
         Adds addresses to conflictChanges where there are changes in the myDiffs
         set and also some changes in the latestDiffs set.
        @param latestDiffs the address set of the changes in LATEST.
        @param myDiffs the address set of the changes in MY.
        @param autoChanges address set for the myDiffs non-conflicting changes.
        @param conflictChanges address set for the myDiffs conflicting changes
        """
        ...

    def equals(self, __a0: object) -> bool: ...

    def getClass(self) -> java.lang.Class: ...

    def hashCode(self) -> int: ...

    def notify(self) -> None: ...

    def notifyAll(self) -> None: ...

    def toString(self) -> unicode: ...

    @overload
    def wait(self) -> None: ...

    @overload
    def wait(self, __a0: long) -> None: ...

    @overload
    def wait(self, __a0: long, __a1: int) -> None: ...
