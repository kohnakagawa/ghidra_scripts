from typing import List
import ghidra.app.plugin.core.overview.entropy
import java.lang


class EntropyKnot(java.lang.Enum):
    ARM: ghidra.app.plugin.core.overview.entropy.EntropyKnot = ARM code
    ASCII: ghidra.app.plugin.core.overview.entropy.EntropyKnot = ASCII strings
    COMPRESSED: ghidra.app.plugin.core.overview.entropy.EntropyKnot = Compressed
    NONE: ghidra.app.plugin.core.overview.entropy.EntropyKnot = None
    POWER_PC: ghidra.app.plugin.core.overview.entropy.EntropyKnot = PowerPC code
    THUMB: ghidra.app.plugin.core.overview.entropy.EntropyKnot = THUMB code
    UTF16: ghidra.app.plugin.core.overview.entropy.EntropyKnot = Unicode UTF16
    X86: ghidra.app.plugin.core.overview.entropy.EntropyKnot = x86 code







    @overload
    def compareTo(self, __a0: java.lang.Enum) -> int: ...

    @overload
    def compareTo(self, __a0: object) -> int: ...

    def equals(self, __a0: object) -> bool: ...

    def getClass(self) -> java.lang.Class: ...

    def getDeclaringClass(self) -> java.lang.Class: ...

    def getRecord(self) -> ghidra.app.plugin.core.overview.entropy.EntropyRecord: ...

    def hashCode(self) -> int: ...

    def name(self) -> unicode: ...

    def notify(self) -> None: ...

    def notifyAll(self) -> None: ...

    def ordinal(self) -> int: ...

    def toString(self) -> unicode: ...

    @overload
    @staticmethod
    def valueOf(__a0: unicode) -> ghidra.app.plugin.core.overview.entropy.EntropyKnot: ...

    @overload
    @staticmethod
    def valueOf(__a0: java.lang.Class, __a1: unicode) -> java.lang.Enum: ...

    @staticmethod
    def values() -> List[ghidra.app.plugin.core.overview.entropy.EntropyKnot]: ...

    @overload
    def wait(self) -> None: ...

    @overload
    def wait(self, __a0: long) -> None: ...

    @overload
    def wait(self, __a0: long, __a1: int) -> None: ...

    @property
    def record(self) -> ghidra.app.plugin.core.overview.entropy.EntropyRecord: ...
