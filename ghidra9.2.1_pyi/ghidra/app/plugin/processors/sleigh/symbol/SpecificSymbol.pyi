import ghidra.app.plugin.processors.sleigh
import ghidra.app.plugin.processors.sleigh.expression
import ghidra.app.plugin.processors.sleigh.symbol
import ghidra.xml
import java.lang
import java.util


class SpecificSymbol(ghidra.app.plugin.processors.sleigh.symbol.TripleSymbol):
    """
    This is a TripleSymbol whose semantic value can be determined
     at compile time (i.e. without an InstructionContext)
     The functionality is not needed for the disassembler interface
     but we keep the structure
    """





    def __init__(self): ...



    def equals(self, __a0: object) -> bool: ...

    def getClass(self) -> java.lang.Class: ...

    def getFixedHandle(self, hand: ghidra.app.plugin.processors.sleigh.FixedHandle, walker: ghidra.app.plugin.processors.sleigh.ParserWalker) -> None: ...

    def getId(self) -> int: ...

    def getName(self) -> unicode: ...

    def getPatternExpression(self) -> ghidra.app.plugin.processors.sleigh.expression.PatternExpression: ...

    def getScopeId(self) -> int: ...

    def hashCode(self) -> int: ...

    def notify(self) -> None: ...

    def notifyAll(self) -> None: ...

    def print(self, walker: ghidra.app.plugin.processors.sleigh.ParserWalker) -> unicode: ...

    def printList(self, __a0: ghidra.app.plugin.processors.sleigh.ParserWalker, __a1: java.util.ArrayList) -> None: ...

    def resolve(self, walker: ghidra.app.plugin.processors.sleigh.ParserWalker, debug: ghidra.app.plugin.processors.sleigh.SleighDebugLogger) -> ghidra.app.plugin.processors.sleigh.Constructor: ...

    def restoreHeaderXml(self, parser: ghidra.xml.XmlPullParser) -> None: ...

    def restoreXml(self, parser: ghidra.xml.XmlPullParser, sleigh: ghidra.app.plugin.processors.sleigh.SleighLanguage) -> None: ...

    def toString(self) -> unicode: ...

    @overload
    def wait(self) -> None: ...

    @overload
    def wait(self, __a0: long) -> None: ...

    @overload
    def wait(self, __a0: long, __a1: int) -> None: ...
