from typing import List
import ghidra.framework.model
import java.lang


class ProgramTreeChangeSet(ghidra.framework.model.ChangeSet, object):
    """
    Interface for a Program Tree Change set.  Objects that implements this interface track
     various change information on a program tree manager.
    """









    def equals(self, __a0: object) -> bool: ...

    def getClass(self) -> java.lang.Class: ...

    def getProgramTreeAdditions(self) -> List[long]:
        """
        returns the list of program tree IDs that have been added.
        """
        ...

    def getProgramTreeChanges(self) -> List[long]:
        """
        returns the list of program tree IDs that have changed.
        """
        ...

    def hashCode(self) -> int: ...

    def notify(self) -> None: ...

    def notifyAll(self) -> None: ...

    def programTreeAdded(self, id: long) -> None:
        """
        adds the program tree id to the list of trees that have been added.
        """
        ...

    def programTreeChanged(self, id: long) -> None:
        """
        adds the program tree id to the list of trees that have changed.
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
    def programTreeAdditions(self) -> List[long]: ...

    @property
    def programTreeChanges(self) -> List[long]: ...
