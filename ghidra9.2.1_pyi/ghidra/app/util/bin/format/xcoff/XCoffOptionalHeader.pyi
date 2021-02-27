import ghidra.app.util.bin
import ghidra.program.model.data
import java.lang


class XCoffOptionalHeader(object, ghidra.app.util.bin.StructConverter):
    AOUTHDRSZ: int = 72
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

    def getCpuFlag(self) -> int:
        """
        Returns the CPU bit flags.
        @return the CPU bit flags
        """
        ...

    def getCpuType(self) -> int:
        """
        Reserved. Always returns 0.
        @return always returns 0
        """
        ...

    def getDataStart(self) -> long:
        """
        Returns the virtual address of the .data section.
        @return the virtual address of the .data section
        """
        ...

    def getDebugger(self) -> long:
        """
        This field should be 0. When the loaded program
         is being debugged, the memory image of this field
         may be modified by the debugger to insert
         a trap instruction.
        @return should return 0
        """
        ...

    def getEntry(self) -> long:
        """
        Returns the virtual address of the entry point.
        @return the virtual address of the entry point
        """
        ...

    def getFlags(self) -> int:
        """
        This field consists of 4 1-bit flags and a 4-bit .tdata alignment.
        @return the flags
        """
        ...

    def getInitializedDataSize(self) -> long:
        """
        Returns the size (in bytes) of the raw data for the .data section.
        @return the size (in bytes) of the raw data for the .data section
        """
        ...

    def getMagic(self) -> int:
        """
        Returns the magic value. The binder assigns the following value: 0x010b.
        @return the magic value
        """
        ...

    def getMaxAlignmentForData(self) -> int:
        """
        Returns log (base-2) of the maximum alignment needed for
         any csect in the .data or .bss section.
        @return the maximum alignment for the .data or .bss section
        """
        ...

    def getMaxAlignmentForText(self) -> int:
        """
        Returns log (base-2) of the maximum alignment needed for
         any csect in the .text section.
        @return the maximum alignment for the .text section
        """
        ...

    def getMaxDataSize(self) -> long:
        """
        Returns the maximum data size allowed for this executable.
         If the value is 0, then the default value is used.
        @return the maximum data size allow for this executable
        """
        ...

    def getMaxStackSize(self) -> long:
        """
        Returns the maximum stack size allowed for this executable.
         If the value is 0, then the default value is used.
        @return the maximum stack size allow for this executable
        """
        ...

    def getModuleType(self) -> unicode:
        """
        Returns the module type.
         Valid module types:
         		RO - Specifies a read-only module.
        @return the module type
        """
        ...

    def getSectionNumberForBss(self) -> int:
        """
        Returns the number of the .bss section.
        @return the number of the .bss section
        """
        ...

    def getSectionNumberForData(self) -> int:
        """
        Returns the number of the .data section.
        @return the number of the .data section
        """
        ...

    def getSectionNumberForEntry(self) -> int:
        """
        Returns the number of the section that contains the entry point.
         The entry point must be in the .text or .data section.
        @return the number of the section that contains the entry point
        """
        ...

    def getSectionNumberForLoader(self) -> int:
        """
        Returns the number of the section that contains the system loader information.
        @return the number of the section that contains the system loader information
        """
        ...

    def getSectionNumberForTBss(self) -> int: ...

    def getSectionNumberForTData(self) -> int: ...

    def getSectionNumberForTOC(self) -> int:
        """
        Returns the number of the section that contains the TOC.
        @return the number of the section that contains the TOC
        """
        ...

    def getSectionNumberForText(self) -> int:
        """
        Returns the number of the .text section.
        @return the number of the .text section
        """
        ...

    def getTOC(self) -> long:
        """
        Returns the virtual address of the TOC anchor.
        @return the virtual address of the TOC anchor
        """
        ...

    def getTextSize(self) -> long:
        """
        Returns the size (in bytes) of the raw data for the .text section.
        @return the size (in bytes) of the raw data for the .text section
        """
        ...

    def getTextStart(self) -> long:
        """
        Returns the virtual address of the .text section.
        @return the virtual address of the .text section
        """
        ...

    def getUninitializedDataSize(self) -> long:
        """
        Returns the size (in bytes) of the .bss section.
         No raw data exists in the file for the .bss section.
        @return the size (in bytes) of the .bss section
        """
        ...

    def getVersionStamp(self) -> int:
        """
        Returns the format version for this auxiliary header.
         The only valid value is 1.
        @return the format version for this auxiliary header
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
    def TOC(self) -> long: ...

    @property
    def cpuFlag(self) -> int: ...

    @property
    def cpuType(self) -> int: ...

    @property
    def dataStart(self) -> long: ...

    @property
    def debugger(self) -> long: ...

    @property
    def entry(self) -> long: ...

    @property
    def flags(self) -> int: ...

    @property
    def initializedDataSize(self) -> long: ...

    @property
    def magic(self) -> int: ...

    @property
    def maxAlignmentForData(self) -> int: ...

    @property
    def maxAlignmentForText(self) -> int: ...

    @property
    def maxDataSize(self) -> long: ...

    @property
    def maxStackSize(self) -> long: ...

    @property
    def moduleType(self) -> unicode: ...

    @property
    def sectionNumberForBss(self) -> int: ...

    @property
    def sectionNumberForData(self) -> int: ...

    @property
    def sectionNumberForEntry(self) -> int: ...

    @property
    def sectionNumberForLoader(self) -> int: ...

    @property
    def sectionNumberForTBss(self) -> int: ...

    @property
    def sectionNumberForTData(self) -> int: ...

    @property
    def sectionNumberForTOC(self) -> int: ...

    @property
    def sectionNumberForText(self) -> int: ...

    @property
    def textSize(self) -> long: ...

    @property
    def textStart(self) -> long: ...

    @property
    def uninitializedDataSize(self) -> long: ...

    @property
    def versionStamp(self) -> int: ...
