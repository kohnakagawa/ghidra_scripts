import ghidra.app.plugin.processors.sleigh
import ghidra.app.plugin.processors.sleigh.expression
import ghidra.xml
import java.lang


class TokenField(ghidra.app.plugin.processors.sleigh.expression.PatternValue):
    """
    A contiguous set of bits within instruction stream, interpreted
     as an integer value
    """





    def __init__(self): ...



    @staticmethod
    def byteSwap(val: long, size: int) -> long:
        """
        Swap the least sig -size- bytes in -val-
        @param val value to be byte swapped
        @param size number of bytes involved in swap
        @return
        """
        ...

    def equals(self, obj: object) -> bool: ...

    def getBitEnd(self) -> int: ...

    def getBitStart(self) -> int: ...

    def getByteEnd(self) -> int: ...

    def getByteStart(self) -> int: ...

    def getClass(self) -> java.lang.Class: ...

    def getShift(self) -> int: ...

    def getValue(self, walker: ghidra.app.plugin.processors.sleigh.ParserWalker) -> long: ...

    def hasSignbit(self) -> bool: ...

    def hashCode(self) -> int: ...

    def isBigEndian(self) -> bool: ...

    def maxValue(self) -> long: ...

    def minValue(self) -> long: ...

    def notify(self) -> None: ...

    def notifyAll(self) -> None: ...

    @staticmethod
    def restoreExpression(parser: ghidra.xml.XmlPullParser, lang: ghidra.app.plugin.processors.sleigh.SleighLanguage) -> ghidra.app.plugin.processors.sleigh.expression.PatternExpression: ...

    def restoreXml(self, parser: ghidra.xml.XmlPullParser, lang: ghidra.app.plugin.processors.sleigh.SleighLanguage) -> None: ...

    @staticmethod
    def signExtend(val: long, bit: int) -> long:
        """
        Sign extend -val- above -bit-
        @param val value to extend
        @param bit bit specifying sign
        @return
        """
        ...

    def toString(self) -> unicode: ...

    @overload
    def wait(self) -> None: ...

    @overload
    def wait(self, __a0: long) -> None: ...

    @overload
    def wait(self, __a0: long, __a1: int) -> None: ...

    @staticmethod
    def zeroExtend(val: long, bit: int) -> long:
        """
        Clear all bits in -val- above -bit-
        @param val value to zero extend
        @param bit bit above which to zero extend
        @return
        """
        ...

    @property
    def bigEndian(self) -> bool: ...

    @property
    def bitEnd(self) -> int: ...

    @property
    def bitStart(self) -> int: ...

    @property
    def byteEnd(self) -> int: ...

    @property
    def byteStart(self) -> int: ...

    @property
    def shift(self) -> int: ...
