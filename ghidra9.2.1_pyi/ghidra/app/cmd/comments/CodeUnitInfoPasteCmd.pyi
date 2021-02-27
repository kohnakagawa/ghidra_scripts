import ghidra.framework.cmd
import ghidra.framework.model
import java.lang


class CodeUnitInfoPasteCmd(object, ghidra.framework.cmd.Command):
    """
    Undoable edit for pasting code unit information at a location.
     This class actually does the work of the "paste."
    """





    def __init__(self, __a0: ghidra.program.model.address.Address, __a1: List[object], __a2: bool, __a3: bool): ...



    def applyTo(self, obj: ghidra.framework.model.DomainObject) -> bool: ...

    def equals(self, __a0: object) -> bool: ...

    def getClass(self) -> java.lang.Class: ...

    def getName(self) -> unicode:
        """
        The name of the edit action.
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
