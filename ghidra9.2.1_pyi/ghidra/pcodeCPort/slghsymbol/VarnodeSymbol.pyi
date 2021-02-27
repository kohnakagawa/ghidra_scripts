import ghidra.pcodeCPort.context
import ghidra.pcodeCPort.pcoderaw
import ghidra.pcodeCPort.semantics
import ghidra.pcodeCPort.sleighbase
import ghidra.pcodeCPort.slghpatexpress
import ghidra.pcodeCPort.slghsymbol
import ghidra.sleigh.grammar
import java.io
import java.lang
import java.util
import org.jdom


class VarnodeSymbol(ghidra.pcodeCPort.slghsymbol.PatternlessSymbol):
    location: ghidra.sleigh.grammar.Location



    @overload
    def __init__(self, __a0: ghidra.sleigh.grammar.Location): ...

    @overload
    def __init__(self, __a0: ghidra.sleigh.grammar.Location, __a1: unicode, __a2: ghidra.pcodeCPort.space.AddrSpace, __a3: long, __a4: int): ...



    def collectLocalValues(self, __a0: java.util.ArrayList) -> None: ...

    @overload
    def compareTo(self, __a0: ghidra.pcodeCPort.slghsymbol.SleighSymbol) -> int: ...

    @overload
    def compareTo(self, __a0: object) -> int: ...

    def dispose(self) -> None: ...

    def equals(self, __a0: object) -> bool: ...

    def getClass(self) -> java.lang.Class: ...

    def getFixedHandle(self, __a0: ghidra.pcodeCPort.context.FixedHandle, __a1: ghidra.pcodeCPort.context.ParserWalker) -> None: ...

    def getFixedVarnode(self) -> ghidra.pcodeCPort.pcoderaw.VarnodeData: ...

    def getId(self) -> int: ...

    def getLocation(self) -> ghidra.sleigh.grammar.Location: ...

    def getName(self) -> unicode: ...

    def getPatternExpression(self) -> ghidra.pcodeCPort.slghpatexpress.PatternExpression: ...

    def getSize(self) -> int: ...

    def getType(self) -> ghidra.pcodeCPort.slghsymbol.symbol_type: ...

    def getVarnode(self) -> ghidra.pcodeCPort.semantics.VarnodeTpl: ...

    def hashCode(self) -> int: ...

    def markAsContext(self) -> None: ...

    def notify(self) -> None: ...

    def notifyAll(self) -> None: ...

    def print(self, __a0: java.io.PrintStream, __a1: ghidra.pcodeCPort.context.ParserWalker) -> None: ...

    def resolve(self, __a0: ghidra.pcodeCPort.context.ParserWalker) -> ghidra.pcodeCPort.slghsymbol.Constructor: ...

    def restoreXml(self, __a0: org.jdom.Element, __a1: ghidra.pcodeCPort.sleighbase.SleighBase) -> None: ...

    def saveXml(self, __a0: java.io.PrintStream) -> None: ...

    def saveXmlHeader(self, __a0: java.io.PrintStream) -> None: ...

    def setLocation(self, __a0: ghidra.sleigh.grammar.Location) -> None: ...

    def setWasSought(self, __a0: bool) -> None: ...

    def toDetailedString(self) -> unicode: ...

    def toString(self) -> unicode: ...

    @overload
    def wait(self) -> None: ...

    @overload
    def wait(self, __a0: long) -> None: ...

    @overload
    def wait(self, __a0: long, __a1: int) -> None: ...

    def wasSought(self) -> bool: ...

    @property
    def fixedVarnode(self) -> ghidra.pcodeCPort.pcoderaw.VarnodeData: ...

    @property
    def size(self) -> int: ...

    @property
    def type(self) -> ghidra.pcodeCPort.slghsymbol.symbol_type: ...

    @property
    def varnode(self) -> ghidra.pcodeCPort.semantics.VarnodeTpl: ...
