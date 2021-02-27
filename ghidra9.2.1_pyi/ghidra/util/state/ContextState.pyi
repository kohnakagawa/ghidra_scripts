from typing import List
import ghidra.program.model.lang
import ghidra.program.model.listing
import ghidra.program.model.pcode
import ghidra.util.state
import ghidra.util.task
import java.lang
import java.util


class ContextState(object):




    @overload
    def __init__(self, entryPt: ghidra.program.model.address.Address, program: ghidra.program.model.listing.Program):
        """
        Constructs an empty state.
        @param entryPt the entry point for the context state
        @param program the program
        """
        ...

    @overload
    def __init__(self, pcodeEntry: ghidra.program.model.pcode.SequenceNumber, previousState: ghidra.util.state.ContextState):
        """
        Derive a new context state from an initial state
        @param pcodeEntry the pcode entry sequence number
        @param previousState previous context state flowing into the specified pcode location
        """
        ...

    @overload
    def __init__(self, entryPt: ghidra.program.model.address.Address, programCtx: ghidra.program.model.listing.ProgramContext, program: ghidra.program.model.listing.Program):
        """
        Constructs an empty state.
        @param entryPt the entry point for the context state
        @param programCtx initial program context or null
        @param program the program
        """
        ...



    def branchState(self, pcodeEntry: ghidra.program.model.pcode.SequenceNumber) -> ghidra.util.state.ContextState:
        """
        Branch the current state.  The current state should be associated with
         branch target, the returned state should be used for the fall-through flow.
        @return
        """
        ...

    def clearUniqueState(self) -> java.util.HashMap:
        """
        When done processing a particular instruction, this method should be invoked to
         clear any unique Varnode state.
        @return previous unique state
        """
        ...

    def equals(self, __a0: object) -> bool: ...

    @overload
    def get(self, varnode: ghidra.program.model.pcode.Varnode) -> ghidra.program.model.pcode.Varnode:
        """
        Retrieve the value/operation stored in the specified addressable location (address or register varnode).
         If varnode is a constant, the input argument will be returned.
         Unique varnodes not permitted once locked.
        @param varnode identifies constant or storage (constant, address, register or unique), if VarnodeOperation
         specified null will always be returned.
        @return stored value/operation
        """
        ...

    @overload
    def get(self, varnode: ghidra.program.model.pcode.Varnode, monitor: ghidra.util.task.TaskMonitor) -> ghidra.program.model.pcode.Varnode:
        """
        Retrieve the value/operation stored in the specified addressable location (address or register varnode).
         If varnode is a constant, the input argument will be returned.
         Unique varnodes not permitted once locked.
        @param varnode identifies constant or storage (constant, address, register or unique), if VarnodeOperation
         specified null will always be returned.
        @return stored value/operation
        """
        ...

    @overload
    def get(self, spaceID: int, offsetValue: ghidra.program.model.pcode.Varnode, size: int) -> ghidra.program.model.pcode.Varnode:
        """
        Retrieve the value/operation stored within the specified space using an offset
         identified by a value/operation.
        @param spaceID
        @param offsetValue
        @param size
        @return stored value/operation or null or DUMMY_BYTE_VARNODE
        """
        ...

    @overload
    def get(self, spaceID: int, offsetValue: ghidra.program.model.pcode.Varnode, size: int, monitor: ghidra.util.task.TaskMonitor) -> ghidra.program.model.pcode.Varnode:
        """
        Retrieve the value/operation stored within the specified space using an offset
         identified by a value/operation.
        @param spaceID
        @param offsetValue
        @param size
        @return stored value/operation or null or DUMMY_BYTE_VARNODE
        """
        ...

    def getClass(self) -> java.lang.Class: ...

    def getDifferingRegisters(self, other: ghidra.util.state.ContextState) -> List[ghidra.program.model.lang.Register]: ...

    def getEntryPoint(self) -> ghidra.program.model.pcode.SequenceNumber:
        """
        Returns the point at which the state was instantiated.
        """
        ...

    def getExitPoint(self) -> ghidra.program.model.pcode.SequenceNumber: ...

    def getFlowFroms(self) -> java.util.Set: ...

    def getPreviousContextState(self) -> ghidra.util.state.ContextState:
        """
        Returns previous ContextState which flowed into this one.
        """
        ...

    def getProgram(self) -> ghidra.program.model.listing.Program:
        """
        Returns program associated with this context state
        """
        ...

    def getSequenceRange(self) -> ghidra.util.state.SequenceRange: ...

    def hasDifferingRegisters(self, other: ghidra.util.state.ContextState) -> bool: ...

    def hashCode(self) -> int: ...

    def isFlowFrom(self, seq: ghidra.program.model.pcode.SequenceNumber) -> bool: ...

    def lock(self) -> None:
        """
        When no longer updating this state, this method should be invoked to
         cleanup resources no longer needed (e.g., uniqueState no longer
         maintained).
        """
        ...

    def notify(self) -> None: ...

    def notifyAll(self) -> None: ...

    def setDebugVarnod(self, varnode: ghidra.program.model.pcode.Varnode) -> None:
        """
        Set a varnode to be debugged.  This will be passed to any states
         derived from this state.
        @param varnode varnode to be debugged
        """
        ...

    @overload
    def store(self, addressVarnode: ghidra.program.model.pcode.Varnode, storedValue: ghidra.program.model.pcode.Varnode) -> None:
        """
        Store a value.  Unique varnodes not permitted once locked.
        @param addressVarnode identifies storage (address, register or unique)
        @param storedValue constant or OperationVarnode
        """
        ...

    @overload
    def store(self, spaceID: int, offsetValue: ghidra.program.model.pcode.Varnode, storedValue: ghidra.program.model.pcode.Varnode, size: int) -> bool: ...

    def toString(self) -> unicode: ...

    @overload
    def wait(self) -> None: ...

    @overload
    def wait(self, __a0: long) -> None: ...

    @overload
    def wait(self, __a0: long, __a1: int) -> None: ...

    @property
    def debugVarnod(self) -> None: ...  # No getter available.

    @debugVarnod.setter
    def debugVarnod(self, value: ghidra.program.model.pcode.Varnode) -> None: ...

    @property
    def entryPoint(self) -> ghidra.program.model.pcode.SequenceNumber: ...

    @property
    def exitPoint(self) -> ghidra.program.model.pcode.SequenceNumber: ...

    @property
    def flowFroms(self) -> java.util.Set: ...

    @property
    def previousContextState(self) -> ghidra.util.state.ContextState: ...

    @property
    def program(self) -> ghidra.program.model.listing.Program: ...

    @property
    def sequenceRange(self) -> ghidra.util.state.SequenceRange: ...
