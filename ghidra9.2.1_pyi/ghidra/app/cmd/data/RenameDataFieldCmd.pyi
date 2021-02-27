import ghidra.framework.cmd
import ghidra.framework.model
import java.lang


class RenameDataFieldCmd(object, ghidra.framework.cmd.Command):
    """
    Command to rename a component in a data type.
    """





    def __init__(self, comp: ghidra.program.model.data.DataTypeComponent, newName: unicode):
        """
        Construct a new RenameDataFieldCmd.
        @param comp component in data type to be renamed
        @param newName new name for the component
        """
        ...



    def applyTo(self, obj: ghidra.framework.model.DomainObject) -> bool: ...

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
