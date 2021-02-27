import ghidra.program.model.address
import ghidra.program.model.lang
import java.lang


class ContextSetting(object):
    """
    Class for context configuration information as
     part of the compiler configuration (CompilerSpec)
    """





    def __init__(self, register: ghidra.program.model.lang.Register, value: long, startAddr: ghidra.program.model.address.Address, endAddr: ghidra.program.model.address.Address): ...



    def equals(self, __a0: object) -> bool: ...

    def getClass(self) -> java.lang.Class: ...

    def getEndAddress(self) -> ghidra.program.model.address.Address: ...

    def getRegister(self) -> ghidra.program.model.lang.Register: ...

    def getStartAddress(self) -> ghidra.program.model.address.Address: ...

    def getValue(self) -> long: ...

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
    def endAddress(self) -> ghidra.program.model.address.Address: ...

    @property
    def register(self) -> ghidra.program.model.lang.Register: ...

    @property
    def startAddress(self) -> ghidra.program.model.address.Address: ...

    @property
    def value(self) -> long: ...