import ghidra.app.util.bin
import ghidra.file.formats.iso9660
import ghidra.program.model.data
import java.lang
import java.util


class ISO9660Header(object, ghidra.app.util.bin.StructConverter):
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



    def __init__(self, __a0: ghidra.app.util.bin.BinaryReader): ...



    def equals(self, __a0: object) -> bool: ...

    def getClass(self) -> java.lang.Class: ...

    def getPrimaryDirectory(self) -> ghidra.file.formats.iso9660.ISO9660Directory: ...

    def getPrimaryVolumeDescriptor(self) -> ghidra.file.formats.iso9660.ISO9660VolumeDescriptor: ...

    def getSupplTypeLIndexSizeTable(self) -> java.util.HashMap: ...

    def getSupplTypeMIndexSizeTable(self) -> java.util.HashMap: ...

    def getTypeLIndexSizeTable(self) -> java.util.HashMap: ...

    def getTypeMIndexSizeTable(self) -> java.util.HashMap: ...

    def getVolumeDescriptorSet(self) -> java.util.ArrayList: ...

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
    def primaryDirectory(self) -> ghidra.file.formats.iso9660.ISO9660Directory: ...

    @property
    def primaryVolumeDescriptor(self) -> ghidra.file.formats.iso9660.ISO9660VolumeDescriptor: ...

    @property
    def supplTypeLIndexSizeTable(self) -> java.util.HashMap: ...

    @property
    def supplTypeMIndexSizeTable(self) -> java.util.HashMap: ...

    @property
    def typeLIndexSizeTable(self) -> java.util.HashMap: ...

    @property
    def typeMIndexSizeTable(self) -> java.util.HashMap: ...

    @property
    def volumeDescriptorSet(self) -> java.util.ArrayList: ...
