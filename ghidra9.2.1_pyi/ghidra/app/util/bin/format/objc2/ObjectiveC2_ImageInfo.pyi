import ghidra.app.util.bin
import ghidra.program.model.data
import java.lang


class ObjectiveC2_ImageInfo(object, ghidra.app.util.bin.StructConverter):
    ASCII: ghidra.program.model.data.DataType = char
    BYTE: ghidra.program.model.data.DataType = byte
    DWORD: ghidra.program.model.data.DataType = dword
    IBO32: ghidra.program.model.data.DataType = ImageBaseOffset32
    OBJC_IMAGE_IS_REPLACEMENT: int = 1
    OBJC_IMAGE_REQUIRES_GC: int = 4
    OBJC_IMAGE_SUPPORTS_GC: int = 2
    POINTER: ghidra.program.model.data.DataType = pointer
    QWORD: ghidra.program.model.data.DataType = qword
    STRING: ghidra.program.model.data.DataType = string
    UTF16: ghidra.program.model.data.DataType = unicode
    UTF8: ghidra.program.model.data.DataType = string-utf8
    VOID: ghidra.program.model.data.DataType = void
    WORD: ghidra.program.model.data.DataType = word



    def __init__(self, state: ghidra.app.util.bin.format.objc2.ObjectiveC2_State, reader: ghidra.app.util.bin.BinaryReader): ...



    def applyTo(self) -> None: ...

    def equals(self, __a0: object) -> bool: ...

    def getClass(self) -> java.lang.Class: ...

    def getFlags(self) -> int: ...

    def getIndex(self) -> long: ...

    def getVersion(self) -> int: ...

    def hashCode(self) -> int: ...

    def isReplacement(self) -> bool: ...

    def isRequiresGarbageCollection(self) -> bool: ...

    def isSupportsGarbageCollection(self) -> bool: ...

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
    def flags(self) -> int: ...

    @property
    def index(self) -> long: ...

    @property
    def replacement(self) -> bool: ...

    @property
    def requiresGarbageCollection(self) -> bool: ...

    @property
    def supportsGarbageCollection(self) -> bool: ...

    @property
    def version(self) -> int: ...
