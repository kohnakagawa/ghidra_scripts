import ghidra.app.util.bin.format.elf
import ghidra.program.model.data
import java.lang
import java.util


class ElfSectionHeaderType(object):
    SHT_ANDROID_REL: ghidra.app.util.bin.format.elf.ElfSectionHeaderType
    SHT_ANDROID_RELA: ghidra.app.util.bin.format.elf.ElfSectionHeaderType
    SHT_CHECKSUM: ghidra.app.util.bin.format.elf.ElfSectionHeaderType
    SHT_DYNAMIC: ghidra.app.util.bin.format.elf.ElfSectionHeaderType
    SHT_DYNSYM: ghidra.app.util.bin.format.elf.ElfSectionHeaderType
    SHT_FINI_ARRAY: ghidra.app.util.bin.format.elf.ElfSectionHeaderType
    SHT_GNU_ATTRIBUTES: ghidra.app.util.bin.format.elf.ElfSectionHeaderType
    SHT_GNU_HASH: ghidra.app.util.bin.format.elf.ElfSectionHeaderType
    SHT_GNU_LIBLIST: ghidra.app.util.bin.format.elf.ElfSectionHeaderType
    SHT_GNU_verdef: ghidra.app.util.bin.format.elf.ElfSectionHeaderType
    SHT_GNU_verneed: ghidra.app.util.bin.format.elf.ElfSectionHeaderType
    SHT_GNU_versym: ghidra.app.util.bin.format.elf.ElfSectionHeaderType
    SHT_GROUP: ghidra.app.util.bin.format.elf.ElfSectionHeaderType
    SHT_HASH: ghidra.app.util.bin.format.elf.ElfSectionHeaderType
    SHT_INIT_ARRAY: ghidra.app.util.bin.format.elf.ElfSectionHeaderType
    SHT_NOBITS: ghidra.app.util.bin.format.elf.ElfSectionHeaderType
    SHT_NOTE: ghidra.app.util.bin.format.elf.ElfSectionHeaderType
    SHT_NULL: ghidra.app.util.bin.format.elf.ElfSectionHeaderType
    SHT_PREINIT_ARRAY: ghidra.app.util.bin.format.elf.ElfSectionHeaderType
    SHT_PROGBITS: ghidra.app.util.bin.format.elf.ElfSectionHeaderType
    SHT_REL: ghidra.app.util.bin.format.elf.ElfSectionHeaderType
    SHT_RELA: ghidra.app.util.bin.format.elf.ElfSectionHeaderType
    SHT_SHLIB: ghidra.app.util.bin.format.elf.ElfSectionHeaderType
    SHT_STRTAB: ghidra.app.util.bin.format.elf.ElfSectionHeaderType
    SHT_SUNW_COMDAT: ghidra.app.util.bin.format.elf.ElfSectionHeaderType
    SHT_SUNW_move: ghidra.app.util.bin.format.elf.ElfSectionHeaderType
    SHT_SUNW_syminfo: ghidra.app.util.bin.format.elf.ElfSectionHeaderType
    SHT_SYMTAB: ghidra.app.util.bin.format.elf.ElfSectionHeaderType
    SHT_SYMTAB_SHNDX: ghidra.app.util.bin.format.elf.ElfSectionHeaderType
    description: unicode
    name: unicode
    value: int



    def __init__(self, value: int, name: unicode, description: unicode): ...



    @staticmethod
    def addDefaultTypes(programHeaderTypeMap: java.util.Map) -> None: ...

    @staticmethod
    def addSectionHeaderType(type: ghidra.app.util.bin.format.elf.ElfSectionHeaderType, sectionHeaderTypeMap: java.util.Map) -> None:
        """
        Add the specified section header type to the specified map.
        @param type section header type
        @param sectionHeaderTypeMap
        @throws DuplicateNameException if new type name already defined within
         the specified map
        """
        ...

    def equals(self, __a0: object) -> bool: ...

    def getClass(self) -> java.lang.Class: ...

    @staticmethod
    def getEnumDataType(is32bit: bool, typeSuffix: unicode, dynamicTypeMap: java.util.Map) -> ghidra.program.model.data.EnumDataType: ...

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
