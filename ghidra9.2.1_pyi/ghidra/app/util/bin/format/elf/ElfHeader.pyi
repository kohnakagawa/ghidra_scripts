from typing import List
import generic.continues
import ghidra.app.util.bin
import ghidra.app.util.bin.format
import ghidra.app.util.bin.format.elf
import ghidra.app.util.bin.format.elf.extend
import ghidra.program.model.data
import ghidra.program.model.mem
import ghidra.util
import java.io
import java.lang


class ElfHeader(object, ghidra.app.util.bin.StructConverter, ghidra.app.util.bin.format.Writeable):
    """
    A class to represent the Executable and Linking Format (ELF)
     header and specification.
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
        """
        ...



    def addProgramHeader(self, ph: ghidra.app.util.bin.format.elf.ElfProgramHeader) -> None:
        """
        Appends the new program header to the end of the existing
         program header table.
        @param ph the new program header
        """
        ...

    @overload
    def addSection(self, name: unicode, sh_name: int) -> ghidra.app.util.bin.format.elf.ElfSectionHeader:
        """
        Adds a new section the specifed name and name index.
         The type of the section will be SHT_PROGBITS.
        @param name the actual name of the new section
        @param sh_name the byte index into the string table where the name begins
        @return the newly created section
        """
        ...

    @overload
    def addSection(self, block: ghidra.program.model.mem.MemoryBlock, sh_name: int) -> ghidra.app.util.bin.format.elf.ElfSectionHeader:
        """
        Adds a new section using the specified memory block.
         The memory block is used to setting the address and size.
         As well as, setting the data.
        @param block the memory block
        @param sh_name the byte index into the string table where the name begins
        @return the newly created section
        @throws MemoryAccessException if any of the requested memory block bytes are uninitialized.
        """
        ...

    @overload
    def addSection(self, name: unicode, sh_name: int, type: int) -> ghidra.app.util.bin.format.elf.ElfSectionHeader:
        """
        Adds a new section the specifed name and name index.
         The type of the section will be SHT_PROGBITS.
        @param name the actual name of the new section
        @param sh_name the byte index into the string table where the name begins
        @param type the type of the new section
        @return the newly created section
        """
        ...

    def adjustAddressForPrelink(self, address: long) -> long:
        """
        Adjust address offset for certain pre-linked binaries which do not adjust certain
         header fields (e.g., dynamic table address entries).  Standard GNU/Linux pre-linked
         shared libraries have adjusted header entries and this method should have no effect.
        @param address
        @return address with appropriate pre-link adjustment added
        """
        ...

    @staticmethod
    def createElfHeader(factory: generic.continues.GenericFactory, provider: ghidra.app.util.bin.ByteProvider) -> ghidra.app.util.bin.format.elf.ElfHeader:
        """
        Constructs a new ELF header using the specified byte provider.
        @param provider the byte provider to supply the bytes
        @throws ElfException if the underlying bytes in the byte provider
         do not constitute a valid ELF.
        """
        ...

    def e_ehsize(self) -> int:
        """
        This member holds the ELF header's size in bytes.
        @return the ELF header's size in bytes
        """
        ...

    def e_entry(self) -> long:
        """
        This member gives the virtual address to which the system first transfers control, thus
         starting the process. If the file has no associated entry point, this member holds zero.
        @return the virtual address to which the system first transfers control
        """
        ...

    def e_flags(self) -> int:
        """
        This member holds processor-specific flags associated with the file. Flag names take
         the form EF_machine_flag.
        @return the processor-specific flags associated with the file
        @see ElfConstants for flag definitions
        """
        ...

    def e_ident_abiversion(self) -> int:
        """
        This member identifies the target ABI version.
        @return the target ABI version
        """
        ...

    def e_ident_osabi(self) -> int:
        """
        This member identifies the target operating system and ABI.
        @return the target operating system and ABI
        """
        ...

    def e_machine(self) -> int:
        """
        This member's value specifies the required architecture for an individual file.
        @return the required architecture for an individual file
        @see ElfConstants for machine definitions
        """
        ...

    def e_phentsize(self) -> int:
        """
        This member holds the size in bytes of one entry in the file's program header table;
         all entries are the same size.
        @return the size in bytes of one program header table entry
        """
        ...

    def e_phnum(self) -> int:
        """
        This member holds the number of entries in the program header table. Thus the product
         of e_phentsize and e_phnum gives the table's size in bytes. If a file has no program
         header table, e_phnum holds the value zero.
        @return the number of entries in the program header table
        """
        ...

    def e_phoff(self) -> long:
        """
        This member holds the program header table's file offset in bytes. If the file has no
         program header table, this member holds zero.
        @return the program header table's file offset in bytes
        """
        ...

    def e_shentsize(self) -> int:
        """
        This member holds the section header's size in bytes. A section header is one entry in
         the section header table; all entries are the same size.
        @return the section header's size in bytes
        """
        ...

    def e_shnum(self) -> int:
        """
        This member holds the number of entries in the section header table. Thus the product
         of e_shentsize and e_shnum gives the section header table's size in bytes. If a file
         has no section header table, e_shnum holds the value zero.
        @return the number of entries in the section header table
        """
        ...

    def e_shoff(self) -> long:
        """
        This member holds the section header table's file offset in bytes. If the file has no section
         header table, this member holds zero.
        @return the section header table's file offset in bytes
        """
        ...

    def e_shstrndx(self) -> int:
        """
        This member holds the section header table index of the entry associated with the section
         name string table. If the file has no section name string table, this member holds
         the value SHN_UNDEF.
        @return the section header table index of the entry associated with the section name string table
        """
        ...

    def e_type(self) -> int:
        """
        This member identifies the object file type; executable, shared object, etc.
        @return the object file type
        """
        ...

    def e_version(self) -> int:
        """
        This member identifies the object file version,
         where "EV_NONE == Invalid Version" and "EV_CURRENT == Current Version"
         The value 1 signifies the original file format; extensions will
         create new versions with higher numbers.
         The value of EV_CURRENT, though given as 1 above, will change as
         necessary to reflect the current version number.
        @return the object file version
        """
        ...

    def equals(self, __a0: object) -> bool: ...

    def findImageBase(self) -> long:
        """
        Inspect the Elf image and determine the default image base prior
         to the {@link #parse()} method being invoked (i.e., only the main Elf
         header structure has been parsed).
         The image base is the virtual address of the PT_LOAD program header
         with the smallest address or 0 if no program headers exist.  By default,
         the image base address should be treated as a addressable unit offset.
        @return preferred image base
        """
        ...

    def getClass(self) -> java.lang.Class: ...

    def getDynamicLibraryNames(self) -> List[unicode]:
        """
        Returns array of dynamic library names defined by DT_NEEDED
        @return array of dynamic library names
        """
        ...

    def getDynamicStringTable(self) -> ghidra.app.util.bin.format.elf.ElfStringTable:
        """
        Returns the dynamic string table as defined in this ELF file.
        @return the dynamic string table as defined in this ELF file
        """
        ...

    def getDynamicSymbolTable(self) -> ghidra.app.util.bin.format.elf.ElfSymbolTable:
        """
        Returns the dynamic symbol table as defined in this ELF file.
        @return the dynamic symbol table as defined in this ELF file
        """
        ...

    def getDynamicTable(self) -> ghidra.app.util.bin.format.elf.ElfDynamicTable:
        """
        Returns the dynamic table defined by program header of type PT_DYNAMIC or the .dynamic program section.
         Or, null if one does not exist.
        @return the dynamic table
        """
        ...

    def getDynamicType(self, type: int) -> ghidra.app.util.bin.format.elf.ElfDynamicType: ...

    def getEntryComponentOrdinal(self) -> int:
        """
        Get the Elf header structure component ordinal
         corresponding to the e_entry element
        @return e_entry component ordinal
        """
        ...

    def getFlags(self) -> unicode:
        """
        Returns a string representation of the numeric flags field.
        @return elf flags field value
        """
        ...

    def getImageBase(self) -> long:
        """
        Returns the image base of this ELF.
         The image base is the virtual address of the first PT_LOAD
         program header or 0 if no program headers. By default,
         the image base address should be treated as a addressable unit offset.s
        @return the image base of this ELF
        """
        ...

    def getLoadAdapter(self) -> ghidra.app.util.bin.format.elf.extend.ElfLoadAdapter:
        """
        Get the installed extension provider.  If the parse method has not yet been
         invoked, the default adapter will be returned.
        @return ELF load adapter
        """
        ...

    def getMachineName(self) -> unicode:
        """
        Returns a string name of the processor specified in this ELF header.
         For example, if "e_machine==EM_386", then it returns "80386".
        @return a string name of the processor specified in this ELF header
        """
        ...

    def getPhoffComponentOrdinal(self) -> int:
        """
        Get the Elf header structure component ordinal
         corresponding to the e_phoff element
        @return e_phoff component ordinal
        """
        ...

    def getProgramHeaderAt(self, virtualAddr: long) -> ghidra.app.util.bin.format.elf.ElfProgramHeader:
        """
        Returns the program header at the specified address,
         or null if no program header exists at that address.
        @param virtualAddr the address of the requested program header
        @return the program header with the specified address
        """
        ...

    def getProgramHeaderProgramHeader(self) -> ghidra.app.util.bin.format.elf.ElfProgramHeader:
        """
        Returns the program header with type of PT_PHDR.
         Or, null if one does not exist.
        @return the program header with type of PT_PHDR
        """
        ...

    def getProgramHeaderType(self, type: int) -> ghidra.app.util.bin.format.elf.ElfProgramHeaderType: ...

    @overload
    def getProgramHeaders(self) -> List[ghidra.app.util.bin.format.elf.ElfProgramHeader]:
        """
        Returns the program headers as defined in this ELF file.
        @return the program headers as defined in this ELF file
        """
        ...

    @overload
    def getProgramHeaders(self, type: int) -> List[ghidra.app.util.bin.format.elf.ElfProgramHeader]:
        """
        Returns the program headers with the specified type.
         The array could be zero-length, but will not be null.
        @param type
        @return the program headers with the specified type
        @see ElfProgramHeader
        """
        ...

    def getProgramLoadHeaderContaining(self, virtualAddr: long) -> ghidra.app.util.bin.format.elf.ElfProgramHeader:
        """
        Returns the PT_LOAD program header which loads a range containing
         the specified address, or null if not found.
        @param virtualAddr the address of the requested program header
        @return the program header with the specified address
        """
        ...

    def getProgramLoadHeaderContainingFileOffset(self, offset: long) -> ghidra.app.util.bin.format.elf.ElfProgramHeader:
        """
        Returns the PT_LOAD program header which loads a range containing
         the specified file offset, or null if not found.
        @param offset the file offset to be loaded
        @return the program header with the specified file offset
        """
        ...

    def getReader(self) -> ghidra.app.util.bin.BinaryReader:
        """
        Returns the binary reader.
        @return the binary reader
        """
        ...

    def getRelocationTable(self, relocSection: ghidra.app.util.bin.format.elf.ElfSectionHeader) -> ghidra.app.util.bin.format.elf.ElfRelocationTable:
        """
        Returns the relocation table associated to the specified section header,
         or null if one does not exist.
        @param relocSection section header corresponding to relocation table
        @return the relocation table associated to the specified section header
        """
        ...

    def getRelocationTableAtOffset(self, fileOffset: long) -> ghidra.app.util.bin.format.elf.ElfRelocationTable:
        """
        Returns the relocation table located at the specified fileOffset,
         or null if one does not exist.
        @param fileOffset file offset corresponding to start of relocation table
        @return the relocation table located at the specified fileOffset or null
        """
        ...

    def getRelocationTables(self) -> List[ghidra.app.util.bin.format.elf.ElfRelocationTable]:
        """
        Returns the relocation tables as defined in this ELF file.
        @return the relocation tables as defined in this ELF file
        """
        ...

    def getSection(self, name: unicode) -> ghidra.app.util.bin.format.elf.ElfSectionHeader:
        """
        Returns the section header with the specified name, or null
         if no section exists with that name.
        @param name the name of the requested section
        @return the section header with the specified name
        """
        ...

    def getSectionAt(self, address: long) -> ghidra.app.util.bin.format.elf.ElfSectionHeader:
        """
        Returns the section header at the specified address,
         or null if no section exists at that address.
        @param address the address of the requested section
        @return the section header with the specified address
        """
        ...

    def getSectionHeaderContainingFileRange(self, fileOffset: long, fileRangeLength: long) -> ghidra.app.util.bin.format.elf.ElfSectionHeader:
        """
        Returns the section header which fully contains the specified file offset range.
        @param fileOffset file offset
        @param fileRangeLength length of file range in bytes
        @return section or null if not found
        """
        ...

    def getSectionHeaderType(self, type: int) -> ghidra.app.util.bin.format.elf.ElfSectionHeaderType: ...

    def getSectionIndex(self, section: ghidra.app.util.bin.format.elf.ElfSectionHeader) -> int:
        """
        Returns the index of the specified section.
         The index is the order in which the section was
         defined in the section header table.
        @param section the section header
        @return the index of the specified section header
        """
        ...

    def getSectionLoadHeaderContaining(self, address: long) -> ghidra.app.util.bin.format.elf.ElfSectionHeader:
        """
        Returns the section header that loads/contains the specified address,
         or null if no section contains the address.
        @param address the address of the requested section
        @return the section header that contains the address
        """
        ...

    @overload
    def getSections(self) -> List[ghidra.app.util.bin.format.elf.ElfSectionHeader]:
        """
        Returns the section headers as defined in this ELF file.
        @return the section headers as defined in this ELF file
        """
        ...

    @overload
    def getSections(self, type: int) -> List[ghidra.app.util.bin.format.elf.ElfSectionHeader]:
        """
        Returns the section headers with the specified type.
         The array could be zero-length, but will not be null.
        @param type
        @return the section headers with the specified type
        @see ElfSectionHeader
        """
        ...

    def getShoffComponentOrdinal(self) -> int:
        """
        Get the Elf header structure component ordinal
         corresponding to the e_shoff element
        @return e_shoff component ordinal
        """
        ...

    def getStringTable(self, section: ghidra.app.util.bin.format.elf.ElfSectionHeader) -> ghidra.app.util.bin.format.elf.ElfStringTable:
        """
        Returns the string table associated to the specified section header.
         Or, null if one does not exist.
        @return the string table associated to the specified section header
        """
        ...

    def getStringTables(self) -> List[ghidra.app.util.bin.format.elf.ElfStringTable]:
        """
        Returns the string tables as defined in this ELF file.
        @return the string tables as defined in this ELF file
        """
        ...

    def getSymbolTable(self, symbolTableSection: ghidra.app.util.bin.format.elf.ElfSectionHeader) -> ghidra.app.util.bin.format.elf.ElfSymbolTable:
        """
        Returns the symbol table associated to the specified section header.
         Or, null if one does not exist.
        @return the symbol table associated to the specified section header
        """
        ...

    def getSymbolTables(self) -> List[ghidra.app.util.bin.format.elf.ElfSymbolTable]:
        """
        Returns the symbol tables as defined in this ELF file.
        @return the symbol tables as defined in this ELF file
        """
        ...

    def hashCode(self) -> int: ...

    def is32Bit(self) -> bool:
        """
        Returns true if this ELF was created for a 32-bit processor.
        @return true if this ELF was created for a 32-bit processor
        """
        ...

    def is64Bit(self) -> bool:
        """
        Returns true if this ELF was created for a 64-bit processor.
        @return true if this ELF was created for a 64-bit processor
        """
        ...

    def isBigEndian(self) -> bool:
        """
        Returns true if this ELF was created for a big endian processor.
        @return true if this ELF was created for a big endian processor
        """
        ...

    def isExecutable(self) -> bool:
        """
        Returns true if this is an executable file.
         <br>
         e_type == NewElfHeaderConstants.ET_EXEC
        @return true if this is a executable file
        """
        ...

    def isLittleEndian(self) -> bool:
        """
        Returns true if this ELF was created for a little endian processor.
        @return true if this ELF was created for a little endian processor
        """
        ...

    def isPreLinked(self) -> bool:
        """
        Determine if the image has been pre-linked.
         NOTE: Currently has very limited support.  Certain pre-link
         cases can not be detected until after a full parse has been
         performed.
        @return true if image has been pre-linked
        """
        ...

    def isRelocatable(self) -> bool:
        """
        Returns true if this is a relocatable file.
         <br>
         e_type == NewElfHeaderConstants.ET_REL
        @return true if this is a relocatable file
        """
        ...

    def isSectionLoaded(self, section: ghidra.app.util.bin.format.elf.ElfSectionHeader) -> bool: ...

    def isSharedObject(self) -> bool:
        """
        Returns true if this is a shared object file.
         <br>
         e_type == NewElfHeaderConstants.ET_DYN
        @return true if this is a shared object file
        """
        ...

    def notify(self) -> None: ...

    def notifyAll(self) -> None: ...

    def parse(self) -> None: ...

    def setProgramHeaderOffset(self, offset: long) -> None:
        """
        Sets the program header offset.
        @param offset the new program header offset
        """
        ...

    def setSectionHeaderOffset(self, offset: long) -> None:
        """
        Sets the section header offset.
        @param offset the new section header offset
        """
        ...

    def toDataType(self) -> ghidra.program.model.data.DataType:
        """
        @see ghidra.app.util.bin.StructConverter#toDataType()
        """
        ...

    def toString(self) -> unicode: ...

    def unadjustAddressForPrelink(self, address: long) -> long:
        """
        Unadjust address offset for certain pre-linked binaries which do not adjust certain
         header fields (e.g., dynamic table address entries).  This may be needed when updating
         a header address field which requires pre-link adjustment.
        @param address
        @return address with appropriate pre-link adjustment subtracted
        """
        ...

    @overload
    def wait(self) -> None: ...

    @overload
    def wait(self, __a0: long) -> None: ...

    @overload
    def wait(self, __a0: long, __a1: int) -> None: ...

    def write(self, raf: java.io.RandomAccessFile, dc: ghidra.util.DataConverter) -> None:
        """
        @see ghidra.app.util.bin.format.Writeable#write(java.io.RandomAccessFile, ghidra.util.DataConverter)
        """
        ...

    @property
    def 32Bit(self) -> bool: ...

    @property
    def 64Bit(self) -> bool: ...

    @property
    def bigEndian(self) -> bool: ...

    @property
    def dynamicLibraryNames(self) -> List[unicode]: ...

    @property
    def dynamicStringTable(self) -> ghidra.app.util.bin.format.elf.ElfStringTable: ...

    @property
    def dynamicSymbolTable(self) -> ghidra.app.util.bin.format.elf.ElfSymbolTable: ...

    @property
    def dynamicTable(self) -> ghidra.app.util.bin.format.elf.ElfDynamicTable: ...

    @property
    def entryComponentOrdinal(self) -> int: ...

    @property
    def executable(self) -> bool: ...

    @property
    def flags(self) -> unicode: ...

    @property
    def imageBase(self) -> long: ...

    @property
    def littleEndian(self) -> bool: ...

    @property
    def loadAdapter(self) -> ghidra.app.util.bin.format.elf.extend.ElfLoadAdapter: ...

    @property
    def machineName(self) -> unicode: ...

    @property
    def phoffComponentOrdinal(self) -> int: ...

    @property
    def preLinked(self) -> bool: ...

    @property
    def programHeaderOffset(self) -> None: ...  # No getter available.

    @programHeaderOffset.setter
    def programHeaderOffset(self, value: long) -> None: ...

    @property
    def programHeaderProgramHeader(self) -> ghidra.app.util.bin.format.elf.ElfProgramHeader: ...

    @property
    def programHeaders(self) -> List[ghidra.app.util.bin.format.elf.ElfProgramHeader]: ...

    @property
    def reader(self) -> ghidra.app.util.bin.BinaryReader: ...

    @property
    def relocatable(self) -> bool: ...

    @property
    def relocationTables(self) -> List[ghidra.app.util.bin.format.elf.ElfRelocationTable]: ...

    @property
    def sectionHeaderOffset(self) -> None: ...  # No getter available.

    @sectionHeaderOffset.setter
    def sectionHeaderOffset(self, value: long) -> None: ...

    @property
    def sections(self) -> List[ghidra.app.util.bin.format.elf.ElfSectionHeader]: ...

    @property
    def sharedObject(self) -> bool: ...

    @property
    def shoffComponentOrdinal(self) -> int: ...

    @property
    def stringTables(self) -> List[ghidra.app.util.bin.format.elf.ElfStringTable]: ...

    @property
    def symbolTables(self) -> List[ghidra.app.util.bin.format.elf.ElfSymbolTable]: ...
