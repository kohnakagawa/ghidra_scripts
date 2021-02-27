from typing import List
import ghidra.framework
import java.lang


class Architecture(java.lang.Enum):
    POWERPC: ghidra.framework.Architecture = POWERPC(aarch64)
    POWERPC_64: ghidra.framework.Architecture = POWERPC_64(aarch64)
    UNKNOWN: ghidra.framework.Architecture = UNKNOWN(aarch64)
    X86: ghidra.framework.Architecture = X86(aarch64)
    X86_64: ghidra.framework.Architecture = X86_64(aarch64)







    @overload
    def compareTo(self, __a0: java.lang.Enum) -> int: ...

    @overload
    def compareTo(self, __a0: object) -> int: ...

    def equals(self, __a0: object) -> bool: ...

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
    def valueOf(__a0: unicode) -> ghidra.framework.Architecture: ...

    @overload
    @staticmethod
    def valueOf(__a0: java.lang.Class, __a1: unicode) -> java.lang.Enum: ...

    @staticmethod
    def values() -> List[ghidra.framework.Architecture]: ...

    @overload
    def wait(self) -> None: ...

    @overload
    def wait(self, __a0: long) -> None: ...

    @overload
    def wait(self, __a0: long, __a1: int) -> None: ...
