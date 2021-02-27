import ghidra.framework.cmd
import ghidra.framework.model
import java.lang


class SetFunctionVarArgsCommand(object, ghidra.framework.cmd.Command):
    """
    A simple command to set whether or not a function has VarArgs.
    """





    def __init__(self, function: ghidra.program.model.listing.Function, hasVarArgs: bool):
        """
        Creates a new command that will set whether or not there are VarArgs on the given
         function.
        @param function The function on which to set whether or not there are VarArgs.
        @param hasVarArgs true if you want to set this function to have VarArgs.
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
