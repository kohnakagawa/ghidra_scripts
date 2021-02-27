import ghidra.app.plugin.processors.sleigh
import ghidra.app.plugin.processors.sleigh.expression
import ghidra.xml
import java.lang


class ContextField(ghidra.app.plugin.processors.sleigh.expression.PatternValue):
    """
    Contiguous bits in the non-instruction part of the context interpreted
     as an integer value
    """





    def __init__(self): ...



    def equals(self, obj: object) -> bool: ...

    def getByteEnd(self) -> int: ...

    def getByteStart(self) -> int: ...

    def getClass(self) -> java.lang.Class: ...

    def getEndBit(self) -> int: ...

    def getShift(self) -> int: ...

    def getSignBit(self) -> bool: ...

    def getStartBit(self) -> int: ...

    def getValue(self, walker: ghidra.app.plugin.processors.sleigh.ParserWalker) -> long: ...

    def hasSignbit(self) -> bool: ...

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
    def byteEnd(self) -> int: ...

    @property
    def byteStart(self) -> int: ...

    @property
    def endBit(self) -> int: ...

    @property
    def shift(self) -> int: ...

    @property
    def signBit(self) -> bool: ...

    @property
    def startBit(self) -> int: ...