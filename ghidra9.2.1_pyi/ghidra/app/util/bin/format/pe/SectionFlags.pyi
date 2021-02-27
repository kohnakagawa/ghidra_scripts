from typing import List
import ghidra.app.util.bin.format.pe
import java.lang
import java.util


class SectionFlags(java.lang.Enum):
    IMAGE_SCN_ALIGN_1024BYTES: ghidra.app.util.bin.format.pe.SectionFlags = IMAGE_SCN_ALIGN_1024BYTES
    IMAGE_SCN_ALIGN_128BYTES: ghidra.app.util.bin.format.pe.SectionFlags = IMAGE_SCN_ALIGN_128BYTES
    IMAGE_SCN_ALIGN_16BYTES: ghidra.app.util.bin.format.pe.SectionFlags = IMAGE_SCN_ALIGN_16BYTES
    IMAGE_SCN_ALIGN_1BYTES: ghidra.app.util.bin.format.pe.SectionFlags = IMAGE_SCN_ALIGN_1BYTES
    IMAGE_SCN_ALIGN_2048BYTES: ghidra.app.util.bin.format.pe.SectionFlags = IMAGE_SCN_ALIGN_2048BYTES
    IMAGE_SCN_ALIGN_256BYTES: ghidra.app.util.bin.format.pe.SectionFlags = IMAGE_SCN_ALIGN_256BYTES
    IMAGE_SCN_ALIGN_2BYTES: ghidra.app.util.bin.format.pe.SectionFlags = IMAGE_SCN_ALIGN_2BYTES
    IMAGE_SCN_ALIGN_32BYTES: ghidra.app.util.bin.format.pe.SectionFlags = IMAGE_SCN_ALIGN_32BYTES
    IMAGE_SCN_ALIGN_4096BYTES: ghidra.app.util.bin.format.pe.SectionFlags = IMAGE_SCN_ALIGN_4096BYTES
    IMAGE_SCN_ALIGN_4BYTES: ghidra.app.util.bin.format.pe.SectionFlags = IMAGE_SCN_ALIGN_4BYTES
    IMAGE_SCN_ALIGN_512BYTES: ghidra.app.util.bin.format.pe.SectionFlags = IMAGE_SCN_ALIGN_512BYTES
    IMAGE_SCN_ALIGN_64BYTES: ghidra.app.util.bin.format.pe.SectionFlags = IMAGE_SCN_ALIGN_64BYTES
    IMAGE_SCN_ALIGN_8192BYTES: ghidra.app.util.bin.format.pe.SectionFlags = IMAGE_SCN_ALIGN_8192BYTES
    IMAGE_SCN_ALIGN_8BYTES: ghidra.app.util.bin.format.pe.SectionFlags = IMAGE_SCN_ALIGN_8BYTES
    IMAGE_SCN_CNT_CODE: ghidra.app.util.bin.format.pe.SectionFlags = IMAGE_SCN_CNT_CODE
    IMAGE_SCN_CNT_INITIALIZED_DATA: ghidra.app.util.bin.format.pe.SectionFlags = IMAGE_SCN_CNT_INITIALIZED_DATA
    IMAGE_SCN_CNT_UNINITIALIZED_DATA: ghidra.app.util.bin.format.pe.SectionFlags = IMAGE_SCN_CNT_UNINITIALIZED_DATA
    IMAGE_SCN_GPREL: ghidra.app.util.bin.format.pe.SectionFlags = IMAGE_SCN_GPREL
    IMAGE_SCN_LNK_COMDAT: ghidra.app.util.bin.format.pe.SectionFlags = IMAGE_SCN_LNK_COMDAT
    IMAGE_SCN_LNK_INFO: ghidra.app.util.bin.format.pe.SectionFlags = IMAGE_SCN_LNK_INFO
    IMAGE_SCN_LNK_NRELOC_OVFL: ghidra.app.util.bin.format.pe.SectionFlags = IMAGE_SCN_LNK_NRELOC_OVFL
    IMAGE_SCN_LNK_OTHER: ghidra.app.util.bin.format.pe.SectionFlags = IMAGE_SCN_LNK_OTHER
    IMAGE_SCN_LNK_REMOVE: ghidra.app.util.bin.format.pe.SectionFlags = IMAGE_SCN_LNK_REMOVE
    IMAGE_SCN_MEM_16BIT: ghidra.app.util.bin.format.pe.SectionFlags = IMAGE_SCN_MEM_16BIT
    IMAGE_SCN_MEM_DISCARDABLE: ghidra.app.util.bin.format.pe.SectionFlags = IMAGE_SCN_MEM_DISCARDABLE
    IMAGE_SCN_MEM_EXECUTE: ghidra.app.util.bin.format.pe.SectionFlags = IMAGE_SCN_MEM_EXECUTE
    IMAGE_SCN_MEM_LOCKED: ghidra.app.util.bin.format.pe.SectionFlags = IMAGE_SCN_MEM_LOCKED
    IMAGE_SCN_MEM_NOT_CACHED: ghidra.app.util.bin.format.pe.SectionFlags = IMAGE_SCN_MEM_NOT_CACHED
    IMAGE_SCN_MEM_NOT_PAGED: ghidra.app.util.bin.format.pe.SectionFlags = IMAGE_SCN_MEM_NOT_PAGED
    IMAGE_SCN_MEM_PRELOAD: ghidra.app.util.bin.format.pe.SectionFlags = IMAGE_SCN_MEM_PRELOAD
    IMAGE_SCN_MEM_PURGEABLE: ghidra.app.util.bin.format.pe.SectionFlags = IMAGE_SCN_MEM_PURGEABLE
    IMAGE_SCN_MEM_READ: ghidra.app.util.bin.format.pe.SectionFlags = IMAGE_SCN_MEM_READ
    IMAGE_SCN_MEM_SHARED: ghidra.app.util.bin.format.pe.SectionFlags = IMAGE_SCN_MEM_SHARED
    IMAGE_SCN_MEM_WRITE: ghidra.app.util.bin.format.pe.SectionFlags = IMAGE_SCN_MEM_WRITE
    IMAGE_SCN_RESERVED_0001: ghidra.app.util.bin.format.pe.SectionFlags = IMAGE_SCN_RESERVED_0001
    IMAGE_SCN_RESERVED_0040: ghidra.app.util.bin.format.pe.SectionFlags = IMAGE_SCN_RESERVED_0040
    IMAGE_SCN_TYPE_NO_PAD: ghidra.app.util.bin.format.pe.SectionFlags = IMAGE_SCN_TYPE_NO_PAD







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
    def resolveFlags(__a0: int) -> java.util.Set: ...

    def toString(self) -> unicode: ...

    @overload
    @staticmethod
    def valueOf(__a0: unicode) -> ghidra.app.util.bin.format.pe.SectionFlags: ...

    @overload
    @staticmethod
    def valueOf(__a0: java.lang.Class, __a1: unicode) -> java.lang.Enum: ...

    @staticmethod
    def values() -> List[ghidra.app.util.bin.format.pe.SectionFlags]: ...

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
