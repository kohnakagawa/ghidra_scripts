from typing import List
import ghidra.program.model.address
import ghidra.program.model.lang
import java.lang


class DisassemblerContext(ghidra.program.model.lang.ProcessorContext, object):








    def clearRegister(self, __a0: ghidra.program.model.lang.Register) -> None: ...

    @overload
    @staticmethod
    def dumpContextValue(__a0: ghidra.program.model.lang.RegisterValue, __a1: unicode) -> unicode: ...

    @overload
    @staticmethod
    def dumpContextValue(__a0: ghidra.program.model.lang.RegisterValue, __a1: unicode, __a2: java.lang.StringBuilder) -> None: ...

    def equals(self, __a0: object) -> bool: ...

    def getBaseContextRegister(self) -> ghidra.program.model.lang.Register: ...

    def getClass(self) -> java.lang.Class: ...

    def getRegister(self, __a0: unicode) -> ghidra.program.model.lang.Register: ...

    def getRegisterValue(self, __a0: ghidra.program.model.lang.Register) -> ghidra.program.model.lang.RegisterValue: ...

    def getRegisters(self) -> List[object]: ...

    def getValue(self, __a0: ghidra.program.model.lang.Register, __a1: bool) -> long: ...

    def hasValue(self, __a0: ghidra.program.model.lang.Register) -> bool: ...

    def hashCode(self) -> int: ...

    def notify(self) -> None: ...

    def notifyAll(self) -> None: ...

    @overload
    def setFutureRegisterValue(self, address: ghidra.program.model.address.Address, value: ghidra.program.model.lang.RegisterValue) -> None:
        """
        Combines <code>value</code> with any previously saved future
         register value at <code>address</code> or any value stored in the program if there is no
         previously saved future value.  Use this method when multiple flows to the same address
         don't matter or the flowing from address is unknown.
         <br>
         When <code>value</code> has conflicting bits with the previously
         saved value, <code>value</code> will take precedence.
         <br>
         If the register value is the value for the
         processor context register and a previously saved
         value does not exist, the user saved values in the
         stored context of the program will be used as existing
         value.
        @param address the address to store the register value
        @param value the register value to store at the address
        """
        ...

    @overload
    def setFutureRegisterValue(self, fromAddr: ghidra.program.model.address.Address, toAddr: ghidra.program.model.address.Address, value: ghidra.program.model.lang.RegisterValue) -> None:
        """
        Combines <code>value</code> with any previously saved future
         register value at <code>fromAddr/toAddr</code> or any value stored in the program if there is no
         previously saved future value.
         <br>
         When <code>value</code> has conflicting bits with the previously
         saved value, <code>value</code> will take precedence.
         <br>
         If the register value is the value for the
         processor context register and a previously saved
         value does not exist, the user saved values in the
         stored context of the program will be used as existing
         value.
        @param fromAddr the address this value if flowing from
        @param toAddr the address to store the register value
        @param value the register value to store at the address
        """
        ...

    def setRegisterValue(self, __a0: ghidra.program.model.lang.RegisterValue) -> None: ...

    def setValue(self, __a0: ghidra.program.model.lang.Register, __a1: long) -> None: ...

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
    def registerValue(self) -> None: ...  # No getter available.

    @registerValue.setter
    def registerValue(self, value: ghidra.program.model.lang.RegisterValue) -> None: ...

    @property
    def registers(self) -> List[object]: ...
