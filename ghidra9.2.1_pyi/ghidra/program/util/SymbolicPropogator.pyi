import ghidra.program.model.address
import ghidra.program.model.lang
import ghidra.program.model.listing
import ghidra.program.model.pcode
import ghidra.program.model.symbol
import ghidra.program.util
import ghidra.program.util.SymbolicPropogator
import ghidra.util.task
import java.lang


class SymbolicPropogator(object):





    class Value(object):








        def equals(self, __a0: object) -> bool: ...

        def getClass(self) -> java.lang.Class: ...

        def getRelativeRegister(self) -> ghidra.program.model.lang.Register: ...

        def getValue(self) -> long: ...

        def hashCode(self) -> int: ...

        def isRegisterRelativeValue(self) -> bool: ...

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
        def registerRelativeValue(self) -> bool: ...

        @property
        def relativeRegister(self) -> ghidra.program.model.lang.Register: ...

        @property
        def value(self) -> long: ...

    def __init__(self, program: ghidra.program.model.listing.Program): ...



    def encounteredBranch(self) -> bool:
        """
        @return true if any branching instructions have been encountered
        """
        ...

    def equals(self, __a0: object) -> bool: ...

    @overload
    def flowConstants(self, startAddr: ghidra.program.model.address.Address, restrictSet: ghidra.program.model.address.AddressSetView, eval: ghidra.program.util.ContextEvaluator, saveContext: bool, monitor: ghidra.util.task.TaskMonitor) -> ghidra.program.model.address.AddressSet:
        """
        Process a subroutine using the processor function.
         The process function can control what flows are followed and when to stop.
        @param startAddr start address
        @param restrictSet the address set to restrict the constant flow to
        @param eval the context evaluator to use
        @param saveContext true if the context should be saved
        @param monitor the task monitor
        @return the address set of instructions that were followed
        @throws CancelledException if the task is cancelled
        """
        ...

    @overload
    def flowConstants(self, startAddr: ghidra.program.model.address.Address, restrictSet: ghidra.program.model.address.AddressSetView, eval: ghidra.program.util.ContextEvaluator, vContext: ghidra.program.util.VarnodeContext, monitor: ghidra.util.task.TaskMonitor) -> ghidra.program.model.address.AddressSet: ...

    @overload
    def flowConstants(self, fromAddr: ghidra.program.model.address.Address, startAddr: ghidra.program.model.address.Address, restrictSet: ghidra.program.model.address.AddressSetView, eval: ghidra.program.util.ContextEvaluator, vContext: ghidra.program.util.VarnodeContext, monitor: ghidra.util.task.TaskMonitor) -> ghidra.program.model.address.AddressSet: ...

    def getClass(self) -> java.lang.Class: ...

    def getRegisterValue(self, toAddr: ghidra.program.model.address.Address, reg: ghidra.program.model.lang.Register) -> ghidra.program.util.SymbolicPropogator.Value:
        """
        Get constant or register relative value assigned to the
         specified register at the specified address
        @param toAddr address
        @param reg register
        @return register value
        """
        ...

    def getRegisterValueRepresentation(self, addr: ghidra.program.model.address.Address, reg: ghidra.program.model.lang.Register) -> unicode:
        """
        Do not depend on this method!  For display debugging purposes only.
         This will change.
        @param addr
        @param reg
        @return
        """
        ...

    def hashCode(self) -> int: ...

    @overload
    def makeReference(self, varnodeContext: ghidra.program.util.VarnodeContext, instruction: ghidra.program.model.listing.Instruction, pcodeop: int, opIndex: int, vt: ghidra.program.model.pcode.Varnode, refType: ghidra.program.model.symbol.RefType, monitor: ghidra.util.task.TaskMonitor) -> None:
        """
        Make from the instruction to the reference based on the varnode passed in.
        @param varnodeContext - context to use for any other infomation needed
        @param instruction - instruction to place the reference on.
        @param pcodeop - pcode op that caused the reference
        @param opIndex - operand it should be placed on, or -1 if unknown
        @param vt - place to reference, could be a full address, or just a constant
        @param refType - type of reference
        @param monitor
        """
        ...

    @overload
    def makeReference(self, vContext: ghidra.program.util.VarnodeContext, instruction: ghidra.program.model.listing.Instruction, opIndex: int, knownSpaceID: long, wordOffset: long, size: int, refType: ghidra.program.model.symbol.RefType, pcodeop: int, knownReference: bool, monitor: ghidra.util.task.TaskMonitor) -> None:
        """
        Make a reference from the instruction to the address based on the spaceID,offset passed in.
           This could make a reference into an overlay (overriding the spaceID), or into memory, if
           spaceID is a constant space.
          The target could be an external Address carried along and then finally used.
          External addresses are OK as long as nothing is done to the offset.
        @param vContext - context to use for any other infomation needed
        @param instruction - instruction to place the reference on.
        @param opIndex - operand it should be placed on, or -1 if unknown
        @param knownSpaceID target space ID or -1 if only offset is known
        @param wordOffset - target offset that is word addressing based
        @param refType - type of reference
        @param pcodeop - pcode op that caused the reference
        @param monitor - the task monitor
        """
        ...

    def notify(self) -> None: ...

    def notifyAll(self) -> None: ...

    def readExecutable(self) -> bool:
        """
        @return return true if the code ever read from an executable location
        """
        ...

    def setDebug(self, debug: bool) -> None: ...

    def setParamRefCheck(self, checkParamRefsOption: bool) -> None:
        """
        enable/disable checking parameters for constant references
        @param checkParamRefsOption true to enable
        """
        ...

    def setRegister(self, addr: ghidra.program.model.address.Address, stackReg: ghidra.program.model.lang.Register) -> None: ...

    def setReturnRefCheck(self, checkReturnRefsOption: bool) -> None:
        """
        enable/disable checking return for constant references
        @param checkReturnRefsOption
        """
        ...

    def setStoredRefCheck(self, checkStoredRefsOption: bool) -> None:
        """
        enable/disable checking stored values for constant references
        @param checkStoredRefsOption
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
    def debug(self) -> None: ...  # No getter available.

    @debug.setter
    def debug(self, value: bool) -> None: ...

    @property
    def paramRefCheck(self) -> None: ...  # No getter available.

    @paramRefCheck.setter
    def paramRefCheck(self, value: bool) -> None: ...

    @property
    def returnRefCheck(self) -> None: ...  # No getter available.

    @returnRefCheck.setter
    def returnRefCheck(self, value: bool) -> None: ...

    @property
    def storedRefCheck(self) -> None: ...  # No getter available.

    @storedRefCheck.setter
    def storedRefCheck(self, value: bool) -> None: ...
