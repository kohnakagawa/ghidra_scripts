import ghidra.pcode.opbehavior
import java.lang


class OpBehaviorFloatFloat2Float(ghidra.pcode.opbehavior.UnaryOpBehavior):




    def __init__(self): ...



    def equals(self, __a0: object) -> bool: ...

    @overload
    def evaluateUnary(self, sizeout: int, sizein: int, in1: long) -> long: ...

    @overload
    def evaluateUnary(self, sizeout: int, sizein: int, in1: long) -> long: ...

    def getClass(self) -> java.lang.Class: ...

    def getOpCode(self) -> int: ...

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
