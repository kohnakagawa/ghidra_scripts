from typing import List
import ghidra.app.plugin.processors.sleigh
import ghidra.app.plugin.processors.sleigh.pattern
import ghidra.app.plugin.processors.sleigh.symbol
import ghidra.xml
import java.lang


class DecisionNode(object):
    """
    A node in the decision tree for resolving a Constructor in
     a SubtableSymbol based on the InstructionContext
    """





    def __init__(self): ...



    def equals(self, __a0: object) -> bool: ...

    def getChildren(self) -> List[ghidra.app.plugin.processors.sleigh.DecisionNode]: ...

    def getClass(self) -> java.lang.Class: ...

    def getConstructors(self) -> List[ghidra.app.plugin.processors.sleigh.Constructor]: ...

    def getPatterns(self) -> List[ghidra.app.plugin.processors.sleigh.pattern.DisjointPattern]: ...

    def hashCode(self) -> int: ...

    def notify(self) -> None: ...

    def notifyAll(self) -> None: ...

    def resolve(self, walker: ghidra.app.plugin.processors.sleigh.ParserWalker, debug: ghidra.app.plugin.processors.sleigh.SleighDebugLogger) -> ghidra.app.plugin.processors.sleigh.Constructor: ...

    def restoreXml(self, parser: ghidra.xml.XmlPullParser, par: ghidra.app.plugin.processors.sleigh.DecisionNode, sub: ghidra.app.plugin.processors.sleigh.symbol.SubtableSymbol) -> None: ...

    def toString(self) -> unicode: ...

    @overload
    def wait(self) -> None: ...

    @overload
    def wait(self, __a0: long) -> None: ...

    @overload
    def wait(self, __a0: long, __a1: int) -> None: ...

    @property
    def children(self) -> List[object]: ...

    @property
    def constructors(self) -> List[object]: ...

    @property
    def patterns(self) -> List[object]: ...
