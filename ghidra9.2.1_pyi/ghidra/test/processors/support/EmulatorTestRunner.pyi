from typing import List
import ghidra.app.emulator
import ghidra.program.model.address
import ghidra.program.model.lang
import ghidra.program.model.listing
import ghidra.test.processors.support
import ghidra.test.processors.support.EmulatorTestRunner
import ghidra.util.task
import java.lang


class EmulatorTestRunner(object):





    class DumpFormat(java.lang.Enum):
        DECIMAL: ghidra.test.processors.support.EmulatorTestRunner.DumpFormat = DECIMAL
        FLOAT: ghidra.test.processors.support.EmulatorTestRunner.DumpFormat = FLOAT
        HEX: ghidra.test.processors.support.EmulatorTestRunner.DumpFormat = HEX







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
        def valueOf(__a0: unicode) -> ghidra.test.processors.support.EmulatorTestRunner.DumpFormat: ...

        @overload
        @staticmethod
        def valueOf(__a0: java.lang.Class, __a1: unicode) -> java.lang.Enum: ...

        @staticmethod
        def values() -> List[ghidra.test.processors.support.EmulatorTestRunner.DumpFormat]: ...

        @overload
        def wait(self) -> None: ...

        @overload
        def wait(self, __a0: long) -> None: ...

        @overload
        def wait(self, __a0: long, __a1: int) -> None: ...



    def __init__(self, program: ghidra.program.model.listing.Program, testGroup: ghidra.test.processors.support.PCodeTestGroup, executionListener: ghidra.test.processors.support.ExecutionListener): ...



    @overload
    def addDumpPoint(self, breakAddr: ghidra.program.model.address.Address, dumpAddr: ghidra.program.model.address.Address, dumpSize: int, elementSize: int, elementFormat: ghidra.test.processors.support.EmulatorTestRunner.DumpFormat, comment: unicode) -> None:
        """
        Add memory dump point
        @param breakAddr instruction address at which execution should pause (before it is executed)
         so that the specified memory may be dumped to the log during trace execution mode.
        @param dumpAddr memory address which should be dumped
        @param dumpSize number elements which should be dumped
        @param elementSize size of each element in bytes (be reasonable!)
        @param elementFormat HEX, DECIMAL or FLOAT
        @param comment dump comment
        """
        ...

    @overload
    def addDumpPoint(self, breakAddr: ghidra.program.model.address.Address, dumpAddrReg: ghidra.program.model.lang.Register, relativeOffset: int, dumpAddrSpace: ghidra.program.model.address.AddressSpace, dumpSize: int, elementSize: int, elementFormat: ghidra.test.processors.support.EmulatorTestRunner.DumpFormat, comment: unicode) -> None:
        """
        Add memory dump point
        @param breakAddr instruction address at which execution should pause (before it is executed)
         so that the specified memory may be dumped to the log during trace execution mode.
        @param dumpAddrReg register containing the memory address offset which should be dumped
        @param relativeOffset dump register relative offset
        @param dumpAddrSpace address space to which memory offset should be applied
        @param dumpSize number elements which should be dumped
        @param elementSize size of each element in bytes (be reasonable!)
        @param elementFormat HEX, DECIMAL or FLOAT
        @param comment dump comment
        """
        ...

    def dispose(self) -> None: ...

    def equals(self, __a0: object) -> bool: ...

    def execute(self, timeLimitMS: int, monitor: ghidra.util.task.TaskMonitor) -> bool:
        """
        Execute test group without instruction stepping/tracing
        @param timeLimitMS
        @param monitor
        @return
        @throws CancelledException
        """
        ...

    def executeSingleStep(self, stepLimit: int) -> bool: ...

    def getCallOtherErrors(self) -> int:
        """
        Get number of CALLOTHER errors detected when a test pass was registered.
         This number should be subtracted from the pass count and possibly added
         to the failure count.  Number does not reflect total number of CALLOTHER
         pcodeops encountered but only the number of passed tests affected.
         See log for all CALLOTHER executions detected.
        @return number of CALLOTHER errors
        """
        ...

    def getClass(self) -> java.lang.Class: ...

    def getCurrentAddress(self) -> ghidra.program.model.address.Address: ...

    def getCurrentInstruction(self) -> ghidra.program.model.listing.Instruction: ...

    def getEmuError(self) -> unicode: ...

    def getEmulatorHelper(self) -> ghidra.app.emulator.EmulatorHelper: ...

    def getProgram(self) -> ghidra.program.model.listing.Program: ...

    def getRegisterValue(self, reg: ghidra.program.model.lang.Register) -> ghidra.program.model.lang.RegisterValue: ...

    def getRegisterValueString(self, reg: ghidra.program.model.lang.Register) -> unicode: ...

    def getTestGroup(self) -> ghidra.test.processors.support.PCodeTestGroup: ...

    def hashCode(self) -> int: ...

    def notify(self) -> None: ...

    def notifyAll(self) -> None: ...

    def setContextRegister(self, ctxRegValue: ghidra.program.model.lang.RegisterValue) -> None: ...

    @overload
    def setRegister(self, regName: unicode, value: long) -> None: ...

    @overload
    def setRegister(self, regName: unicode, value: long) -> None: ...

    def toString(self) -> unicode: ...

    @overload
    def wait(self) -> None: ...

    @overload
    def wait(self, __a0: long) -> None: ...

    @overload
    def wait(self, __a0: long, __a1: int) -> None: ...

    @property
    def callOtherErrors(self) -> int: ...

    @property
    def contextRegister(self) -> None: ...  # No getter available.

    @contextRegister.setter
    def contextRegister(self, value: ghidra.program.model.lang.RegisterValue) -> None: ...

    @property
    def currentAddress(self) -> ghidra.program.model.address.Address: ...

    @property
    def currentInstruction(self) -> ghidra.program.model.listing.Instruction: ...

    @property
    def emuError(self) -> unicode: ...

    @property
    def emulatorHelper(self) -> ghidra.app.emulator.EmulatorHelper: ...

    @property
    def program(self) -> ghidra.program.model.listing.Program: ...

    @property
    def testGroup(self) -> ghidra.test.processors.support.PCodeTestGroup: ...
