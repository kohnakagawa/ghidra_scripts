import ghidra.framework.cmd
import ghidra.framework.model
import java.lang


class MergeFolderCmd(object, ghidra.framework.cmd.Command):
    """
    Command to merge a Folder with its Parent folder. Immediate children of
     the folder are moved to its parent.
    """





    def __init__(self, treeName: unicode, folderName: unicode, parentName: unicode):
        """
        Construct a new command.
        @param treeName name of the tree that this command affects
        @param folderName name of the folder (module) that is being merged in
         with its parent
        @param parentName name of the parent that will end up with children of
         the folder named folderName
        """
        ...



    def applyTo(self, obj: ghidra.framework.model.DomainObject) -> bool: ...

    def equals(self, __a0: object) -> bool: ...

    def getClass(self) -> java.lang.Class: ...

    def getName(self) -> unicode: ...

    def getStatusMsg(self) -> unicode: ...

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
