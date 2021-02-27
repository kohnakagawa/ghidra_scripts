from typing import List
import ghidra.framework.model
import java.lang


class FunctionTagChangeSet(ghidra.framework.model.ChangeSet, object):
    """
    Defines a Function Tag Change set.  This is meant to track changes that
     are made to FunctionTag objects in a program.
    """









    def equals(self, __a0: object) -> bool: ...

    def getClass(self) -> java.lang.Class: ...

    def getTagChanges(self) -> List[long]:
        """
        Returns a list of all tag ids that have been changed (edited/deleted).
        @return the list of tag ids (from {@link ghidra.program.database.function.FunctionTagAdapter FunctionTagAdapter})
        """
        ...

    def getTagCreations(self) -> List[long]:
        """
        Returns a list of all tag ids that have been created.
        @return the list of tag ids (from {@link ghidra.program.database.function.FunctionTagAdapter FunctionTagAdapter})
        """
        ...

    def hashCode(self) -> int: ...

    def notify(self) -> None: ...

    def notifyAll(self) -> None: ...

    def tagChanged(self, id: long) -> None:
        """
        Indicates that a tag has been changed (edited/deleted).
        @param id the id of the tag (from {@link ghidra.program.database.function.FunctionTagAdapter FunctionTagAdapter})
        """
        ...

    def tagCreated(self, id: long) -> None:
        """
        Indicates that a tag has been created.
        @param id id the id of the tag (from {@link ghidra.program.database.function.FunctionTagAdapter FunctionTagAdapter})
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
    def tagChanges(self) -> List[long]: ...

    @property
    def tagCreations(self) -> List[long]: ...
