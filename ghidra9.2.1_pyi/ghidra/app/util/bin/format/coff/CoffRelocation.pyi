import ghidra.app.util.bin
import ghidra.program.model.data
import java.lang


class CoffRelocation(object, ghidra.app.util.bin.StructConverter):
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

    def getAddress(self) -> long:
        """
        Returns the address where the relocation
         should be performed.
        @return the relocation address
        """
        ...

    def getClass(self) -> java.lang.Class: ...

    def getExtendedAddress(self) -> int:
        """
        Returns the extended address value.
         This is only used for COFF2.
        @return the extended address value
        """
        ...

    def getSymbolIndex(self) -> long:
        """
        Returns the symbol being relocated.
        @return the symbol being relocated
        """
        ...

    def getType(self) -> int:
        """
        Returns the relocation type.
        @return the relocation type
        """
        ...

    def hashCode(self) -> int: ...

    def notify(self) -> None: ...

    def notifyAll(self) -> None: ...

    def sizeof(self) -> int: ...

    def toDataType(self) -> ghidra.program.model.data.DataType: ...

    def toString(self) -> unicode: ...

    @overload
    def wait(self) -> None: ...

    @overload
    def wait(self, __a0: long) -> None: ...

    @overload
    def wait(self, __a0: long, __a1: int) -> None: ...

    @property
    def address(self) -> long: ...

    @property
    def extendedAddress(self) -> int: ...

    @property
    def symbolIndex(self) -> long: ...

    @property
    def type(self) -> int: ...
