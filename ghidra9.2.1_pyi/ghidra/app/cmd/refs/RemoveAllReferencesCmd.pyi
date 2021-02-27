import ghidra.framework.cmd
import ghidra.framework.model
import java.lang


class RemoveAllReferencesCmd(object, ghidra.framework.cmd.Command):
    """
    Command to remove all references at an address or for a particular operand
     index at an address.
    """





    @overload
    def __init__(self, fromAddr: ghidra.program.model.address.Address):
        """
        Constructs a new command for removing all references.
        @param fromAddr the address of the codeunit making the reference.
        """
        ...

    @overload
    def __init__(self, fromAddr: ghidra.program.model.address.Address, opIndex: int):
        """
        Constructs a new command for removing all references.
        @param fromAddr the address of the codeunit making the reference.
        @param opIndex the operand index.
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
