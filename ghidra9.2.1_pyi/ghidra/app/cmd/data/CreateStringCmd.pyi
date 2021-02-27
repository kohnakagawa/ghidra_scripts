import ghidra.framework.cmd
import ghidra.framework.model
import java.lang


class CreateStringCmd(object, ghidra.framework.cmd.Command):
    """
    Command to create a String and optionally label it.
    """





    @overload
    def __init__(self, addr: ghidra.program.model.address.Address):
        """
        Constructs a new command for creating strings.
        """
        ...

    @overload
    def __init__(self, addr: ghidra.program.model.address.Address, length: int):
        """
        Constructs a new command for creating strings.
        """
        ...

    @overload
    def __init__(self, addr: ghidra.program.model.address.Address, length: int, unicode: bool):
        """
        Constructs a new command for creating strings.
        """
        ...

    @overload
    def __init__(self, addr: ghidra.program.model.address.Address, stringDataType: ghidra.program.model.data.AbstractStringDataType, length: int, clearMode: ghidra.program.model.data.DataUtilities.ClearDataMode): ...

    @overload
    def __init__(self, addr: ghidra.program.model.address.Address, length: int, unicode: bool, clearMode: ghidra.program.model.data.DataUtilities.ClearDataMode):
        """
        Constructs a new command for creating strings.
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
