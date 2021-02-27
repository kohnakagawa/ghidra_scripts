from typing import List
import ghidra.program.model.address
import ghidra.program.model.lang
import java.lang


class ProgramContext(object):
    """
    Interface to define a processor register context over the address space.
    """









    def equals(self, __a0: object) -> bool: ...

    def getBaseContextRegister(self) -> ghidra.program.model.lang.Register:
        """
        Returns the base context register.
        @return the base context register.
        """
        ...

    def getClass(self) -> java.lang.Class: ...

    def getContextRegisters(self) -> List[ghidra.program.model.lang.Register]:
        """
        Gets the registers for this context that are used for processor context states.
        @return all processor context registers
        """
        ...

    def getDefaultDisassemblyContext(self) -> ghidra.program.model.lang.RegisterValue:
        """
        @return Get the current default disassembly context to be used when initiating disassmbly
        """
        ...

    @overload
    def getDefaultRegisterValueAddressRanges(self, register: ghidra.program.model.lang.Register) -> ghidra.program.model.address.AddressRangeIterator:
        """
        Returns an AddressRangeIterator over all addresses that have an associated default value for the given
         register.  Each range returned will have the same default value associated with the register for all
         addresses in that range.
        @param register the register for which to get set default value ranges.
        @return An AddressRangeIterator over all address that have default values for the given register.
        """
        ...

    @overload
    def getDefaultRegisterValueAddressRanges(self, register: ghidra.program.model.lang.Register, start: ghidra.program.model.address.Address, end: ghidra.program.model.address.Address) -> ghidra.program.model.address.AddressRangeIterator:
        """
        Returns an AddressRangeIterator over all addresses that have an associated default value within the
         given range for the given register.  Each range returned will have the same default value
         associated with the register for all addresses in that range.
        @param register the register for which to get default value ranges.
        @param start start of address range to search
        @param end end of address range to search
        @return An AddressRangeIterator over all address within the given range that have default values
          for the given register.
        """
        ...

    def getDefaultValue(self, register: ghidra.program.model.lang.Register, address: ghidra.program.model.address.Address) -> ghidra.program.model.lang.RegisterValue:
        """
        Returns the default value of a register at a given address.
        @param register the register for which to get a default value.
        @param address the address at which to get a default value.
        @return the default value of the register at the given address or null if no default value
         has been assigned.
        """
        ...

    def getDisassemblyContext(self, address: ghidra.program.model.address.Address) -> ghidra.program.model.lang.RegisterValue:
        """
        Get the disassembly context for a specified address.  This context is formed
         from the default disassembly context and the context register value stored
         at the specified address.  Those bits specified by the stored context value
         take precedence.
        @param address program address
        @return disassembly context register value
        """
        ...

    def getFlowValue(self, value: ghidra.program.model.lang.RegisterValue) -> ghidra.program.model.lang.RegisterValue:
        """
        Modify register value to eliminate non-flowing bits
        @param value register value to be modified
        @return value suitable for flowing
        """
        ...

    def getNonDefaultValue(self, register: ghidra.program.model.lang.Register, address: ghidra.program.model.address.Address) -> ghidra.program.model.lang.RegisterValue:
        """
        Returns the (non-default)value assigned to a register at a given address.
        @param register the register for which to get its value.
        @param address the address at which to get a value.
        @return a RegisterValue object containing the value of the register at the given address or
         possibly null if no value has been assigned.
        """
        ...

    def getNonFlowValue(self, value: ghidra.program.model.lang.RegisterValue) -> ghidra.program.model.lang.RegisterValue:
        """
        Modify register value to only include non-flowing bits
        @param value register value to be modified
        @return new value or null
        """
        ...

    def getRegister(self, name: unicode) -> ghidra.program.model.lang.Register:
        """
        Get a Register object given the name of a register
        @param name the name of the register.
        @return The register with the given name or null if no register has that name.
        """
        ...

    def getRegisterNames(self) -> List[unicode]:
        """
        Get an alphabetical sorted unmodifiable list of original register names
         (including context registers).  Names correspond to orignal register
         name and not aliases which may be defined.
        @return alphabetical sorted unmodifiable list of original register names.
        """
        ...

    def getRegisterValue(self, register: ghidra.program.model.lang.Register, address: ghidra.program.model.address.Address) -> ghidra.program.model.lang.RegisterValue:
        """
        Returns a register value and mask for the given register.
        @param register the register
        @param address the address of the value
        @return a register value and mask for the given register
        """
        ...

    @overload
    def getRegisterValueAddressRanges(self, register: ghidra.program.model.lang.Register) -> ghidra.program.model.address.AddressRangeIterator:
        """
        Returns an AddressRangeIterator over all addresses that have an associated value for the given
         register.  Each range returned will have the same value associated with the register for all
         addresses in that range.
        @param register the register for which to get set value ranges.
        @return An AddressRangeIterator over all address that have values for the given register.
        """
        ...

    @overload
    def getRegisterValueAddressRanges(self, register: ghidra.program.model.lang.Register, start: ghidra.program.model.address.Address, end: ghidra.program.model.address.Address) -> ghidra.program.model.address.AddressRangeIterator:
        """
        Returns an AddressRangeIterator over all addresses that have an associated value within the
         given range for the given register.  Each range returned will have the same value
         associated with the register for all addresses in that range.
        @param register the register for which to get set value ranges.
        @param start start of address range to search
        @param end end of address range to search
        @return An AddressRangeIterator over all address within the given range that have values
          for the given register.
        """
        ...

    def getRegisterValueRangeContaining(self, register: ghidra.program.model.lang.Register, addr: ghidra.program.model.address.Address) -> ghidra.program.model.address.AddressRange:
        """
        Returns the bounding address-range containing addr and the the same RegisterValue throughout.
         The range returned may be limited by other value changes associated with register's base-register.
        @param register program register
        @param addr program address
        @return single register-value address-range containing addr
        """
        ...

    def getRegisters(self) -> List[ghidra.program.model.lang.Register]:
        """
        Get all the register descriptions defined for this program context.
        @return unmodifiable list of defined register descriptions
        """
        ...

    def getRegistersWithValues(self) -> List[ghidra.program.model.lang.Register]:
        """
        Returns an array of all registers that at least one value associated with an address.
        @return a array of all registers that at least one value associated with an address.
        """
        ...

    def getValue(self, register: ghidra.program.model.lang.Register, address: ghidra.program.model.address.Address, signed: bool) -> long:
        """
        Returns the value assigned to a register at a given address.  This method will return any
         default value assigned to the register at the given address if no explicit value has been set
         at that address.
        @param register the register for which to get its value.
        @param address the address at which to get a value.
        @param signed if true, interprets the fix-bit size register value as a signed value.
        @return a BigInteger object containing the value of the registe at the given address or null
         if no value has been assigned.
        """
        ...

    def hasNonFlowingContext(self) -> bool:
        """
        @return true if one or more non-flowing context registers fields
         have been defined within the base processor context register.
        """
        ...

    def hasValueOverRange(self, reg: ghidra.program.model.lang.Register, value: long, addrSet: ghidra.program.model.address.AddressSetView) -> bool:
        """
        Returns true if the given register has the value over the addressSet
        @param reg the register whose value is to be tested.
        @param value the value to test for.
        @param addrSet the set of addresses to test
        @return true if every address in the addrSet has the value.
        """
        ...

    def hashCode(self) -> int: ...

    def notify(self) -> None: ...

    def notifyAll(self) -> None: ...

    def remove(self, start: ghidra.program.model.address.Address, end: ghidra.program.model.address.Address, register: ghidra.program.model.lang.Register) -> None:
        """
        Remove (unset) the register values for a given address range.
        @param start starting address.
        @param end ending adddress.
        @param register handle to the register to be set.
        @throws ContextChangeException thrown if context change not permitted over specified
         range (e.g., instructions exist)
        """
        ...

    def setDefaultDisassemblyContext(self, value: ghidra.program.model.lang.RegisterValue) -> None:
        """
        Set the initial disassembly context to be used when initiating disassmbly
        @param value context register value
        """
        ...

    def setRegisterValue(self, start: ghidra.program.model.address.Address, end: ghidra.program.model.address.Address, value: ghidra.program.model.lang.RegisterValue) -> None:
        """
        Sets the register context over the given range to the given value.
        @param start the start address to set values
        @param end the end address to set values
        @param value the actual values to store at address
        @throws ContextChangeException if failed to modifiy context across specified range
         (e.g., instruction exists).
        """
        ...

    def setValue(self, register: ghidra.program.model.lang.Register, start: ghidra.program.model.address.Address, end: ghidra.program.model.address.Address, value: long) -> None:
        """
        Associates a value with a register over a given address range. Any previous values will be
         overwritten.
        @param register the register for which to assign a value.
        @param start the start address.
        @param end the end address (inclusive).
        @param value the value to assign.  A value of null will effective clear any existing values.
        @throws ContextChangeException if failed to modifiy context across specified range
         (e.g., instruction exists).
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
    def baseContextRegister(self) -> ghidra.program.model.lang.Register: ...

    @property
    def contextRegisters(self) -> List[object]: ...

    @property
    def defaultDisassemblyContext(self) -> ghidra.program.model.lang.RegisterValue: ...

    @defaultDisassemblyContext.setter
    def defaultDisassemblyContext(self, value: ghidra.program.model.lang.RegisterValue) -> None: ...

    @property
    def registerNames(self) -> List[object]: ...

    @property
    def registers(self) -> List[object]: ...

    @property
    def registersWithValues(self) -> List[ghidra.program.model.lang.Register]: ...
