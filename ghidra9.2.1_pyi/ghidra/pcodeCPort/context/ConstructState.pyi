import java.lang


class ConstructState(object):
    ct: ghidra.pcodeCPort.slghsymbol.Constructor
    hand: ghidra.pcodeCPort.context.FixedHandle
    length: int
    offset: int
    oper: int
    parent: ghidra.pcodeCPort.context.ConstructState
    resolve: generic.stl.VectorSTL



    def __init__(self): ...



    def equals(self, __a0: object) -> bool: ...

    def getClass(self) -> java.lang.Class: ...

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
