from typing import Iterator
from typing import List
import ghidra.program.model.address
import ghidra.program.model.lang
import ghidra.program.model.pcode
import ghidra.util.state
import ghidra.util.task
import java.lang
import java.util


class ResultsState(object):





    class FramePointerCandidate(object):
        assignedAt: ghidra.program.model.pcode.SequenceNumber
        register: ghidra.program.model.lang.Register
        value: ghidra.program.model.pcode.Varnode







        def equals(self, __a0: object) -> bool: ...

        def getClass(self) -> java.lang.Class: ...

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



    @overload
    def __init__(self, entryPt: ghidra.program.model.address.Address, analyzer: ghidra.util.state.FunctionAnalyzer, program: ghidra.program.model.listing.Program, maintainInstructionResults: bool, monitor: ghidra.util.task.TaskMonitor):
        """
        Constructor from a function entry point.  Program context is used to establish the entry context state.
         Analysis is performed during construction.
        @param entryPt function entry point
        @param analyzer function analysis call-back handler
        @param program program containing function
        @param maintainInstructionResults true to maintain the instruction results
        @param monitor task monitor
        @throws CancelledException
        """
        ...

    @overload
    def __init__(self, flowList: java.util.LinkedList, analyzer: ghidra.util.state.FunctionAnalyzer, entryState: ghidra.util.state.ContextState, maintainInstructionResults: bool, monitor: ghidra.util.task.TaskMonitor):
        """
        Constructor for replaying over a specified set of context states indicated via a flowList.
         Analysis is performed during construction.
        @param flowList ordered list of context state entry points
        @param analyzer function analysis call-back handler
        @param entryState context state which feeds into the first point within the flowList
        @param maintainInstructionResults
        @param monitor task monitor
        @throws CancelledException
        """
        ...



    def assume(self, register: ghidra.program.model.lang.Register, value: long) -> None:
        """
        Set an assumed register value immediately following construction and prior to flow.
        @param register (context register not permitted)
        @param value
        """
        ...

    def equals(self, __a0: object) -> bool: ...

    def getClass(self) -> java.lang.Class: ...

    def getContextStates(self, seq: ghidra.program.model.pcode.SequenceNumber) -> Iterator[ghidra.util.state.ContextState]: ...

    def getEntryPoint(self) -> ghidra.program.model.pcode.SequenceNumber:
        """
        Returns entry point associated with this results state.
        """
        ...

    def getExaminedSet(self) -> ghidra.program.model.address.AddressSetView:
        """
        Returns set of addresses analyzed with function.
         (In-line functions not included)
        """
        ...

    def getFramePointerCandidates(self) -> java.util.Collection:
        """
        Returns collection of frame pointer candidates.
        """
        ...

    def getInputRegisters(self) -> List[ghidra.program.model.lang.Register]:
        """
        Returns list of registers which are read before written.
        """
        ...

    def getModifiedRegisters(self) -> List[ghidra.program.model.lang.Register]:
        """
        Returns the set of registers which were modified
        """
        ...

    def getPreservedRegisters(self) -> List[ghidra.program.model.lang.Register]:
        """
        Returns the set of registers which were modified yet preserved.
        """
        ...

    def getReturnAddresses(self) -> java.util.Set: ...

    def getReturnValues(self, varnode: ghidra.program.model.pcode.Varnode) -> java.util.Set: ...

    @staticmethod
    def getSignedOffset(v: ghidra.program.model.pcode.Varnode) -> long: ...

    def getStackPointerVarnode(self) -> ghidra.program.model.pcode.Varnode:
        """
        @return Varnode that represents the stack pointer register
        """
        ...

    @staticmethod
    def getUnsignedOffset(v: ghidra.program.model.pcode.Varnode, size: int) -> long: ...

    def hashCode(self) -> int: ...

    def notify(self) -> None: ...

    def notifyAll(self) -> None: ...

    @staticmethod
    def simplify(pcodeOp: ghidra.program.model.pcode.PcodeOp, values: List[ghidra.program.model.pcode.Varnode], addrFactory: ghidra.program.model.address.AddressFactory, monitor: ghidra.util.task.TaskMonitor) -> ghidra.program.model.pcode.Varnode:
        """
        Generate simplified operation
        @param pcodeOp pcode operation
        @param values values associated with pcodeOp inputs
        @return operation output result or simplification of an operation.
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
    def entryPoint(self) -> ghidra.program.model.pcode.SequenceNumber: ...

    @property
    def examinedSet(self) -> ghidra.program.model.address.AddressSetView: ...

    @property
    def framePointerCandidates(self) -> java.util.Collection: ...

    @property
    def inputRegisters(self) -> List[object]: ...

    @property
    def modifiedRegisters(self) -> List[object]: ...

    @property
    def preservedRegisters(self) -> List[object]: ...

    @property
    def returnAddresses(self) -> java.util.Set: ...

    @property
    def stackPointerVarnode(self) -> ghidra.program.model.pcode.Varnode: ...
