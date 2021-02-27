from typing import List
import ghidra.program.model.lang
import java.lang


class ProcessorContext(ghidra.program.model.lang.ProcessorContextView, object):
    """
    Defines the interface for an object containing the state
     of all processor registers relative to a specific address.
    """









    def clearRegister(self, register: ghidra.program.model.lang.Register) -> None:
        """
        Clears the register within this context.
        @param register register to be cleared.
        @throws ContextChangeException an illegal attempt to change context was made
        """
        ...

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

    def setRegisterValue(self, value: ghidra.program.model.lang.RegisterValue) -> None:
        """
        Sets the specified register value within this context.
        @param value register value
        @throws ContextChangeException an illegal attempt to change context was made
        """
        ...

    def setValue(self, register: ghidra.program.model.lang.Register, value: long) -> None:
        """
        Sets the value for a Register.
        @param register the register to have its value set
        @param value the value for the register (null is not permitted).
        @throws ContextChangeException an illegal attempt to change context was made
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
    def registerValue(self) -> None: ...  # No getter available.

    @registerValue.setter
    def registerValue(self, value: ghidra.program.model.lang.RegisterValue) -> None: ...

    @property
    def registers(self) -> List[object]: ...
