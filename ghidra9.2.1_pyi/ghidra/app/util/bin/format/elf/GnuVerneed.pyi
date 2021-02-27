import ghidra.app.util.bin
import ghidra.program.model.data
import java.lang


class GnuVerneed(object, ghidra.app.util.bin.StructConverter):
    """
    Version dependency section.

     typedef struct {
       Elf32_Half	vn_version;		//Version of structure
       Elf32_Half	vn_cnt;			//Number of associated aux entries
       Elf32_Word	vn_file;		//Offset of filename for this dependency
       Elf32_Word	vn_aux;			//Offset in bytes to vernaux array
       Elf32_Word	vn_next;		//Offset in bytes to next verneed entry
     } Elf32_Verneed;

     typedef struct {
       Elf64_Half	vn_version;		//Version of structure
       Elf64_Half	vn_cnt;			//Number of associated aux entries
       Elf64_Word	vn_file;		//Offset of filename for this dependency
       Elf64_Word	vn_aux;			//Offset in bytes to vernaux array
       Elf64_Word	vn_next;		//Offset in bytes to next verneed entry
     } Elf64_Verneed;


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

    def getFile(self) -> int: ...

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
    def file(self) -> int: ...

    @property
    def next(self) -> int: ...

    @property
    def version(self) -> int: ...
