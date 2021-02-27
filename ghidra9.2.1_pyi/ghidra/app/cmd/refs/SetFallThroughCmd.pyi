import ghidra.framework.cmd
import ghidra.framework.model
import java.lang


class SetFallThroughCmd(object, ghidra.framework.cmd.Command):
    """
    Command for setting the fallthrough property on an instruction.
    """





    def __init__(self, instAddr: ghidra.program.model.address.Address, fallthroughAddr: ghidra.program.model.address.Address):
        """
        Constructs a new command for setting the fallthrough property on an instruction.
        @param instAddr the address of the instruction whose fallthrought property is
         to be set.
        @param fallthroughAddr the address to use for the instructions fallthrough.
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
