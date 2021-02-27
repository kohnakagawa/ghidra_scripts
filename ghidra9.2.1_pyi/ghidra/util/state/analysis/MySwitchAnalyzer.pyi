from typing import List
import ghidra.program.model.address
import ghidra.program.model.listing
import ghidra.program.model.pcode
import ghidra.program.model.symbol
import ghidra.util.state
import ghidra.util.task
import java.lang


class MySwitchAnalyzer(object, ghidra.util.state.FunctionAnalyzer):




    def __init__(self, program: ghidra.program.model.listing.Program): ...



    @staticmethod
    def analyze(program: ghidra.program.model.listing.Program, functionEntry: ghidra.program.model.address.Address, monitor: ghidra.util.task.TaskMonitor) -> ghidra.util.state.ResultsState: ...

    def dataReference(self, op: ghidra.program.model.pcode.PcodeOp, instrOpIndex: int, storageVarnode: ghidra.program.model.pcode.Varnode, refType: ghidra.program.model.symbol.RefType, monitor: ghidra.util.task.TaskMonitor) -> None: ...

    def equals(self, __a0: object) -> bool: ...

    def getClass(self) -> java.lang.Class: ...

    def hashCode(self) -> int: ...

    def indirectDataReference(self, op: ghidra.program.model.pcode.PcodeOp, instrOpIndex: int, offsetVarnode: ghidra.program.model.pcode.Varnode, size: int, storageSpaceID: int, refType: ghidra.program.model.symbol.RefType, monitor: ghidra.util.task.TaskMonitor) -> None: ...

    def notify(self) -> None: ...

    def notifyAll(self) -> None: ...

    @overload
    def resolvedFlow(self, op: ghidra.program.model.pcode.PcodeOp, instrOpIndex: int, destAddr: ghidra.program.model.address.Address, currentState: ghidra.util.state.ContextState, results: ghidra.util.state.ResultsState, monitor: ghidra.util.task.TaskMonitor) -> bool: ...

    @overload
    def resolvedFlow(self, op: ghidra.program.model.pcode.PcodeOp, opIndex: object, destAddr: ghidra.program.model.address.Address, currentState: ghidra.util.state.ContextState, results: ghidra.util.state.ResultsState, monitor: ghidra.util.task.TaskMonitor) -> bool: ...

    @overload
    def stackReference(self, op: ghidra.program.model.pcode.PcodeOp, instrOpIndex: int, stackOffset: int, size: int, storageSpaceID: int, refType: ghidra.program.model.symbol.RefType, monitor: ghidra.util.task.TaskMonitor) -> None: ...

    @overload
    def stackReference(self, op: ghidra.program.model.pcode.PcodeOp, instrOpIndex: int, computedStackOffset: ghidra.util.state.VarnodeOperation, size: int, storageSpaceID: int, refType: ghidra.program.model.symbol.RefType, monitor: ghidra.util.task.TaskMonitor) -> None: ...

    def toString(self) -> unicode: ...

    @overload
    def unresolvedIndirectFlow(self, op: ghidra.program.model.pcode.PcodeOp, instrOpIndex: int, destination: ghidra.program.model.pcode.Varnode, currentState: ghidra.util.state.ContextState, results: ghidra.util.state.ResultsState, monitor: ghidra.util.task.TaskMonitor) -> List[ghidra.program.model.address.Address]: ...

    @overload
    def unresolvedIndirectFlow(self, op: ghidra.program.model.pcode.PcodeOp, opIndex: object, destination: ghidra.program.model.pcode.Varnode, currentState: ghidra.util.state.ContextState, results: ghidra.util.state.ResultsState, monitor: ghidra.util.task.TaskMonitor) -> List[ghidra.program.model.address.Address]: ...

    @overload
    def wait(self) -> None: ...

    @overload
    def wait(self, __a0: long) -> None: ...

    @overload
    def wait(self, __a0: long, __a1: int) -> None: ...
