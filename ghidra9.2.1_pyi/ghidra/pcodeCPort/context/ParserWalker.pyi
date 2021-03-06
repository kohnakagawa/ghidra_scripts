import ghidra.pcodeCPort.address
import ghidra.pcodeCPort.context
import ghidra.pcodeCPort.slghsymbol
import ghidra.pcodeCPort.space
import java.lang


class ParserWalker(object):




    def __init__(self, __a0: ghidra.pcodeCPort.context.ParserContext): ...



    def baseState(self) -> None: ...

    def equals(self, __a0: object) -> bool: ...

    def getAddr(self) -> ghidra.pcodeCPort.address.Address: ...

    def getClass(self) -> java.lang.Class: ...

    def getConstSpace(self) -> ghidra.pcodeCPort.space.AddrSpace: ...

    def getConstructor(self) -> ghidra.pcodeCPort.slghsymbol.Constructor: ...

    def getContextBits(self, __a0: int, __a1: int) -> int: ...

    def getContextBytes(self, __a0: int, __a1: int) -> int: ...

    def getCurSpace(self) -> ghidra.pcodeCPort.space.AddrSpace: ...

    def getFixedHandle(self, __a0: int) -> ghidra.pcodeCPort.context.FixedHandle: ...

    def getFlowDestAddr(self) -> ghidra.pcodeCPort.address.Address: ...

    def getFlowRefAddr(self) -> ghidra.pcodeCPort.address.Address: ...

    def getInstructionBits(self, __a0: int, __a1: int) -> int: ...

    def getInstructionBytes(self, __a0: int, __a1: int) -> int: ...

    def getLength(self) -> int: ...

    def getNaddr(self) -> ghidra.pcodeCPort.address.Address: ...

    def getOffset(self, __a0: int) -> int: ...

    def getOperand(self) -> int: ...

    def getParentHandle(self) -> ghidra.pcodeCPort.context.FixedHandle: ...

    def getParserContext(self) -> ghidra.pcodeCPort.context.ParserContext: ...

    def hashCode(self) -> int: ...

    def isState(self) -> bool: ...

    def notify(self) -> None: ...

    def notifyAll(self) -> None: ...

    def popOperand(self) -> None: ...

    def pushOperand(self, __a0: int) -> None: ...

    def setOutOfBandState(self, __a0: ghidra.pcodeCPort.slghsymbol.Constructor, __a1: int, __a2: ghidra.pcodeCPort.context.ConstructState, __a3: ghidra.pcodeCPort.context.ParserWalker) -> None: ...

    def toString(self) -> unicode: ...

    @overload
    def wait(self) -> None: ...

    @overload
    def wait(self, __a0: long) -> None: ...

    @overload
    def wait(self, __a0: long, __a1: int) -> None: ...

    @property
    def addr(self) -> ghidra.pcodeCPort.address.Address: ...

    @property
    def constSpace(self) -> ghidra.pcodeCPort.space.AddrSpace: ...

    @property
    def constructor(self) -> ghidra.pcodeCPort.slghsymbol.Constructor: ...

    @property
    def curSpace(self) -> ghidra.pcodeCPort.space.AddrSpace: ...

    @property
    def flowDestAddr(self) -> ghidra.pcodeCPort.address.Address: ...

    @property
    def flowRefAddr(self) -> ghidra.pcodeCPort.address.Address: ...

    @property
    def length(self) -> int: ...

    @property
    def naddr(self) -> ghidra.pcodeCPort.address.Address: ...

    @property
    def operand(self) -> int: ...

    @property
    def parentHandle(self) -> ghidra.pcodeCPort.context.FixedHandle: ...

    @property
    def parserContext(self) -> ghidra.pcodeCPort.context.ParserContext: ...

    @property
    def state(self) -> bool: ...
