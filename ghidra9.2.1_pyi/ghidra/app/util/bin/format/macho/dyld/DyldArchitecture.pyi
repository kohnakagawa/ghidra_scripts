import ghidra.app.util.bin
import ghidra.app.util.bin.format.macho.dyld
import ghidra.program.model.lang
import java.lang


class DyldArchitecture(object):
    ARCHITECTURES: List[ghidra.app.util.bin.format.macho.dyld.DyldArchitecture] = array(ghidra.app.util.bin.format.macho.dyld.DyldArchitecture, [dyld_v1    i386, dyld_v1  x86_64, dyld_v1 x86_64h, dyld_v1     ppc, dyld_v1   armv6, dyld_v1   armv7, dyld_v1  armv7f, dyld_v1  armv7s, dyld_v1  armv7k, dyld_v1   arm64, dyld_v1  arm64e])
    ARMV6: ghidra.app.util.bin.format.macho.dyld.DyldArchitecture = dyld_v1   armv6
    ARMV7: ghidra.app.util.bin.format.macho.dyld.DyldArchitecture = dyld_v1   armv7
    ARMV7F: ghidra.app.util.bin.format.macho.dyld.DyldArchitecture = dyld_v1  armv7f
    ARMV7K: ghidra.app.util.bin.format.macho.dyld.DyldArchitecture = dyld_v1  armv7k
    ARMV7S: ghidra.app.util.bin.format.macho.dyld.DyldArchitecture = dyld_v1  armv7s
    ARMV8A: ghidra.app.util.bin.format.macho.dyld.DyldArchitecture = dyld_v1   arm64
    ARMV8Ae: ghidra.app.util.bin.format.macho.dyld.DyldArchitecture = dyld_v1  arm64e
    DYLD_V1_SIGNATURE_LEN: int = 16
    DYLD_V1_SIGNATURE_PREFIX: unicode = u'dyld_v1'
    POWERPC: ghidra.app.util.bin.format.macho.dyld.DyldArchitecture = dyld_v1     ppc
    X86: ghidra.app.util.bin.format.macho.dyld.DyldArchitecture = dyld_v1    i386
    X86_64: ghidra.app.util.bin.format.macho.dyld.DyldArchitecture = dyld_v1  x86_64
    X86_64h: ghidra.app.util.bin.format.macho.dyld.DyldArchitecture = dyld_v1 x86_64h







    def equals(self, __a0: object) -> bool: ...

    @overload
    @staticmethod
    def getArchitecture(signature: unicode) -> ghidra.app.util.bin.format.macho.dyld.DyldArchitecture:
        """
        Returns the architecture object with the given signature.
         Returns NULL if one does not exist.
        @param signature the signature string
        @return the architecture object with the given signature or NULL
        """
        ...

    @overload
    @staticmethod
    def getArchitecture(provider: ghidra.app.util.bin.ByteProvider) -> ghidra.app.util.bin.format.macho.dyld.DyldArchitecture: ...

    def getClass(self) -> java.lang.Class: ...

    def getCpuSubType(self) -> int: ...

    def getCpuType(self) -> int: ...

    def getEndianness(self) -> ghidra.program.model.lang.Endian: ...

    def getLanguageCompilerSpecPair(self, languageService: ghidra.program.model.lang.LanguageService) -> ghidra.program.model.lang.LanguageCompilerSpecPair: ...

    def getProcessor(self) -> unicode: ...

    def getSignature(self) -> unicode: ...

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
    def cpuSubType(self) -> int: ...

    @property
    def cpuType(self) -> int: ...

    @property
    def endianness(self) -> ghidra.program.model.lang.Endian: ...

    @property
    def processor(self) -> unicode: ...

    @property
    def signature(self) -> unicode: ...
