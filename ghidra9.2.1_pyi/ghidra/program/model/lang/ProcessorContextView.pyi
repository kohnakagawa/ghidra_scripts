from typing import List
import ghidra.program.model.lang
import java.lang


class ProcessorContextView(object):
    """
    Defines the interface for an object containing the state
     of all processor registers relative to a specific address.
    """









    @overload
    @staticmethod
    def dumpContextValue(value: ghidra.program.model.lang.RegisterValue, indent: unicode) -> unicode: ...

    @overload
    @staticmethod
    def dumpContextValue(value: ghidra.program.model.lang.RegisterValue, indent: unicode, buf: java.lang.StringBuilder) -> None: ...

    def equals(self, __a0: object) -> bool: ...

    def getBaseContextRegister(self) -> ghidra.program.model.lang.Register:
        """
        @return the base processor context register or null if one
         has not been defined
        """
        ...

    def getClass(self) -> java.lang.Class: ...

    def getRegister(self, name: unicode) -> ghidra.program.model.lang.Register:
        """
        Get a Register given the name of a register
        @param name the name of the register.
        @return The register with the given name.
        """
        ...

    def getRegisterValue(self, register: ghidra.program.model.lang.Register) -> ghidra.program.model.lang.RegisterValue:
        """
        Get the RegisterValue for the given register.
        @param register register to get the value for
        @return RegisterValue object containing the value of the register if a value exists,
         otherwise null.
        """
        ...

    def getRegisters(self) -> List[ghidra.program.model.lang.Register]:
        """
        Returns all the Registers for the processor as an unmodifiable list
        @return all the Registers for the processor
        """
        ...

    def getValue(self, register: ghidra.program.model.lang.Register, signed: bool) -> long:
        """
        Get the contents of a processor register as a BigInteger object
        @param register register to get the value for
        @return a BigInteger object containing the value of the register if a value exists,
         otherwise null.
        """
        ...

    def hasValue(self, register: ghidra.program.model.lang.Register) -> bool:
        """
        Returns true if a value is defined for the given register.
        @param register the register to check for a value.
        @return true if the given register has a value.
        """
        ...

    def hashCode(self) -> int: ...

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
    def baseContextRegister(self) -> ghidra.program.model.lang.Register: ...

    @property
    def registers(self) -> List[object]: ...
