import ghidra.framework.cmd
import ghidra.framework.model
import java.lang


class SetCommentsCmd(object, ghidra.framework.cmd.Command):
    """
    Command for editing and removing comments at an address.
    """





    def __init__(self, addr: ghidra.program.model.address.Address, newPreComment: unicode, newPostComment: unicode, newEolComment: unicode, newPlateComment: unicode, newRepeatableComment: unicode):
        """
        Construct command for setting all the different types of comments at an
         address.
        @param addr address of code unit where comment will edited
        @param newPreComment new pre comment
        @param newPostComment new post comment
        @param newEolComment new eol comment
        @param newPlateComment new plate comment
        @param newRepeatableComment new repeatable comment
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
        The name of the edit action.
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
