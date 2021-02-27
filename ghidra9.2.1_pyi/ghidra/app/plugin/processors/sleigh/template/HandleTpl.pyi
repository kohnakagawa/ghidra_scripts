import ghidra.app.plugin.processors.sleigh
import ghidra.program.model.address
import ghidra.xml
import java.lang


class HandleTpl(object):
    """
    Placeholder that resolves for a specific InstructionContext into
      a FixedHandle representing the semantic value of a Constructor
    """









    def equals(self, __a0: object) -> bool: ...

    def fix(self, hand: ghidra.app.plugin.processors.sleigh.FixedHandle, walker: ghidra.app.plugin.processors.sleigh.ParserWalker) -> None: ...

    def fixPrintPiece(self, hand: ghidra.app.plugin.processors.sleigh.FixedHandle, walker: ghidra.app.plugin.processors.sleigh.ParserWalker, handleIndex: int) -> None: ...

    def getClass(self) -> java.lang.Class: ...

    def getOffsetOperandIndex(self) -> int: ...

    def getSize(self) -> int:
        """
        Get the size of the expected value in bits
        @return the number of bits
        """
        ...

    def hashCode(self) -> int: ...

    def notify(self) -> None: ...

    def notifyAll(self) -> None: ...

    def restoreXml(self, parser: ghidra.xml.XmlPullParser, factory: ghidra.program.model.address.AddressFactory) -> None: ...

    def toString(self) -> unicode: ...

    @overload
    def wait(self) -> None: ...

    @overload
    def wait(self, __a0: long) -> None: ...

    @overload
    def wait(self, __a0: long, __a1: int) -> None: ...

    @property
    def offsetOperandIndex(self) -> int: ...

    @property
    def size(self) -> int: ...
