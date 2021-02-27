from typing import List
import ghidra.program.database
import ghidra.program.model.address
import ghidra.program.model.lang
import ghidra.program.util
import ghidra.util.task
import java.lang


class ProgramRegisterContextDB(ghidra.program.util.AbstractStoredProgramContext, ghidra.program.database.ManagerDB):




    def __init__(self, dbHandle: db.DBHandle, errHandler: db.util.ErrorHandler, lang: ghidra.program.model.lang.Language, compilerSpec: ghidra.program.model.lang.CompilerSpec, addrMap: ghidra.program.database.map.AddressMap, lock: ghidra.util.Lock, openMode: int, codeMgr: ghidra.program.database.code.CodeManager, monitor: ghidra.util.task.TaskMonitor): ...



    def deleteAddressRange(self, start: ghidra.program.model.address.Address, end: ghidra.program.model.address.Address, monitor: ghidra.util.task.TaskMonitor) -> None: ...

    def equals(self, __a0: object) -> bool: ...

    def flushProcessorContextWriteCache(self) -> None: ...

    def getBaseContextRegister(self) -> ghidra.program.model.lang.Register: ...

    def getClass(self) -> java.lang.Class: ...

    def getContextRegisters(self) -> List[ghidra.program.model.lang.Register]: ...

    def getDefaultDisassemblyContext(self) -> ghidra.program.model.lang.RegisterValue: ...

    @overload
    def getDefaultRegisterValueAddressRanges(self, register: ghidra.program.model.lang.Register) -> ghidra.program.model.address.AddressRangeIterator: ...

    @overload
    def getDefaultRegisterValueAddressRanges(self, register: ghidra.program.model.lang.Register, start: ghidra.program.model.address.Address, end: ghidra.program.model.address.Address) -> ghidra.program.model.address.AddressRangeIterator: ...

    def getDefaultValue(self, register: ghidra.program.model.lang.Register, address: ghidra.program.model.address.Address) -> ghidra.program.model.lang.RegisterValue: ...

    def getDisassemblyContext(self, address: ghidra.program.model.address.Address) -> ghidra.program.model.lang.RegisterValue: ...

    def getFlowValue(self, value: ghidra.program.model.lang.RegisterValue) -> ghidra.program.model.lang.RegisterValue:
        """
        Modify register value to eliminate non-flowing bits
        @param value context register value to be modified
        @return value suitable for flowing
        """
        ...

    def getLanguage(self) -> ghidra.program.model.lang.Language:
        """
        Get underlying language associated with this context and its registers
        @return language
        """
        ...

    def getNonDefaultValue(self, register: ghidra.program.model.lang.Register, address: ghidra.program.model.address.Address) -> ghidra.program.model.lang.RegisterValue: ...

    def getNonFlowValue(self, value: ghidra.program.model.lang.RegisterValue) -> ghidra.program.model.lang.RegisterValue:
        """
        Modify register value to only include non-flowing bits
        @param value context register value to be modified
        @return new value or null if value does not correspond to a context register or
         non-flowing context fields have not been defined
        """
        ...

    def getRegister(self, name: unicode) -> ghidra.program.model.lang.Register: ...

    def getRegisterNames(self) -> List[unicode]: ...

    def getRegisterValue(self, register: ghidra.program.model.lang.Register, address: ghidra.program.model.address.Address) -> ghidra.program.model.lang.RegisterValue: ...

    @overload
    def getRegisterValueAddressRanges(self, register: ghidra.program.model.lang.Register) -> ghidra.program.model.address.AddressRangeIterator: ...

    @overload
    def getRegisterValueAddressRanges(self, register: ghidra.program.model.lang.Register, start: ghidra.program.model.address.Address, end: ghidra.program.model.address.Address) -> ghidra.program.model.address.AddressRangeIterator: ...

    def getRegisterValueRangeContaining(self, register: ghidra.program.model.lang.Register, addr: ghidra.program.model.address.Address) -> ghidra.program.model.address.AddressRange: ...

    def getRegisters(self) -> List[ghidra.program.model.lang.Register]: ...

    def getRegistersWithValues(self) -> List[ghidra.program.model.lang.Register]: ...

    def getValue(self, register: ghidra.program.model.lang.Register, address: ghidra.program.model.address.Address, signed: bool) -> long: ...

    def hasNonFlowingContext(self) -> bool:
        """
        @return true if one or more non-flowing context registers fields
         have been defined within the base processor context register.
        """
        ...

    def hasValueOverRange(self, reg: ghidra.program.model.lang.Register, value: long, addrSet: ghidra.program.model.address.AddressSetView) -> bool: ...

    def hashCode(self) -> int: ...

    def initializeDefaultValues(self, lang: ghidra.program.model.lang.Language, compilerSpec: ghidra.program.model.lang.CompilerSpec) -> None:
        """
        Intialize context with default values defined by pspec and cspec.
         NOTE: cspec values take precedence
        @param lang processor language
        @param compilerSpec compiler specification
        """
        ...

    def invalidateCache(self, all: bool) -> None: ...

    def invalidateProcessorContextWriteCache(self) -> None: ...

    def moveAddressRange(self, fromAddr: ghidra.program.model.address.Address, toAddr: ghidra.program.model.address.Address, length: long, monitor: ghidra.util.task.TaskMonitor) -> None: ...

    def notify(self) -> None: ...

    def notifyAll(self) -> None: ...

    def programReady(self, openMode: int, currentRevision: int, monitor: ghidra.util.task.TaskMonitor) -> None: ...

    def remove(self, start: ghidra.program.model.address.Address, end: ghidra.program.model.address.Address, register: ghidra.program.model.lang.Register) -> None: ...

    def setDefaultDisassemblyContext(self, value: ghidra.program.model.lang.RegisterValue) -> None: ...

    def setDefaultValue(self, registerValue: ghidra.program.model.lang.RegisterValue, start: ghidra.program.model.address.Address, end: ghidra.program.model.address.Address) -> None: ...

    def setLanguage(self, translator: ghidra.program.util.LanguageTranslator, newCompilerSpec: ghidra.program.model.lang.CompilerSpec, programMemory: ghidra.program.model.address.AddressSetView, monitor: ghidra.util.task.TaskMonitor) -> None:
        """
        Perform context upgrade due to a language change
        @param translator language translator required by major upgrades (may be null)
        @param newCompilerSpec new compiler specification
        @param programMemory program memory
        @param monitor task monitor
        @throws CancelledException thrown if monitor cancelled
        """
        ...

    def setProgram(self, program: ghidra.program.database.ProgramDB) -> None: ...

    def setRegisterValue(self, start: ghidra.program.model.address.Address, end: ghidra.program.model.address.Address, value: ghidra.program.model.lang.RegisterValue) -> None: ...

    def setValue(self, register: ghidra.program.model.lang.Register, start: ghidra.program.model.address.Address, end: ghidra.program.model.address.Address, value: long) -> None: ...

    def toString(self) -> unicode: ...

    @overload
    def wait(self) -> None: ...

    @overload
    def wait(self, __a0: long) -> None: ...

    @overload
    def wait(self, __a0: long, __a1: int) -> None: ...

    @property
    def program(self) -> None: ...  # No getter available.

    @program.setter
    def program(self, value: ghidra.program.database.ProgramDB) -> None: ...

    @property
    def registersWithValues(self) -> List[ghidra.program.model.lang.Register]: ...
