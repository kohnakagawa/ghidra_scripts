from typing import List
import ghidra.app.plugin.processors.sleigh
import ghidra.app.plugin.processors.sleigh.symbol
import ghidra.program.model.address
import ghidra.program.model.lang
import ghidra.program.model.mem
import java.lang


class SleighParserContext(object, ghidra.program.model.lang.ParserContext):
    """
    All the recovered context for a single instruction
     The main data structure is the tree of constructors and operands
    """





    @overload
    def __init__(self, memBuf: ghidra.program.model.mem.MemBuffer, prototype: ghidra.app.plugin.processors.sleigh.SleighInstructionPrototype, processorContext: ghidra.program.model.lang.ProcessorContextView): ...

    @overload
    def __init__(self, aAddr: ghidra.program.model.address.Address, nAddr: ghidra.program.model.address.Address, rAddr: ghidra.program.model.address.Address, dAddr: ghidra.program.model.address.Address):
        """
        Constructor for building precompiled templates
        @param aAddr = address to which 'inst_start' resolves
        @param nAddr = address to which 'inst_next' resolves
        @param rAddr = special address associated with original call
        @param dAddr = destination address of original call being replaced
        """
        ...



    def addCommit(self, point: ghidra.app.plugin.processors.sleigh.ConstructState, sym: ghidra.app.plugin.processors.sleigh.symbol.TripleSymbol, num: int, mask: int) -> None: ...

    def applyCommits(self, ctx: ghidra.program.model.lang.ProcessorContext) -> None: ...

    def equals(self, __a0: object) -> bool: ...

    def getAddr(self) -> ghidra.program.model.address.Address: ...

    def getClass(self) -> java.lang.Class: ...

    def getConstSpace(self) -> ghidra.program.model.address.AddressSpace: ...

    def getContextBits(self, startbit: int, bitsize: int) -> int:
        """
        Get bits from context into an int
        @param startbit
        @param bitsize number of bits (range: 1 - 32)
        @return
        """
        ...

    @overload
    def getContextBytes(self) -> List[int]:
        """
        Get full set of context bytes.  Sleigh only supports context
         which is a multiple of 4-bytes (i.e., size of int)
        @return
        """
        ...

    @overload
    def getContextBytes(self, bytestart: int, bytesize: int) -> int:
        """
        Get bytes from context into an int
        @param bytestart
        @param bytesize number of bytes (range: 1 - 4)
        @return
        """
        ...

    def getCurSpace(self) -> ghidra.program.model.address.AddressSpace: ...

    def getFixedHandle(self, constructState: ghidra.app.plugin.processors.sleigh.ConstructState) -> ghidra.app.plugin.processors.sleigh.FixedHandle: ...

    def getFlowDestAddr(self) -> ghidra.program.model.address.Address: ...

    def getFlowRefAddr(self) -> ghidra.program.model.address.Address: ...

    def getInstructionBits(self, offset: int, startbit: int, size: int) -> int:
        """
        Get bits from the instruction stream into an int
         (packed in big endian format).  Uninitialized or
         undefined memory will return zero bit values.
        @param offset offset relative start of this context
        @param startbit
        @param size
        @return requested bit-range value
        @throws MemoryAccessException if no bytes are available at first byte when (offset+bytestart/8==0).
        """
        ...

    def getInstructionBytes(self, offset: int, bytestart: int, size: int) -> int:
        """
        Get bytes from the instruction stream into an int
         (packed in big endian format).  Uninitialized or
         undefined memory will return zero byte values.
        @param offset offset relative start of this context
        @param bytestart pattern byte offset relative to specified context offset
        @param size
        @return requested byte-range value
        @throws MemoryAccessException if no bytes are available at first byte when (offset+bytestart==0).
        """
        ...

    def getMemBuffer(self) -> ghidra.program.model.mem.MemBuffer: ...

    def getNaddr(self) -> ghidra.program.model.address.Address: ...

    def getPrototype(self) -> ghidra.app.plugin.processors.sleigh.SleighInstructionPrototype: ...

    def hashCode(self) -> int: ...

    def isValid(self, buf: ghidra.program.model.mem.MemBuffer) -> bool: ...

    def notify(self) -> None: ...

    def notifyAll(self) -> None: ...

    def setContextWord(self, i: int, val: int, mask: int) -> None: ...

    def setDelaySlotLength(self, delayByteLength: int) -> None: ...

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
    def contextBytes(self) -> List[int]: ...

    @property
    def curSpace(self) -> ghidra.program.model.address.AddressSpace: ...

    @property
    def delaySlotLength(self) -> None: ...  # No getter available.

    @delaySlotLength.setter
    def delaySlotLength(self, value: int) -> None: ...

    @property
    def flowDestAddr(self) -> ghidra.program.model.address.Address: ...

    @property
    def flowRefAddr(self) -> ghidra.program.model.address.Address: ...

    @property
    def memBuffer(self) -> ghidra.program.model.mem.MemBuffer: ...

    @property
    def naddr(self) -> ghidra.program.model.address.Address: ...

    @property
    def prototype(self) -> ghidra.app.plugin.processors.sleigh.SleighInstructionPrototype: ...
