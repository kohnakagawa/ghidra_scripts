import ghidra.framework.cmd
import ghidra.framework.model
import java.lang


class RenameCmd(object, ghidra.framework.cmd.Command):
    """
    Command for renaming a fragment or a module in listing.
    """





    @overload
    def __init__(self, treeName: unicode, isModule: bool, oldName: unicode, newName: unicode):
        """
        Construct a new RenameCmd.
        @param treeName name of the tree where the module or fragment resides
        @param isModule true if a module is to be renamed
        @param oldName current name of the module or fragment
        @param newName new name for the module or fragment
        """
        ...

    @overload
    def __init__(self, treeName: unicode, isModule: bool, oldName: unicode, newName: unicode, ignoreDuplicateName: bool):
        """
        Construct a new RenameCmd.
        @param treeName name of the tree where the module or fragment resides
        @param isModule true if a module is to be renamed
        @param oldName current name of the module or fragment
        @param newName new name for the module or fragment
        @param ignoreDuplicateName true means to ignore the exception and
         don't do anything
        """
        ...



    def applyTo(self, obj: ghidra.framework.model.DomainObject) -> bool:
        """
        @see ghidra.framework.cmd.Command#applyTo(ghidra.framework.model.DomainObject)
        """
        ...

    def equals(self, __a0: object) -> bool: ...

    def getClass(self) -> java.lang.Class: ...

    def getName(self) -> unicode:
        """
        @see ghidra.framework.cmd.Command#getName()
        """
        ...

    def getStatusMsg(self) -> unicode:
        """
        @see ghidra.framework.cmd.Command#getStatusMsg()
        """
        ...

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

    @property
    def name(self) -> unicode: ...

    @property
    def statusMsg(self) -> unicode: ...
