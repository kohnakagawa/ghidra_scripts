from typing import List
import ghidra.program.model.address
import ghidra.program.model.lang
import ghidra.program.model.listing
import java.lang


class DisassemblerContextImpl(object, ghidra.program.model.lang.DisassemblerContext):
    """
    Maintains processor state information during disassembly and analysis.  Tracks register state
     associated with instruction flows.  Within this context, a flow is defined as a contiguous
     range of instructions.  Also, this context provides storage for context states at future flow
     addresses, which will be used when subsequent flowTo(Address) or flowStart(Address) calls
     are made with those addresses.
    """





    def __init__(self, programContext: ghidra.program.model.listing.ProgramContext):
        """
        Constructor for DisassemblerContext.
        @param programContext contains the values for registers at specific addresses store in the program.
        """
        ...



    def clearRegister(self, register: ghidra.program.model.lang.Register) -> None: ...

    @overload
    def copyToFutureFlowState(self, address: ghidra.program.model.address.Address) -> ghidra.program.model.lang.RegisterValue:
        """
        Saves the current processor state for when this context flows to the given address.

         Use this method if keeping separate flows from different flow from addresses is not important.
        @param address the address at which to save the current processor state.
        @return context register value which was copied
        """
        ...

    @overload
    def copyToFutureFlowState(self, fromAddr: ghidra.program.model.address.Address, destAddr: ghidra.program.model.address.Address) -> ghidra.program.model.lang.RegisterValue:
        """
        Saves the current processor state flowing from the fromAddr, for when this context flows to the given address.
        @param fromAddr the address from which this flow originates.
        @param destAddr the address at which to save the current processor state.
        @return context register value which was copied
        """
        ...

    @overload
    @staticmethod
    def dumpContextValue(__a0: ghidra.program.model.lang.RegisterValue, __a1: unicode) -> unicode: ...

    @overload
    @staticmethod
    def dumpContextValue(__a0: ghidra.program.model.lang.RegisterValue, __a1: unicode, __a2: java.lang.StringBuilder) -> None: ...

    def equals(self, __a0: object) -> bool: ...

    def flowAbort(self) -> None:
        """
        Terminate active flow while preserving any accumulated future context.
         Any context commits resulting from a flowToAddress or flowEnd will be
         unaffected.
        """
        ...

    def flowEnd(self, maxAddress: ghidra.program.model.address.Address) -> None:
        """
        Ends the current flow.  Unsaved register values will be saved up to and including max address.
        @param maxAddress the maximum address of an instruction flow.  If maxAddress is null,
         or the current flow address has already advanced beyond maxAddress, then no save is performed.
        @throws IllegalStateException if a flow has not been started.
        """
        ...

    @overload
    def flowStart(self, address: ghidra.program.model.address.Address) -> None:
        """
        Starts a new flow. Initializes the current state for all registers using any future flow state
         that has been set.

         Use this method if keeping separate flows from different flow from addresses is not important.
        @param address the starting address of a new instruction flow.
        @throws IllegalStateException if a previous flow was not ended.
        """
        ...

    @overload
    def flowStart(self, fromAddr: ghidra.program.model.address.Address, toAddr: ghidra.program.model.address.Address) -> None:
        """
        Starts a new flow from an address to the new start.
         Initializes the current state for all registers using any future flow state
         that has been set flowing from the fromAddr.
        @param fromAddr address that this flow is flowing from.
        @param toAddr the starting address of a new instruction flow.
        @throws IllegalStateException if a previous flow was not ended.
        """
        ...

    @overload
    def flowToAddress(self, address: ghidra.program.model.address.Address) -> None:
        """
        Continues the current flow at the given address.  Checks for register values that have been
         stored in the future flow state.  If any registers have saved future state, the current state
         for all registers is written to the program context upto the specified address(exclusive).
         The future flow state values are then loaded into the current context.

         Use this method if keeping separate flows from different flow from addresses is not important.
        @param address the address to flow to.
        @throws IllegalStateException if no flow was started.
        """
        ...

    @overload
    def flowToAddress(self, fromAddr: ghidra.program.model.address.Address, destAddr: ghidra.program.model.address.Address) -> None:
        """
        Continues the current flow from an address to the given address.  Checks for register values that have been
         stored in the future flow state.  If any registers have saved future state, the current state
         for all registers is written to the program context upto the specified address(exclusive).
         The future flow state values are then loaded into the current context.
        @param fromAddr address that this flow is flowing from.
        @param destAddr the starting address of a new instruction flow.
        @throws IllegalStateException if a previous flow was not ended.
        """
        ...

    def getAddress(self) -> ghidra.program.model.address.Address:
        """
        Returns the current flow address for this context.
        """
        ...

    def getBaseContextRegister(self) -> ghidra.program.model.lang.Register: ...

    def getClass(self) -> java.lang.Class: ...

    @overload
    def getFlowContextValue(self, destAddr: ghidra.program.model.address.Address, isFallThrough: bool) -> ghidra.program.model.lang.RegisterValue:
        """
        Get flowed context value at arbitrary destination address without affecting state.

         Use this method if keeping separate flows from different flow from addresses is not important.
        @param destAddr
        @param isFallThrough
        @return the flowed context value
        """
        ...

    @overload
    def getFlowContextValue(self, fromAddr: ghidra.program.model.address.Address, destAddr: ghidra.program.model.address.Address, isFallThrough: bool) -> ghidra.program.model.lang.RegisterValue:
        """
        Get flowed context value at a destination address, that has been flowed from the fromAddr, without affecting state.
        @param fromAddr address that this flow is flowing from.
        @param destAddr the starting address of a new instruction flow.
        @throws IllegalStateException if a previous flow was not ended.
        """
        ...

    def getKnownFlowToAddresses(self, toAddr: ghidra.program.model.address.Address) -> List[ghidra.program.model.address.Address]:
        """
        Returns an array of locations that have values that will flow to this location
        @param toAddr address that is the target of a flow to
        @return and array of known address flows to this location
        """
        ...

    def getProgramContext(self) -> ghidra.program.model.listing.ProgramContext: ...

    def getRegister(self, name: unicode) -> ghidra.program.model.lang.Register: ...

    @overload
    def getRegisterValue(self, register: ghidra.program.model.lang.Register) -> ghidra.program.model.lang.RegisterValue: ...

    @overload
    def getRegisterValue(self, register: ghidra.program.model.lang.Register, address: ghidra.program.model.address.Address) -> ghidra.program.model.lang.RegisterValue:
        """
        Returns the future RegisterValue at the specified address.  If no future value is stored,
         it will return the value stored in the program. The value returned may not have a complete
         value for the requested register.

         Use this method if keeping separate flows from different flow from addresses is not important.
        @param register the register to get a value for.
        @param address the address at which to get a value.
        @return a RegisterValue object if one has been stored in the future flow or the program.
         The RegisterValue object may have a "no value" state for the bits specified by the given register.
         Also, null may be returned if no value have been stored.
        """
        ...

    @overload
    def getRegisterValue(self, register: ghidra.program.model.lang.Register, fromAddr: ghidra.program.model.address.Address, destAddr: ghidra.program.model.address.Address) -> ghidra.program.model.lang.RegisterValue:
        """
        Returns the future RegisterValue at the specified address that occurred because of a flow from
         the fromAddr.  If no future value is stored, it will return the value stored in the program.
         The value returned may not have a complete value for the requested register.
        @param register the register to get a value for.
        @param fromAddr the address from which the flow originated
        @param destAddr the address at which to get a value.
        @return a RegisterValue object if one has been stored in the future flow or the program.
         The RegisterValue object may have a "no value" state for the bits specified by the given register.
         Also, null may be returned if no value have been stored.
        """
        ...

    def getRegisters(self) -> List[ghidra.program.model.lang.Register]: ...

    @overload
    def getValue(self, register: ghidra.program.model.lang.Register, signed: bool) -> long: ...

    @overload
    def getValue(self, register: ghidra.program.model.lang.Register, address: ghidra.program.model.address.Address, signed: bool) -> long:
        """
        Returns the future register value at the specified address.  If no future value is stored,
         it will return the value stored in the program.

         Use this method if keeping separate flows from different flow from addresses is not important.
        @param register the register to get a value for.
        @param address the address at which to get a value.
        @param signed if true, interpret the value as signed.
        @return the value of the register at the location, or null if a full value is not established.
        """
        ...

    @overload
    def getValue(self, register: ghidra.program.model.lang.Register, fromAddr: ghidra.program.model.address.Address, toAddr: ghidra.program.model.address.Address, signed: bool) -> long:
        """
        Returns the future register value at the specified address that occurred because of a flow
         from the fromAddr.  If no future value is stored, it will return the value stored in the program.
        @param register the register to get a value for.
        @param fromAddr the address from which this flow originated.
        @param toAddr the future flow address to save the value.
        @param signed if true, interpret the value as signed.
        @return the value of the register at the location, or null if a full value is not established.
        """
        ...

    def hasValue(self, register: ghidra.program.model.lang.Register) -> bool: ...

    def hashCode(self) -> int: ...

    def isFlowActive(self) -> bool:
        """
        Returns true if a flow has been started and not yet ended.
        @return true if a flow has been started and not yet ended.
        """
        ...

    @overload
    def mergeToFutureFlowState(self, address: ghidra.program.model.address.Address) -> List[ghidra.program.model.lang.RegisterValue]:
        """
        Saves the current processor state for when this context is later used at the given address.
         If the address already has a value, return the value on a collision list!

         Use this method if keeping separate flows from different flow from addresses is not important.
        @param address the address at which to save the current processor state.
        """
        ...

    @overload
    def mergeToFutureFlowState(self, fromAddr: ghidra.program.model.address.Address, destAddr: ghidra.program.model.address.Address) -> List[ghidra.program.model.lang.RegisterValue]:
        """
        Saves the current processor state flowing from the fromAddr to the destAddr for when this context is later used.
         If the address already has a value, return the value on a collision list!
        @param fromAddr the address from which this flow originated
        @param destAddr the address at which to save the current processor state.
        """
        ...

    def notify(self) -> None: ...

    def notifyAll(self) -> None: ...

    @overload
    def setContextRegisterValue(self, value: ghidra.program.model.lang.RegisterValue, address: ghidra.program.model.address.Address) -> None:
        """
        Modify the current context register value at the specified address.  If current
         disassembly flow address equals specified address the current disassembly context
         will be changed, otherwise the future flow state will be changed. This differs from
         {@link #setValue(Register, Address, BigInteger)} in that is can affect the current
         context state at the current address in a non-delayed fashion.

         Use this method if keeping separate flows from different flow from addresses is not important.
        @param value register value
        @param address disassembly address
        """
        ...

    @overload
    def setContextRegisterValue(self, value: ghidra.program.model.lang.RegisterValue, fromAddr: ghidra.program.model.address.Address, toAddr: ghidra.program.model.address.Address) -> None:
        """
        Modify the current context register value at the specified address.  If current
         disassembly toAddr address equals specified address the current disassembly context
         will be changed, otherwise the future flow state flowing from the fromAddr will be changed.
         This differs from {@link #setValue(Register, Address, BigInteger)} in that is can
         affect the current context state at the current address in a non-delayed fashion.
        @param value register value
        @param fromAddr the address from which this flow originated
        @param toAddr the future flow address to save the value.
        """
        ...

    @overload
    def setFutureRegisterValue(self, address: ghidra.program.model.address.Address, value: ghidra.program.model.lang.RegisterValue) -> None: ...

    @overload
    def setFutureRegisterValue(self, fromAddr: ghidra.program.model.address.Address, toAddr: ghidra.program.model.address.Address, value: ghidra.program.model.lang.RegisterValue) -> None: ...

    def setRegisterValue(self, value: ghidra.program.model.lang.RegisterValue) -> None: ...

    @overload
    def setValue(self, register: ghidra.program.model.lang.Register, value: long) -> None: ...

    @overload
    def setValue(self, register: ghidra.program.model.lang.Register, address: ghidra.program.model.address.Address, newValue: long) -> None:
        """
        Sets the value for the given register to be used when the flow advances to the given address
         using either the flowTo() or flowStart() methods.  The new value has precedence over any
         existing value.

         Use this method if keeping separate flows from different flow from addresses is not important.
        @param register the register for which the value is to be saved.
        @param address the future flow address to save the value.
        @param newValue the value to save for future flow.
        """
        ...

    @overload
    def setValue(self, register: ghidra.program.model.lang.Register, fromAddr: ghidra.program.model.address.Address, toAddr: ghidra.program.model.address.Address, newValue: long) -> None:
        """
        Sets the value for the given register to be used when the flow advances to the given address
         using either the flowTo() or flowStart() methods.  The new value has precedence over any
         existing value.
        @param register the register for which the value is to be saved.
        @param fromAddr the address from which this flow originated
        @param toAddr the future flow address to save the value.
        @param newValue the value to save for future flow.
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
    def address(self) -> ghidra.program.model.address.Address: ...

    @property
    def baseContextRegister(self) -> ghidra.program.model.lang.Register: ...

    @property
    def flowActive(self) -> bool: ...

    @property
    def programContext(self) -> ghidra.program.model.listing.ProgramContext: ...

    @property
    def registerValue(self) -> None: ...  # No getter available.

    @registerValue.setter
    def registerValue(self, value: ghidra.program.model.lang.RegisterValue) -> None: ...

    @property
    def registers(self) -> List[object]: ...
