from typing import List
import ghidra.app.util.bin
import ghidra.app.util.bin.format.coff
import ghidra.program.model.address
import ghidra.program.model.data
import ghidra.program.model.lang
import java.io
import java.lang


class CoffSectionHeader3(ghidra.app.util.bin.format.coff.CoffSectionHeader):
    """
    A 0x2c byte COFF section header
    """









    def equals(self, __a0: object) -> bool: ...

    @overload
    @staticmethod
    def getAddress(language: ghidra.program.model.lang.Language, offset: long, section: ghidra.app.util.bin.format.coff.CoffSectionHeader) -> ghidra.program.model.address.Address:
        """
        Convert address offset to an Address object.  The default data space (defined by pspec)
         will be used if section is null or corresponds to a data section.  The language default
         space (defined by slaspec) will be used for all non-data sections.  If pspec does not
         specify a default data space, the default language space is used.
        @param language
        @param offset address offset (byte offset assumed if section is null or is not explicitly
         byte aligned, otherwise word offset assumed).
        @param section section which contains the specified offset or null (data space assumed)
        @return address object
        """
        ...

    @overload
    @staticmethod
    def getAddress(language: ghidra.program.model.lang.Language, offset: long, space: ghidra.program.model.address.AddressSpace) -> ghidra.program.model.address.Address:
        """
        Convert address offset to an Address in the specified space (defined by pspec).
         If pspec does not specify a default data space, the default language space is used.
        @param language
        @param offset address offset (word offset assumed).
        @param space address space
        @return address object
        """
        ...

    def getClass(self) -> java.lang.Class: ...

    def getFlags(self) -> int:
        """
        Returns the flags for this section.
        @return the flags for this section
        """
        ...

    def getLineNumberCount(self) -> int:
        """
        Returns the number of line number entries for this section.
        @return the number of line number entries for this section
        """
        ...

    def getLineNumbers(self) -> List[ghidra.app.util.bin.format.coff.CoffLineNumber]: ...

    def getName(self) -> unicode:
        """
        Returns the section name.
         The section name will never be more than eight characters.
        @return the section name
        """
        ...

    def getPage(self) -> int: ...

    @overload
    def getPhysicalAddress(self) -> int:
        """
        Returns the physical address offset.
         This is the address at which the section
         should be loaded into memory and reflects a addressable word offset.
         For linked executables, this is the absolute
         address within the program space.
         For unlinked objects, this address is relative
         to the object's address space (i.e. the first section
         is always at offset zero).
        @return the physical address
        """
        ...

    @overload
    def getPhysicalAddress(self, language: ghidra.program.model.lang.Language) -> ghidra.program.model.address.Address:
        """
        Returns the physical address.
         This is the address at which the section
         should be loaded into memory.
         For linked executables, this is the absolute
         address within the program space.
         For unlinked objects, this address is relative
         to the object's address space (i.e. the first section
         is always at offset zero).
        @return the physical address
        """
        ...

    def getPointerToLineNumbers(self) -> int:
        """
        Returns the file offset to the line numbers for this section.
        @return the file offset to the line numbers for this section
        """
        ...

    def getPointerToRawData(self) -> int:
        """
        Returns the file offset to the section data.
        @return the file offset to the section data
        """
        ...

    def getPointerToRelocations(self) -> int:
        """
        Returns the file offset to the relocations for this section.
        @return the file offset to the relocations for this section
        """
        ...

    def getRawDataStream(self, provider: ghidra.app.util.bin.ByteProvider, language: ghidra.program.model.lang.Language) -> java.io.InputStream:
        """
        Returns an input stream that will supply the bytes
         for this section.
        @return the input stream
        @throws IOException if an I/O error occurs
        """
        ...

    def getRelocationCount(self) -> int:
        """
        Returns the number of relocations for this section.
        @return the number of relocations for this section
        """
        ...

    def getRelocations(self) -> List[ghidra.app.util.bin.format.coff.CoffRelocation]: ...

    def getReserved(self) -> int: ...

    def getSize(self, language: ghidra.program.model.lang.Language) -> int:
        """
        Returns the number of bytes of data stored in the file for this section.
         NOTE: This value does not strictly indicate size in bytes.
               For word-oriented machines, this value is represents
               size in words.
        @return the number of bytes of data stored in the file for this section
        """
        ...

    def getVirtualAddress(self) -> int:
        """
        Returns the virtual address.
         This value is always the same as s_paddr.
        @return the virtual address
        """
        ...

    def hashCode(self) -> int: ...

    def isAllocated(self) -> bool: ...

    def isData(self) -> bool: ...

    def isExecutable(self) -> bool: ...

    def isExplicitlyByteAligned(self) -> bool:
        """
        Returns true if this section is byte oriented and aligned and should assume
         an addressable unit size of 1.
        @return true if byte aligned, false if word aligned
        """
        ...

    def isGroup(self) -> bool: ...

    def isInitializedData(self) -> bool: ...

    def isProcessedBytes(self, language: ghidra.program.model.lang.Language) -> bool: ...

    def isReadable(self) -> bool: ...

    def isUninitializedData(self) -> bool: ...

    def isWritable(self) -> bool: ...

    def move(self, offset: int) -> None:
        """
        Adds offset to the physical address; this must be performed before
         relocations in order to achieve the proper result.
        @param offset the offset to add to the physical address
        """
        ...

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
