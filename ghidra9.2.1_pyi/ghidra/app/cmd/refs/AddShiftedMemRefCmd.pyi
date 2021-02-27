import ghidra.framework.cmd
import ghidra.framework.model
import java.lang


class AddShiftedMemRefCmd(object, ghidra.framework.cmd.Command):
    """
    Command class to add a shifted memory reference to the program.
    """





    def __init__(self, fromAddr: ghidra.program.model.address.Address, toAddr: ghidra.program.model.address.Address, refType: ghidra.program.model.symbol.RefType, source: ghidra.program.model.symbol.SourceType, opIndex: int, shift: int):
        """
        Command constructor for adding a shifted memory reference
        @param fromAddr address of the codeunit where the reference occurs
        @param toAddr computed as the value of the operand at opIndex shifted
         by the number of bits specified by shiftValue
        @param refType reference type - how the location is being referenced.
        @param source the source of the reference
        @param opIndex the operand index in the code unit where the reference occurs
        @param shift the number of bits to shift the value by
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
