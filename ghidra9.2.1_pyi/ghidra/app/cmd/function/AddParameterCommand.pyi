import ghidra.framework.cmd
import ghidra.framework.model
import java.lang


class AddParameterCommand(object, ghidra.framework.cmd.Command):
    """
    Allows for the adding of a parameter to a given function.

     Note: If no ordinal is provided to this class at construction time, then
     the ordinal of hte given parameter will be used.
    """





    def __init__(self, function: ghidra.program.model.listing.Function, parameter: ghidra.program.model.listing.Parameter, ordinal: int, source: ghidra.program.model.symbol.SourceType): ...



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
