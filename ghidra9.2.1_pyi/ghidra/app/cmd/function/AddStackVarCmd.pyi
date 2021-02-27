import ghidra.framework.cmd
import ghidra.framework.model
import java.lang


class AddStackVarCmd(object, ghidra.framework.cmd.Command):
    """
    Command to add a stack variable to a function.
    """





    def __init__(self, addr: ghidra.program.model.address.Address, stackOffset: int, name: unicode, dataType: ghidra.program.model.data.DataType, source: ghidra.program.model.symbol.SourceType):
        """
        Constructs a new command to add a stack variable to a function.
        @param addr initial declaration point of variable.
        @param stackOffset offset into the stack for the new variable.
        @param name name of the new variable.
        @param dataType variable data-type or null for a default data type of minimal size
        @param source the source of this stack variable
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
