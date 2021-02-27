import generic.stl
import ghidra.pcodeCPort.semantics
import ghidra.pcodeCPort.slgh_compile
import ghidra.sleigh.grammar
import java.lang


class ExprTree(object):
    location: ghidra.sleigh.grammar.Location



    @overload
    def __init__(self, __a0: ghidra.sleigh.grammar.Location): ...

    @overload
    def __init__(self, __a0: ghidra.sleigh.grammar.Location, __a1: ghidra.pcodeCPort.semantics.OpTpl): ...

    @overload
    def __init__(self, __a0: ghidra.sleigh.grammar.Location, __a1: ghidra.pcodeCPort.semantics.VarnodeTpl): ...



    def equals(self, __a0: object) -> bool: ...

    def getClass(self) -> java.lang.Class: ...

    def hashCode(self) -> int: ...

    def notify(self) -> None: ...

    def notifyAll(self) -> None: ...

    def setOutput(self, __a0: ghidra.sleigh.grammar.Location, __a1: ghidra.pcodeCPort.semantics.VarnodeTpl) -> None: ...

    def toString(self) -> unicode: ...

    @staticmethod
    def toVector(__a0: ghidra.pcodeCPort.slgh_compile.ExprTree) -> generic.stl.VectorSTL: ...

    @overload
    def wait(self) -> None: ...

    @overload
    def wait(self, __a0: long) -> None: ...

    @overload
    def wait(self, __a0: long, __a1: int) -> None: ...
