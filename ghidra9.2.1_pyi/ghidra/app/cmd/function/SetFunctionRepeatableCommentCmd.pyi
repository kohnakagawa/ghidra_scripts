import ghidra.framework.cmd
import ghidra.framework.model
import java.lang


class SetFunctionRepeatableCommentCmd(object, ghidra.framework.cmd.Command):
    """
    Command to set the Function's Repeatable Comment.
    """





    def __init__(self, entry: ghidra.program.model.address.Address, newRepeatableComment: unicode):
        """
        Constructs a new command for setting the Repeatable comment.
        @param entry address of the function for which to set a Repeatablecomment.
        @param newRepeatableComment comment to set as the function Repeatable comment.
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
