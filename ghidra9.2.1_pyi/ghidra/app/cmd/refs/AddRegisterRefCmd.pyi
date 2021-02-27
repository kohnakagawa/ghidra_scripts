import ghidra.framework.cmd
import ghidra.framework.model
import java.lang


class AddRegisterRefCmd(object, ghidra.framework.cmd.Command):
    """
    Command class to add a register reference to the program.
    """





    @overload
    def __init__(self, fromAddr: ghidra.program.model.address.Address, opIndex: int, reg: ghidra.program.model.lang.Register, source: ghidra.program.model.symbol.SourceType):
        """
        Constructs a new command for adding a register reference.
        @param fromAddr "from" address
        @param opIndex operand index
        @param reg register to add the reference to
        @param source the source of this reference
        """
        ...

    @overload
    def __init__(self, fromAddr: ghidra.program.model.address.Address, opIndex: int, reg: ghidra.program.model.lang.Register, refType: ghidra.program.model.symbol.RefType, source: ghidra.program.model.symbol.SourceType):
        """
        Constructs a new command for adding a register reference.
        @param fromAddr "from" address
        @param opIndex operand index
        @param reg register to add the reference to
        @param refType reference type or null to use a default RefType
        @param source the source of this reference
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
