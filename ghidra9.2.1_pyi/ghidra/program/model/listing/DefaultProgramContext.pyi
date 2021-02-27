import ghidra.program.model.address
import ghidra.program.model.lang
import java.lang


class DefaultProgramContext(object):








    def equals(self, __a0: object) -> bool: ...

    def getClass(self) -> java.lang.Class: ...

    def getDefaultValue(self, register: ghidra.program.model.lang.Register, address: ghidra.program.model.address.Address) -> ghidra.program.model.lang.RegisterValue:
        """
        Returns the default value of a register at a given address.
        @param register the register for which to get a default value.
        @param address the address at which to get a default value.
        @return the default value of the register at the given address or null if no default value
         has been assigned.
        """
        ...

    def hashCode(self) -> int: ...

    def notify(self) -> None: ...

    def notifyAll(self) -> None: ...

    def setDefaultValue(self, registerValue: ghidra.program.model.lang.RegisterValue, start: ghidra.program.model.address.Address, end: ghidra.program.model.address.Address) -> None:
        """
        Associates a default value with the given register over the given range.
        @param registerValue the register for which to associate a default value.
        @param start the start address.
        @param end the end address (inclusive)
        """
        ...

    def toString(self) -> unicode: ...

    @overload
    def wait(self) -> None: ...

    @overload
    def wait(self, __a0: long) -> None: ...

    @overload
    def wait(self, __a0: long, __a1: int) -> None: ...
