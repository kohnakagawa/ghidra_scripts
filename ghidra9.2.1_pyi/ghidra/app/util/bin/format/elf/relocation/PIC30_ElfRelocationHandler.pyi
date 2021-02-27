import ghidra.app.util.bin.format.elf
import ghidra.app.util.bin.format.elf.relocation
import ghidra.app.util.importer
import ghidra.program.model.address
import ghidra.program.model.listing
import java.lang
import java.util


class PIC30_ElfRelocationHandler(ghidra.app.util.bin.format.elf.relocation.ElfRelocationHandler):
    R_PIC30_16: int = 2
    R_PIC30_32: int = 3
    R_PIC30_8: int = 1
    R_PIC30_ACCESS: int = 55
    R_PIC30_BIT_SELECT_3: int = 36
    R_PIC30_BIT_SELECT_4: int = 38
    R_PIC30_BIT_SELECT_4_BYTE: int = 37
    R_PIC30_BRANCH_ABSOLUTE: int = 29
    R_PIC30_CALL_ACCESS: int = 53
    R_PIC30_DMAOFFSET: int = 46
    R_PIC30_DO_ABSOLUTE: int = 31
    R_PIC30_DSP_6: int = 39
    R_PIC30_DSP_PRESHIFT: int = 40
    R_PIC30_EDSOFFSET: int = 62
    R_PIC30_EDSPAGE: int = 59
    R_PIC30_FILE_REG: int = 5
    R_PIC30_FILE_REG_BYTE: int = 4
    R_PIC30_FILE_REG_WORD: int = 6
    R_PIC30_FILE_REG_WORD_WITH_DST: int = 7
    R_PIC30_FRAME_SIZE: int = 44
    R_PIC30_HANDLE: int = 11
    R_PIC30_L_ACCESS: int = 57
    R_PIC30_L_PSVPTR: int = 51
    R_PIC30_NONE: int = 0
    R_PIC30_PADDR: int = 12
    R_PIC30_PBYTE: int = 9
    R_PIC30_PCREL_ACCESS: int = 54
    R_PIC30_PCREL_BRANCH: int = 28
    R_PIC30_PCREL_DO: int = 30
    R_PIC30_PGM_ADDR_LSB: int = 32
    R_PIC30_PGM_ADDR_MSB: int = 33
    R_PIC30_PSVOFFSET: int = 14
    R_PIC30_PSVPAGE: int = 18
    R_PIC30_PSVPTR: int = 49
    R_PIC30_PWORD: int = 10
    R_PIC30_PWRSAV_MODE: int = 45
    R_PIC30_P_ACCESS: int = 56
    R_PIC30_P_DMAOFFSET: int = 47
    R_PIC30_P_EDSOFFSET: int = 63
    R_PIC30_P_EDSPAGE: int = 60
    R_PIC30_P_HANDLE: int = 25
    R_PIC30_P_PADDR: int = 13
    R_PIC30_P_PSVOFFSET: int = 26
    R_PIC30_P_PSVPAGE: int = 19
    R_PIC30_P_PSVPTR: int = 50
    R_PIC30_P_TBLOFFSET: int = 27
    R_PIC30_P_TBLPAGE: int = 23
    R_PIC30_SIGNED_10_BYTE: int = 41
    R_PIC30_TBLOFFSET: int = 15
    R_PIC30_TBLPAGE: int = 22
    R_PIC30_UNSIGNED_10: int = 42
    R_PIC30_UNSIGNED_14: int = 43
    R_PIC30_UNSIGNED_4: int = 34
    R_PIC30_UNSIGNED_5: int = 35
    R_PIC30_UNSIGNED_8: int = 65
    R_PIC30_WORD: int = 8
    R_PIC30_WORD_ACCESS: int = 58
    R_PIC30_WORD_DMAOFFSET: int = 48
    R_PIC30_WORD_EDSOFFSET: int = 64
    R_PIC30_WORD_EDSPAGE: int = 61
    R_PIC30_WORD_HANDLE: int = 16
    R_PIC30_WORD_PSVOFFSET: int = 17
    R_PIC30_WORD_PSVPAGE: int = 20
    R_PIC30_WORD_PSVPTR: int = 52
    R_PIC30_WORD_TBLOFFSET: int = 21
    R_PIC30_WORD_TBLPAGE: int = 24



    def __init__(self): ...



    def canRelocate(self, __a0: ghidra.app.util.bin.format.elf.ElfHeader) -> bool: ...

    def createRelocationContext(self, __a0: ghidra.app.util.bin.format.elf.ElfLoadHelper, __a1: ghidra.app.util.bin.format.elf.ElfRelocationTable, __a2: java.util.Map) -> ghidra.app.util.bin.format.elf.relocation.ElfRelocationContext: ...

    def equals(self, __a0: object) -> bool: ...

    def getClass(self) -> java.lang.Class: ...

    def getRelrRelocationType(self) -> int: ...

    def hashCode(self) -> int: ...

    @overload
    @staticmethod
    def markAsError(__a0: ghidra.program.model.listing.Program, __a1: ghidra.program.model.address.Address, __a2: long, __a3: unicode, __a4: unicode, __a5: ghidra.app.util.importer.MessageLog) -> None: ...

    @overload
    @staticmethod
    def markAsError(__a0: ghidra.program.model.listing.Program, __a1: ghidra.program.model.address.Address, __a2: unicode, __a3: unicode, __a4: unicode, __a5: ghidra.app.util.importer.MessageLog) -> None: ...

    @staticmethod
    def markAsUnhandled(__a0: ghidra.program.model.listing.Program, __a1: ghidra.program.model.address.Address, __a2: long, __a3: long, __a4: unicode, __a5: ghidra.app.util.importer.MessageLog) -> None: ...

    @staticmethod
    def markAsUninitializedMemory(__a0: ghidra.program.model.listing.Program, __a1: ghidra.program.model.address.Address, __a2: long, __a3: long, __a4: unicode, __a5: ghidra.app.util.importer.MessageLog) -> None: ...

    @staticmethod
    def markAsUnsupportedRelr(__a0: ghidra.program.model.listing.Program, __a1: ghidra.program.model.address.Address) -> None: ...

    @overload
    @staticmethod
    def markAsWarning(__a0: ghidra.program.model.listing.Program, __a1: ghidra.program.model.address.Address, __a2: unicode, __a3: unicode, __a4: ghidra.app.util.importer.MessageLog) -> None: ...

    @overload
    @staticmethod
    def markAsWarning(__a0: ghidra.program.model.listing.Program, __a1: ghidra.program.model.address.Address, __a2: unicode, __a3: unicode, __a4: long, __a5: unicode, __a6: ghidra.app.util.importer.MessageLog) -> None: ...

    def notify(self) -> None: ...

    def notifyAll(self) -> None: ...

    def relocate(self, __a0: ghidra.app.util.bin.format.elf.relocation.ElfRelocationContext, __a1: ghidra.app.util.bin.format.elf.ElfRelocation, __a2: ghidra.program.model.address.Address) -> None: ...

    def toString(self) -> unicode: ...

    @overload
    def wait(self) -> None: ...

    @overload
    def wait(self, __a0: long) -> None: ...

    @overload
    def wait(self, __a0: long, __a1: int) -> None: ...
