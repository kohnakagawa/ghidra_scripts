import ghidra.framework.cmd
import ghidra.framework.model
import java.lang


class AddFunctionTagCmd(object, ghidra.framework.cmd.Command):
    """
    Command for assigning a tag to a function. Executing this will pop up a dialog
     allowing the user to assign tags to a function.
    """





    def __init__(self, tagName: unicode, entryPoint: ghidra.program.model.address.Address):
        """
        Constructor.
        @param tagName the name of the tag to add
        @param entryPoint the function address
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
