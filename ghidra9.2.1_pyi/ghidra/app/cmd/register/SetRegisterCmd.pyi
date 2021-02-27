import ghidra.framework.cmd
import ghidra.framework.model
import java.lang


class SetRegisterCmd(object, ghidra.framework.cmd.Command):
    """
    Command for setting the value of a register over a range of addresses.
    """





    def __init__(self, register: ghidra.program.model.lang.Register, start: ghidra.program.model.address.Address, end: ghidra.program.model.address.Address, value: long):
        """
        Constructor for SetRegisterCmd.
        @param register the register to change.
        @param start the starting address of the range.
        @param end the ending address of the range.
        @param value the value to associated over the range.
                              A null value indicates that no value should be associated over the range.
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
