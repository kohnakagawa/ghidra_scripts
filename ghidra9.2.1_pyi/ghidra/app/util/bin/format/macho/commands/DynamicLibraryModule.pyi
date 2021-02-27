import ghidra.app.util.bin
import ghidra.app.util.bin.format
import ghidra.app.util.bin.format.macho
import ghidra.app.util.bin.format.macho.commands
import ghidra.program.model.data
import java.lang


class DynamicLibraryModule(object, ghidra.app.util.bin.StructConverter):
    ASCII: ghidra.program.model.data.DataType = char
    BYTE: ghidra.program.model.data.DataType = byte
    DWORD: ghidra.program.model.data.DataType = dword
    IBO32: ghidra.program.model.data.DataType = ImageBaseOffset32
    POINTER: ghidra.program.model.data.DataType = pointer
    QWORD: ghidra.program.model.data.DataType = qword
    STRING: ghidra.program.model.data.DataType = string
    UTF16: ghidra.program.model.data.DataType = unicode
    UTF8: ghidra.program.model.data.DataType = string-utf8
    VOID: ghidra.program.model.data.DataType = void
    WORD: ghidra.program.model.data.DataType = word



    def __init__(self):
        """
        DO NOT USE THIS CONSTRUCTOR, USE create*(GenericFactory ...) FACTORY METHODS INSTEAD.
        """
        ...



    @staticmethod
    def createDynamicLibraryModule(reader: ghidra.app.util.bin.format.FactoryBundledWithBinaryReader, header: ghidra.app.util.bin.format.macho.MachHeader) -> ghidra.app.util.bin.format.macho.commands.DynamicLibraryModule: ...

    def equals(self, __a0: object) -> bool: ...

    def getClass(self) -> java.lang.Class: ...

    def getExtDefSymCount(self) -> int: ...

    def getExtDefSymIndex(self) -> int: ...

    def getExternalRelocationCount(self) -> int: ...

    def getExternalRelocationIndex(self) -> int: ...

    def getInitTermCount(self) -> int:
        """
        low 16 bits are the number of init section entries,
         high 16 bits are the number of term section entries
        @return
        """
        ...

    def getInitTermIndex(self) -> int:
        """
        low 16 bits are the index into the init section,
         high 16 bits are the index into the term section
        """
        ...

    def getLocalSymbolCount(self) -> int: ...

    def getLocalSymbolIndex(self) -> int: ...

    def getModuleName(self) -> unicode: ...

    def getModuleNameIndex(self) -> int: ...

    def getObjcModuleInfoAddress(self) -> long: ...

    def getObjcModuleInfoSize(self) -> int: ...

    def getReferenceSymbolTableCount(self) -> int: ...

    def getReferenceSymbolTableIndex(self) -> int: ...

    def hashCode(self) -> int: ...

    def notify(self) -> None: ...

    def notifyAll(self) -> None: ...

    def toDataType(self) -> ghidra.program.model.data.DataType: ...

    def toString(self) -> unicode: ...

    @overload
    def wait(self) -> None: ...

    @overload
    def wait(self, __a0: long) -> None: ...

    @overload
    def wait(self, __a0: long, __a1: int) -> None: ...

    @property
    def extDefSymCount(self) -> int: ...

    @property
    def extDefSymIndex(self) -> int: ...

    @property
    def externalRelocationCount(self) -> int: ...

    @property
    def externalRelocationIndex(self) -> int: ...

    @property
    def initTermCount(self) -> int: ...

    @property
    def initTermIndex(self) -> int: ...

    @property
    def localSymbolCount(self) -> int: ...

    @property
    def localSymbolIndex(self) -> int: ...

    @property
    def moduleName(self) -> unicode: ...

    @property
    def moduleNameIndex(self) -> int: ...

    @property
    def objcModuleInfoAddress(self) -> long: ...

    @property
    def objcModuleInfoSize(self) -> int: ...

    @property
    def referenceSymbolTableCount(self) -> int: ...

    @property
    def referenceSymbolTableIndex(self) -> int: ...
