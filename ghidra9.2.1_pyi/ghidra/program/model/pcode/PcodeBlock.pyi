import ghidra.program.model.address
import ghidra.program.model.pcode
import ghidra.xml
import java.io
import java.lang
import java.util


class PcodeBlock(object):
    """
    Blocks of PcodeOps
    """

    BASIC: int = 1
    CONDITION: int = 7
    COPY: int = 3
    DOWHILE: int = 12
    GOTO: int = 4
    GRAPH: int = 2
    IFELSE: int = 9
    IFGOTO: int = 10
    INFLOOP: int = 14
    LIST: int = 6
    MULTIGOTO: int = 5
    PLAIN: int = 0
    PROPERIF: int = 8
    SWITCH: int = 13
    WHILEDO: int = 11




    class BlockEdge(object):
        label: int
        point: ghidra.program.model.pcode.PcodeBlock
        reverse_index: int



        @overload
        def __init__(self): ...

        @overload
        def __init__(self, __a0: ghidra.program.model.pcode.PcodeBlock, __a1: int, __a2: int): ...



        def equals(self, __a0: object) -> bool: ...

        def getClass(self) -> java.lang.Class: ...

        def hashCode(self) -> int: ...

        def notify(self) -> None: ...

        def notifyAll(self) -> None: ...

        @overload
        def restoreXml(self, __a0: ghidra.xml.XmlPullParser, __a1: ghidra.program.model.pcode.BlockMap) -> None: ...

        @overload
        def restoreXml(self, __a0: ghidra.xml.XmlPullParser, __a1: java.util.ArrayList) -> None: ...

        def saveXml(self, __a0: java.lang.StringBuilder) -> None: ...

        def toString(self) -> unicode: ...

        @overload
        def wait(self) -> None: ...

        @overload
        def wait(self, __a0: long) -> None: ...

        @overload
        def wait(self, __a0: long, __a1: int) -> None: ...



    def __init__(self): ...



    def calcDepth(self, leaf: ghidra.program.model.pcode.PcodeBlock) -> int: ...

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

    def getStart(self) -> ghidra.program.model.address.Address:
        """
        @return the first Address covered by this block
        """
        ...

    def getStop(self) -> ghidra.program.model.address.Address:
        """
        @return the last Address covered by this block
        """
        ...

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

    def restoreXmlBody(self, parser: ghidra.xml.XmlPullParser, resolver: ghidra.program.model.pcode.BlockMap) -> None:
        """
        Restore the any additional information beyond header and edges from XML
        @param parser is the XML parser
        @param resolver is for looking up edge references
        @throws PcodeXMLException for invalid XML descriptions
        """
        ...

    def restoreXmlEdges(self, parser: ghidra.xml.XmlPullParser, resolver: ghidra.program.model.pcode.BlockMap) -> None: ...

    def restoreXmlHeader(self, el: ghidra.xml.XmlElement) -> None: ...

    def saveXml(self, writer: java.io.Writer) -> None: ...

    def saveXmlBody(self, writer: java.io.Writer) -> None:
        """
        Serialize information about the block to XML,
         other than header and edge info
        @param writer is where to serialize to
        @throws IOException if there is a problem with the stream
        """
        ...

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
    def falseOut(self) -> ghidra.program.model.pcode.PcodeBlock: ...

    @property
    def frontLeaf(self) -> ghidra.program.model.pcode.PcodeBlock: ...

    @property
    def inSize(self) -> int: ...

    @property
    def index(self) -> int: ...

    @index.setter
    def index(self, value: int) -> None: ...

    @property
    def outSize(self) -> int: ...

    @property
    def parent(self) -> ghidra.program.model.pcode.PcodeBlock: ...

    @property
    def start(self) -> ghidra.program.model.address.Address: ...

    @property
    def stop(self) -> ghidra.program.model.address.Address: ...

    @property
    def trueOut(self) -> ghidra.program.model.pcode.PcodeBlock: ...

    @property
    def type(self) -> int: ...
