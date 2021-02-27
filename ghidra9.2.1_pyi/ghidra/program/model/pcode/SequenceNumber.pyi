import ghidra.program.model.address
import ghidra.program.model.pcode
import ghidra.xml
import java.lang


class SequenceNumber(object, java.lang.Comparable):
    """
    Basically a unique address for a PcodeOp
     It is unique, maintains original assembly instruction address, and is comparable
     within a basic block
    """





    def __init__(self, instrAddr: ghidra.program.model.address.Address, sequenceNum: int):
        """
        Construct a sequence number for an instruction at an address and sequence of pcode op within
         that instructions set of pcode.
        @param instrAddr address of instruction
        @param sequenceNum sequence of pcode op with an instructions pcode ops
        """
        ...



    def buildXML(self) -> java.lang.StringBuilder:
        """
        @return Build XML tag for SequenceNumber
        """
        ...

    @overload
    def compareTo(self, sq: ghidra.program.model.pcode.SequenceNumber) -> int: ...

    @overload
    def compareTo(self, __a0: object) -> int: ...

    def equals(self, o: object) -> bool: ...

    def getClass(self) -> java.lang.Class: ...

    def getOrder(self) -> int:
        """
        Get relative position information of PcodeOps within
         a basic block, may change as basic block is edited.
        @return relative position of pcode in a basic block
        """
        ...

    def getTarget(self) -> ghidra.program.model.address.Address:
        """
        @return get address of instruction this sequence belongs to
        """
        ...

    def getTime(self) -> int:
        """
        Get unique Sub-address for distinguishing multiple PcodeOps at one
         instruction address.
         Does not change over lifetime of PcodeOp
        @return unique id for a pcode op within a given instruction
        """
        ...

    def hashCode(self) -> int: ...

    def notify(self) -> None: ...

    def notifyAll(self) -> None: ...

    @staticmethod
    def readXML(parser: ghidra.xml.XmlPullParser, factory: ghidra.program.model.address.AddressFactory) -> ghidra.program.model.pcode.SequenceNumber:
        """
        Create a new Sequence number from XML SAX tree element.
        @param parser the xml parser
        @param factory pcode factory used to create new pcode
        @return new sequence number
        """
        ...

    def setOrder(self, o: int) -> None:
        """
        Set relative position information of PcodeOps within
         a basic block, may change as basic block is edited.
        @param o relative position of pcodeOp within a basic block
        """
        ...

    def setTime(self, t: int) -> None:
        """
        Set unique Sub-address for distinguishing multiple PcodeOps at one
         instruction address.
         Does not change over lifetime of PcodeOp
        @param t unique id
        """
        ...

    def toString(self) -> unicode: ...

    @overload
    def wait(self) -> None: ...

    @overload
    def wait(self, __a0: long) -> None: ...

    @overload
    def wait(self, __a0: long, __a1: int) -> None: ...

    @property
    def order(self) -> int: ...

    @order.setter
    def order(self, value: int) -> None: ...

    @property
    def target(self) -> ghidra.program.model.address.Address: ...

    @property
    def time(self) -> int: ...

    @time.setter
    def time(self, value: int) -> None: ...
