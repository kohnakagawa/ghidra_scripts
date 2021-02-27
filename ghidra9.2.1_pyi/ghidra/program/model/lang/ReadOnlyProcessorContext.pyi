from typing import List
import ghidra.program.model.lang
import java.lang


class ReadOnlyProcessorContext(object, ghidra.program.model.lang.ProcessorContext):




    def __init__(self, context: ghidra.program.model.lang.ProcessorContextView): ...



    def clearRegister(self, register: ghidra.program.model.lang.Register) -> None: ...

    @overload
    @staticmethod
    def dumpContextValue(__a0: ghidra.program.model.lang.RegisterValue, __a1: unicode) -> unicode: ...

    @overload
    @staticmethod
    def dumpContextValue(__a0: ghidra.program.model.lang.RegisterValue, __a1: unicode, __a2: java.lang.StringBuilder) -> None: ...

    def equals(self, __a0: object) -> bool: ...

    def getBaseContextRegister(self) -> ghidra.program.model.lang.Register: ...

    def getClass(self) -> java.lang.Class: ...

    def getRegister(self, name: unicode) -> ghidra.program.model.lang.Register: ...

    def getRegisterValue(self, register: ghidra.program.model.lang.Register) -> ghidra.program.model.lang.RegisterValue: ...

    def getRegisters(self) -> List[ghidra.program.model.lang.Register]: ...

    def getValue(self, register: ghidra.program.model.lang.Register, signed: bool) -> long: ...

    def hasValue(self, register: ghidra.program.model.lang.Register) -> bool: ...

    def hashCode(self) -> int: ...

    def notify(self) -> None: ...

    def notifyAll(self) -> None: ...

    def setRegisterValue(self, value: ghidra.program.model.lang.RegisterValue) -> None: ...

    def setValue(self, register: ghidra.program.model.lang.Register, value: long) -> None: ...

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