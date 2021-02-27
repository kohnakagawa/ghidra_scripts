import ghidra.sleigh.grammar
import java.lang


class SleighPreprocessor(object, ghidra.sleigh.grammar.ExpressionEnvironment):




    def __init__(self, definitions: ghidra.pcodeCPort.slgh_compile.PreprocessorDefinitions, inputFile: java.io.File): ...



    @overload
    def equals(self, __a0: object) -> bool: ...

    @overload
    def equals(self, lhs: unicode, rhs: unicode) -> bool: ...

    def getClass(self) -> java.lang.Class: ...

    def hashCode(self) -> int: ...

    def isCompatible(self) -> bool: ...

    def lookup(self, variable: unicode) -> unicode: ...

    def notify(self) -> None: ...

    def notifyAll(self) -> None: ...

    def process(self, writer: ghidra.sleigh.grammar.LineArrayListWriter) -> None: ...

    def reportError(self, msg: unicode) -> None: ...

    def scanForTimestamp(self) -> long: ...

    def setCompatible(self, compatible: bool) -> None: ...

    def toString(self) -> unicode: ...

    @overload
    def wait(self) -> None: ...

    @overload
    def wait(self, __a0: long) -> None: ...

    @overload
    def wait(self, __a0: long, __a1: int) -> None: ...

    @property
    def compatible(self) -> bool: ...

    @compatible.setter
    def compatible(self, value: bool) -> None: ...
