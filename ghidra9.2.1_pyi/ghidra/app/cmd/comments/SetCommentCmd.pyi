import ghidra.framework.cmd
import ghidra.framework.model
import ghidra.program.model.address
import ghidra.program.model.listing
import java.lang


class SetCommentCmd(object, ghidra.framework.cmd.Command):
    """
    Command to set a specific type of comment on a code unit.
    """





    def __init__(self, addr: ghidra.program.model.address.Address, commentType: int, comment: unicode):
        """
        Construct command
        @param addr address of code unit where comment will be placed
        @param commentType valid comment type (see CodeUnit)
        @param comment comment for code unit
        """
        ...



    def applyTo(self, obj: ghidra.framework.model.DomainObject) -> bool:
        """
        @see ghidra.framework.cmd.Command#applyTo(ghidra.framework.model.DomainObject)
        """
        ...

    @staticmethod
    def createComment(program: ghidra.program.model.listing.Program, addr: ghidra.program.model.address.Address, comment: unicode, commentType: int) -> None:
        """
        Creates the specified comment of the specified type at address.  The current comment of
         this commentType will be cleared.
        @param program the program being analyzed
        @param addr the address where data is created
        @param comment the comment about the data
        @param commentType the type of comment ({@link CodeUnit#PLATE_COMMENT},
         {@link CodeUnit#PRE_COMMENT}, {@link CodeUnit#EOL_COMMENT}, {@link CodeUnit#POST_COMMENT},
         {@link CodeUnit#REPEATABLE_COMMENT})
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
