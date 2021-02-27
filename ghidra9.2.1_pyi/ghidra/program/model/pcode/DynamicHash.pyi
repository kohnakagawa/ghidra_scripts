from typing import List
import ghidra.program.model.address
import ghidra.program.model.listing
import ghidra.program.model.pcode
import java.lang
import java.util


class DynamicHash(object):
    """
    A hash utility to uniquely identify a temporary Varnode in data-flow

     Most Varnodes can be identified within the data-flow graph by their storage address
     and the address of the PcodeOp that defines them.  For temporary registers,
     this does not work because the storage address is ephemeral. This class allows
     Varnodes like temporary registers (and constants) to be robustly identified
     by hashing details of the local data-flow.

     This class, when presented with a Varnode (via constructor), calculates a hash (getHash())
     and an address (getAddress()) of the PcodeOp most closely associated with the Varnode,
     either the defining op or the op directly reading the Varnode.
     There are actually four hash variants that can be calculated, labeled 0, 1, 2, or 3,
     which incrementally hash in a larger portion of data-flow.
    """

    transtable: List[int] = array('i', [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 11, 13, 13, 15, 15, 17, 18, 19, 19, 21, 22, 23, 24, 25, 26, 27, 28, 32, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 41, 43, 43, 0, 46, 47, 48, 49, 47, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 0, 19, 19, 67, 68, 69, 70, 71, 72])



    @overload
    def __init__(self, op: ghidra.program.model.pcode.PcodeOp, inputIndex: int):
        """
        Construct a level 0 hash on the input Varnode to the given PcodeOp

         The PcodeOp can be raw, no linked into a PcodeSyntaxTree
        @param op is the given PcodeOp
        @param inputIndex is the index of the input Varnode to hash
        """
        ...

    @overload
    def __init__(self, root: ghidra.program.model.pcode.Varnode, method: int):
        """
        Construct a hash of the given Varnode with a specific hash method.
        @param root is the given Varnode
        @param method is the method (0, 1, 2, 3)
        """
        ...

    @overload
    def __init__(self, root: ghidra.program.model.pcode.Varnode, fd: ghidra.program.model.pcode.PcodeSyntaxTree):
        """
        Construct a unique hash for the given Varnode, which must be in
         a syntax tree.  The hash method is cycled into a uniquely identifying one is found.
        @param root is the given Varnode
        @param fd is the PcodeSyntaxTree containing the Varnode
        """
        ...



    @staticmethod
    def calcConstantHash(instr: ghidra.program.model.listing.Instruction, value: long) -> List[long]:
        """
        Given a constant value accessed as an operand by a particular instruction,
         calculate a (level 0) hash for (any) corresponding constant varnode
        @param instr is the instruction referencing the constant
        @param value of the constant
        @return array of hash values (may be zero length)
        """
        ...

    @staticmethod
    def clearTotalPosition(h: long) -> long: ...

    def equals(self, __a0: object) -> bool: ...

    @staticmethod
    def findVarnode(fd: ghidra.program.model.pcode.PcodeSyntaxTree, addr: ghidra.program.model.address.Address, h: long) -> ghidra.program.model.pcode.Varnode: ...

    @staticmethod
    def gatherFirstLevelVars(__a0: java.util.ArrayList, __a1: ghidra.program.model.pcode.PcodeSyntaxTree, __a2: ghidra.program.model.address.Address, __a3: long) -> None: ...

    def getAddress(self) -> ghidra.program.model.address.Address: ...

    def getClass(self) -> java.lang.Class: ...

    def getHash(self) -> long: ...

    @staticmethod
    def getIsNotAttached(h: long) -> bool: ...

    @staticmethod
    def getMethodFromHash(h: long) -> int: ...

    @staticmethod
    def getOpCodeFromHash(h: long) -> int: ...

    @staticmethod
    def getPositionFromHash(h: long) -> int: ...

    @staticmethod
    def getSlotFromHash(h: long) -> int: ...

    @staticmethod
    def getTotalFromHash(h: long) -> int: ...

    def hashCode(self) -> int: ...

    def notify(self) -> None: ...

    def notifyAll(self) -> None: ...

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
    def hash(self) -> long: ...
