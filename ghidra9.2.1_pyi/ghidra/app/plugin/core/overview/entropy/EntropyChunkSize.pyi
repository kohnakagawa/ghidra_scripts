from typing import List
import ghidra.app.plugin.core.overview.entropy
import java.lang


class EntropyChunkSize(java.lang.Enum):
    LARGE: ghidra.app.plugin.core.overview.entropy.EntropyChunkSize = 1024 Bytes
    MEDIUM: ghidra.app.plugin.core.overview.entropy.EntropyChunkSize = 512 Bytes
    SMALL: ghidra.app.plugin.core.overview.entropy.EntropyChunkSize = 256 Bytes







    @overload
    def compareTo(self, __a0: java.lang.Enum) -> int: ...

    @overload
    def compareTo(self, __a0: object) -> int: ...

    def equals(self, __a0: object) -> bool: ...

    def getChunkSize(self) -> int: ...

    def getClass(self) -> java.lang.Class: ...

    def getDeclaringClass(self) -> java.lang.Class: ...

    def hashCode(self) -> int: ...

    def name(self) -> unicode: ...

    def notify(self) -> None: ...

    def notifyAll(self) -> None: ...

    def ordinal(self) -> int: ...

    def toString(self) -> unicode: ...

    @overload
    @staticmethod
    def valueOf(__a0: unicode) -> ghidra.app.plugin.core.overview.entropy.EntropyChunkSize: ...

    @overload
    @staticmethod
    def valueOf(__a0: java.lang.Class, __a1: unicode) -> java.lang.Enum: ...

    @staticmethod
    def values() -> List[ghidra.app.plugin.core.overview.entropy.EntropyChunkSize]: ...

    @overload
    def wait(self) -> None: ...

    @overload
    def wait(self, __a0: long) -> None: ...

    @overload
    def wait(self, __a0: long, __a1: int) -> None: ...

    @property
    def chunkSize(self) -> int: ...
