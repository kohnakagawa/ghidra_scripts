import ghidra.app.util.bin.format
import ghidra.app.util.bin.format.elf
import ghidra.program.model.address
import ghidra.util.task
import java.io
import java.lang
import java.util


class ElfLoadAdapter(object):
    """
    ElfLoadAdapter provides the base ELF load adapter implementation
     which may be extended to facilitate target specific behavior.
    """





    def __init__(self): ...



    def addDynamicTypes(self, dynamicTypeMap: java.util.Map) -> None:
        """
        Add all extension specific Dynamic table entry types (e.g., DT_ prefix).
         This method will add all those statically defined ElfDynamicType fields
         within this class.
        @param dynamicTypeMap map to which ElfDynamicType definitions should be added
        """
        ...

    def addProgramHeaderTypes(self, programHeaderTypeMap: java.util.Map) -> None:
        """
        Add all extension specific Program Header types (e.g., PT_ prefix).
         This method will add all those statically defined ElfProgramHeaderType fields
         within this class.
        @param programHeaderTypeMap map to which ElfProgramHeaderType definitions should be added
        """
        ...

    def addSectionHeaderTypes(self, sectionHeaderTypeMap: java.util.HashMap) -> None:
        """
        Add all extension specific Section Header types (e.g., SHT_ prefix).
         This method will add all those statically defined ElfSectionHeaderType fields
         within this class.
        @param sectionHeaderTypeMap map to which ElfSectionHeaderType definitions should be added
        """
        ...

    @overload
    def canHandle(self, elf: ghidra.app.util.bin.format.elf.ElfHeader) -> bool:
        """
        Check if this extension can handle the specified elf header.  If this method returns
         true, this extension will be used to obtain extended types definitions and to perform
         additional load processing.
        @param elf elf header
        @return true if this extension should be used when loading the elf image which
         corresponds to the specified header.
        """
        ...

    @overload
    def canHandle(self, elfLoadHelper: ghidra.app.util.bin.format.elf.ElfLoadHelper) -> bool:
        """
        Check if this extension can handle the specified elf image.  This method can provide
         a more accurate check based upon the actual language utilized.  While the ELF header
         may have stipulated a specific processor via the machine-id, a completely different
         and incompatible language may have been used.
        @param elfLoadHelper elf header
        @return true if this extension can properly support the ELF header and the
         current program/language.
        """
        ...

    def creatingFunction(self, elfLoadHelper: ghidra.app.util.bin.format.elf.ElfLoadHelper, functionAddress: ghidra.program.model.address.Address) -> ghidra.program.model.address.Address:
        """
        Prior to the ELF loader creating a function this method will be invoked to permit an
         extension to adjust the address and/or apply context to the intended location.
        @param elfLoadHelper load helper object
        @param functionAddress function address
        @return adjusted function address (required)
        """
        ...

    def equals(self, __a0: object) -> bool: ...

    def evaluateElfSymbol(self, elfLoadHelper: ghidra.app.util.bin.format.elf.ElfLoadHelper, elfSymbol: ghidra.app.util.bin.format.elf.ElfSymbol, address: ghidra.program.model.address.Address, isExternal: bool) -> ghidra.program.model.address.Address:
        """
        During symbol processing this method will be invoked to permit an extension to
         adjust the address and/or apply context to the intended symbol location.
        @param elfLoadHelper load helper object
        @param elfSymbol elf symbol
        @param address program memory address where symbol will be created
        @param isExternal true if symbol treated as external to the program and has been
         assigned a fake memory address in the EXTERNAL memory block.
        @return adjusted symbol address or null if extension will handle applying the elfSymbol
         to the program (must also invoke {@link ElfLoadHelper#setElfSymbolAddress(ElfSymbol, Address)},
         or symbol should not be applied.
        """
        ...

    def getAdjustedLoadSize(self, elfProgramHeader: ghidra.app.util.bin.format.elf.ElfProgramHeader) -> long:
        """
        Return the memory bytes to be loaded from the underlying file for the specified program header.
         The returned value will be consistent with any byte filtering which may be required.
        @param elfProgramHeader
        @return preferred memory block size in bytes which corresponds to the specified program header
        """
        ...

    def getAdjustedMemoryOffset(self, elfOffset: long, space: ghidra.program.model.address.AddressSpace) -> long:
        """
        Perform any required offset adjustment to account for differences between offset
         values contained within ELF headers and the language modeling of the
         associated address space.
         <br>
         WARNING: This is an experimental method and is not yet fully supported.
         <br>
         NOTE: This has currently been utilized for symbol address offset adjustment only.
        @param elfOffset memory offset from ELF header
        @param space associated address space
        @return offset appropriate for use in space (does not account for image base alterations)
        """
        ...

    def getAdjustedMemorySize(self, elfProgramHeader: ghidra.app.util.bin.format.elf.ElfProgramHeader) -> long:
        """
        Return the memory segment size in bytes for the specified program header.
         The returned value will be consistent with any byte filtering which may be required.
        @param elfProgramHeader
        @return preferred memory block size in bytes which corresponds to the specified program header
        """
        ...

    def getAdjustedSize(self, section: ghidra.app.util.bin.format.elf.ElfSectionHeader) -> long:
        """
        Return the memory section size in bytes for the specified section header.
         The returned value will be consistent with any byte filtering which may be required.
        @param section the section header
        @return preferred memory block size in bytes which corresponds to the specified section header
        """
        ...

    def getClass(self) -> java.lang.Class: ...

    def getDataTypeSuffix(self) -> unicode:
        """
        Return the data type naming suffix which should be used when creating types derived
         from data supplied by this extension.
        @return type naming suffix or null
        """
        ...

    def getDefaultAlignment(self, elfLoadHelper: ghidra.app.util.bin.format.elf.ElfLoadHelper) -> int:
        """
        Get the default alignment within the default address space.
        @param elfLoadHelper helper object
        @return default alignment within the default address space.
        """
        ...

    def getExternalBlockReserveSize(self) -> int:
        """
        Get reserve size of the EXTERNAL memory block as addressable units
         within the default memory space.  This size represents the largest
         expansion size to the block which could occur during relocation
         processing.
        @return reserve size of the EXTERNAL memory block as addressable units
        """
        ...

    def getFilteredLoadInputStream(self, elfLoadHelper: ghidra.app.util.bin.format.elf.ElfLoadHelper, loadable: ghidra.app.util.bin.format.MemoryLoadable, start: ghidra.program.model.address.Address, dataLength: long, dataInput: java.io.InputStream) -> java.io.InputStream:
        """
        Return filtered InputStream for loading a memory block (includes non-loaded OTHER blocks).
         NOTE: If this method is overriden, the {@link #hasFilteredLoadInputStream(ElfLoadHelper, MemoryLoadable, Address)}
         must also be overriden in a consistent fashion.
        @param elfLoadHelper
        @param loadable Corresponding ElfSectionHeader or ElfProgramHeader for the memory block to be created.
        @param start memory load address
        @param dataLength the in-memory data length in bytes (actual bytes read from dataInput may be more)
        @param dataInput the source input stream
        @return filtered input stream or original input stream
        """
        ...

    def getLinkageBlockAlignment(self) -> int:
        """
        Get the dynamic memory block allocation alignment as addressable units
         within the default memory space.
        @return dynamic memory block allocation alignment.
        """
        ...

    def getPreferredExternalBlockSize(self) -> int:
        """
        Get the preferred free range size for the EXTERNAL memory block as addressable units
         within the default memory space.
        @return minimum free range size for EXTERNAL memory block as addressable units
        """
        ...

    def getPreferredSectionAddress(self, elfLoadHelper: ghidra.app.util.bin.format.elf.ElfLoadHelper, elfSectionHeader: ghidra.app.util.bin.format.elf.ElfSectionHeader) -> ghidra.program.model.address.Address:
        """
        Get the preferred load address for an allocated program section.
        @param elfLoadHelper load helper object
        @param elfSectionHeader elf program section header
        @return preferred load address
        """
        ...

    def getPreferredSectionAddressSpace(self, elfLoadHelper: ghidra.app.util.bin.format.elf.ElfLoadHelper, elfSectionHeader: ghidra.app.util.bin.format.elf.ElfSectionHeader) -> ghidra.program.model.address.AddressSpace:
        """
        Get the preferred load address space for an allocated section.   The OTHER space
         is reserved and should not be returned by this method.
        @param elfLoadHelper load helper object
        @param elfSectionHeader elf section header
        @return preferred load address space
        """
        ...

    def getPreferredSegmentAddress(self, elfLoadHelper: ghidra.app.util.bin.format.elf.ElfLoadHelper, elfProgramHeader: ghidra.app.util.bin.format.elf.ElfProgramHeader) -> ghidra.program.model.address.Address:
        """
        Get the preferred load address for a program segment
        @param elfLoadHelper load helper object
        @param elfProgramHeader elf program segment header
        @return preferred load address
        """
        ...

    def getPreferredSegmentAddressSpace(self, elfLoadHelper: ghidra.app.util.bin.format.elf.ElfLoadHelper, elfProgramHeader: ghidra.app.util.bin.format.elf.ElfProgramHeader) -> ghidra.program.model.address.AddressSpace:
        """
        Get the preferred load address space for an allocated program segment.
         The OTHER space is reserved and should not be returned by this method.
        @param elfLoadHelper load helper object
        @param elfProgramHeader elf program segment header
        @return preferred load address space
        """
        ...

    def getRelocationClass(self, elfHeader: ghidra.app.util.bin.format.elf.ElfHeader) -> java.lang.Class:
        """
        Get the ElfRelocation class which should be used to properly parse
         the relocation tables.
        @param elfHeader ELF header object (for header field access only)
        @return ElfRelocation class or null for default behavior
        """
        ...

    def hasFilteredLoadInputStream(self, elfLoadHelper: ghidra.app.util.bin.format.elf.ElfLoadHelper, loadable: ghidra.app.util.bin.format.MemoryLoadable, start: ghidra.program.model.address.Address) -> bool:
        """
        Determine if the use of {@link #getFilteredLoadInputStream(ElfLoadHelper, MemoryLoadable, Address, long, InputStream)}
         is required when loading a memory block.  If a filtered input stream is required this will prevent the use of a direct
         mapping to file bytes.
        @param elfLoadHelper
        @param loadable Corresponding ElfSectionHeader or ElfProgramHeader for the memory block to be loaded.
        @param start memory load address
        @return true if the use of a filtered input stream is required
        """
        ...

    def hashCode(self) -> int: ...

    def isSectionAllocated(self, section: ghidra.app.util.bin.format.elf.ElfSectionHeader) -> bool:
        """
        Determine if the specified section is "allocated" within memory.
        @param section section header object
        @return true if section should be allocated, else false or null to use standard Elf section
         flags to make the determination.
        """
        ...

    def isSectionExecutable(self, section: ghidra.app.util.bin.format.elf.ElfSectionHeader) -> bool:
        """
        Get the execute permission for the specified section (i.e., instructions permitted).
        @param section section header object
        @return true if execute enabled, else false or null to use standard Elf section
         flags to make the determination.
        """
        ...

    def isSectionWritable(self, section: ghidra.app.util.bin.format.elf.ElfSectionHeader) -> bool:
        """
        Get the write permission for the specified section.
        @param section section header object
        @return true if write enabled, else false or null to use standard Elf section
         flags to make the determination.
        """
        ...

    def isSegmentExecutable(self, segment: ghidra.app.util.bin.format.elf.ElfProgramHeader) -> bool:
        """
        Get the execute permission for the specified segment.
        @param segment program header object
        @return true if execute enabled, else false or null to use standard Elf program header
         flags to make the determination.
        """
        ...

    def isSegmentReadable(self, segment: ghidra.app.util.bin.format.elf.ElfProgramHeader) -> bool:
        """
        Get the read permission for the specified segment.
        @param segment program header object
        @return true if read enabled, else false or null to use standard Elf program header
         flags to make the determination.
        """
        ...

    def isSegmentWritable(self, segment: ghidra.app.util.bin.format.elf.ElfProgramHeader) -> bool:
        """
        Get the write permission for the specified segment.
        @param segment program header object
        @return true if write enabled, else false or null to use standard Elf program header
         flags to make the determination.
        """
        ...

    def notify(self) -> None: ...

    def notifyAll(self) -> None: ...

    def processElf(self, elfLoadHelper: ghidra.app.util.bin.format.elf.ElfLoadHelper, monitor: ghidra.util.task.TaskMonitor) -> None:
        """
        Perform extension specific processing of Elf image during program load.
         The following loading steps will have already been completed:
         <pre>
         1. default processing of all program headers and section headers
         2. memory resolution and loading of all program headers and section headers
         3. Markup completed of Elf header, program headers, section headers, dynamic table,
            string tables, and symbol tables.
         </pre>
         Markup and application of relocation tables will NOT have been done yet.
        @param elfLoadHelper load helper object
        @param monitor
        @throws CancelledException
        """
        ...

    def processGotPlt(self, elfLoadHelper: ghidra.app.util.bin.format.elf.ElfLoadHelper, monitor: ghidra.util.task.TaskMonitor) -> None:
        """
        Perform extension specific processing of Elf GOT/PLT tables and any other
         related function relocation mechanism (e.g., function descriptors, etc) after
         normal REL/RELA relocation fix-ups have been applied.
        @param elfLoadHelper load helper object
        @param monitor
        @throws CancelledException
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
    def dataTypeSuffix(self) -> unicode: ...

    @property
    def externalBlockReserveSize(self) -> int: ...

    @property
    def linkageBlockAlignment(self) -> int: ...

    @property
    def preferredExternalBlockSize(self) -> int: ...
