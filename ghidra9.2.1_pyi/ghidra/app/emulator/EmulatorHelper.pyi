from typing import List
import ghidra.app.emulator
import ghidra.app.emulator.memory
import ghidra.pcode.emulate
import ghidra.pcode.memstate
import ghidra.program.model.address
import ghidra.program.model.lang
import ghidra.program.model.listing
import ghidra.program.model.mem
import ghidra.util.task
import java.lang


class EmulatorHelper(object, ghidra.pcode.memstate.MemoryFaultHandler, ghidra.app.emulator.EmulatorConfiguration):




    def __init__(self, program: ghidra.program.model.listing.Program): ...



    def clearBreakpoint(self, addr: ghidra.program.model.address.Address) -> None:
        """
        Clear breakpoint
        @param addr memory address for breakpoint to be cleared
        """
        ...

    def createMemoryBlockFromMemoryState(self, name: unicode, start: ghidra.program.model.address.Address, length: int, overlay: bool, monitor: ghidra.util.task.TaskMonitor) -> ghidra.program.model.mem.MemoryBlock:
        """
        Create a new initialized memory block using the current emulator memory state
        @param name block name
        @param start start address of the block
        @param length the size of the block
        @param overlay if true, the block will be created as an OVERLAY which means that a new
         overlay address space will be created and the block will have a starting address at the same
         offset as the given start address parameter, but in the new address space.
        @param monitor
        @return new memory block
        @throws LockException if exclusive lock not in place (see haveLock())
        @throws MemoryConflictException if the new block overlaps with a
         previous block
        @throws AddressOverflowException if the start is beyond the
         address space
        @throws CancelledException user cancelled operation
        @throws DuplicateNameException
        """
        ...

    def dispose(self) -> None: ...

    def enableMemoryWriteTracking(self, enable: bool) -> None:
        """
        Enable/Disable tracking of memory writes in the form of an
         address set.
        @param enable
        """
        ...

    def equals(self, __a0: object) -> bool: ...

    def getClass(self) -> java.lang.Class: ...

    def getContextRegister(self) -> ghidra.program.model.lang.RegisterValue:
        """
        Get the current context register value
        @return context register value or null if not set or unknown
        """
        ...

    def getEmulateExecutionState(self) -> ghidra.pcode.emulate.EmulateExecutionState:
        """
        @return the low-level emulator execution state
        """
        ...

    def getEmulator(self) -> ghidra.app.emulator.Emulator: ...

    def getExecutionAddress(self) -> ghidra.program.model.address.Address:
        """
        Get current execution address
        @return current execution address
        """
        ...

    def getLanguage(self) -> ghidra.program.model.lang.Language: ...

    def getLastError(self) -> unicode:
        """
        @return last error message associated with execution failure
        """
        ...

    def getLoadData(self) -> ghidra.app.emulator.memory.EmulatorLoadData: ...

    def getMemoryFaultHandler(self) -> ghidra.pcode.memstate.MemoryFaultHandler: ...

    def getPCRegister(self) -> ghidra.program.model.lang.Register:
        """
        Get Program Counter (PC) register defined by applicable processor specification
        @return Program Counter register
        """
        ...

    def getPreferredMemoryPageSize(self) -> int: ...

    def getProgram(self) -> ghidra.program.model.listing.Program: ...

    def getProgramCounterName(self) -> unicode: ...

    def getStackPointerRegister(self) -> ghidra.program.model.lang.Register:
        """
        Get Stack Pointer register defined by applicable compiler specification
        @return Stack Pointer register
        """
        ...

    def getTrackedMemoryWriteSet(self) -> ghidra.program.model.address.AddressSetView:
        """
        @return address set of memory locations written by the emulator
         if memory write tracking is enabled, otherwise null is returned.
         The address set returned will continue to be updated unless
         memory write tracking becomes disabled.
        """
        ...

    def hashCode(self) -> int: ...

    def isWriteBackEnabled(self) -> bool: ...

    def notify(self) -> None: ...

    def notifyAll(self) -> None: ...

    def readMemory(self, addr: ghidra.program.model.address.Address, length: int) -> List[int]: ...

    def readMemoryByte(self, addr: ghidra.program.model.address.Address) -> int: ...

    def readNullTerminatedString(self, addr: ghidra.program.model.address.Address, maxLength: int) -> unicode:
        """
        Read string from memory state.
        @param addr memory address
        @param maxLength limit string read to this length.  If return string is
         truncated, "..." will be appended.
        @return string read from memory state
        """
        ...

    @overload
    def readRegister(self, regName: unicode) -> long: ...

    @overload
    def readRegister(self, reg: ghidra.program.model.lang.Register) -> long: ...

    def readStackValue(self, relativeOffset: int, size: int, signed: bool) -> long:
        """
        Read a stack value from the memory state.
        @param relativeOffset offset relative to current stack pointer
        @param size data size in bytes
        @param signed true if value read is signed, false if unsigned
        @return value
        @throws Exception error occurs reading stack pointer
        """
        ...

    def registerCallOtherCallback(self, pcodeOpName: unicode, callback: ghidra.pcode.emulate.BreakCallBack) -> None:
        """
        Register callback for language defined pcodeop (call other).
         WARNING! Using this method may circumvent the default CALLOTHER emulation support
         when supplied by the Processor module.
        @param pcodeOpName the name of the pcode op
        @param callback the callback to register
        """
        ...

    def registerDefaultCallOtherCallback(self, callback: ghidra.pcode.emulate.BreakCallBack) -> None:
        """
        Register default callback for language defined pcodeops (call other).
         WARNING! Using this method may circumvent the default CALLOTHER emulation support
         when supplied by the Processor module.
        @param callback the default callback to register
        """
        ...

    @overload
    def run(self, monitor: ghidra.util.task.TaskMonitor) -> bool:
        """
        Continue execution from the current execution address.
         No adjustment will be made to the context beyond the normal
         context flow behavior defined by the language.
         Method will block until execution stops.
        @param monitor
        @return true if execution completes without error (i.e., is at breakpoint)
        @throws CancelledException if execution cancelled via monitor
        """
        ...

    @overload
    def run(self, addr: ghidra.program.model.address.Address, context: ghidra.program.model.lang.ProcessorContext, monitor: ghidra.util.task.TaskMonitor) -> bool:
        """
        Start execution at the specified address using the initial context specified.
         Method will block until execution stops.  This method will initialize context
         register based upon the program stored context if not already done.  In addition,
         both general register value and the context register may be further modified
         via the context parameter if specified.
        @param addr initial program address
        @param context optional context settings which override current program context
        @param monitor
        @return true if execution completes without error (i.e., is at breakpoint)
        @throws CancelledException if execution cancelled via monitor
        """
        ...

    def setBreakpoint(self, addr: ghidra.program.model.address.Address) -> None:
        """
        Establish breakpoint
        @param addr memory address for new breakpoint
        """
        ...

    @overload
    def setContextRegister(self, ctxRegValue: ghidra.program.model.lang.RegisterValue) -> None:
        """
        Set current context register value.
         Keep in mind that any non-flowing context values will be stripped.
        @param ctxRegValue
        """
        ...

    @overload
    def setContextRegister(self, ctxReg: ghidra.program.model.lang.Register, value: long) -> None:
        """
        Set current context register value.
         Keep in mind that any non-flowing context values will be stripped.
        @param ctxReg context register
        @param value context value
        """
        ...

    def setMemoryFaultHandler(self, handler: ghidra.pcode.memstate.MemoryFaultHandler) -> None:
        """
        Provides ability to install a low-level memory fault handler.
         The handler methods should generally return 'false' to allow
         the default handler to generate the appropriate target error.
         Within the fault handler, the EmulateExecutionState can be used
         to distinguish the pcode-emit state and the actual execution state
         since an attempt to execute an instruction at an uninitialized
         memory location will cause an uninitializedRead during the PCODE_EMIT
         state.
        @param handler memory fault handler.
        """
        ...

    def step(self, monitor: ghidra.util.task.TaskMonitor) -> bool:
        """
        Step execution one instruction which may consist of multiple
         pcode operations.  No adjustment will be made to the context beyond the normal
         context flow behavior defined by the language.
         Method will block until execution stops.
        @return true if execution completes without error
        @throws CancelledException if execution cancelled via monitor
        """
        ...

    def toString(self) -> unicode: ...

    def uninitializedRead(self, address: ghidra.program.model.address.Address, size: int, buf: List[int], bufOffset: int) -> bool: ...

    def unknownAddress(self, address: ghidra.program.model.address.Address, write: bool) -> bool: ...

    def unregisterCallOtherCallback(self, pcodeOpName: unicode) -> None:
        """
        Unregister callback for language defined pcodeop (call other).
        @param pcodeOpName the name of the pcode op
        """
        ...

    def unregisterDefaultCallOtherCallback(self) -> None:
        """
        Unregister default callback for language defined pcodeops (call other).
         WARNING! Using this method may circumvent the default CALLOTHER emulation support
         when supplied by the Processor module.
        """
        ...

    @overload
    def wait(self) -> None: ...

    @overload
    def wait(self, __a0: long) -> None: ...

    @overload
    def wait(self, __a0: long, __a1: int) -> None: ...

    def writeMemory(self, addr: ghidra.program.model.address.Address, bytes: List[int]) -> None: ...

    def writeMemoryValue(self, addr: ghidra.program.model.address.Address, size: int, value: long) -> None: ...

    @overload
    def writeRegister(self, regName: unicode, value: long) -> None: ...

    @overload
    def writeRegister(self, reg: ghidra.program.model.lang.Register, value: long) -> None: ...

    @overload
    def writeRegister(self, regName: unicode, value: long) -> None: ...

    @overload
    def writeRegister(self, reg: ghidra.program.model.lang.Register, value: long) -> None: ...

    @overload
    def writeStackValue(self, relativeOffset: int, size: int, value: long) -> None:
        """
        Write a value onto the stack
        @param relativeOffset offset relative to current stack pointer
        @param size data size in bytes
        @param value
        @throws Exception error occurs reading stack pointer
        """
        ...

    @overload
    def writeStackValue(self, relativeOffset: int, size: int, value: long) -> None:
        """
        Write a value onto the stack
        @param relativeOffset offset relative to current stack pointer
        @param size data size in bytes
        @param value
        @throws Exception error occurs reading stack pointer
        """
        ...

    @property
    def PCRegister(self) -> ghidra.program.model.lang.Register: ...

    @property
    def breakpoint(self) -> None: ...  # No getter available.

    @breakpoint.setter
    def breakpoint(self, value: ghidra.program.model.address.Address) -> None: ...

    @property
    def contextRegister(self) -> ghidra.program.model.lang.RegisterValue: ...

    @contextRegister.setter
    def contextRegister(self, value: ghidra.program.model.lang.RegisterValue) -> None: ...

    @property
    def emulateExecutionState(self) -> ghidra.pcode.emulate.EmulateExecutionState: ...

    @property
    def emulator(self) -> ghidra.app.emulator.Emulator: ...

    @property
    def executionAddress(self) -> ghidra.program.model.address.Address: ...

    @property
    def language(self) -> ghidra.program.model.lang.Language: ...

    @property
    def lastError(self) -> unicode: ...

    @property
    def loadData(self) -> ghidra.app.emulator.memory.EmulatorLoadData: ...

    @property
    def memoryFaultHandler(self) -> ghidra.pcode.memstate.MemoryFaultHandler: ...

    @memoryFaultHandler.setter
    def memoryFaultHandler(self, value: ghidra.pcode.memstate.MemoryFaultHandler) -> None: ...

    @property
    def preferredMemoryPageSize(self) -> int: ...

    @property
    def program(self) -> ghidra.program.model.listing.Program: ...

    @property
    def programCounterName(self) -> unicode: ...

    @property
    def stackPointerRegister(self) -> ghidra.program.model.lang.Register: ...

    @property
    def trackedMemoryWriteSet(self) -> ghidra.program.model.address.AddressSetView: ...

    @property
    def writeBackEnabled(self) -> bool: ...
