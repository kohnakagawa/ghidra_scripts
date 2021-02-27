import ghidra.app.util.bin
import ghidra.app.util.bin.format
import ghidra.app.util.bin.format.macho.commands
import ghidra.program.model.data
import java.lang


class DynamicLibrary(object, ghidra.app.util.bin.StructConverter):
    """
    Represents a dylib structure.
    """

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
    def createDynamicLibrary(reader: ghidra.app.util.bin.format.FactoryBundledWithBinaryReader, command: ghidra.app.util.bin.format.macho.commands.LoadCommand) -> ghidra.app.util.bin.format.macho.commands.DynamicLibrary: ...

    def equals(self, __a0: object) -> bool: ...

    def getClass(self) -> java.lang.Class: ...

    def getCompatibilityVersion(self) -> int: ...

    def getCurrentVersion(self) -> int: ...

    def getName(self) -> ghidra.app.util.bin.format.macho.commands.LoadCommandString: ...

    def getTimestamp(self) -> int: ...

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
    def compatibilityVersion(self) -> int: ...

    @property
    def currentVersion(self) -> int: ...

    @property
    def name(self) -> ghidra.app.util.bin.format.macho.commands.LoadCommandString: ...

    @property
    def timestamp(self) -> int: ...
