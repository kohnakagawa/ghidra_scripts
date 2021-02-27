from typing import List
import ghidra.app.plugin.exceptionhandlers.gcc
import java.lang


class DwarfEHDataDecodeFormat(java.lang.Enum):
    DW_EH_PE_absptr: ghidra.app.plugin.exceptionhandlers.gcc.DwarfEHDataDecodeFormat = DW_EH_PE_absptr
    DW_EH_PE_omit: ghidra.app.plugin.exceptionhandlers.gcc.DwarfEHDataDecodeFormat = DW_EH_PE_omit
    DW_EH_PE_sdata2: ghidra.app.plugin.exceptionhandlers.gcc.DwarfEHDataDecodeFormat = DW_EH_PE_sdata2
    DW_EH_PE_sdata4: ghidra.app.plugin.exceptionhandlers.gcc.DwarfEHDataDecodeFormat = DW_EH_PE_sdata4
    DW_EH_PE_sdata8: ghidra.app.plugin.exceptionhandlers.gcc.DwarfEHDataDecodeFormat = DW_EH_PE_sdata8
    DW_EH_PE_signed: ghidra.app.plugin.exceptionhandlers.gcc.DwarfEHDataDecodeFormat = DW_EH_PE_signed
    DW_EH_PE_sleb128: ghidra.app.plugin.exceptionhandlers.gcc.DwarfEHDataDecodeFormat = DW_EH_PE_sleb128
    DW_EH_PE_udata2: ghidra.app.plugin.exceptionhandlers.gcc.DwarfEHDataDecodeFormat = DW_EH_PE_udata2
    DW_EH_PE_udata4: ghidra.app.plugin.exceptionhandlers.gcc.DwarfEHDataDecodeFormat = DW_EH_PE_udata4
    DW_EH_PE_udata8: ghidra.app.plugin.exceptionhandlers.gcc.DwarfEHDataDecodeFormat = DW_EH_PE_udata8
    DW_EH_PE_uleb128: ghidra.app.plugin.exceptionhandlers.gcc.DwarfEHDataDecodeFormat = DW_EH_PE_uleb128







    @overload
    def compareTo(self, __a0: java.lang.Enum) -> int: ...

    @overload
    def compareTo(self, __a0: object) -> int: ...

    def equals(self, __a0: object) -> bool: ...

    def getClass(self) -> java.lang.Class: ...

    def getCode(self) -> int: ...

    def getDeclaringClass(self) -> java.lang.Class: ...

    def hashCode(self) -> int: ...

    def name(self) -> unicode: ...

    def notify(self) -> None: ...

    def notifyAll(self) -> None: ...

    def ordinal(self) -> int: ...

    def toString(self) -> unicode: ...

    @overload
    @staticmethod
    def valueOf(__a0: int) -> ghidra.app.plugin.exceptionhandlers.gcc.DwarfEHDataDecodeFormat: ...

    @overload
    @staticmethod
    def valueOf(__a0: unicode) -> ghidra.app.plugin.exceptionhandlers.gcc.DwarfEHDataDecodeFormat: ...

    @overload
    @staticmethod
    def valueOf(__a0: java.lang.Class, __a1: unicode) -> java.lang.Enum: ...

    @staticmethod
    def values() -> List[ghidra.app.plugin.exceptionhandlers.gcc.DwarfEHDataDecodeFormat]: ...

    @overload
    def wait(self) -> None: ...

    @overload
    def wait(self, __a0: long) -> None: ...

    @overload
    def wait(self, __a0: long, __a1: int) -> None: ...

    @property
    def code(self) -> int: ...
