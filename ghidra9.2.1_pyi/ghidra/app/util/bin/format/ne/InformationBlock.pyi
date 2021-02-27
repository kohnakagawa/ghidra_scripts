import java.lang


class InformationBlock(object):
    """

     A class to represent the Information Block
     defined in the Windows new-style executable.


     ...as defined in WINNT.H


     typedef struct _IMAGE_OS2_HEADER {      // OS/2 .EXE header
         WORD   ne_magic;                    // Magic number
         CHAR   ne_ver;                      // Version number
         CHAR   ne_rev;                      // Revision number
         WORD   ne_enttab;                   // Offset of Entry Table
         WORD   ne_cbenttab;                 // Number of bytes in Entry Table
         LONG   ne_crc;                      // Checksum of whole file
         WORD   ne_flags;                    // Flag word
         WORD   ne_autodata;                 // Automatic data segment number
         WORD   ne_heap;                     // Initial heap allocation
         WORD   ne_stack;                    // Initial stack allocation
         LONG   ne_csip;                     // Initial CS:IP setting
         LONG   ne_sssp;                     // Initial SS:SP setting
         WORD   ne_cseg;                     // Count of file segments
         WORD   ne_cmod;                     // Entries in Module Reference Table
         WORD   ne_cbnrestab;                // Size of non-resident name table
         WORD   ne_segtab;                   // Offset of Segment Table
         WORD   ne_rsrctab;                  // Offset of Resource Table
         WORD   ne_restab;                   // Offset of resident name table
         WORD   ne_modtab;                   // Offset of Module Reference Table
         WORD   ne_imptab;                   // Offset of Imported Names Table
         LONG   ne_nrestab;                  // Offset of Non-resident Names Table
         WORD   ne_cmovent;                  // Count of movable entries
         WORD   ne_align;                    // Segment alignment shift count
         WORD   ne_cres;                     // Count of resource segments
         BYTE   ne_exetyp;                   // Target Operating system
         BYTE   ne_flagsothers;              // Other .EXE flags
         WORD   ne_pretthunks;               // offset to return thunks
         WORD   ne_psegrefbytes;             // offset to segment ref. bytes
         WORD   ne_swaparea;                 // Minimum code swap area size
         WORD   ne_expver;                   // Expected Windows version number
     } IMAGE_OS2_HEADER, *PIMAGE_OS2_HEADER;

    """

    EXETYPE_BOSS: int = 5
    EXETYPE_EUROPEAN_DOS_4: int = 4
    EXETYPE_OS2: int = 1
    EXETYPE_PHARLAP_286_OS2: int = -127
    EXETYPE_PHARLAP_286_WIN: int = -126
    EXETYPE_RESERVED4: int = 8
    EXETYPE_UNKNOWN: int = 0
    EXETYPE_WINDOWS: int = 2
    EXETYPE_WINDOWS_386: int = 4
    FLAGS_APP_FULL_SCREEN: int = 1
    FLAGS_APP_LIBRARY_MODULE: int = -128
    FLAGS_APP_LINK_ERRS: int = 32
    FLAGS_APP_LOAD_CODE: int = 8
    FLAGS_APP_NONCONFORMING_PROG: int = 64
    FLAGS_APP_WINDOWS_PM: int = 3
    FLAGS_APP_WIN_PM_COMPATIBLE: int = 2
    FLAGS_PROG_80286: int = 32
    FLAGS_PROG_80386: int = 64
    FLAGS_PROG_8086: int = 16
    FLAGS_PROG_80x87: int = -128
    FLAGS_PROG_GLOBAL_INIT: int = 4
    FLAGS_PROG_MULTIPLE_DATA: int = 2
    FLAGS_PROG_NO_AUTO_DATA: int = 0
    FLAGS_PROG_PROTECTED_MODE: int = 8
    FLAGS_PROG_SINGLE_DATA: int = 1
    OTHER_FLAGS_GANGLOAD_AREA: int = 4
    OTHER_FLAGS_PROPORTIONAL_FONT: int = 2
    OTHER_FLAGS_PROTECTED_MODE: int = 1
    OTHER_FLAGS_SUPPORTS_LONG_NAMES: int = 0







    def equals(self, __a0: object) -> bool: ...

    def getApplicationFlags(self) -> int:
        """
        Returns the application flags.
        @return the application flags
        """
        ...

    def getApplicationFlagsAsString(self) -> unicode:
        """
        Returns a string representation of the application flags.
        @return a string representation of the application flags
        """
        ...

    def getAutomaticDataSegment(self) -> int:
        """
        Returns the automatic data segment.
        @return the automatic data segment
        """
        ...

    def getChecksum(self) -> int:
        """
        Returns the checksum.
        @return the checksum
        """
        ...

    def getClass(self) -> java.lang.Class: ...

    def getEntryPointOffset(self) -> int:
        """
        Returns the offset portion of the entry point.
        @return the offset portion of the entry point
        """
        ...

    def getEntryPointSegment(self) -> int:
        """
        Returns the segment portion of the entry point.
        @return the segment portion of the entry point
        """
        ...

    def getExpectedWindowsVersion(self) -> int:
        """
        Returns the expected windows version.
        @return the expected windows version
        """
        ...

    def getInitialHeapSize(self) -> int:
        """
        Returns the initial heap size.
        @return the initial heap size
        """
        ...

    def getInitialStackSize(self) -> int:
        """
        Returns the initial stack size.
        @return the initial stack size
        """
        ...

    def getMagicNumber(self) -> int:
        """
        Returns the magic number.
        @return the magic number
        """
        ...

    def getMinCodeSwapSize(self) -> int:
        """
        Returns the minimum code swap size.
        @return the minimum code swap size
        """
        ...

    def getOtherFlags(self) -> int:
        """
        Returns the other flags.
        @return the other flags
        """
        ...

    def getOtherFlagsAsString(self) -> unicode:
        """
        Returns a string representation of the other flags.
        @return a string representation of the other flags
        """
        ...

    def getProgramFlags(self) -> int:
        """
        Returns the program flags.
        @return the program flags
        """
        ...

    def getProgramFlagsAsString(self) -> unicode:
        """
        Returns a string representation of the program flags.
        @return a string representation of the program flags
        """
        ...

    def getRevision(self) -> int:
        """
        Returns the revision number.
        @return the revision number
        """
        ...

    def getStackPointerOffset(self) -> int:
        """
        Returns the offset portion of the stack pointer.
        @return the offset portion of the stack pointer
        """
        ...

    def getStackPointerSegment(self) -> int:
        """
        Returns the segment portion of the stack pointer.
        @return the segment portion of the stack pointer
        """
        ...

    def getTargetOpSys(self) -> int:
        """
        Returns the target operating system.
        @return the target operating system
        """
        ...

    def getTargetOpSysAsString(self) -> unicode:
        """
        Returns a string representation of the target operating system.
        @return a string representation of the target operating system
        """
        ...

    def getVersion(self) -> int:
        """
        Returns the version number.
        @return the version number
        """
        ...

    def hashCode(self) -> int: ...

    def notify(self) -> None: ...

    def notifyAll(self) -> None: ...

    def toString(self) -> unicode: ...

    @overload
    def wait(self) -> None: ...

    @overload
    def wait(self, __a0: long) -> None: ...

    @overload
    def wait(self, __a0: long, __a1: int) -> None: ...

    @property
    def applicationFlags(self) -> int: ...

    @property
    def applicationFlagsAsString(self) -> unicode: ...

    @property
    def automaticDataSegment(self) -> int: ...

    @property
    def checksum(self) -> int: ...

    @property
    def entryPointOffset(self) -> int: ...

    @property
    def entryPointSegment(self) -> int: ...

    @property
    def expectedWindowsVersion(self) -> int: ...

    @property
    def initialHeapSize(self) -> int: ...

    @property
    def initialStackSize(self) -> int: ...

    @property
    def magicNumber(self) -> int: ...

    @property
    def minCodeSwapSize(self) -> int: ...

    @property
    def otherFlags(self) -> int: ...

    @property
    def otherFlagsAsString(self) -> unicode: ...

    @property
    def programFlags(self) -> int: ...

    @property
    def programFlagsAsString(self) -> unicode: ...

    @property
    def revision(self) -> int: ...

    @property
    def stackPointerOffset(self) -> int: ...

    @property
    def stackPointerSegment(self) -> int: ...

    @property
    def targetOpSys(self) -> int: ...

    @property
    def targetOpSysAsString(self) -> unicode: ...

    @property
    def version(self) -> int: ...
