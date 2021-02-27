import ghidra.app.plugin.processors.sleigh
import ghidra.program.model.address
import java.lang


class ParserWalker(object):
    """
    Class for walking the Sleigh Parser tree.  The nodes of the tree are the Sleigh Constructors arranged for a particular
     instruction.  This tree is walked for various purposes:

         SleighInstructionPrototype.resolve        - initial parsing of instruction and building the tree
         SleighInstructionPrototype.resolveHandles - filling in Varnode values for all the Constructor exports
         PcodeEmit                                 - for weaving together p-code for an instruction

    """





    @overload
    def __init__(self, c: ghidra.app.plugin.processors.sleigh.SleighParserContext): ...

    @overload
    def __init__(self, c: ghidra.app.plugin.processors.sleigh.SleighParserContext, cross: ghidra.app.plugin.processors.sleigh.SleighParserContext):
        """
        For use with pcode cross-build
        @param c context
        @param cross cross context
        """
        ...



    def allocateOperand(self) -> None: ...

    def baseState(self) -> None:
        """
        Initialize a walk of the tree
        """
        ...

    def calcCurrentLength(self, minLength: int, numopers: int) -> None:
        """
        Calculate the length of the current constructor state
         assuming all its operands are constructed
        """
        ...

    def equals(self, __a0: object) -> bool: ...

    def getAddr(self) -> ghidra.program.model.address.Address: ...

    def getClass(self) -> java.lang.Class: ...

    def getConstSpace(self) -> ghidra.program.model.address.AddressSpace: ...

    def getConstructor(self) -> ghidra.app.plugin.processors.sleigh.Constructor:
        """
        @return the Constructor for the current node in the walk
        """
        ...

    def getContextBits(self, startbit: int, size: int) -> int: ...

    def getContextBytes(self, byteoff: int, numbytes: int) -> int: ...

    def getCurSpace(self) -> ghidra.program.model.address.AddressSpace: ...

    def getCurrentLength(self) -> int: ...

    def getCurrentSubtableName(self) -> unicode: ...

    def getFixedHandle(self, i: int) -> ghidra.app.plugin.processors.sleigh.FixedHandle: ...

    def getFlowDestAddr(self) -> ghidra.program.model.address.Address: ...

    def getFlowRefAddr(self) -> ghidra.program.model.address.Address: ...

    def getInstructionBits(self, startbit: int, size: int) -> int: ...

    def getInstructionBytes(self, byteoff: int, numbytes: int) -> int: ...

    def getNaddr(self) -> ghidra.program.model.address.Address: ...

    def getOffset(self, i: int) -> int:
        """
        Get the offset into the instruction for the current node (i=-1) or one of the current node's children
        @param i selects the desired child of the current node
        @return the offset (in bytes) for the selected node
        """
        ...

    def getOperand(self) -> int:
        """
        Find the next child that needs to be traversed
        @return the index of the child
        """
        ...

    def getParentHandle(self) -> ghidra.app.plugin.processors.sleigh.FixedHandle: ...

    def getParserContext(self) -> ghidra.app.plugin.processors.sleigh.SleighParserContext: ...

    def getState(self) -> ghidra.app.plugin.processors.sleigh.ConstructState: ...

    def hashCode(self) -> int: ...

    def isState(self) -> bool:
        """
        Are we at the end of the tree walk
        @return true if there is more walk to go
        """
        ...

    def notify(self) -> None: ...

    def notifyAll(self) -> None: ...

    def popOperand(self) -> None:
        """
        Move to the parent of the current node
        """
        ...

    def pushOperand(self, i: int) -> None:
        """
        Move down to a particular child of the current node.  Store what would be the next sibling to walk
        @param i is the index of the desired child
        """
        ...

    def setConstructor(self, ct: ghidra.app.plugin.processors.sleigh.Constructor) -> None: ...

    def setCurrentLength(self, len: int) -> None: ...

    def setOffset(self, off: int) -> None: ...

    def setOutOfBandState(self, ct: ghidra.app.plugin.processors.sleigh.Constructor, index: int, tempstate: ghidra.app.plugin.processors.sleigh.ConstructState, otherwalker: ghidra.app.plugin.processors.sleigh.ParserWalker) -> None: ...

    def snippetState(self) -> None:
        """
        Create state suitable for parsing a just a p-code semantics snippet
        """
        ...

    def subTreeState(self, subtree: ghidra.app.plugin.processors.sleigh.ConstructState) -> None: ...

    def toString(self) -> unicode: ...

    @overload
    def wait(self) -> None: ...

    @overload
    def wait(self, __a0: long) -> None: ...

    @overload
    def wait(self, __a0: long, __a1: int) -> None: ...

    @property
    def addr(self) -> ghidra.program.model.address.Address: ...

    @property
    def constSpace(self) -> ghidra.program.model.address.AddressSpace: ...

    @property
    def constructor(self) -> ghidra.app.plugin.processors.sleigh.Constructor: ...

    @constructor.setter
    def constructor(self, value: ghidra.app.plugin.processors.sleigh.Constructor) -> None: ...

    @property
    def curSpace(self) -> ghidra.program.model.address.AddressSpace: ...

    @property
    def currentLength(self) -> int: ...

    @currentLength.setter
    def currentLength(self, value: int) -> None: ...

    @property
    def currentSubtableName(self) -> unicode: ...

    @property
    def flowDestAddr(self) -> ghidra.program.model.address.Address: ...

    @property
    def flowRefAddr(self) -> ghidra.program.model.address.Address: ...

    @property
    def naddr(self) -> ghidra.program.model.address.Address: ...

    @property
    def offset(self) -> None: ...  # No getter available.

    @offset.setter
    def offset(self, value: int) -> None: ...

    @property
    def operand(self) -> int: ...

    @property
    def parentHandle(self) -> ghidra.app.plugin.processors.sleigh.FixedHandle: ...

    @property
    def parserContext(self) -> ghidra.app.plugin.processors.sleigh.SleighParserContext: ...

    @property
    def state(self) -> bool: ...
