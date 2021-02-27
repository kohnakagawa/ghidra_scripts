import ghidra.pcodeCPort.context
import ghidra.pcodeCPort.slghpattern
import java.io
import java.lang
import org.jdom


class OrPattern(ghidra.pcodeCPort.slghpattern.Pattern):




    @overload
    def __init__(self): ...

    @overload
    def __init__(self, __a0: generic.stl.VectorSTL): ...

    @overload
    def __init__(self, __a0: ghidra.pcodeCPort.slghpattern.DisjointPattern, __a1: ghidra.pcodeCPort.slghpattern.DisjointPattern): ...



    def alwaysFalse(self) -> bool: ...

    def alwaysInstructionTrue(self) -> bool: ...

    def alwaysTrue(self) -> bool: ...

    def commonSubPattern(self, __a0: ghidra.pcodeCPort.slghpattern.Pattern, __a1: int) -> ghidra.pcodeCPort.slghpattern.Pattern: ...

    def dispose(self) -> None: ...

    def doAnd(self, __a0: ghidra.pcodeCPort.slghpattern.Pattern, __a1: int) -> ghidra.pcodeCPort.slghpattern.Pattern: ...

    def doOr(self, __a0: ghidra.pcodeCPort.slghpattern.Pattern, __a1: int) -> ghidra.pcodeCPort.slghpattern.Pattern: ...

    def equals(self, __a0: object) -> bool: ...

    def getClass(self) -> java.lang.Class: ...

    def getDisjoint(self, __a0: int) -> ghidra.pcodeCPort.slghpattern.DisjointPattern: ...

    def hashCode(self) -> int: ...

    def isMatch(self, __a0: ghidra.pcodeCPort.context.ParserWalker) -> bool: ...

    def notify(self) -> None: ...

    def notifyAll(self) -> None: ...

    def numDisjoint(self) -> int: ...

    def restoreXml(self, __a0: org.jdom.Element) -> None: ...

    def saveXml(self, __a0: java.io.PrintStream) -> None: ...

    def shiftInstruction(self, __a0: int) -> None: ...

    def simplifyClone(self) -> ghidra.pcodeCPort.slghpattern.Pattern: ...

    def toString(self) -> unicode: ...

    @overload
    def wait(self) -> None: ...

    @overload
    def wait(self, __a0: long) -> None: ...

    @overload
    def wait(self, __a0: long, __a1: int) -> None: ...