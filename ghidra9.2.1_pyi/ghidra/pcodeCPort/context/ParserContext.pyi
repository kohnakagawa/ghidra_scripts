from typing import List
import ghidra.pcodeCPort.address
import ghidra.pcodeCPort.context
import ghidra.pcodeCPort.slghsymbol
import ghidra.pcodeCPort.space
import java.lang


class ParserContext(object):





    class ContextState(java.lang.Enum):
        disassembly: ghidra.pcodeCPort.context.ParserContext.ContextState = disassembly
        pcode: ghidra.pcodeCPort.context.ParserContext.ContextState = pcode
        uninitialized: ghidra.pcodeCPort.context.ParserContext.ContextState = uninitialized







        @overload
        def compareTo(self, __a0: java.lang.Enum) -> int: ...

        @overload
        def compareTo(self, __a0: object) -> int: ...

        def equals(self, __a0: object) -> bool: ...

        def getClass(self) -> java.lang.Class: ...

        def getDeclaringClass(self) -> java.lang.Class: ...

        def hashCode(self) -> int: ...

        def name(self) -> unicode: ...

        def notify(self) -> None: ...

        def notifyAll(self) -> None: ...

        def ordinal(self) -> int: ...

        def toString(self) -> unicode: ...

        @overload
        @staticmethod
        def valueOf(__a0: unicode) -> ghidra.pcodeCPort.context.ParserContext.ContextState: ...

        @overload
        @staticmethod
        def valueOf(__a0: java.lang.Class, __a1: unicode) -> java.lang.Enum: ...

        @staticmethod
        def values() -> List[ghidra.pcodeCPort.context.ParserContext.ContextState]: ...

        @overload
        def wait(self) -> None: ...

        @overload
        def wait(self, __a0: long) -> None: ...

        @overload
        def wait(self, __a0: long, __a1: int) -> None: ...



    def __init__(self, __a0: ghidra.pcodeCPort.globalcontext.ContextCache): ...



    def addCommit(self, __a0: ghidra.pcodeCPort.slghsymbol.TripleSymbol, __a1: int, __a2: int, __a3: bool, __a4: ghidra.pcodeCPort.context.ConstructState) -> None: ...

    def allocateOperand(self, __a0: int, __a1: ghidra.pcodeCPort.context.ParserWalkerChange) -> None: ...

    def applyCommits(self) -> None: ...

    def clearCommits(self) -> None: ...

    def deallocateState(self, __a0: ghidra.pcodeCPort.context.ParserWalkerChange) -> None: ...

    def dispose(self) -> None: ...

    def equals(self, __a0: object) -> bool: ...

    def getAddr(self) -> ghidra.pcodeCPort.address.Address: ...

    def getBuffer(self) -> List[int]: ...

    def getClass(self) -> java.lang.Class: ...

    def getConstSpace(self) -> ghidra.pcodeCPort.space.AddrSpace: ...

    def getContextBits(self, __a0: int, __a1: int) -> int: ...

    def getContextBytes(self, __a0: int, __a1: int) -> int: ...

    def getCurSpace(self) -> ghidra.pcodeCPort.space.AddrSpace: ...

    def getDelaySlot(self) -> int: ...

    def getFlowDestAddr(self) -> ghidra.pcodeCPort.address.Address: ...

    def getFlowRefAddr(self) -> ghidra.pcodeCPort.address.Address: ...

    def getInstructionBits(self, __a0: int, __a1: int, __a2: int) -> int: ...

    def getInstructionBytes(self, __a0: int, __a1: int, __a2: int) -> int: ...

    def getLength(self) -> int: ...

    def getNaddr(self) -> ghidra.pcodeCPort.address.Address: ...

    def getParserState(self) -> ghidra.pcodeCPort.context.ParserContext.ContextState: ...

    def hashCode(self) -> int: ...

    def initialize(self, __a0: int, __a1: int, __a2: ghidra.pcodeCPort.space.AddrSpace) -> None: ...

    def loadContext(self) -> None: ...

    def notify(self) -> None: ...

    def notifyAll(self) -> None: ...

    def setAddr(self, __a0: ghidra.pcodeCPort.address.Address) -> None: ...

    def setContextWord(self, __a0: int, __a1: int, __a2: int) -> None: ...

    def setDelaySlot(self, __a0: int) -> None: ...

    def setNaddr(self, __a0: ghidra.pcodeCPort.address.Address) -> None: ...

    def setOffsetOutOfBand(self, __a0: ghidra.pcodeCPort.slghsymbol.Constructor, __a1: int) -> None: ...

    def setParserState(self, __a0: ghidra.pcodeCPort.context.ParserContext.ContextState) -> None: ...

    def toString(self) -> unicode: ...

    @overload
    def wait(self) -> None: ...

    @overload
    def wait(self, __a0: long) -> None: ...

    @overload
    def wait(self, __a0: long, __a1: int) -> None: ...

    @property
    def addr(self) -> ghidra.pcodeCPort.address.Address: ...

    @addr.setter
    def addr(self, value: ghidra.pcodeCPort.address.Address) -> None: ...

    @property
    def buffer(self) -> List[int]: ...

    @property
    def constSpace(self) -> ghidra.pcodeCPort.space.AddrSpace: ...

    @property
    def curSpace(self) -> ghidra.pcodeCPort.space.AddrSpace: ...

    @property
    def delaySlot(self) -> int: ...

    @delaySlot.setter
    def delaySlot(self, value: int) -> None: ...

    @property
    def flowDestAddr(self) -> ghidra.pcodeCPort.address.Address: ...

    @property
    def flowRefAddr(self) -> ghidra.pcodeCPort.address.Address: ...

    @property
    def length(self) -> int: ...

    @property
    def naddr(self) -> ghidra.pcodeCPort.address.Address: ...

    @naddr.setter
    def naddr(self, value: ghidra.pcodeCPort.address.Address) -> None: ...

    @property
    def parserState(self) -> ghidra.pcodeCPort.context.ParserContext.ContextState: ...

    @parserState.setter
    def parserState(self, value: ghidra.pcodeCPort.context.ParserContext.ContextState) -> None: ...
