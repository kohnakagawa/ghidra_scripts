from typing import List
import ghidra.app.util.bin.format.pe
import java.lang
import java.util


class DllCharacteristics(java.lang.Enum):
    IMAGE_DLLCHARACTERISTICS_APPCONTAINER: ghidra.app.util.bin.format.pe.DllCharacteristics = IMAGE_DLLCHARACTERISTICS_APPCONTAINER
    IMAGE_DLLCHARACTERISTICS_DYNAMIC_BASE: ghidra.app.util.bin.format.pe.DllCharacteristics = IMAGE_DLLCHARACTERISTICS_DYNAMIC_BASE
    IMAGE_DLLCHARACTERISTICS_FORCE_INTEGRITY: ghidra.app.util.bin.format.pe.DllCharacteristics = IMAGE_DLLCHARACTERISTICS_FORCE_INTEGRITY
    IMAGE_DLLCHARACTERISTICS_GUARD_CF: ghidra.app.util.bin.format.pe.DllCharacteristics = IMAGE_DLLCHARACTERISTICS_GUARD_CF
    IMAGE_DLLCHARACTERISTICS_HIGH_ENTROPY_VA: ghidra.app.util.bin.format.pe.DllCharacteristics = IMAGE_DLLCHARACTERISTICS_HIGH_ENTROPY_VA
    IMAGE_DLLCHARACTERISTICS_NO_BIND: ghidra.app.util.bin.format.pe.DllCharacteristics = IMAGE_DLLCHARACTERISTICS_NO_BIND
    IMAGE_DLLCHARACTERISTICS_NO_ISOLATION: ghidra.app.util.bin.format.pe.DllCharacteristics = IMAGE_DLLCHARACTERISTICS_NO_ISOLATION
    IMAGE_DLLCHARACTERISTICS_NO_SEH: ghidra.app.util.bin.format.pe.DllCharacteristics = IMAGE_DLLCHARACTERISTICS_NO_SEH
    IMAGE_DLLCHARACTERISTICS_NX_COMPAT: ghidra.app.util.bin.format.pe.DllCharacteristics = IMAGE_DLLCHARACTERISTICS_NX_COMPAT
    IMAGE_DLLCHARACTERISTICS_TERMINAL_SERVER_AWARE: ghidra.app.util.bin.format.pe.DllCharacteristics = IMAGE_DLLCHARACTERISTICS_TERMINAL_SERVER_AWARE
    IMAGE_DLLCHARACTERISTICS_WDM_DRIVER: ghidra.app.util.bin.format.pe.DllCharacteristics = IMAGE_DLLCHARACTERISTICS_WDM_DRIVER







    @overload
    def compareTo(self, __a0: java.lang.Enum) -> int: ...

    @overload
    def compareTo(self, __a0: object) -> int: ...

    def equals(self, __a0: object) -> bool: ...

    def getAlias(self) -> unicode: ...

    def getClass(self) -> java.lang.Class: ...

    def getDeclaringClass(self) -> java.lang.Class: ...

    def getDescription(self) -> unicode: ...

    def getMask(self) -> int: ...

    def hashCode(self) -> int: ...

    def name(self) -> unicode: ...

    def notify(self) -> None: ...

    def notifyAll(self) -> None: ...

    def ordinal(self) -> int: ...

    @staticmethod
    def resolveCharacteristics(__a0: int) -> java.util.Set: ...

    def toString(self) -> unicode: ...

    @overload
    @staticmethod
    def valueOf(__a0: unicode) -> ghidra.app.util.bin.format.pe.DllCharacteristics: ...

    @overload
    @staticmethod
    def valueOf(__a0: java.lang.Class, __a1: unicode) -> java.lang.Enum: ...

    @staticmethod
    def values() -> List[ghidra.app.util.bin.format.pe.DllCharacteristics]: ...

    @overload
    def wait(self) -> None: ...

    @overload
    def wait(self, __a0: long) -> None: ...

    @overload
    def wait(self, __a0: long, __a1: int) -> None: ...

    @property
    def alias(self) -> unicode: ...

    @property
    def description(self) -> unicode: ...

    @property
    def mask(self) -> int: ...
