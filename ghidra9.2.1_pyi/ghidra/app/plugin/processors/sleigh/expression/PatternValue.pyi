import ghidra.app.plugin.processors.sleigh
import ghidra.app.plugin.processors.sleigh.expression
import ghidra.xml
import java.lang


class PatternValue(ghidra.app.plugin.processors.sleigh.expression.PatternExpression):
    """
    This is a PatternExpression which can be interpreted as an
     integer value. Restricting the PatternValue to a specific integer
     yields an actual pattern.

     None of the functionality is needed for the disassembly interface,
     (only for the compiler interface) but we preserve the structure
    """





    def __init__(self): ...



    def equals(self, __a0: object) -> bool: ...

    def getClass(self) -> java.lang.Class: ...

    def getValue(self, walker: ghidra.app.plugin.processors.sleigh.ParserWalker) -> long: ...

    def hashCode(self) -> int: ...

    def maxValue(self) -> long: ...

    def minValue(self) -> long: ...

    def notify(self) -> None: ...

    def notifyAll(self) -> None: ...

    @staticmethod
    def restoreExpression(parser: ghidra.xml.XmlPullParser, lang: ghidra.app.plugin.processors.sleigh.SleighLanguage) -> ghidra.app.plugin.processors.sleigh.expression.PatternExpression: ...

    def restoreXml(self, parser: ghidra.xml.XmlPullParser, lang: ghidra.app.plugin.processors.sleigh.SleighLanguage) -> None: ...

    def toString(self) -> unicode: ...

    @overload
    def wait(self) -> None: ...

    @overload
    def wait(self, __a0: long) -> None: ...

    @overload
    def wait(self, __a0: long, __a1: int) -> None: ...
