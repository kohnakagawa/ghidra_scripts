import ghidra.framework.model
import java.lang


class UndoRedoToolState(object):




    def __init__(self, __a0: List[object], __a1: ghidra.framework.model.DomainObject): ...



    def equals(self, __a0: object) -> bool: ...

    def getClass(self) -> java.lang.Class: ...

    def hashCode(self) -> int: ...

    def notify(self) -> None: ...

    def notifyAll(self) -> None: ...

    def restoreTool(self, domainObject: ghidra.framework.model.DomainObject) -> None:
        """
        Restore the tool's state.
        """
        ...

    def toString(self) -> unicode: ...

    @overload
    def wait(self) -> None: ...

    @overload
    def wait(self, __a0: long) -> None: ...

    @overload
    def wait(self, __a0: long, __a1: int) -> None: ...
