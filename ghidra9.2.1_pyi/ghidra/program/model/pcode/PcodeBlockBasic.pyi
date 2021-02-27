from typing import Iterator
import ghidra.program.model.address
import ghidra.program.model.pcode
import ghidra.xml
import java.io
import java.lang


class PcodeBlockBasic(ghidra.program.model.pcode.PcodeBlock):
    """
    A basic block constructed from PcodeOps
    """









    def calcDepth(self, leaf: ghidra.program.model.pcode.PcodeBlock) -> int: ...

    def contains(self, addr: ghidra.program.model.address.Address) -> bool:
        """
        Is the given address in the range of instructions represented by this basic block
        @param addr is the Address
        @return true if the Address is contained
        """
        ...

    def equals(self, __a0: object) -> bool: ...

    def getClass(self) -> java.lang.Class: ...

    def getFalseOut(self) -> ghidra.program.model.pcode.PcodeBlock:
        """
        Assuming paths out of this block depend on a boolean condition
        @return the PcodeBlock coming out of this if the condition is false
        """
        ...

    def getFrontLeaf(self) -> ghidra.program.model.pcode.PcodeBlock: ...

    def getIn(self, i: int) -> ghidra.program.model.pcode.PcodeBlock: ...

    def getInRevIndex(self, i: int) -> int:
        """
        Get reverse index of the i-th incoming block. I.e. this.getIn(i).getOut(reverse_index) == this
        @param i is the incoming block to request reverse index from
        @return the reverse index
        """
        ...

    def getInSize(self) -> int: ...

    def getIndex(self) -> int: ...

    def getIterator(self) -> Iterator[ghidra.program.model.pcode.PcodeOp]:
        """
        @return an iterator over the PcodeOps in this basic block
        """
        ...

    def getOut(self, i: int) -> ghidra.program.model.pcode.PcodeBlock: ...

    def getOutRevIndex(self, i: int) -> int:
        """
        Get reverse index of the i-th outgoing block. I.e this.getOut(i).getIn(reverse_index) == this
        @param i is the outgoing block to request reverse index from
        @return the reverse index
        """
        ...

    def getOutSize(self) -> int: ...

    def getParent(self) -> ghidra.program.model.pcode.PcodeBlock: ...

    def getStart(self) -> ghidra.program.model.address.Address: ...

    def getStop(self) -> ghidra.program.model.address.Address: ...

    def getTrueOut(self) -> ghidra.program.model.pcode.PcodeBlock:
        """
        Assuming paths out of this block depend on a boolean condition
        @return the PcodeBlock coming out of this if the condition is true
        """
        ...

    def getType(self) -> int: ...

    def hashCode(self) -> int: ...

    @staticmethod
    def nameToType(name: unicode) -> int: ...

    def notify(self) -> None: ...

    def notifyAll(self) -> None: ...

    def restoreXml(self, parser: ghidra.xml.XmlPullParser, resolver: ghidra.program.model.pcode.BlockMap) -> None: ...

    def restoreXmlBody(self, parser: ghidra.xml.XmlPullParser, resolver: ghidra.program.model.pcode.BlockMap) -> None: ...

    def restoreXmlEdges(self, parser: ghidra.xml.XmlPullParser, resolver: ghidra.program.model.pcode.BlockMap) -> None: ...

    def restoreXmlHeader(self, el: ghidra.xml.XmlElement) -> None: ...

    def saveXml(self, writer: java.io.Writer) -> None: ...

    def saveXmlBody(self, writer: java.io.Writer) -> None: ...

    def saveXmlEdges(self, writer: java.io.Writer) -> None: ...

    def saveXmlHeader(self, buffer: java.lang.StringBuilder) -> None: ...

    def setIndex(self, i: int) -> None: ...

    def toString(self) -> unicode: ...

    @staticmethod
    def typeToName(type: int) -> unicode: ...

    @overload
    def wait(self) -> None: ...

    @overload
    def wait(self, __a0: long) -> None: ...

    @overload
    def wait(self, __a0: long, __a1: int) -> None: ...

    @property
    def iterator(self) -> java.util.Iterator: ...

    @property
    def start(self) -> ghidra.program.model.address.Address: ...

    @property
    def stop(self) -> ghidra.program.model.address.Address: ...
