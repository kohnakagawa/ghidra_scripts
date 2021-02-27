from typing import List
import ghidra.app.emulator
import ghidra.app.emulator.memory
import ghidra.app.emulator.state
import ghidra.app.plugin.processors.sleigh
import ghidra.pcode.emulate
import ghidra.pcode.memstate
import ghidra.program.model.address
import ghidra.program.model.lang
import ghidra.util.task
import java.lang
import java.util


class Emulator(object):




    def __init__(self, cfg: ghidra.app.emulator.EmulatorConfiguration): ...



    def addMemoryAccessFilter(self, filter: ghidra.app.emulator.MemoryAccessFilter) -> None: ...

    def addProvider(self, provider: ghidra.app.emulator.memory.MemoryLoadImage, view: ghidra.program.model.address.AddressSetView) -> None:
        """
        Add memory load image provider
        @param provider memory load image provider
        @param view memory region which corresponds to provider
        """
        ...

    def cloneMemory(self) -> ghidra.pcode.memstate.MemoryState: ...

    def disassemble(self, count: int) -> List[unicode]:
        """
        Disassemble from the current execute address
        @param count number of contiguous instructions to disassemble
        @return list of instructions
        """
        ...

    def dispose(self) -> None: ...

    def equals(self, __a0: object) -> bool: ...

    def executeInstruction(self, stopAtBreakpoint: bool, monitor: ghidra.util.task.TaskMonitor) -> None: ...

    def genAddress(self, addr: unicode) -> ghidra.program.model.address.Address: ...

    def getBreakTable(self) -> ghidra.pcode.emulate.BreakTableCallBack: ...

    def getClass(self) -> java.lang.Class: ...

    def getContextRegisterValue(self) -> ghidra.program.model.lang.RegisterValue:
        """
        Returns the current context register value.  The context value returned reflects
         its state when the previously executed instruction was
         parsed/executed.  The context value returned will feed into the next
         instruction to be parsed with its non-flowing bits cleared and
         any future context state merged in.
        @return context as a RegisterValue object
        """
        ...

    def getDefaultContext(self) -> java.util.Set: ...

    def getEmulateExecutionState(self) -> ghidra.pcode.emulate.EmulateExecutionState:
        """
        @return emulator execution state.  This can be useful within a memory fault handler to
         determine if a memory read was associated with instruction parsing (i.e., PCODE_EMIT) or
         normal an actual emulated read (i.e., EXECUTE).
        """
        ...

    def getExecuteAddress(self) -> ghidra.program.model.address.Address: ...

    def getFilteredMemState(self) -> ghidra.app.emulator.FilteredMemoryState: ...

    def getHalt(self) -> bool: ...

    def getLanguage(self) -> ghidra.app.plugin.processors.sleigh.SleighLanguage: ...

    def getLastExecuteAddress(self) -> ghidra.program.model.address.Address: ...

    def getMemState(self) -> ghidra.pcode.memstate.MemoryState: ...

    def getMemoryBank(self, space: ghidra.program.model.address.AddressSpace, ps: int) -> ghidra.app.emulator.state.FilteredMemoryPageOverlay: ...

    def getPC(self) -> long: ...

    def getPCRegisterName(self) -> unicode: ...

    def getTickCount(self) -> int: ...

    def hashCode(self) -> int: ...

    def isAtBreakpoint(self) -> bool:
        """
        @return true if halted at a breakpoint
        """
        ...

    def isExecuting(self) -> bool:
        """
        @return true if emulator is busy executing an instruction
        """
        ...

    def notify(self) -> None: ...

    def notifyAll(self) -> None: ...

    def setContextRegisterValue(self, regValue: ghidra.program.model.lang.RegisterValue) -> None:
        """
        Sets the context register value at the current execute address.
         The Emulator should not be running when this method is invoked.
         Only flowing context bits should be set, as non-flowing bits
         will be cleared prior to parsing on instruction.  In addition,
         any future context state set by the pcode emitter will
         take precedence over context set using this method.  This method
         is primarily intended to be used to establish the initial
         context state.
        @param regValue is the value to set context to
        """
        ...

    def setExecuteAddress(self, addressableWordOffset: long) -> None: ...

    def setHalt(self, halt: bool) -> None: ...

    def toString(self) -> unicode: ...

    @overload
    def wait(self) -> None: ...

    @overload
    def wait(self, __a0: long) -> None: ...

    @overload
    def wait(self, __a0: long, __a1: int) -> None: ...

    @property
    def PC(self) -> long: ...

    @property
    def PCRegisterName(self) -> unicode: ...

    @property
    def atBreakpoint(self) -> bool: ...

    @property
    def breakTable(self) -> ghidra.pcode.emulate.BreakTableCallBack: ...

    @property
    def contextRegisterValue(self) -> ghidra.program.model.lang.RegisterValue: ...

    @contextRegisterValue.setter
    def contextRegisterValue(self, value: ghidra.program.model.lang.RegisterValue) -> None: ...

    @property
    def defaultContext(self) -> java.util.Set: ...

    @property
    def emulateExecutionState(self) -> ghidra.pcode.emulate.EmulateExecutionState: ...

    @property
    def executeAddress(self) -> ghidra.program.model.address.Address: ...

    @property
    def executing(self) -> bool: ...

    @property
    def filteredMemState(self) -> ghidra.app.emulator.FilteredMemoryState: ...

    @property
    def halt(self) -> bool: ...

    @halt.setter
    def halt(self, value: bool) -> None: ...

    @property
    def language(self) -> ghidra.app.plugin.processors.sleigh.SleighLanguage: ...

    @property
    def lastExecuteAddress(self) -> ghidra.program.model.address.Address: ...

    @property
    def memState(self) -> ghidra.pcode.memstate.MemoryState: ...

    @property
    def tickCount(self) -> int: ...
