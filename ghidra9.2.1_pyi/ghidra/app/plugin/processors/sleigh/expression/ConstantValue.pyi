import ghidra.app.plugin.processors.sleigh
import ghidra.app.plugin.processors.sleigh.expression
import ghidra.xml
import java.lang


class ConstantValue(ghidra.app.plugin.processors.sleigh.expression.PatternValue):
    """
    A constant value associated with an alwaysTrue pattern
    """





    @overload
    def __init__(self): ...

    @overload
    def __init__(self, b: long): ...



    def equals(self, obj: object) -> bool: ...

    def getClass(self) -> java.lang.Class: ...

    @overload
    def getValue(self) -> long: ...

    @overload
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

    @property
    def value(self) -> long: ...
