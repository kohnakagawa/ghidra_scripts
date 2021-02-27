from typing import List
import ghidra.app.util.bin.format.pdb2.pdbreader
import java.lang


class ImageFileMachine(java.lang.Enum):
    ALPHA: ghidra.app.util.bin.format.pdb2.pdbreader.ImageFileMachine = Alpha_AXP
    ALPHA64: ghidra.app.util.bin.format.pdb2.pdbreader.ImageFileMachine = ALPHA64
    AM33: ghidra.app.util.bin.format.pdb2.pdbreader.ImageFileMachine = TAM33BD
    AMD64: ghidra.app.util.bin.format.pdb2.pdbreader.ImageFileMachine = AMD64 (K8)
    ARM: ghidra.app.util.bin.format.pdb2.pdbreader.ImageFileMachine = ARM Little-Endian
    ARM64: ghidra.app.util.bin.format.pdb2.pdbreader.ImageFileMachine = ARM64 Little-Endian
    ARMNT: ghidra.app.util.bin.format.pdb2.pdbreader.ImageFileMachine = ARM Thumb-2 Little-Endian
    AXP64: ghidra.app.util.bin.format.pdb2.pdbreader.ImageFileMachine = AXP64
    CEE: ghidra.app.util.bin.format.pdb2.pdbreader.ImageFileMachine = CEE
    CEF: ghidra.app.util.bin.format.pdb2.pdbreader.ImageFileMachine = CEF
    EBC: ghidra.app.util.bin.format.pdb2.pdbreader.ImageFileMachine = EFI Byte Code
    I386: ghidra.app.util.bin.format.pdb2.pdbreader.ImageFileMachine = Intel 386
    I860: ghidra.app.util.bin.format.pdb2.pdbreader.ImageFileMachine = Intel I860
    IA64: ghidra.app.util.bin.format.pdb2.pdbreader.ImageFileMachine = Intel 64
    M32R: ghidra.app.util.bin.format.pdb2.pdbreader.ImageFileMachine = M32R little-endian
    M68K: ghidra.app.util.bin.format.pdb2.pdbreader.ImageFileMachine = Motorola 68000
    MIPS16: ghidra.app.util.bin.format.pdb2.pdbreader.ImageFileMachine = MIPS16
    MIPSFPU: ghidra.app.util.bin.format.pdb2.pdbreader.ImageFileMachine = MIPSFPU
    MIPSFPU16: ghidra.app.util.bin.format.pdb2.pdbreader.ImageFileMachine = MIPSFPU16
    POWERPC: ghidra.app.util.bin.format.pdb2.pdbreader.ImageFileMachine = IBM PowerPC Little-Endian
    POWERPCBE: ghidra.app.util.bin.format.pdb2.pdbreader.ImageFileMachine = POWERPCBE
    POWERPCFP: ghidra.app.util.bin.format.pdb2.pdbreader.ImageFileMachine = POWERPCFP
    R10000: ghidra.app.util.bin.format.pdb2.pdbreader.ImageFileMachine = MIPS little-endian
    R3000: ghidra.app.util.bin.format.pdb2.pdbreader.ImageFileMachine = MIPS little-endian, 0x160 big-endian
    R4000: ghidra.app.util.bin.format.pdb2.pdbreader.ImageFileMachine = MIPS little-endian
    SH3: ghidra.app.util.bin.format.pdb2.pdbreader.ImageFileMachine = SH3 little-endian
    SH3DSP: ghidra.app.util.bin.format.pdb2.pdbreader.ImageFileMachine = SH3DSP
    SH3E: ghidra.app.util.bin.format.pdb2.pdbreader.ImageFileMachine = SH3E little-endian
    SH4: ghidra.app.util.bin.format.pdb2.pdbreader.ImageFileMachine = SH4 little-endian
    SH5: ghidra.app.util.bin.format.pdb2.pdbreader.ImageFileMachine = SH5
    TARGET_HOST: ghidra.app.util.bin.format.pdb2.pdbreader.ImageFileMachine = Interacts with the host and not a WOW64 guest
    THUMB: ghidra.app.util.bin.format.pdb2.pdbreader.ImageFileMachine = ARM Thumb/Thumb-2 Little-Endian
    TRICORE: ghidra.app.util.bin.format.pdb2.pdbreader.ImageFileMachine = Infineon
    UNKNOWN: ghidra.app.util.bin.format.pdb2.pdbreader.ImageFileMachine = Unknown
    WCEMIPSV2: ghidra.app.util.bin.format.pdb2.pdbreader.ImageFileMachine = MIPS little-endian WCE v2







    @overload
    def compareTo(self, __a0: java.lang.Enum) -> int: ...

    @overload
    def compareTo(self, __a0: object) -> int: ...

    def equals(self, __a0: object) -> bool: ...

    @staticmethod
    def fromValue(__a0: int) -> ghidra.app.util.bin.format.pdb2.pdbreader.ImageFileMachine: ...

    def getClass(self) -> java.lang.Class: ...

    def getDeclaringClass(self) -> java.lang.Class: ...

    def getProcessor(self) -> ghidra.app.util.bin.format.pdb2.pdbreader.Processor: ...

    def hashCode(self) -> int: ...

    def name(self) -> unicode: ...

    def notify(self) -> None: ...

    def notifyAll(self) -> None: ...

    def ordinal(self) -> int: ...

    def toString(self) -> unicode: ...

    @overload
    @staticmethod
    def valueOf(__a0: unicode) -> ghidra.app.util.bin.format.pdb2.pdbreader.ImageFileMachine: ...

    @overload
    @staticmethod
    def valueOf(__a0: java.lang.Class, __a1: unicode) -> java.lang.Enum: ...

    @staticmethod
    def values() -> List[ghidra.app.util.bin.format.pdb2.pdbreader.ImageFileMachine]: ...

    @overload
    def wait(self) -> None: ...

    @overload
    def wait(self, __a0: long) -> None: ...

    @overload
    def wait(self, __a0: long, __a1: int) -> None: ...

    @property
    def processor(self) -> ghidra.app.util.bin.format.pdb2.pdbreader.Processor: ...
