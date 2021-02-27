import ghidra.pcodeCPort.context
import ghidra.pcodeCPort.slghpattern
import java.io
import java.lang
import org.jdom


class ContextPattern(ghidra.pcodeCPort.slghpattern.DisjointPattern):




    @overload
    def __init__(self): ...

    @overload
    def __init__(self, __a0: ghidra.pcodeCPort.slghpattern.PatternBlock): ...



    def alwaysFalse(self) -> bool: ...

    def alwaysInstructionTrue(self) -> bool: ...

    def alwaysTrue(self) -> bool: ...

    def commonSubPattern(self, __a0: ghidra.pcodeCPort.slghpattern.Pattern, __a1: int) -> ghidra.pcodeCPort.slghpattern.Pattern: ...

    def dispose(self) -> None: ...

    def doAnd(self, __a0: ghidra.pcodeCPort.slghpattern.Pattern, __a1: int) -> ghidra.pcodeCPort.slghpattern.Pattern: ...

    def doOr(self, __a0: ghidra.pcodeCPort.slghpattern.Pattern, __a1: int) -> ghidra.pcodeCPort.slghpattern.Pattern: ...

    def equals(self, __a0: object) -> bool: ...

    def getBlock(self) -> ghidra.pcodeCPort.slghpattern.PatternBlock: ...

    def getClass(self) -> java.lang.Class: ...

    def getDisjoint(self, __a0: int) -> ghidra.pcodeCPort.slghpattern.DisjointPattern: ...

    def getLength(self, __a0: bool) -> int: ...

    def getMask(self, __a0: int, __a1: int, __a2: bool) -> int: ...

    def getValue(self, __a0: int, __a1: int, __a2: bool) -> int: ...

    def hashCode(self) -> int: ...

    def identical(self, __a0: ghidra.pcodeCPort.slghpattern.DisjointPattern) -> bool: ...

    def isMatch(self, __a0: ghidra.pcodeCPort.context.ParserWalker) -> bool: ...

    def notify(self) -> None: ...

    def notifyAll(self) -> None: ...

    def numDisjoint(self) -> int: ...

    @staticmethod
    def resolveIntersectBlock(__a0: ghidra.pcodeCPort.slghpattern.PatternBlock, __a1: ghidra.pcodeCPort.slghpattern.PatternBlock, __a2: ghidra.pcodeCPort.slghpattern.PatternBlock) -> bool: ...

    def resolvesIntersect(self, __a0: ghidra.pcodeCPort.slghpattern.DisjointPattern, __a1: ghidra.pcodeCPort.slghpattern.DisjointPattern) -> bool: ...

    @staticmethod
    def restoreDisjoint(__a0: org.jdom.Element) -> ghidra.pcodeCPort.slghpattern.DisjointPattern: ...

    def restoreXml(self, __a0: org.jdom.Element) -> None: ...

    def saveXml(self, __a0: java.io.PrintStream) -> None: ...

    def shiftInstruction(self, __a0: int) -> None: ...

    def simplifyClone(self) -> ghidra.pcodeCPort.slghpattern.Pattern: ...

    def specializes(self, __a0: ghidra.pcodeCPort.slghpattern.DisjointPattern) -> bool: ...

    def toString(self) -> unicode: ...

    @overload
    def wait(self) -> None: ...

    @overload
    def wait(self, __a0: long) -> None: ...

    @overload
    def wait(self, __a0: long, __a1: int) -> None: ...

    @property
    def block(self) -> ghidra.pcodeCPort.slghpattern.PatternBlock: ...
