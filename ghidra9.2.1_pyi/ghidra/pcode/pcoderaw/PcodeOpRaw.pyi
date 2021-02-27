from typing import Iterator
from typing import List
import ghidra.pcode.opbehavior
import ghidra.program.model.address
import ghidra.program.model.pcode
import ghidra.xml
import java.lang


class PcodeOpRaw(ghidra.program.model.pcode.PcodeOp):




    def __init__(self, op: ghidra.program.model.pcode.PcodeOp): ...



    def buildXML(self, resBuf: java.lang.StringBuilder, addrFactory: ghidra.program.model.address.AddressFactory) -> None: ...

    def equals(self, __a0: object) -> bool: ...

    def getAddress(self) -> ghidra.program.model.address.Address: ...

    def getBasicIter(self) -> Iterator[ghidra.program.model.pcode.PcodeOp]: ...

    def getBehavior(self) -> ghidra.pcode.opbehavior.OpBehavior: ...

    def getClass(self) -> java.lang.Class: ...

    def getInput(self, i: int) -> ghidra.program.model.pcode.Varnode:
        """
        @param i the i'th input varnode
        @return the i'th input varnode
        """
        ...

    def getInputs(self) -> List[ghidra.program.model.pcode.Varnode]:
        """
        @return get input varnodes
        """
        ...

    def getInsertIter(self) -> Iterator[object]: ...

    @overload
    def getMnemonic(self) -> unicode:
        """
        @return get the string representation for the pcode operation
        """
        ...

    @overload
    @staticmethod
    def getMnemonic(op: int) -> unicode:
        """
        Get string representation for p-code operation
        @param op operation code
        @return String representation of p-code operation
        """
        ...

    def getNumInputs(self) -> int:
        """
        @return number of input varnodes
        """
        ...

    @overload
    def getOpcode(self) -> int:
        """
        @return pcode operation code
        """
        ...

    @overload
    @staticmethod
    def getOpcode(s: unicode) -> int:
        """
        Get the p-code op code for the given mnemonic string.
        @param s is the mnemonic string
        @return the op code
        @throws UnknownInstructionException if there is no matching mnemonic
        """
        ...

    def getOutput(self) -> ghidra.program.model.pcode.Varnode:
        """
        @return get output varnodes
        """
        ...

    def getParent(self) -> ghidra.program.model.pcode.PcodeBlockBasic:
        """
        @return the pcode basic block this pcode belongs to
        """
        ...

    def getSeqnum(self) -> ghidra.program.model.pcode.SequenceNumber:
        """
        @return the sequence number this pcode is within some number of pcode
        """
        ...

    def getSlot(self, vn: ghidra.program.model.pcode.Varnode) -> int:
        """
        Assuming vn is an input to this op, return its input slot number
        @param vn is the input varnode
        @return the slot number
        """
        ...

    def hashCode(self) -> int: ...

    def insertInput(self, vn: ghidra.program.model.pcode.Varnode, slot: int) -> None:
        """
        Insert an input varnode at the given index of input varnodes
        @param vn varnode to insert
        @param slot insert index in input varnode list
        """
        ...

    def isAssignment(self) -> bool:
        """
        @return true if the pcode assigns a value to an output varnode
        """
        ...

    def isDead(self) -> bool:
        """
        Check if the pcode has been determined to be a dead operation.
        @return true if the pcode has been determined to have no effect in the context it is used
        """
        ...

    def notify(self) -> None: ...

    def notifyAll(self) -> None: ...

    @staticmethod
    def readXML(parser: ghidra.xml.XmlPullParser, pfact: ghidra.program.model.pcode.PcodeFactory) -> ghidra.program.model.pcode.PcodeOp:
        """
        Read p-code from XML stream
        @param parser is the XML stream
        @param pfact factory used to create p-code correctly
        @return new PcodeOp
        @throws PcodeXMLException if XML layout is incorrect
        """
        ...

    def removeInput(self, slot: int) -> None:
        """
        Remove a varnode at the given slot from the list of input varnodes
        @param slot index of input varnode to remove
        """
        ...

    def setInput(self, vn: ghidra.program.model.pcode.Varnode, slot: int) -> None:
        """
        Set/Replace an input varnode at the given slot.
        @param vn varnode to replace
        @param slot index of input varnode to be replaced
        """
        ...

    def setOpcode(self, o: int) -> None:
        """
        Set the pcode operation code
        @param o pcode operation code
        """
        ...

    def setOrder(self, ord: int) -> None:
        """
        Set relative position information of PcodeOps within
         a basic block, may change as basic block is edited.
        @param ord relative position of pcode op in basic block
        """
        ...

    def setOutput(self, vn: ghidra.program.model.pcode.Varnode) -> None:
        """
        Set the output varnode for the pcode operation.
        @param vn new output varnode
        """
        ...

    def setTime(self, t: int) -> None:
        """
        Set a unique number for pcode ops that are attached to the same address
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
    def address(self) -> ghidra.program.model.address.Address: ...

    @property
    def behavior(self) -> ghidra.pcode.opbehavior.OpBehavior: ...
