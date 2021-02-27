import ghidra.app.util.bin
import ghidra.program.model.data
import java.lang


class ExportedSymbolKey(object, ghidra.app.util.bin.StructConverter):
    """
    See Apple's -- PEFBinaryFormat.h * Exported Symbol Hash Key

     struct PEFExportedSymbolKey {
         union {
             UInt32            fullHashWord;
             PEFSplitHashWord  splitHashWord;
         } u;
     };


     struct PEFSplitHashWord {
         UInt16  nameLength;
         UInt16  hashValue;
     };

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







    def equals(self, __a0: object) -> bool: ...

    def getClass(self) -> java.lang.Class: ...

    def getFullHashWord(self) -> int: ...

    def getHashValue(self) -> int: ...

    def getNameLength(self) -> int: ...

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
    def fullHashWord(self) -> int: ...

    @property
    def hashValue(self) -> int: ...

    @property
    def nameLength(self) -> int: ...
