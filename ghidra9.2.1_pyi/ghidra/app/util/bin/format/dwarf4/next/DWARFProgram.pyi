from typing import List
import ghidra.app.util.bin
import ghidra.app.util.bin.format.dwarf4
import ghidra.app.util.bin.format.dwarf4.attribs
import ghidra.app.util.bin.format.dwarf4.next
import ghidra.program.model.listing
import ghidra.util.task
import java.io
import java.lang


class DWARFProgram(object, java.io.Closeable):
    """
    DWARFProgram encapsulates a Program with DWARF specific reference data
     used by DWARFDataTypeImporter and DWARFFunctionImporter, along with some
     helper functions.
    """

    DEFAULT_NAME_LENGTH_CUTOFF: int = 2000
    DWARF_ROOT_NAME: unicode = u'DWARF'
    MAX_NAME_LENGTH_CUTOFF: int = 2000
    MIN_NAME_LENGTH_CUTOFF: int = 20



    @overload
    def __init__(self, program: ghidra.program.model.listing.Program, importOptions: ghidra.app.util.bin.format.dwarf4.next.DWARFImportOptions, monitor: ghidra.util.task.TaskMonitor):
        """
        Main constructor for DWARFProgram.
         <p>
         Auto-detects the DWARFSectionProvider and chains to the next constructor.
        @param program Ghidra {@link Program}.
        @param importOptions {@link DWARFImportOptions} to controls options during reading / parsing /importing.
        @param monitor {@link TaskMonitor} to control canceling and progress.
        @throws CancelledException if user cancels
        @throws IOException if error reading data
        @throws DWARFException if bad stuff happens.
        """
        ...

    @overload
    def __init__(self, program: ghidra.program.model.listing.Program, importOptions: ghidra.app.util.bin.format.dwarf4.next.DWARFImportOptions, monitor: ghidra.util.task.TaskMonitor, sectionProvider: ghidra.app.util.bin.format.dwarf4.next.sectionprovider.DWARFSectionProvider):
        """
        Constructor for DWARFProgram.
        @param program Ghidra {@link Program}.
        @param importOptions {@link DWARFImportOptions} to controls options during reading / parsing /importing.
        @param monitor {@link TaskMonitor} to control canceling and progress.
        @param sectionProvider {@link DWARFSectionProvider} factory that finds DWARF .debug_* sections
         wherever they live.
        @throws CancelledException if user cancels
        @throws IOException if error reading data
        @throws DWARFException if bad stuff happens.
        """
        ...



    @staticmethod
    def alreadyDWARFImported(prog: ghidra.program.model.listing.Program) -> bool: ...

    def cacheDNIByOffset(self, offset: long, dni: ghidra.app.util.bin.format.dwarf4.next.DWARFNameInfo) -> None: ...

    def checkPreconditions(self, monitor: ghidra.util.task.TaskMonitor) -> None:
        """
        Iterates over all the DWARF DIE records in the program and checks for some
         pre-known issues, throwing an exception if there is a problem that would
         prevent a successful run.
        @param monitor {@link TaskMonitor} to check for cancel and upate with status.
        @throws DWARFException if DWARF structure error.
        @throws CancelledException if user cancels.
        @throws IOException if error reading data.
        """
        ...

    def clearDIEIndexes(self) -> None:
        """
        Releases the memory used by the DIE entries read when invoking
         {@link #checkPreconditions(TaskMonitor)}.
        """
        ...

    def close(self) -> None: ...

    def equals(self, __a0: object) -> bool: ...

    @overload
    def getAggregate(self, offset: long) -> ghidra.app.util.bin.format.dwarf4.DIEAggregate:
        """
        Returns the {@link DIEAggregate} that contains the {@link DebugInfoEntry} specified
         by the offset.
        @param offset offset of a DIE record
        @return {@link DIEAggregate} that contains the DIE record specified, or null if bad
         offset.
        """
        ...

    @overload
    def getAggregate(self, die: ghidra.app.util.bin.format.dwarf4.DebugInfoEntry) -> ghidra.app.util.bin.format.dwarf4.DIEAggregate:
        """
        Returns the {@link DIEAggregate} that contains the specified {@link DebugInfoEntry}.
        @param die {@link DebugInfoEntry} or null
        @return {@link DIEAggregate} that contains the specified DIE, or null if DIE null or
         the aggregate was not found.
        """
        ...

    def getAggregates(self) -> List[ghidra.app.util.bin.format.dwarf4.DIEAggregate]:
        """
        Returns the list of all currently loaded {@link DIEAggregate}s, which will be either
         just the DIEA of the current CU, or all DIEA if {@link DWARFImportOptions#isPreloadAllDIEs()}.
        @return List of {@link DIEAggregate}.
        """
        ...

    def getAttributeFactory(self) -> ghidra.app.util.bin.format.dwarf4.attribs.DWARFAttributeFactory: ...

    def getClass(self) -> java.lang.Class: ...

    def getCompilationUnitFor(self, offset: long) -> ghidra.app.util.bin.format.dwarf4.DWARFCompilationUnit: ...

    def getCompilationUnits(self) -> List[ghidra.app.util.bin.format.dwarf4.DWARFCompilationUnit]: ...

    def getDIECount(self) -> int:
        """
        Returns the count of the DIE records in this compilation unit.
         <p>
         Only valid if called after {@link #checkPreconditions(TaskMonitor)}
         and before {@link #clearDIEIndexes()}.
        @return number of DIE records in the compunit.
        @throws IOException
        @throws CancelledException
        """
        ...

    def getDebugInfo(self) -> ghidra.app.util.bin.BinaryReader: ...

    def getDebugLine(self) -> ghidra.app.util.bin.BinaryReader: ...

    def getDebugLocation(self) -> ghidra.app.util.bin.BinaryReader: ...

    def getDebugRanges(self) -> ghidra.app.util.bin.BinaryReader: ...

    def getDebugStrings(self) -> ghidra.app.util.bin.format.dwarf4.next.StringTable: ...

    def getEntries(self) -> List[ghidra.app.util.bin.format.dwarf4.DebugInfoEntry]:
        """
        @return the entries list
        """
        ...

    def getEntryAtByteOffsetUnchecked(self, byteOffset: long) -> ghidra.app.util.bin.format.dwarf4.DebugInfoEntry:
        """
        Returns the entry with the given byte offset.
         <p>
         The byte offset corresponds to the byte index
         in the original file where the entry was defined.
         <p>
         Returns null if the requested entry does not exist.
        @param byteOffset the byte offset
        @return the entry with the given byte offset
        """
        ...

    def getEntryName(self, diea: ghidra.app.util.bin.format.dwarf4.DIEAggregate) -> unicode: ...

    def getFoundCrossCURefs(self) -> bool: ...

    def getGhidraProgram(self) -> ghidra.program.model.listing.Program: ...

    def getImportOptions(self) -> ghidra.app.util.bin.format.dwarf4.next.DWARFImportOptions: ...

    def getName(self, diea: ghidra.app.util.bin.format.dwarf4.DIEAggregate) -> ghidra.app.util.bin.format.dwarf4.next.DWARFNameInfo: ...

    def getProgramBaseAddressFixup(self) -> long:
        """
        A fixup value that needs to be applied to static addresses of the program.
         <p>
         This value is necessary if the program's built-in base address is overridden at import time.
         <p>
        @return long value to add to static addresses discovered in DWARF to make it agree with
         Ghidra's imported program.
        """
        ...

    def getRegisterMappings(self) -> ghidra.app.util.bin.format.dwarf4.next.DWARFRegisterMappings: ...

    def getRootDNI(self) -> ghidra.app.util.bin.format.dwarf4.next.DWARFNameInfo: ...

    def getTotalAggregateCount(self) -> int:
        """
        Returns the total number of {@link DIEAggregate} objects in the entire program.
        @return the total number of {@link DIEAggregate} objects in the entire program.
        """
        ...

    def getTotalDIECount(self) -> int:
        """
        Returns the total number of DIE records in the entire program.
        @return the total number of DIE records in the entire program.
        """
        ...

    def getTypeReferers(self, targetDIEA: ghidra.app.util.bin.format.dwarf4.DIEAggregate, tag: int) -> List[ghidra.app.util.bin.format.dwarf4.DIEAggregate]:
        """
        Returns a list of {@link DIEAggregate}s that refer to the targetDIEA via an
         attribute of the specified tag type.
        @param targetDIEA {@link DIEAggregate} that might be pointed to by other DIEAs.
        @param tag the {@link DWARFTag} attribute type that is pointing DIEAs are using
         to refer to the target DIEA.
        @return list of DIEAs that point to the target, empty list if nothing found.
        """
        ...

    def getUncategorizedRootDNI(self) -> ghidra.app.util.bin.format.dwarf4.next.DWARFNameInfo: ...

    def hashCode(self) -> int: ...

    def internAttributeSpec(self, das: ghidra.app.util.bin.format.dwarf4.DWARFAttributeSpecification) -> ghidra.app.util.bin.format.dwarf4.DWARFAttributeSpecification: ...

    def isBigEndian(self) -> bool: ...

    @staticmethod
    def isDWARF(program: ghidra.program.model.listing.Program, monitor: ghidra.util.task.TaskMonitor) -> bool:
        """
        Returns true if the {@link Program program} probably DWARF information.
         <p>
         If the program is an Elf binary, it must have (at least) ".debug_info" and ".debug_abbr" program sections.
         <p>
         If the program is a MachO binary (ie. Mac), it must have a ".dSYM" directory co-located next to the
         original binary file on the native filesystem.  (ie. outside of Ghidra).  See the DSymSectionProvider
         for more info.
         <p>
        @param program
        @param monitor
        @return
        """
        ...

    def isLittleEndian(self) -> bool: ...

    def lookupDNIByOffset(self, offset: long) -> ghidra.app.util.bin.format.dwarf4.next.DWARFNameInfo: ...

    def notify(self) -> None: ...

    def notifyAll(self) -> None: ...

    def setAttributeFactory(self, attributeFactory: ghidra.app.util.bin.format.dwarf4.attribs.DWARFAttributeFactory) -> None: ...

    def setCurrentCompilationUnit(self, cu: ghidra.app.util.bin.format.dwarf4.DWARFCompilationUnit, monitor: ghidra.util.task.TaskMonitor) -> None:
        """
        Sets the currently active compilation unit.  Used when 'paging' through the DIE records
         in a compilation-unit-at-a-time manner, vs the {@link DWARFImportOptions#isPreloadAllDIEs()}
         where all DIE/DIEA records are loaded at once.
        @param cu {@link DWARFCompilationUnit} to set as the active element and load it's DIE records.
        @param monitor {@link TaskMonitor} to update with status and check for cancelation.
        @throws CancelledException if user cancels
        @throws IOException if error reading data
        @throws DWARFException if error in DWARF record structure
        """
        ...

    def setFoundCrossCURefs(self, b: bool) -> None: ...

    def setNameLengthCutoff(self, nameLenCutoff: int) -> None:
        """
        Sets the maximum length of symbols and datatypes created during import.
        @param nameLenCutoff int, should not be more than {@link SymbolUtilities#MAX_SYMBOL_NAME_LENGTH}.
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
    def DIECount(self) -> int: ...

    @property
    def aggregates(self) -> List[object]: ...

    @property
    def attributeFactory(self) -> ghidra.app.util.bin.format.dwarf4.attribs.DWARFAttributeFactory: ...

    @attributeFactory.setter
    def attributeFactory(self, value: ghidra.app.util.bin.format.dwarf4.attribs.DWARFAttributeFactory) -> None: ...

    @property
    def bigEndian(self) -> bool: ...

    @property
    def compilationUnits(self) -> List[object]: ...

    @property
    def debugInfo(self) -> ghidra.app.util.bin.BinaryReader: ...

    @property
    def debugLine(self) -> ghidra.app.util.bin.BinaryReader: ...

    @property
    def debugLocation(self) -> ghidra.app.util.bin.BinaryReader: ...

    @property
    def debugRanges(self) -> ghidra.app.util.bin.BinaryReader: ...

    @property
    def debugStrings(self) -> ghidra.app.util.bin.format.dwarf4.next.StringTable: ...

    @property
    def entries(self) -> List[object]: ...

    @property
    def foundCrossCURefs(self) -> bool: ...

    @foundCrossCURefs.setter
    def foundCrossCURefs(self, value: bool) -> None: ...

    @property
    def ghidraProgram(self) -> ghidra.program.model.listing.Program: ...

    @property
    def importOptions(self) -> ghidra.app.util.bin.format.dwarf4.next.DWARFImportOptions: ...

    @property
    def littleEndian(self) -> bool: ...

    @property
    def nameLengthCutoff(self) -> None: ...  # No getter available.

    @nameLengthCutoff.setter
    def nameLengthCutoff(self, value: int) -> None: ...

    @property
    def programBaseAddressFixup(self) -> long: ...

    @property
    def registerMappings(self) -> ghidra.app.util.bin.format.dwarf4.next.DWARFRegisterMappings: ...

    @property
    def rootDNI(self) -> ghidra.app.util.bin.format.dwarf4.next.DWARFNameInfo: ...

    @property
    def totalAggregateCount(self) -> int: ...

    @property
    def totalDIECount(self) -> int: ...

    @property
    def uncategorizedRootDNI(self) -> ghidra.app.util.bin.format.dwarf4.next.DWARFNameInfo: ...
