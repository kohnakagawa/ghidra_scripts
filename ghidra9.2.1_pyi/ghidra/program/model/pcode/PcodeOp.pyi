from typing import Iterator
from typing import List
import ghidra.program.model.address
import ghidra.program.model.pcode
import ghidra.xml
import java.lang


class PcodeOp(object):
    """
    Pcode Op describes a generic machine operation.  You can think of
     it as the microcode for a specific processor's instruction set.  There
     are a finite number of PcodeOp's that theoretically can define the
     operations for any given processor.

     Pcode have
        An operation code
        Some number of input parameter varnodes
        possible output varnode
    """

    BOOL_AND: int = 39
    BOOL_NEGATE: int = 37
    BOOL_OR: int = 40
    BOOL_XOR: int = 38
    BRANCH: int = 4
    BRANCHIND: int = 6
    CALL: int = 7
    CALLIND: int = 8
    CALLOTHER: int = 9
    CAST: int = 64
    CBRANCH: int = 5
    COPY: int = 1
    CPOOLREF: int = 68
    EXTRACT: int = 71
    FLOAT_ABS: int = 52
    FLOAT_ADD: int = 47
    FLOAT_CEIL: int = 57
    FLOAT_DIV: int = 48
    FLOAT_EQUAL: int = 41
    FLOAT_FLOAT2FLOAT: int = 55
    FLOAT_FLOOR: int = 58
    FLOAT_INT2FLOAT: int = 54
    FLOAT_LESS: int = 43
    FLOAT_LESSEQUAL: int = 44
    FLOAT_MULT: int = 49
    FLOAT_NAN: int = 46
    FLOAT_NEG: int = 51
    FLOAT_NOTEQUAL: int = 42
    FLOAT_ROUND: int = 59
    FLOAT_SQRT: int = 53
    FLOAT_SUB: int = 50
    FLOAT_TRUNC: int = 56
    INDIRECT: int = 61
    INSERT: int = 70
    INT_2COMP: int = 24
    INT_ADD: int = 19
    INT_AND: int = 27
    INT_CARRY: int = 21
    INT_DIV: int = 33
    INT_EQUAL: int = 11
    INT_LEFT: int = 29
    INT_LESS: int = 15
    INT_LESSEQUAL: int = 16
    INT_MULT: int = 32
    INT_NEGATE: int = 25
    INT_NOTEQUAL: int = 12
    INT_OR: int = 28
    INT_REM: int = 35
    INT_RIGHT: int = 30
    INT_SBORROW: int = 23
    INT_SCARRY: int = 22
    INT_SDIV: int = 34
    INT_SEXT: int = 18
    INT_SLESS: int = 13
    INT_SLESSEQUAL: int = 14
    INT_SREM: int = 36
    INT_SRIGHT: int = 31
    INT_SUB: int = 20
    INT_XOR: int = 26
    INT_ZEXT: int = 17
    LOAD: int = 2
    MULTIEQUAL: int = 60
    NEW: int = 69
    PCODE_MAX: int = 73
    PIECE: int = 62
    POPCOUNT: int = 72
    PTRADD: int = 65
    PTRSUB: int = 66
    RETURN: int = 10
    SEGMENTOP: int = 67
    STORE: int = 3
    SUBPIECE: int = 63
    UNIMPLEMENTED: int = 0



    @overload
    def __init__(self, a: ghidra.program.model.address.Address, sequencenumber: int, op: int):
        """
        Constructor - no inputs, output
        @param a address pcode is attached to
        @param sequencenumber id within a single address
        @param op pcode operation
        """
        ...

    @overload
    def __init__(self, a: ghidra.program.model.address.Address, sequencenumber: int, op: int, in_: List[ghidra.program.model.pcode.Varnode]):
        """
        Constructor - no output
        @param a address pcode is attached to
        @param sequencenumber id within a single address
        @param op operation pcode performs
        @param in inputs from pcode operation
        """
        ...

    @overload
    def __init__(self, sq: ghidra.program.model.pcode.SequenceNumber, op: int, numinputs: int, out: ghidra.program.model.pcode.Varnode):
        """
        Constructor - pcode part of sequence of pcodes, some number of inputs, output
        @param sq place in sequence of pcode
        @param op pcode operation
        @param numinputs number of inputs to operation, actual inputs not defined yet.
        @param out output from operation
        """
        ...

    @overload
    def __init__(self, sq: ghidra.program.model.pcode.SequenceNumber, op: int, in_: List[ghidra.program.model.pcode.Varnode], out: ghidra.program.model.pcode.Varnode):
        """
        Constructor - pcode part of sequence of pcodes, inputs, outputs
        @param sq place in sequence of pcode
        @param op pcode operation
        @param in inputs to operation
        @param out output from operation
        """
        ...

    @overload
    def __init__(self, a: ghidra.program.model.address.Address, sequencenumber: int, op: int, in_: List[ghidra.program.model.pcode.Varnode], out: ghidra.program.model.pcode.Varnode):
        """
        Constructor - inputs and outputs
        @param a address pcode is attached to
        @param sequencenumber unique sequence number for the specified address.
        @param op pcode operation
        @param in inputs to operation
        @param out output from operation
        """
        ...



    def buildXML(self, resBuf: java.lang.StringBuilder, addrFactory: ghidra.program.model.address.AddressFactory) -> None: ...

    def equals(self, __a0: object) -> bool: ...

    def getBasicIter(self) -> Iterator[ghidra.program.model.pcode.PcodeOp]: ...

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
    def assignment(self) -> bool: ...

    @property
    def basicIter(self) -> java.util.Iterator: ...

    @property
    def dead(self) -> bool: ...

    @property
    def inputs(self) -> List[ghidra.program.model.pcode.Varnode]: ...

    @property
    def insertIter(self) -> java.util.Iterator: ...

    @property
    def mnemonic(self) -> unicode: ...

    @property
    def numInputs(self) -> int: ...

    @property
    def opcode(self) -> int: ...

    @opcode.setter
    def opcode(self, value: int) -> None: ...

    @property
    def order(self) -> None: ...  # No getter available.

    @order.setter
    def order(self, value: int) -> None: ...

    @property
    def output(self) -> ghidra.program.model.pcode.Varnode: ...

    @output.setter
    def output(self, value: ghidra.program.model.pcode.Varnode) -> None: ...

    @property
    def parent(self) -> ghidra.program.model.pcode.PcodeBlockBasic: ...

    @property
    def seqnum(self) -> ghidra.program.model.pcode.SequenceNumber: ...

    @property
    def time(self) -> None: ...  # No getter available.

    @time.setter
    def time(self, value: int) -> None: ...
