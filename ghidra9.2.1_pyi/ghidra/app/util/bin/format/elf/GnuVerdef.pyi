import ghidra.app.util.bin
import ghidra.program.model.data
import java.lang


class GnuVerdef(object, ghidra.app.util.bin.StructConverter):
    """
    Version definition sections.

     typedef struct {
       Elf32_Half	vd_version;		//Version revision
       Elf32_Half	vd_flags;		//Version information
       Elf32_Half	vd_ndx;			//Version Index
       Elf32_Half	vd_cnt;			//Number of associated aux entries
       Elf32_Word	vd_hash;		//Version name hash value
       Elf32_Word	vd_aux;			//Offset in bytes to verdaux array
       Elf32_Word	vd_next;		//Offset in bytes to next verdef entry
     } Elf32_Verdef;

     typedef struct {
       Elf64_Half	vd_version;		//Version revision
       Elf64_Half	vd_flags;		//Version information
       Elf64_Half	vd_ndx;			//Version Index
       Elf64_Half	vd_cnt;			//Number of associated aux entries
       Elf64_Word	vd_hash;		//Version name hash value
       Elf64_Word	vd_aux;			//Offset in bytes to verdaux array
       Elf64_Word	vd_next;		//Offset in bytes to next verdef entry
     } Elf64_Verdef;


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

    def getAux(self) -> int: ...

    def getClass(self) -> java.lang.Class: ...

    def getCnt(self) -> int: ...

    def getFlags(self) -> int: ...

    def getHash(self) -> int: ...

    def getNdx(self) -> int: ...

    def getNext(self) -> int: ...

    def getVersion(self) -> int: ...

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
    def aux(self) -> int: ...

    @property
    def cnt(self) -> int: ...

    @property
    def flags(self) -> int: ...

    @property
    def hash(self) -> int: ...

    @property
    def ndx(self) -> int: ...

    @property
    def next(self) -> int: ...

    @property
    def version(self) -> int: ...
