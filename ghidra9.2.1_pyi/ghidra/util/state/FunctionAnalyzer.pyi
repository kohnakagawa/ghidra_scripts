from typing import List
import ghidra.program.model.address
import ghidra.program.model.pcode
import ghidra.program.model.symbol
import ghidra.util.state
import ghidra.util.task
import java.lang


class FunctionAnalyzer(object):








    def dataReference(self, op: ghidra.program.model.pcode.PcodeOp, instrOpIndex: int, storageVarnode: ghidra.program.model.pcode.Varnode, refType: ghidra.program.model.symbol.RefType, monitor: ghidra.util.task.TaskMonitor) -> None:
        """
        Callback indicating that an absolute memory reference was encountered
        @param op pcode operation
        @param instrOpIndex opIndex associated with reference or -1 if it could not be determined
        @param storageVarnode absolute storage Varnode
        @param refType read/write/data reference type
        @param monitor task monitor
        @throws CancelledException if callback canceled by monitor
        """
        ...

    def equals(self, __a0: object) -> bool: ...

    def getClass(self) -> java.lang.Class: ...

    def hashCode(self) -> int: ...

    def indirectDataReference(self, op: ghidra.program.model.pcode.PcodeOp, instrOpIndex: int, offsetVarnode: ghidra.program.model.pcode.Varnode, size: int, storageSpaceID: int, refType: ghidra.program.model.symbol.RefType, monitor: ghidra.util.task.TaskMonitor) -> None:
        """
        Callback indicating that an indirect/computed memory reference was encountered using an indirect/computed offset
        @param op pcode operation
        @param instrOpIndex opIndex associated with reference or -1 if it could not be determined
        @param offsetVarnode indirect/computed offset
        @param size access size or -1 if not applicable
        @param storageSpaceID storage space ID
        @param refType read/write/data reference type
        @param monitor task monitor
        @throws CancelledException if callback canceled by monitor
        """
        ...

    def notify(self) -> None: ...

    def notifyAll(self) -> None: ...

    def resolvedFlow(self, op: ghidra.program.model.pcode.PcodeOp, instrOpIndex: int, destAddr: ghidra.program.model.address.Address, currentState: ghidra.util.state.ContextState, results: ghidra.util.state.ResultsState, monitor: ghidra.util.task.TaskMonitor) -> bool:
        """
        Callback indicating that a call/branch destination was identified.
         Analyzer should create reference if appropriate
         Keep in mind that there could be other unidentified destinations.
        @param op branch or call flow operation
        @param instrOpIndex opIndex associated with reference or -1 if it could not be determined
        @param destAddr destination address
        @param results contains previous states leading upto the currentState
        @param currentState current state at the branch/call
        @param monitor task monitor
        @return true if destination should be disassembled if not already
        @throws CancelledException if callback canceled by monitor
        """
        ...

    @overload
    def stackReference(self, op: ghidra.program.model.pcode.PcodeOp, instrOpIndex: int, stackOffset: int, size: int, storageSpaceID: int, refType: ghidra.program.model.symbol.RefType, monitor: ghidra.util.task.TaskMonitor) -> None:
        """
        Callback indicating that an absolute stack reference was encountered.  A non-load/store
         operation will have a -1 for both storageSpaceId and size.
        @param op pcode operation
        @param instrOpIndex opIndex associated with reference or -1 if it could not be determined
        @param stackOffset stack offset
        @param size access size or -1 if not applicable
        @param storageSpaceID storage space ID or -1 if not applicable
        @param refType read/write/data reference type
        @param monitor task monitor
        @throws CancelledException if callback canceled by monitor
        """
        ...

    @overload
    def stackReference(self, op: ghidra.program.model.pcode.PcodeOp, instrOpIndex: int, computedStackOffset: ghidra.util.state.VarnodeOperation, size: int, storageSpaceID: int, refType: ghidra.program.model.symbol.RefType, monitor: ghidra.util.task.TaskMonitor) -> None:
        """
        Callback indicating that a computed stack reference was encountered.  A non-load/store
         operation will have a -1 for both storageSpaceId and size.
        @param op pcode operation
        @param instrOpIndex opIndex associated with reference or -1 if it could not be determined
        @param computedStackOffset stack offset computation (i.e., VarnodeOperation w/ stack pointer)
        @param size access size or -1 if not applicable
        @param storageSpaceID storage space ID or -1 if not applicable
        @param refType read/write/data reference type
        @param monitor task monitor
        @throws CancelledException if callback canceled by monitor
        """
        ...

    def toString(self) -> unicode: ...

    def unresolvedIndirectFlow(self, op: ghidra.program.model.pcode.PcodeOp, instrOpIndex: int, destination: ghidra.program.model.pcode.Varnode, currentState: ghidra.util.state.ContextState, results: ghidra.util.state.ResultsState, monitor: ghidra.util.task.TaskMonitor) -> List[ghidra.program.model.address.Address]:
        """
        Callback indicating that a computed call/branch destination was not resolved.
        @param op indirect branch or call flow operation
        @param instrOpIndex opIndex associated with reference or -1 if it could not be determined
        @param destination destination identified as a Varnode (may be an expression represented by
         a {@link VarnodeOperation}
        @param results contains previous states leading upto the currentState
        @param currentState current state at the branch/call
        @param monitor task monitor
        @return list of resolved destinations which should be used or null.  List of destination
         addresses will trigger disassembly where necessary.
        @throws CancelledException if callback cancelled by monitor
        """
        ...

    @overload
    def wait(self) -> None: ...

    @overload
    def wait(self, __a0: long) -> None: ...

    @overload
    def wait(self, __a0: long, __a1: int) -> None: ...
