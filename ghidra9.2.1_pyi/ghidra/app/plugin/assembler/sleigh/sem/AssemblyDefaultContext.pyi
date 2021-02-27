from typing import List
import ghidra.app.plugin.assembler.sleigh.sem
import ghidra.program.model.address
import ghidra.program.model.lang
import ghidra.program.model.listing
import java.lang


class AssemblyDefaultContext(object, ghidra.program.model.lang.DisassemblerContext, ghidra.program.model.listing.DefaultProgramContext):
    """
    A class that computes the default context for a language, and acts as a pseudo context

     This class helps maintain context consistency when performing both assembly and disassembly.
    """





    def __init__(self, lang: ghidra.app.plugin.processors.sleigh.SleighLanguage):
        """
        Compute the default context at most addresses for the given language
        @param lang the language
        """
        ...



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

    def getDefault(self) -> ghidra.app.plugin.assembler.sleigh.sem.AssemblyPatternBlock:
        """
        Get the default value of the context register
        @return the value as a pattern block for assembly
        """
        ...

    def getDefaultAt(self, addr: ghidra.program.model.address.Address) -> ghidra.app.plugin.assembler.sleigh.sem.AssemblyPatternBlock:
        """
        Compute the default value of the context register at the given address
        @param addr the addres
        @return the value as a pattern block for assembly
        """
        ...

    def getDefaultValue(self, register: ghidra.program.model.lang.Register, address: ghidra.program.model.address.Address) -> ghidra.program.model.lang.RegisterValue: ...

    def getRegister(self, name: unicode) -> ghidra.program.model.lang.Register: ...

    def getRegisterValue(self, register: ghidra.program.model.lang.Register) -> ghidra.program.model.lang.RegisterValue: ...

    def getRegisters(self) -> List[ghidra.program.model.lang.Register]: ...

    def getValue(self, register: ghidra.program.model.lang.Register, signed: bool) -> long: ...

    def hasValue(self, register: ghidra.program.model.lang.Register) -> bool: ...

    def hashCode(self) -> int: ...

    def notify(self) -> None: ...

    def notifyAll(self) -> None: ...

    def setContextRegister(self, val: List[int]) -> None:
        """
        Set the value of the pseudo context register

         If the provided value has length less than the register, it will be left aligned, and the
         remaining bytes will be set to unknown (masked out).
        @param val the value of the register
        """
        ...

    def setDefaultValue(self, registerValue: ghidra.program.model.lang.RegisterValue, start: ghidra.program.model.address.Address, end: ghidra.program.model.address.Address) -> None: ...

    @overload
    def setFutureRegisterValue(self, address: ghidra.program.model.address.Address, value: ghidra.program.model.lang.RegisterValue) -> None: ...

    @overload
    def setFutureRegisterValue(self, fromAddr: ghidra.program.model.address.Address, toAddr: ghidra.program.model.address.Address, value: ghidra.program.model.lang.RegisterValue) -> None: ...

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
    def contextRegister(self) -> None: ...  # No getter available.

    @contextRegister.setter
    def contextRegister(self, value: List[int]) -> None: ...

    @property
    def default(self) -> ghidra.app.plugin.assembler.sleigh.sem.AssemblyPatternBlock: ...

    @property
    def registerValue(self) -> None: ...  # No getter available.

    @registerValue.setter
    def registerValue(self, value: ghidra.program.model.lang.RegisterValue) -> None: ...

    @property
    def registers(self) -> List[object]: ...
