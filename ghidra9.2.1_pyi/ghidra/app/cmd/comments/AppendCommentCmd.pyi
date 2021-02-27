import ghidra.framework.cmd
import ghidra.framework.model
import java.lang


class AppendCommentCmd(object, ghidra.framework.cmd.Command):
    """
    Command to append a specific type of comment on a code unit.
    """





    def __init__(self, addr: ghidra.program.model.address.Address, commentType: int, comment: unicode, separator: unicode):
        """
        Construct command
        @param addr address of code unit where comment will be placed
        @param commentType valid comment type (see {@link CodeUnit#EOL_COMMENT},
         {@link CodeUnit#PLATE_COMMENT}, etc)
        @param comment comment for code unit, should not be null
        @param separator characters to separate the new comment from the previous comment when
         concatenating.
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
