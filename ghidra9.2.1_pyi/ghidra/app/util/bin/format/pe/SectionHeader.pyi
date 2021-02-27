from typing import List
import ghidra.app.util.bin
import ghidra.program.model.data
import ghidra.program.model.mem
import ghidra.util
import java.io
import java.lang


class SectionHeader(object, ghidra.app.util.bin.StructConverter, ghidra.app.util.bin.ByteArrayConverter):
    """
    A class to the represent the IMAGE_SECTION_HEADER
     struct as defined in winnt.h.


     typedef struct _IMAGE_SECTION_HEADER {
        BYTE    Name[IMAGE_SIZEOF_SHORT_NAME];
        union {
                DWORD   PhysicalAddress;
                DWORD   VirtualSize;			// MANDATORY
        } Misc;
        DWORD   VirtualAddress;				// MANDATORY
        DWORD   SizeOfRawData;				// MANDATORY
        DWORD   PointerToRawData;				// MANDATORY
        DWORD   PointerToRelocations;
        DWORD   PointerToLinenumbers;
        WORD    NumberOfRelocations;
        WORD    NumberOfLinenumbers;
        DWORD   Characteristics;				// MANDATORY
     } IMAGE_SECTION_HEADER, *PIMAGE_SECTION_HEADER; *


     #define IMAGE_SIZEOF_SECTION_HEADER 40 *
    """

    ASCII: ghidra.program.model.data.DataType = char
    BYTE: ghidra.program.model.data.DataType = byte
    DWORD: ghidra.program.model.data.DataType = dword
    IBO32: ghidra.program.model.data.DataType = ImageBaseOffset32
    IMAGE_SCN_ALIGN_1024BYTES: int = 11534336
    IMAGE_SCN_ALIGN_128BYTES: int = 8388608
    IMAGE_SCN_ALIGN_16BYTES: int = 5242880
    IMAGE_SCN_ALIGN_1BYTES: int = 1048576
    IMAGE_SCN_ALIGN_2048BYTES: int = 12582912
    IMAGE_SCN_ALIGN_256BYTES: int = 9437184
    IMAGE_SCN_ALIGN_2BYTES: int = 2097152
    IMAGE_SCN_ALIGN_32BYTES: int = 6291456
    IMAGE_SCN_ALIGN_4096BYTES: int = 13631488
    IMAGE_SCN_ALIGN_4BYTES: int = 3145728
    IMAGE_SCN_ALIGN_512BYTES: int = 10485760
    IMAGE_SCN_ALIGN_64BYTES: int = 7340032
    IMAGE_SCN_ALIGN_8192BYTES: int = 14680064
    IMAGE_SCN_ALIGN_8BYTES: int = 4194304
    IMAGE_SCN_CNT_CODE: int = 32
    IMAGE_SCN_CNT_INITIALIZED_DATA: int = 64
    IMAGE_SCN_CNT_UNINITIALIZED_DATA: int = 128
    IMAGE_SCN_GPREL: int = 32768
    IMAGE_SCN_LNK_COMDAT: int = 4096
    IMAGE_SCN_LNK_INFO: int = 512
    IMAGE_SCN_LNK_NRELOC_OVFL: int = 16777216
    IMAGE_SCN_LNK_REMOVE: int = 2048
    IMAGE_SCN_MEM_DISCARDABLE: int = 33554432
    IMAGE_SCN_MEM_EXECUTE: int = 536870912
    IMAGE_SCN_MEM_NOT_CACHED: int = 67108864
    IMAGE_SCN_MEM_NOT_PAGED: int = 134217728
    IMAGE_SCN_MEM_READ: int = 1073741824
    IMAGE_SCN_MEM_SHARED: int = 268435456
    IMAGE_SCN_MEM_WRITE: int = -2147483648
    IMAGE_SCN_NO_DEFER_SPEC_EXC: int = 16384
    IMAGE_SIZEOF_SECTION_HEADER: int = 40
    IMAGE_SIZEOF_SHORT_NAME: int = 8
    NAME: unicode = u'IMAGE_SECTION_HEADER'
    NOT_SET: int = -1
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
        """
        ...



    def equals(self, __a0: object) -> bool: ...

    def getCharacteristics(self) -> int:
        """
        Returns the flags OR'ed together, indicating the
         attributes of this section. Many of these flags
         can be set with the linker's /SECTION option.
         Common values include those listed in Figure 7.
        @return the flags OR'ed together, indicating the attributes of this section
        """
        ...

    def getClass(self) -> java.lang.Class: ...

    def getDataStream(self) -> java.io.InputStream:
        """
        Returns an input stream to underlying bytes of this section.
        @return an input stream to underlying bytes of this section
        @throws IOException if an i/o error occurs.
        """
        ...

    def getName(self) -> unicode:
        """
        Returns the ASCII name of the section. A
         section name is not guaranteed to be
         null-terminated. If you specify a section name
         longer than eight characters, the linker
         truncates it to eight characters in the
         executable. A mechanism exists for allowing
         longer section names in OBJ files. Section
         names often start with a period, but this is
         not a requirement. Section names with a $ in
         the name get special treatment from the linker.
         Sections with identical names prior to the $
         character are merged. The characters following
         the $ provide an alphabetic ordering for how the
         merged sections appear in the final section.
         There's quite a bit more to the subject of sections
         with $ in the name and how they're combined, but
         the details are outside the scope of this article
        @return the ASCII name of the section
        """
        ...

    def getNumberOfLinenumbers(self) -> int:
        """
        Returns the number of line numbers pointed to by the
         NumberOfRelocations field.
        @return the number of line numbers
        """
        ...

    def getNumberOfRelocations(self) -> int:
        """
        Returns the number of relocations pointed
         to by the PointerToRelocations field.
        @return the number of relocations
        """
        ...

    def getPhysicalAddress(self) -> int:
        """
        Returns the physical (file) address of this section.
        @return the physical (file) address of this section
        """
        ...

    def getPointerToLinenumbers(self) -> int:
        """
        Return the file offset for COFF-style line
         numbers for this section.
        @return the file offset for COFF-style line numbers for this section
        """
        ...

    def getPointerToRawData(self) -> int:
        """
        Returns the file offset where the data
         for the section begins. For executables,
         this value must be a multiple of the file
         alignment given in the PE header.
        @return the file offset where the data for the section begins
        """
        ...

    def getPointerToRelocations(self) -> int:
        """
        Returns the file offset of relocations for this section.
        @return the file offset of relocations for this section
        """
        ...

    def getReadableName(self) -> unicode:
        """
        Returns a readable ascii version of the name.
         All non-readable characters
         are replaced with underscores.
        @return a readable ascii version of the name
        """
        ...

    def getSizeOfRawData(self) -> int:
        """
        Returns the size (in bytes) of data stored for the section
         in the executable or OBJ.
        @return the size (in bytes) of data stored for the section
        """
        ...

    def getVirtualAddress(self) -> int:
        """
        In executables, returns the RVA where
         the section begins in memory. Should be set to 0 in OBJs.
         this section should be loaded into memory.
        @return the RVA where the section begins in memory.
        """
        ...

    def getVirtualSize(self) -> int:
        """
        Returns the actual, used size of the section.
         This field may be larger or
         smaller than the SizeOfRawData field.
         If the VirtualSize is larger, the
         SizeOfRawData field is the size of the
         initialized data from the executable,
         and the remaining bytes up to the VirtualSize
         should be zero-padded. This field is set
         to 0 in OBJ files.
        @return the actual, used size of the section
        """
        ...

    def hashCode(self) -> int: ...

    def notify(self) -> None: ...

    def notifyAll(self) -> None: ...

    def setSizeOfRawData(self, size: int) -> None: ...

    def setVirtualSize(self, size: int) -> None: ...

    def toBytes(self, dc: ghidra.util.DataConverter) -> List[int]: ...

    def toDataType(self) -> ghidra.program.model.data.DataType: ...

    def toString(self) -> unicode:
        """
        @see java.lang.Object#toString()
        """
        ...

    @overload
    def wait(self) -> None: ...

    @overload
    def wait(self, __a0: long) -> None: ...

    @overload
    def wait(self, __a0: long, __a1: int) -> None: ...

    def writeBytes(self, raf: java.io.RandomAccessFile, rafIndex: int, dc: ghidra.util.DataConverter, block: ghidra.program.model.mem.MemoryBlock, useBlockBytes: bool) -> None:
        """
        Writes the bytes from this section into the specified random access file.
         The bytes will be written starting at the byte position
         specified by <code>getPointerToRawData()</code>.
        @param raf the random access file
        @param rafIndex the index into the RAF where the bytes will be written
        @param dc the data converter
        @param block the memory block corresponding to this section
        @param useBlockBytes if true, then use the bytes from the memory block,
                              otherwise use the bytes from this section.
        @throws IOException if there are errors writing to the file
        @throws MemoryAccessException if the byte from the memory block cannot be accesses
        """
        ...

    def writeHeader(self, raf: java.io.RandomAccessFile, dc: ghidra.util.DataConverter) -> None:
        """
        Writes this section header to the specified random access file.
        @param raf the random access file
        @param dc the data converter
        @throws IOException if an I/O error occurs
        """
        ...

    @property
    def characteristics(self) -> int: ...

    @property
    def dataStream(self) -> java.io.InputStream: ...

    @property
    def name(self) -> unicode: ...

    @property
    def numberOfLinenumbers(self) -> int: ...

    @property
    def numberOfRelocations(self) -> int: ...

    @property
    def physicalAddress(self) -> int: ...

    @property
    def pointerToLinenumbers(self) -> int: ...

    @property
    def pointerToRawData(self) -> int: ...

    @property
    def pointerToRelocations(self) -> int: ...

    @property
    def readableName(self) -> unicode: ...

    @property
    def sizeOfRawData(self) -> int: ...

    @sizeOfRawData.setter
    def sizeOfRawData(self, value: int) -> None: ...

    @property
    def virtualAddress(self) -> int: ...

    @property
    def virtualSize(self) -> int: ...

    @virtualSize.setter
    def virtualSize(self, value: int) -> None: ...
