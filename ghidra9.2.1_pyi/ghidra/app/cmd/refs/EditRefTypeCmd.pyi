import ghidra.framework.cmd
import ghidra.framework.model
import java.lang


class EditRefTypeCmd(object, ghidra.framework.cmd.Command):
    """
    Command to change the reference type of a memory reference
    """





    def __init__(self, ref: ghidra.program.model.symbol.Reference, newRefType: ghidra.program.model.symbol.RefType):
        """
        Constructs a new command for changing the reference type of a reference.
        @param ref the reference whose type it to be changed.
        @param newRefType the ref type to assign to the reference.
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
