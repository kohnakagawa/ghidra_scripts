from typing import List
import ghidra.program.model.address
import ghidra.program.model.lang
import ghidra.program.util
import java.lang


class AbstractStoredProgramContext(ghidra.program.util.AbstractProgramContext):








    def equals(self, __a0: object) -> bool: ...

    def flushProcessorContextWriteCache(self) -> None:
        """
        Flush any cached context not yet written to database
        """
        ...

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

    def invalidateProcessorContextWriteCache(self) -> None:
        """
        Flush any cached context not yet written to database
        """
        ...

    def notify(self) -> None: ...

    def notifyAll(self) -> None: ...

    def remove(self, start: ghidra.program.model.address.Address, end: ghidra.program.model.address.Address, register: ghidra.program.model.lang.Register) -> None: ...

    def setDefaultDisassemblyContext(self, value: ghidra.program.model.lang.RegisterValue) -> None: ...

    def setDefaultValue(self, registerValue: ghidra.program.model.lang.RegisterValue, start: ghidra.program.model.address.Address, end: ghidra.program.model.address.Address) -> None: ...

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
    def registersWithValues(self) -> List[ghidra.program.model.lang.Register]: ...
