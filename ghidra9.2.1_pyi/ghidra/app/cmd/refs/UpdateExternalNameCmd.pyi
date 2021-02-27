import ghidra.framework.cmd
import ghidra.framework.model
import java.lang


class UpdateExternalNameCmd(object, ghidra.framework.cmd.Command):
    """
    Command to update the name for an external program.
    """





    def __init__(self, oldName: unicode, newName: unicode, source: ghidra.program.model.symbol.SourceType):
        """
        Constructs a new command for updating the name of an external program.
        @param oldName the current name of the external program link.
        @param newName the new name to be used for the external program link.
        @param source the source of this external name
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
