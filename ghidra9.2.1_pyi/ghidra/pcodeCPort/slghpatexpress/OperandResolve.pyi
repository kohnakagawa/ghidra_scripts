import java.lang


class OperandResolve(object):
    base: int
    cur_rightmost: int
    offset: int
    operands: generic.stl.VectorSTL
    size: int



    def __init__(self, __a0: generic.stl.VectorSTL): ...



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
