from typing import List
import ghidra.app.util.bin
import ghidra.app.util.bin.format.dwarf4
import ghidra.app.util.bin.format.dwarf4.next
import ghidra.util.task
import java.lang
import java.util


class DWARFCompilationUnit(object):
    """
    A DWARF "CompilationUnit" is a contiguous block of DebugInfoEntry records found
     in a ".debug_info" section of an ELF program.  The compilation unit block starts with a
     header that has a few important values and flags, and is followed by the DIE records.

     The first DIE record must be a DW_TAG_compile_unit (see DWARFCompileUnit,
     and #getCompileUnit()).

     DIE records are identified by their byte offset in the ".debug_info" section.

    """

    DWARF_32: int = 32
    DWARF_64: int = 64



    def __init__(self, dwarfProgram: ghidra.app.util.bin.format.dwarf4.next.DWARFProgram, startOffset: long, endOffset: long, length: long, format: int, version: int, abbreviationOffset: long, pointerSize: int, compUnitNumber: int, firstDIEOffset: long, codeToAbbreviationMap: java.util.Map):
        """
        This ctor is public only for junit tests.  Do not use directly.
        """
        ...



    def containsOffset(self, offset: long) -> bool:
        """
        Returns true if the {@code offset} value is within
         this compUnit's start and end position in the debug_info section.
        @param offset DIE offset
        @return true if within range of this compunit
        """
        ...

    def equals(self, __a0: object) -> bool: ...

    def getClass(self) -> java.lang.Class: ...

    def getCodeToAbbreviationMap(self) -> java.util.Map: ...

    def getCompUnitNumber(self) -> int: ...

    def getCompileUnit(self) -> ghidra.app.util.bin.format.dwarf4.DWARFCompileUnit: ...

    def getEndOffset(self) -> long:
        """
        Returns the byte offset to the end of this compilation unit.
        @return the byte offset to the end of this compilation unit
        """
        ...

    def getFirstDIEOffset(self) -> long: ...

    def getFormat(self) -> int:
        """
        Returns either DWARF_32 or DWARF_64 depending on the current compilation unit format
        @return DWARF_32 or DWARF_64 constant depending on the current compilation unit format
        """
        ...

    def getLength(self) -> long:
        """
        An unsigned long (4 bytes in 32-bit or 8 bytes in 64-bit format) representing
         the length of the .debug_info contribution for that compilation unit,
         not including the length field itself.
        @return the length in bytes of the this compilation unit
        """
        ...

    def getPointerSize(self) -> int:
        """
        A 1-byte unsigned integer representing the size
         in bytes of an address on the target
         architecture. If the system uses segmented addressing, this
         value represents the size of the offset portion of an address.
        @return the size in bytes of pointers
        """
        ...

    def getProgram(self) -> ghidra.app.util.bin.format.dwarf4.next.DWARFProgram: ...

    def getStartOffset(self) -> long:
        """
        Returns the byte offset to the start of this compilation unit.
        @return the byte offset to the start of this compilation unit
        """
        ...

    def hashCode(self) -> int: ...

    def notify(self) -> None: ...

    def notifyAll(self) -> None: ...

    @staticmethod
    def readCompilationUnit(dwarfProgram: ghidra.app.util.bin.format.dwarf4.next.DWARFProgram, debugInfoBR: ghidra.app.util.bin.BinaryReader, debugAbbrBR: ghidra.app.util.bin.BinaryReader, cuNumber: int, monitor: ghidra.util.task.TaskMonitor) -> ghidra.app.util.bin.format.dwarf4.DWARFCompilationUnit:
        """
        Creates a new {@link DWARFCompilationUnit} by reading a compilationUnit's header data
         from the debug_info section and the debug_abbr section and its compileUnit DIE (ie.
         the first DIE right after the header).
         <p>
         Returns NULL if there was an ignorable error while reading the compilation unit (and
         leaves the input stream at the next compilation unit to read), otherwise throws
         an IOException if there was an unrecoverable error.
        @param dwarfProgram the dwarf program.
        @param debugInfoBR the debug info binary reader.
        @param debugAbbrBR the debug abbreviation binary reader
        @param cuNumber the compilation unit number
        @param monitor the current task monitor
        @return the read compilation unit.
        @throws DWARFException if an invalid or unsupported DWARF version is read.
        @throws IOException if the length of the compilation unit is invalid.
        @throws CancelledException if the task has been canceled.
        """
        ...

    def readDIEs(self, __a0: List[object], __a1: ghidra.util.task.TaskMonitor) -> None: ...

    def toString(self) -> unicode: ...

    @overload
    def wait(self) -> None: ...

    @overload
    def wait(self, __a0: long) -> None: ...

    @overload
    def wait(self, __a0: long, __a1: int) -> None: ...

    @property
    def codeToAbbreviationMap(self) -> java.util.Map: ...

    @property
    def compUnitNumber(self) -> int: ...

    @property
    def compileUnit(self) -> ghidra.app.util.bin.format.dwarf4.DWARFCompileUnit: ...

    @property
    def endOffset(self) -> long: ...

    @property
    def firstDIEOffset(self) -> long: ...

    @property
    def format(self) -> int: ...

    @property
    def length(self) -> long: ...

    @property
    def pointerSize(self) -> int: ...

    @property
    def program(self) -> ghidra.app.util.bin.format.dwarf4.next.DWARFProgram: ...

    @property
    def startOffset(self) -> long: ...
