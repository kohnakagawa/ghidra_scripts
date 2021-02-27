from typing import List
import ghidra.app.util.bin
import ghidra.program.model.data
import ghidra.util
import java.lang


class BaseRelocation(object, ghidra.app.util.bin.StructConverter, ghidra.app.util.bin.ByteArrayConverter):
    """
    A class to represent the IMAGE_BASE_RELOCATION
     data structure defined in winnt.h.

     typedef struct _IMAGE_BASE_RELOCATION {
         DWORD   VirtualAddress;
         DWORD   SizeOfBlock;
     //  WORD    TypeOffset[1];
     } IMAGE_BASE_RELOCATION;
     typedef IMAGE_BASE_RELOCATION UNALIGNED * PIMAGE_BASE_RELOCATION;

    """

    ASCII: ghidra.program.model.data.DataType = char
    BYTE: ghidra.program.model.data.DataType = byte
    DWORD: ghidra.program.model.data.DataType = dword
    IBO32: ghidra.program.model.data.DataType = ImageBaseOffset32
    IMAGE_REL_BASED_ABSOLUTE: int = 0
    IMAGE_REL_BASED_DIR64: int = 10
    IMAGE_REL_BASED_HIGH: int = 1
    IMAGE_REL_BASED_HIGH3ADJ: int = 11
    IMAGE_REL_BASED_HIGHADJ: int = 4
    IMAGE_REL_BASED_HIGHLOW: int = 3
    IMAGE_REL_BASED_IA64_IMM64: int = 9
    IMAGE_REL_BASED_LOW: int = 2
    IMAGE_REL_BASED_MIPS_JMPADDR: int = 5
    IMAGE_REL_BASED_MIPS_JMPADDR16: int = 9
    IMAGE_REL_BASED_NOOP: int = 0
    IMAGE_REL_BASED_REL32: int = 7
    IMAGE_REL_BASED_SECTION: int = 6
    IMAGE_SIZEOF_BASE_RELOCATION: int = 8
    NAME: unicode = u'IMAGE_BASE_RELOCATION'
    POINTER: ghidra.program.model.data.DataType = pointer
    QWORD: ghidra.program.model.data.DataType = qword
    STRING: ghidra.program.model.data.DataType = string
    TYPE_STRINGS: List[unicode] = array(java.lang.String, [u'ABSOLUTE', u'HIGH', u'LOW', u'HIGHLOW', u'HIGHADJ', u'MIPS_JMPADDR', u'???6', u'???7', u'???8', u'IA64_IMM64', u'DIR64'])
    UTF16: ghidra.program.model.data.DataType = unicode
    UTF8: ghidra.program.model.data.DataType = string-utf8
    VOID: ghidra.program.model.data.DataType = void
    WORD: ghidra.program.model.data.DataType = word



    def __init__(self):
        """
        DO NOT USE THIS CONSTRUCTOR, USE create*(GenericFactory ...) FACTORY METHODS INSTEAD.
        """
        ...



    def addRelocation(self, type: int, offset: int) -> None:
        """
        Adds a relocation to this base relocation block.
        @param type the relocation type
        @param offset the relocation offset
        """
        ...

    def equals(self, __a0: object) -> bool: ...

    def getClass(self) -> java.lang.Class: ...

    def getCount(self) -> int:
        """
        Returns the number of relocation in this block.
        @return the number of relocation in this block
        """
        ...

    def getOffset(self, index: int) -> int:
        """
        Returns the lower 12 bits of the offset.
        @param index the ith relocation
        @return int the offset of the relocation
        """
        ...

    def getSizeOfBlock(self) -> int:
        """
        Returns the size (in bytes) of this relocation block.
        @return the size (in bytes) of this relocation block
        """
        ...

    def getType(self, index: int) -> int:
        """
        Returns the upper 4 bits of the offset.
        @param index the ith relocation
        @return int the type of the relocation
        ,
        """
        ...

    def getVirtualAddress(self) -> int:
        """
        Returns the base address of the relocations in this block.
        @return the base address of the relocations in this block
        """
        ...

    def hashCode(self) -> int: ...

    def notify(self) -> None: ...

    def notifyAll(self) -> None: ...

    def toBytes(self, dc: ghidra.util.DataConverter) -> List[int]:
        """
        @see ghidra.app.util.bin.ByteArrayConverter#toBytes(ghidra.util.DataConverter)
        """
        ...

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
    def count(self) -> int: ...

    @property
    def sizeOfBlock(self) -> int: ...

    @property
    def virtualAddress(self) -> int: ...
