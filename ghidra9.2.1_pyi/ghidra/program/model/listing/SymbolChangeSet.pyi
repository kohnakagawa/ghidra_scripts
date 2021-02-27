from typing import List
import ghidra.framework.model
import java.lang


class SymbolChangeSet(ghidra.framework.model.ChangeSet, object):
    """
    Interface for a Symbol Change set.  Objects that implements this interface track
     various change information on a symbol manager.
    """









    def equals(self, __a0: object) -> bool: ...

    def getClass(self) -> java.lang.Class: ...

    def getSymbolAdditions(self) -> List[long]:
        """
        returns the list of symbols IDs that have been added.
        """
        ...

    def getSymbolChanges(self) -> List[long]:
        """
        returns the list of symbol IDs that have changed.
        """
        ...

    def hashCode(self) -> int: ...

    def notify(self) -> None: ...

    def notifyAll(self) -> None: ...

    def symbolAdded(self, id: long) -> None:
        """
        adds the symbols id to the list of symbols that have been added.
        """
        ...

    def symbolChanged(self, id: long) -> None:
        """
        adds the symbol id to the list of symbols that have changed.
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
    def symbolAdditions(self) -> List[long]: ...

    @property
    def symbolChanges(self) -> List[long]: ...
