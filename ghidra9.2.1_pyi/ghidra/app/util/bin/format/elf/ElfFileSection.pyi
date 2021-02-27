import ghidra.app.util.bin
import ghidra.program.model.data
import java.lang


class ElfFileSection(ghidra.app.util.bin.StructConverter, object):
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







    def equals(self, __a0: object) -> bool: ...

    def getAddressOffset(self) -> long:
        """
        Preferred memory address offset where data should be loaded.
         The returned offset will already have the prelink adjustment
         applied, although will not reflect any change in the image base.
        @return default memory address offset where data should be loaded
        """
        ...

    def getClass(self) -> java.lang.Class: ...

    def getEntrySize(self) -> int:
        """
        Size of each structured entry in bytes
        @return entry size or -1 if variable
        """
        ...

    def getFileOffset(self) -> long:
        """
        Offset within file where section bytes are specified
        @return offset within file where section bytes are specified
        """
        ...

    def getLength(self) -> long:
        """
        Length of file section in bytes
        @return length of file section in bytes
        """
        ...

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
    def addressOffset(self) -> long: ...

    @property
    def entrySize(self) -> int: ...

    @property
    def fileOffset(self) -> long: ...

    @property
    def length(self) -> long: ...
