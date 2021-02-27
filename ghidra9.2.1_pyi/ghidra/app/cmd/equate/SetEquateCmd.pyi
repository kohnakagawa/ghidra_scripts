import ghidra.framework.cmd
import ghidra.framework.model
import ghidra.program.model.symbol
import java.lang


class SetEquateCmd(object, ghidra.framework.cmd.Command):
    """
    Command for setting an equate at a location.
    """





    def __init__(self, equateName: unicode, addr: ghidra.program.model.address.Address, opIndex: int, equateValue: long):
        """
        Constructor
        @param equateName the name of the equate to applied or removed at this location.
        @param addr the address of the current location.
        @param opIndex the operand index of the current location.
        @param equateValue the numeric value at the current location.
        """
        ...



    def applyTo(self, obj: ghidra.framework.model.DomainObject) -> bool: ...

    def equals(self, __a0: object) -> bool: ...

    def getClass(self) -> java.lang.Class: ...

    def getEquate(self) -> ghidra.program.model.symbol.Equate: ...

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
    def equate(self) -> ghidra.program.model.symbol.Equate: ...

    @property
    def name(self) -> unicode: ...

    @property
    def statusMsg(self) -> unicode: ...
