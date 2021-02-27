from typing import List
import ghidra.app.util.bin.format.elf
import java.lang
import java.util


class ElfDynamicType(object):
    DF_1_DIRECT: int = 256
    DF_1_GLOBAL: int = 2
    DF_1_GROUP: int = 4
    DF_1_INITFIRST: int = 32
    DF_1_INTERPOSE: int = 1024
    DF_1_LOADFLTR: int = 16
    DF_1_NODEFLIB: int = 2048
    DF_1_NODELETE: int = 8
    DF_1_NOOPEN: int = 64
    DF_1_NOW: int = 1
    DF_1_ORIGIN: int = 128
    DF_BIND_NOW: int = 8
    DF_ORIGIN: int = 1
    DF_STATIC_TLS: int = 16
    DF_SYMBOLIC: int = 2
    DF_TEXTREL: int = 4
    DT_ANDROID_REL: ghidra.app.util.bin.format.elf.ElfDynamicType
    DT_ANDROID_RELA: ghidra.app.util.bin.format.elf.ElfDynamicType
    DT_ANDROID_RELASZ: ghidra.app.util.bin.format.elf.ElfDynamicType
    DT_ANDROID_RELR: ghidra.app.util.bin.format.elf.ElfDynamicType
    DT_ANDROID_RELRENT: ghidra.app.util.bin.format.elf.ElfDynamicType
    DT_ANDROID_RELRSZ: ghidra.app.util.bin.format.elf.ElfDynamicType
    DT_ANDROID_RELSZ: ghidra.app.util.bin.format.elf.ElfDynamicType
    DT_AUDIT: ghidra.app.util.bin.format.elf.ElfDynamicType
    DT_AUXILIARY: ghidra.app.util.bin.format.elf.ElfDynamicType
    DT_BIND_NOW: ghidra.app.util.bin.format.elf.ElfDynamicType
    DT_CHECKSUM: ghidra.app.util.bin.format.elf.ElfDynamicType
    DT_CONFIG: ghidra.app.util.bin.format.elf.ElfDynamicType
    DT_DEBUG: ghidra.app.util.bin.format.elf.ElfDynamicType
    DT_DEPAUDIT: ghidra.app.util.bin.format.elf.ElfDynamicType
    DT_FEATURE_1: ghidra.app.util.bin.format.elf.ElfDynamicType
    DT_FILTER: ghidra.app.util.bin.format.elf.ElfDynamicType
    DT_FINI: ghidra.app.util.bin.format.elf.ElfDynamicType
    DT_FINI_ARRAY: ghidra.app.util.bin.format.elf.ElfDynamicType
    DT_FINI_ARRAYSZ: ghidra.app.util.bin.format.elf.ElfDynamicType
    DT_FLAGS: ghidra.app.util.bin.format.elf.ElfDynamicType
    DT_FLAGS_1: ghidra.app.util.bin.format.elf.ElfDynamicType
    DT_GNU_CONFLICT: ghidra.app.util.bin.format.elf.ElfDynamicType
    DT_GNU_CONFLICTSZ: ghidra.app.util.bin.format.elf.ElfDynamicType
    DT_GNU_HASH: ghidra.app.util.bin.format.elf.ElfDynamicType
    DT_GNU_LIBLIST: ghidra.app.util.bin.format.elf.ElfDynamicType
    DT_GNU_LIBLISTSZ: ghidra.app.util.bin.format.elf.ElfDynamicType
    DT_GNU_PRELINKED: ghidra.app.util.bin.format.elf.ElfDynamicType
    DT_HASH: ghidra.app.util.bin.format.elf.ElfDynamicType
    DT_INIT: ghidra.app.util.bin.format.elf.ElfDynamicType
    DT_INIT_ARRAY: ghidra.app.util.bin.format.elf.ElfDynamicType
    DT_INIT_ARRAYSZ: ghidra.app.util.bin.format.elf.ElfDynamicType
    DT_JMPREL: ghidra.app.util.bin.format.elf.ElfDynamicType
    DT_MOVEENT: ghidra.app.util.bin.format.elf.ElfDynamicType
    DT_MOVESZ: ghidra.app.util.bin.format.elf.ElfDynamicType
    DT_MOVETAB: ghidra.app.util.bin.format.elf.ElfDynamicType
    DT_NEEDED: ghidra.app.util.bin.format.elf.ElfDynamicType
    DT_NULL: ghidra.app.util.bin.format.elf.ElfDynamicType
    DT_PLTGOT: ghidra.app.util.bin.format.elf.ElfDynamicType
    DT_PLTPAD: ghidra.app.util.bin.format.elf.ElfDynamicType
    DT_PLTPADSZ: ghidra.app.util.bin.format.elf.ElfDynamicType
    DT_PLTREL: ghidra.app.util.bin.format.elf.ElfDynamicType
    DT_PLTRELSZ: ghidra.app.util.bin.format.elf.ElfDynamicType
    DT_POSFLAG_1: ghidra.app.util.bin.format.elf.ElfDynamicType
    DT_PREINIT_ARRAY: ghidra.app.util.bin.format.elf.ElfDynamicType
    DT_PREINIT_ARRAYSZ: ghidra.app.util.bin.format.elf.ElfDynamicType
    DT_REL: ghidra.app.util.bin.format.elf.ElfDynamicType
    DT_RELA: ghidra.app.util.bin.format.elf.ElfDynamicType
    DT_RELACOUNT: ghidra.app.util.bin.format.elf.ElfDynamicType
    DT_RELAENT: ghidra.app.util.bin.format.elf.ElfDynamicType
    DT_RELASZ: ghidra.app.util.bin.format.elf.ElfDynamicType
    DT_RELCOUNT: ghidra.app.util.bin.format.elf.ElfDynamicType
    DT_RELENT: ghidra.app.util.bin.format.elf.ElfDynamicType
    DT_RELR: ghidra.app.util.bin.format.elf.ElfDynamicType
    DT_RELRENT: ghidra.app.util.bin.format.elf.ElfDynamicType
    DT_RELRSZ: ghidra.app.util.bin.format.elf.ElfDynamicType
    DT_RELSZ: ghidra.app.util.bin.format.elf.ElfDynamicType
    DT_RPATH: ghidra.app.util.bin.format.elf.ElfDynamicType
    DT_RUNPATH: ghidra.app.util.bin.format.elf.ElfDynamicType
    DT_SONAME: ghidra.app.util.bin.format.elf.ElfDynamicType
    DT_STRSZ: ghidra.app.util.bin.format.elf.ElfDynamicType
    DT_STRTAB: ghidra.app.util.bin.format.elf.ElfDynamicType
    DT_SYMBOLIC: ghidra.app.util.bin.format.elf.ElfDynamicType
    DT_SYMENT: ghidra.app.util.bin.format.elf.ElfDynamicType
    DT_SYMINENT: ghidra.app.util.bin.format.elf.ElfDynamicType
    DT_SYMINFO: ghidra.app.util.bin.format.elf.ElfDynamicType
    DT_SYMINSZ: ghidra.app.util.bin.format.elf.ElfDynamicType
    DT_SYMTAB: ghidra.app.util.bin.format.elf.ElfDynamicType
    DT_TEXTREL: ghidra.app.util.bin.format.elf.ElfDynamicType
    DT_TLSDESC_GOT: ghidra.app.util.bin.format.elf.ElfDynamicType
    DT_TLSDESC_PLT: ghidra.app.util.bin.format.elf.ElfDynamicType
    DT_VERDEF: ghidra.app.util.bin.format.elf.ElfDynamicType
    DT_VERDEFNUM: ghidra.app.util.bin.format.elf.ElfDynamicType
    DT_VERNEED: ghidra.app.util.bin.format.elf.ElfDynamicType
    DT_VERNEEDNUM: ghidra.app.util.bin.format.elf.ElfDynamicType
    DT_VERSYM: ghidra.app.util.bin.format.elf.ElfDynamicType
    description: unicode
    name: unicode
    value: int
    valueType: ghidra.app.util.bin.format.elf.ElfDynamicType.ElfDynamicValueType




    class ElfDynamicValueType(java.lang.Enum):
        ADDRESS: ghidra.app.util.bin.format.elf.ElfDynamicType.ElfDynamicValueType = ADDRESS
        STRING: ghidra.app.util.bin.format.elf.ElfDynamicType.ElfDynamicValueType = STRING
        VALUE: ghidra.app.util.bin.format.elf.ElfDynamicType.ElfDynamicValueType = VALUE







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
        def valueOf(__a0: unicode) -> ghidra.app.util.bin.format.elf.ElfDynamicType.ElfDynamicValueType: ...

        @overload
        @staticmethod
        def valueOf(__a0: java.lang.Class, __a1: unicode) -> java.lang.Enum: ...

        @staticmethod
        def values() -> List[ghidra.app.util.bin.format.elf.ElfDynamicType.ElfDynamicValueType]: ...

        @overload
        def wait(self) -> None: ...

        @overload
        def wait(self, __a0: long) -> None: ...

        @overload
        def wait(self, __a0: long, __a1: int) -> None: ...



    def __init__(self, value: int, name: unicode, description: unicode, valueType: ghidra.app.util.bin.format.elf.ElfDynamicType.ElfDynamicValueType): ...



    @staticmethod
    def addDefaultTypes(dynamicTypeMap: java.util.Map) -> None: ...

    @staticmethod
    def addDynamicType(type: ghidra.app.util.bin.format.elf.ElfDynamicType, dynamicTypeMap: java.util.Map) -> None:
        """
        Add the specified dynamic entry type to the specified map.
        @param type dynamic entry type
        @param dynamicTypeMap
        @throws DuplicateNameException if new type name already defined within
         the specified map
        """
        ...

    def equals(self, __a0: object) -> bool: ...

    def getClass(self) -> java.lang.Class: ...

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
