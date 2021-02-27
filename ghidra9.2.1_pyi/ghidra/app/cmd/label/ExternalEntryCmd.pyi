import ghidra.framework.cmd
import ghidra.framework.model
import java.lang


class ExternalEntryCmd(object, ghidra.framework.cmd.Command):
    """
    Command for setting/unsetting an external entry point.
    """





    def __init__(self, addr: ghidra.program.model.address.Address, isEntry: bool):
        """
        Construct a new command for setting/unsetting an external entry point
        @param addr address to set or unset as an external entry point.
        @param isEntry true if the address is to be an entry. Otherwise, false.
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
