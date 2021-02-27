from typing import List
import ghidra.app.plugin.exceptionhandlers.gcc
import java.lang


class DwarfEHDataApplicationMode(java.lang.Enum):
    DW_EH_PE_absptr: ghidra.app.plugin.exceptionhandlers.gcc.DwarfEHDataApplicationMode = DW_EH_PE_absptr
    DW_EH_PE_aligned: ghidra.app.plugin.exceptionhandlers.gcc.DwarfEHDataApplicationMode = DW_EH_PE_aligned
    DW_EH_PE_datarel: ghidra.app.plugin.exceptionhandlers.gcc.DwarfEHDataApplicationMode = DW_EH_PE_datarel
    DW_EH_PE_funcrel: ghidra.app.plugin.exceptionhandlers.gcc.DwarfEHDataApplicationMode = DW_EH_PE_funcrel
    DW_EH_PE_indirect: ghidra.app.plugin.exceptionhandlers.gcc.DwarfEHDataApplicationMode = DW_EH_PE_indirect
    DW_EH_PE_omit: ghidra.app.plugin.exceptionhandlers.gcc.DwarfEHDataApplicationMode = DW_EH_PE_omit
    DW_EH_PE_pcrel: ghidra.app.plugin.exceptionhandlers.gcc.DwarfEHDataApplicationMode = DW_EH_PE_pcrel
    DW_EH_PE_texrel: ghidra.app.plugin.exceptionhandlers.gcc.DwarfEHDataApplicationMode = DW_EH_PE_texrel







    @overload
    def compareTo(self, __a0: java.lang.Enum) -> int: ...

    @overload
    def compareTo(self, __a0: object) -> int: ...

    def equals(self, __a0: object) -> bool: ...

    def getClass(self) -> java.lang.Class: ...

    def getDeclaringClass(self) -> java.lang.Class: ...

    def hashCode(self) -> int: ...

    def name(self) -> unicode: ...

    def notify(self) -> None: ...

    def notifyAll(self) -> None: ...

    def ordinal(self) -> int: ...

    def toString(self) -> unicode: ...

    @overload
    @staticmethod
    def valueOf(__a0: int) -> ghidra.app.plugin.exceptionhandlers.gcc.DwarfEHDataApplicationMode: ...

    @overload
    @staticmethod
    def valueOf(__a0: unicode) -> ghidra.app.plugin.exceptionhandlers.gcc.DwarfEHDataApplicationMode: ...

    @overload
    @staticmethod
    def valueOf(__a0: java.lang.Class, __a1: unicode) -> java.lang.Enum: ...

    @staticmethod
    def values() -> List[ghidra.app.plugin.exceptionhandlers.gcc.DwarfEHDataApplicationMode]: ...

    @overload
    def wait(self) -> None: ...

    @overload
    def wait(self, __a0: long) -> None: ...

    @overload
    def wait(self, __a0: long, __a1: int) -> None: ...
