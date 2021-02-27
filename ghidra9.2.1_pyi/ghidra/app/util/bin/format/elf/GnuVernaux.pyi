import ghidra.app.util.bin
import ghidra.program.model.data
import java.lang


class GnuVernaux(object, ghidra.app.util.bin.StructConverter):
    """
    Auxiliary needed version information.

     typedef struct {
       Elf32_Word	vna_hash;		//Hash value of dependency name
       Elf32_Half	vna_flags;		//Dependency specific information
       Elf32_Half	vna_other;		//Unused
       Elf32_Word	vna_name;		//Dependency name string offset
       Elf32_Word	vna_next;		//Offset in bytes to next vernaux entry
     } Elf32_Vernaux;

     typedef struct {
       Elf64_Word	vna_hash;		//Hash value of dependency name
       Elf64_Half	vna_flags;		//Dependency specific information
       Elf64_Half	vna_other;		//Unused
       Elf64_Word	vna_name;		//Dependency name string offset
       Elf64_Word	vna_next;		//Offset in bytes to next vernaux entry
     } Elf64_Vernaux;


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

    def getFlags(self) -> int: ...

    def getHash(self) -> int: ...

    def getName(self) -> int: ...

    def getNext(self) -> int: ...

    def getOther(self) -> int: ...

    def hashCode(self) -> int: ...

    def notify(self) -> None: ...

    def notifyAll(self) -> None: ...

    def toDataType(self) -> ghidra.program.model.data.DataType:
        """
        @see ghidra.app.util.bin.StructConverter#toDataType()
        """
        ...

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
    def hash(self) -> int: ...

    @property
    def name(self) -> int: ...

    @property
    def next(self) -> int: ...

    @property
    def other(self) -> int: ...
