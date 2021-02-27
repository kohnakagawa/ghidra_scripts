from typing import List
import ghidra.app.util.bin.format.pdb2.pdbreader
import java.lang


class Processor(java.lang.Enum):
    ALPHA_21064: ghidra.app.util.bin.format.pdb2.pdbreader.Processor = Alpha/Alpha 21064
    ALPHA_21164: ghidra.app.util.bin.format.pdb2.pdbreader.Processor = Alpha 21164
    ALPHA_21164A: ghidra.app.util.bin.format.pdb2.pdbreader.Processor = Alpha 21164a
    ALPHA_21264: ghidra.app.util.bin.format.pdb2.pdbreader.Processor = Alpha 21264
    ALPHA_21364: ghidra.app.util.bin.format.pdb2.pdbreader.Processor = Alpha 21364
    AM33: ghidra.app.util.bin.format.pdb2.pdbreader.Processor = AM33
    ARM3: ghidra.app.util.bin.format.pdb2.pdbreader.Processor = ARMv3 (CE)
    ARM4: ghidra.app.util.bin.format.pdb2.pdbreader.Processor = ARMv4 (CE)
    ARM4T: ghidra.app.util.bin.format.pdb2.pdbreader.Processor = ARMv4T (CE)
    ARM5: ghidra.app.util.bin.format.pdb2.pdbreader.Processor = ARMv5 (CE)
    ARM5T: ghidra.app.util.bin.format.pdb2.pdbreader.Processor = ARMv5T (CE)
    ARM6: ghidra.app.util.bin.format.pdb2.pdbreader.Processor = ARMv6 (CE)
    ARM64: ghidra.app.util.bin.format.pdb2.pdbreader.Processor = ARM64
    ARM7: ghidra.app.util.bin.format.pdb2.pdbreader.Processor = ARMv7 (CE)
    ARMNT: ghidra.app.util.bin.format.pdb2.pdbreader.Processor = ARM
    ARM_WMMX: ghidra.app.util.bin.format.pdb2.pdbreader.Processor = ARM (XMMX) (CE)
    ARM_XMAC: ghidra.app.util.bin.format.pdb2.pdbreader.Processor = ARM (XMAC) (CE)
    CEE: ghidra.app.util.bin.format.pdb2.pdbreader.Processor = CEE
    D3D11_SHADER: ghidra.app.util.bin.format.pdb2.pdbreader.Processor = D3D11_SHADER
    EBC: ghidra.app.util.bin.format.pdb2.pdbreader.Processor = EBC
    I80286: ghidra.app.util.bin.format.pdb2.pdbreader.Processor = 80286
    I80386: ghidra.app.util.bin.format.pdb2.pdbreader.Processor = 80386
    I80486: ghidra.app.util.bin.format.pdb2.pdbreader.Processor = 80486
    I8080: ghidra.app.util.bin.format.pdb2.pdbreader.Processor = 8080
    I8086: ghidra.app.util.bin.format.pdb2.pdbreader.Processor = 8086
    IA64_2: ghidra.app.util.bin.format.pdb2.pdbreader.Processor = Itanium (McKinley)
    IA64_IA64_1: ghidra.app.util.bin.format.pdb2.pdbreader.Processor = Itanium
    M32R: ghidra.app.util.bin.format.pdb2.pdbreader.Processor = M32R
    M68000: ghidra.app.util.bin.format.pdb2.pdbreader.Processor = M68000
    M68010: ghidra.app.util.bin.format.pdb2.pdbreader.Processor = M68010
    M68020: ghidra.app.util.bin.format.pdb2.pdbreader.Processor = M68020
    M68030: ghidra.app.util.bin.format.pdb2.pdbreader.Processor = M68030
    M68040: ghidra.app.util.bin.format.pdb2.pdbreader.Processor = M68040
    MIPS16: ghidra.app.util.bin.format.pdb2.pdbreader.Processor = MIPS16
    MIPS32: ghidra.app.util.bin.format.pdb2.pdbreader.Processor = MIPS32
    MIPS64: ghidra.app.util.bin.format.pdb2.pdbreader.Processor = MIPS64
    MIPSI: ghidra.app.util.bin.format.pdb2.pdbreader.Processor = MIPS I
    MIPSII: ghidra.app.util.bin.format.pdb2.pdbreader.Processor = MIPS II
    MIPSIII: ghidra.app.util.bin.format.pdb2.pdbreader.Processor = MIPS III
    MIPSIV: ghidra.app.util.bin.format.pdb2.pdbreader.Processor = MIPS IV
    MIPSV: ghidra.app.util.bin.format.pdb2.pdbreader.Processor = MIPS V
    MIPS_MIPSR4000: ghidra.app.util.bin.format.pdb2.pdbreader.Processor = MIPS (Generic)/R4000
    OMNI: ghidra.app.util.bin.format.pdb2.pdbreader.Processor = Omni
    PENTIUM: ghidra.app.util.bin.format.pdb2.pdbreader.Processor = Pentium
    PENTIUMIII: ghidra.app.util.bin.format.pdb2.pdbreader.Processor = Pentium III
    PENTIUMPRO_PENTIUMII: ghidra.app.util.bin.format.pdb2.pdbreader.Processor = Pentium Pro/Pentium II
    PPC601: ghidra.app.util.bin.format.pdb2.pdbreader.Processor = PPC 601
    PPC603: ghidra.app.util.bin.format.pdb2.pdbreader.Processor = PPC 603
    PPC604: ghidra.app.util.bin.format.pdb2.pdbreader.Processor = PPC 604
    PPC620: ghidra.app.util.bin.format.pdb2.pdbreader.Processor = PPC 620
    PPCBE: ghidra.app.util.bin.format.pdb2.pdbreader.Processor = PPC (Big Endian)
    PPCFP: ghidra.app.util.bin.format.pdb2.pdbreader.Processor = PPC w/FP
    SH3: ghidra.app.util.bin.format.pdb2.pdbreader.Processor = SH3
    SH3DSP: ghidra.app.util.bin.format.pdb2.pdbreader.Processor = SH3DSP
    SH3E: ghidra.app.util.bin.format.pdb2.pdbreader.Processor = SH3E
    SH4: ghidra.app.util.bin.format.pdb2.pdbreader.Processor = SH4
    SHMEDIA: ghidra.app.util.bin.format.pdb2.pdbreader.Processor = SHmedia
    THUMB: ghidra.app.util.bin.format.pdb2.pdbreader.Processor = Thumb (CE)
    TRICORE: ghidra.app.util.bin.format.pdb2.pdbreader.Processor = TriCore
    UNK1AB: ghidra.app.util.bin.format.pdb2.pdbreader.Processor = Unknown1ab
    UNK304: ghidra.app.util.bin.format.pdb2.pdbreader.Processor = Unknown304
    UNKNOWN: ghidra.app.util.bin.format.pdb2.pdbreader.Processor = ???
    X64_AMD64: ghidra.app.util.bin.format.pdb2.pdbreader.Processor = x64
    label: unicode







    @overload
    def compareTo(self, __a0: java.lang.Enum) -> int: ...

    @overload
    def compareTo(self, __a0: object) -> int: ...

    def equals(self, __a0: object) -> bool: ...

    @staticmethod
    def fromValue(__a0: int) -> ghidra.app.util.bin.format.pdb2.pdbreader.Processor: ...

    def getClass(self) -> java.lang.Class: ...

    def getDeclaringClass(self) -> java.lang.Class: ...

    def getValue(self) -> int: ...

    def hashCode(self) -> int: ...

    def name(self) -> unicode: ...

    def notify(self) -> None: ...

    def notifyAll(self) -> None: ...

    def ordinal(self) -> int: ...

    def toString(self) -> unicode: ...

    @overload
    @staticmethod
    def valueOf(__a0: unicode) -> ghidra.app.util.bin.format.pdb2.pdbreader.Processor: ...

    @overload
    @staticmethod
    def valueOf(__a0: java.lang.Class, __a1: unicode) -> java.lang.Enum: ...

    @staticmethod
    def values() -> List[ghidra.app.util.bin.format.pdb2.pdbreader.Processor]: ...

    @overload
    def wait(self) -> None: ...

    @overload
    def wait(self, __a0: long) -> None: ...

    @overload
    def wait(self, __a0: long, __a1: int) -> None: ...

    @property
    def value(self) -> int: ...
