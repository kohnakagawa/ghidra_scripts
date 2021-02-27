from typing import List
import ghidra.app.util.bin.format.pe
import java.lang


class PeSubsystem(java.lang.Enum):
    IMAGE_SUBSYSTEM_EFI_APPLICATION: ghidra.app.util.bin.format.pe.PeSubsystem = IMAGE_SUBSYSTEM_EFI_APPLICATION
    IMAGE_SUBSYSTEM_EFI_BOOT_SERVICE_DRIVER: ghidra.app.util.bin.format.pe.PeSubsystem = IMAGE_SUBSYSTEM_EFI_BOOT_SERVICE_DRIVER
    IMAGE_SUBSYSTEM_EFI_ROM: ghidra.app.util.bin.format.pe.PeSubsystem = IMAGE_SUBSYSTEM_EFI_ROM
    IMAGE_SUBSYSTEM_EFI_RUNTIME_DRIVER: ghidra.app.util.bin.format.pe.PeSubsystem = IMAGE_SUBSYSTEM_EFI_RUNTIME_DRIVER
    IMAGE_SUBSYSTEM_NATIVE: ghidra.app.util.bin.format.pe.PeSubsystem = IMAGE_SUBSYSTEM_NATIVE
    IMAGE_SUBSYSTEM_NATIVE_WINDOWS: ghidra.app.util.bin.format.pe.PeSubsystem = IMAGE_SUBSYSTEM_NATIVE_WINDOWS
    IMAGE_SUBSYSTEM_OS2_CUI: ghidra.app.util.bin.format.pe.PeSubsystem = IMAGE_SUBSYSTEM_OS2_CUI
    IMAGE_SUBSYSTEM_POSIX_CUI: ghidra.app.util.bin.format.pe.PeSubsystem = IMAGE_SUBSYSTEM_POSIX_CUI
    IMAGE_SUBSYSTEM_UNKNOWN: ghidra.app.util.bin.format.pe.PeSubsystem = IMAGE_SUBSYSTEM_UNKNOWN
    IMAGE_SUBSYSTEM_WINDOWS_BOOT_APPLICATION: ghidra.app.util.bin.format.pe.PeSubsystem = IMAGE_SUBSYSTEM_WINDOWS_BOOT_APPLICATION
    IMAGE_SUBSYSTEM_WINDOWS_CE_GUI: ghidra.app.util.bin.format.pe.PeSubsystem = IMAGE_SUBSYSTEM_WINDOWS_CE_GUI
    IMAGE_SUBSYSTEM_WINDOWS_CUI: ghidra.app.util.bin.format.pe.PeSubsystem = IMAGE_SUBSYSTEM_WINDOWS_CUI
    IMAGE_SUBSYSTEM_WINDOWS_GUI: ghidra.app.util.bin.format.pe.PeSubsystem = IMAGE_SUBSYSTEM_WINDOWS_GUI
    IMAGE_SUBSYSTEM_XBOX: ghidra.app.util.bin.format.pe.PeSubsystem = IMAGE_SUBSYSTEM_XBOX







    @overload
    def compareTo(self, __a0: java.lang.Enum) -> int: ...

    @overload
    def compareTo(self, __a0: object) -> int: ...

    def equals(self, __a0: object) -> bool: ...

    def getAlias(self) -> unicode: ...

    def getClass(self) -> java.lang.Class: ...

    def getDeclaringClass(self) -> java.lang.Class: ...

    def getDescription(self) -> unicode: ...

    def getValue(self) -> int: ...

    def hashCode(self) -> int: ...

    def name(self) -> unicode: ...

    def notify(self) -> None: ...

    def notifyAll(self) -> None: ...

    def ordinal(self) -> int: ...

    @staticmethod
    def parse(__a0: int) -> ghidra.app.util.bin.format.pe.PeSubsystem: ...

    def toString(self) -> unicode: ...

    @overload
    @staticmethod
    def valueOf(__a0: unicode) -> ghidra.app.util.bin.format.pe.PeSubsystem: ...

    @overload
    @staticmethod
    def valueOf(__a0: java.lang.Class, __a1: unicode) -> java.lang.Enum: ...

    @staticmethod
    def values() -> List[ghidra.app.util.bin.format.pe.PeSubsystem]: ...

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
    def value(self) -> int: ...
