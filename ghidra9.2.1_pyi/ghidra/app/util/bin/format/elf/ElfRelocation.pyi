from typing import List
import ghidra.app.util.bin
import ghidra.program.model.data
import ghidra.util
import java.lang


class ElfRelocation(object, ghidra.app.util.bin.ByteArrayConverter, ghidra.app.util.bin.StructConverter):
    """
    A class to represent the Elf32_Rel and Elf64_Rel data structure.


     typedef uint32_t Elf32_Addr;
     typedef uint64_t Elf64_Addr;
     typedef uint32_t Elf32_Word;
     typedef uint64_t Elf64_Xword;

     REL entry:

        typedef struct {
            Elf32_Addr   r_offset;
            Elf32_Word   r_info;
        } Elf32_Rel;

        typedef struct {
            Elf64_Addr   r_offset;
            Elf64_Xword  r_info;
        } Elf64_Rel;

     RELA entry with addend:

        typedef struct {
            Elf32_Addr    r_offset;
            Elf32_Word    r_info;
            Elf32_Sword   r_addend;
        } Elf32_Rela;

        typedef struct {
            Elf64_Addr    r_offset;   //Address
            Elf64_Xword   r_info;     //Relocation type and symbol index
            Elf64_Sxword  r_addend;   //Addend
        } Elf64_Rela;

     RELR entry (see SHT_RELR, DT_RELR):
        NOTE: Relocation type is data relative and must be specified by appropriate relocation handler
        (see ElfRelocationHandler#getRelrRelocationType()) since it is not contained within the
        relocation table which only specifies r_offset for each entry.


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
        @see ElfRelocation#createElfRelocation
        """
        ...



    def equals(self, __a0: object) -> bool: ...

    def getAddend(self) -> long:
        """
        This member specifies a constant addend used to compute
         the value to be stored into the relocatable field.  This
         value will be 0 for REL entries which do not supply an addend.
        @return a constant addend
        """
        ...

    def getClass(self) -> java.lang.Class: ...

    def getOffset(self) -> long:
        """
        This member gives the location at which to apply the relocation action.

         For a relocatable file, the value is the byte offset from the
         beginning of the section to the storage unit affected by the relocation.

         For an executable file or a shared object, the value is the virtual address of
         the storage unit affected by the relocation.
        @return the location at which to apply the relocation
        """
        ...

    def getRelocationIndex(self) -> int:
        """
        @return index of relocation within its corresponding relocation table
        """
        ...

    def getRelocationInfo(self) -> long:
        """
        Returns the r_info relocation entry field value
        @return r_info value
        """
        ...

    @staticmethod
    def getStandardRelocationEntrySize(is64bit: bool, hasAddend: bool) -> int:
        """
        Get the standard relocation size when one has notbeen specified
        @param is64bit true if ELF 64-bit
        @param hasAddend true if relocation has addend
        @return size of relocation entry
        """
        ...

    def getSymbolIndex(self) -> int:
        """
        Returns the symbol index where the relocation must be made.
         A value of 0 is generally returned when no symbol is relavent
         to the relocation.
        @return the symbol index
        """
        ...

    def getType(self) -> int:
        """
        The type of relocation to apply.
         NOTE 1: Relocation types are processor-specific (see {@link ElfRelocationHandler}).
         NOTE 2: A type of 0 is returned by default for RELR relocations and must be updated
         during relocation processing (see {@link #setType(long)}).  The appropriate RELR
         relocation type can be obtained from the appropriate
         {@link ElfRelocationHandler#getRelrRelocationType()} or
         {@link ElfRelocationContext#getRelrRelocationType()} if available.
        @return type of relocation to apply
        """
        ...

    def hasAddend(self) -> bool:
        """
        Returns true if this is a RELA entry with addend
        @return true if this is a RELA entry with addend
        """
        ...

    def hashCode(self) -> int: ...

    def notify(self) -> None: ...

    def notifyAll(self) -> None: ...

    @overload
    def setOffset(self, offset: long) -> None:
        """
        Sets the relocation offset to the new specified value.
        @param offset the new offset value
        """
        ...

    @overload
    def setOffset(self, offset: int) -> None:
        """
        Sets the relocation offset to the new specified value.
        @param offset the new offset value
        """
        ...

    def setType(self, type: long) -> None:
        """
        Set the relocation type associated with this relocation.
         Updating the relocation type is required for RELR relocations.
        @param type relocation type to be applied
        """
        ...

    def toBytes(self, dc: ghidra.util.DataConverter) -> List[int]:
        """
        @see ghidra.app.util.bin.ByteArrayConverter#toBytes(ghidra.util.DataConverter)
        """
        ...

    def toDataType(self) -> ghidra.program.model.data.DataType: ...

    def toString(self) -> unicode: ...

    @overload
    def wait(self) -> None: ...

    @overload
    def wait(self, __a0: long) -> None: ...

    @overload
    def wait(self, __a0: long, __a1: int) -> None: ...

    @property
    def addend(self) -> long: ...

    @property
    def offset(self) -> long: ...

    @offset.setter
    def offset(self, value: long) -> None: ...

    @property
    def relocationIndex(self) -> int: ...

    @property
    def relocationInfo(self) -> long: ...

    @property
    def symbolIndex(self) -> int: ...

    @property
    def type(self) -> int: ...
