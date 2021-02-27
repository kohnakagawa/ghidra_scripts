from typing import List
import ghidra.app.util.bin
import ghidra.app.util.bin.format.pef
import ghidra.program.model.data
import java.lang


class LoaderRelocationHeader(object, ghidra.app.util.bin.StructConverter):
    """
    See Apple's -- PEFBinaryFormat.h

     struct PEFLoaderRelocationHeader {
         UInt16   sectionIndex;     // Index of the section to be fixed up.
         UInt16   reservedA;        // Reserved, must be zero.
         UInt32   relocCount;       // Number of 16 bit relocation chunks.
         UInt32   firstRelocOffset; // Offset of first relocation instruction.
     };

     typedef UInt16 PEFRelocChunk;

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

    def getFirstRelocOffset(self) -> int:
        """
        The firstRelocOffset field (4 bytes) indicates the byte
         offset from the start of the relocations area to the first relocation
         instruction for this section.
        @return offset from the start of the relocations area to the first relocation
        """
        ...

    def getRelocCount(self) -> int:
        """
        The relocCount field (4 bytes) indicates the
         number of 16-bit relocation blocks for this section.
        @return number of 16-bit relocation blocks for this section
        """
        ...

    def getRelocations(self) -> List[ghidra.app.util.bin.format.pef.Relocation]: ...

    def getReservedA(self) -> int:
        """
        Reserved, must be set to zero (0).
        @return reserved, must be set to zero (0)
        """
        ...

    def getSectionIndex(self) -> int:
        """
        The sectionIndex field (2 bytes) designates the
         section number to which this relocation header refers.
        @return section number to which this relocation header refers
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
    def firstRelocOffset(self) -> int: ...

    @property
    def relocCount(self) -> int: ...

    @property
    def relocations(self) -> List[object]: ...

    @property
    def reservedA(self) -> int: ...

    @property
    def sectionIndex(self) -> int: ...
