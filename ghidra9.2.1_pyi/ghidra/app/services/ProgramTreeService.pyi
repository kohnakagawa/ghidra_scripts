from typing import List
import ghidra.program.model.address
import ghidra.program.util
import java.lang


class ProgramTreeService(object):
    """
    Service provided by the program tree plugin to get the current view
     (address set shown in the Code Browser),
     and the name of the tree currently being viewed.
    """









    def equals(self, __a0: object) -> bool: ...

    def getClass(self) -> java.lang.Class: ...

    def getView(self) -> ghidra.program.model.address.AddressSet:
        """
        Get the address set of the current view (what is currently being shown in
         the Code Browser).
        """
        ...

    def getViewedTreeName(self) -> unicode:
        """
        Get the name of the tree currently being viewed.
        """
        ...

    def hashCode(self) -> int: ...

    def notify(self) -> None: ...

    def notifyAll(self) -> None: ...

    def setGroupSelection(self, gps: List[ghidra.program.util.GroupPath]) -> None:
        """
        Set the selection to the given group paths.
        @param gps paths to select
        """
        ...

    def setViewedTree(self, treeName: unicode) -> None:
        """
        Set the current view to that of the given name. If treeName is not
         a known view, then nothing happens.
        @param treeName name of the view
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
    def groupSelection(self) -> None: ...  # No getter available.

    @groupSelection.setter
    def groupSelection(self, value: List[ghidra.program.util.GroupPath]) -> None: ...

    @property
    def view(self) -> ghidra.program.model.address.AddressSet: ...

    @property
    def viewedTree(self) -> None: ...  # No getter available.

    @viewedTree.setter
    def viewedTree(self, value: unicode) -> None: ...

    @property
    def viewedTreeName(self) -> unicode: ...
