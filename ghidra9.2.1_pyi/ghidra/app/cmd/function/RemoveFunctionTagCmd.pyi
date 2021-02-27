import ghidra.framework.cmd
import ghidra.framework.model
import java.lang


class RemoveFunctionTagCmd(object, ghidra.framework.cmd.Command):
    """
    Command for removing a tag from a function.
    """





    def __init__(self, tagName: unicode, entryPoint: ghidra.program.model.address.Address):
        """
        @param tagName the name of the tag to remove
        @param entryPoint the address of the function
        """
        ...



    def applyTo(self, obj: ghidra.framework.model.DomainObject) -> bool:
        """
        PUBLIC METHODS
        """
        ...

    def equals(self, __a0: object) -> bool: ...

    def getClass(self) -> java.lang.Class: ...

    def getName(self) -> unicode: ...

    def getStatusMsg(self) -> unicode: ...

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
