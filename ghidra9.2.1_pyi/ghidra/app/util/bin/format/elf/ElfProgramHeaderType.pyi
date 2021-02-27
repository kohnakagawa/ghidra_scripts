import ghidra.app.util.bin.format.elf
import ghidra.program.model.data
import java.lang
import java.util


class ElfProgramHeaderType(object):
    PT_DYNAMIC: ghidra.app.util.bin.format.elf.ElfProgramHeaderType
    PT_GNU_EH_FRAME: ghidra.app.util.bin.format.elf.ElfProgramHeaderType
    PT_GNU_RELRO: ghidra.app.util.bin.format.elf.ElfProgramHeaderType
    PT_GNU_STACK: ghidra.app.util.bin.format.elf.ElfProgramHeaderType
    PT_INTERP: ghidra.app.util.bin.format.elf.ElfProgramHeaderType
    PT_LOAD: ghidra.app.util.bin.format.elf.ElfProgramHeaderType
    PT_NOTE: ghidra.app.util.bin.format.elf.ElfProgramHeaderType
    PT_NULL: ghidra.app.util.bin.format.elf.ElfProgramHeaderType
    PT_PHDR: ghidra.app.util.bin.format.elf.ElfProgramHeaderType
    PT_SHLIB: ghidra.app.util.bin.format.elf.ElfProgramHeaderType
    PT_TLS: ghidra.app.util.bin.format.elf.ElfProgramHeaderType
    description: unicode
    name: unicode
    value: int



    def __init__(self, value: int, name: unicode, description: unicode): ...



    @staticmethod
    def addDefaultTypes(programHeaderTypeMap: java.util.Map) -> None: ...

    @staticmethod
    def addProgramHeaderType(type: ghidra.app.util.bin.format.elf.ElfProgramHeaderType, programHeaderTypeMap: java.util.Map) -> None:
        """
        Add the specified program header type to the specified map.
        @param type program header type
        @param programHeaderTypeMap
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
