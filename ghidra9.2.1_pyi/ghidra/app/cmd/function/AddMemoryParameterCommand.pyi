import ghidra.app.cmd.function
import ghidra.framework.model
import java.lang


class AddMemoryParameterCommand(ghidra.app.cmd.function.AddParameterCommand):
    """
    A command to create a new function memory parameter.
    """





    def __init__(self, function: ghidra.program.model.listing.Function, memAddr: ghidra.program.model.address.Address, name: unicode, dataType: ghidra.program.model.data.DataType, ordinal: int, source: ghidra.program.model.symbol.SourceType): ...



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
