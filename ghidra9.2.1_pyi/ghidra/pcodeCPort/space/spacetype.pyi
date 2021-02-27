from typing import List
import ghidra.pcodeCPort.space
import java.lang


class spacetype(java.lang.Enum):
    IPTR_CONSTANT: ghidra.pcodeCPort.space.spacetype = IPTR_CONSTANT
    IPTR_FSPEC: ghidra.pcodeCPort.space.spacetype = IPTR_FSPEC
    IPTR_INTERNAL: ghidra.pcodeCPort.space.spacetype = IPTR_INTERNAL
    IPTR_IOP: ghidra.pcodeCPort.space.spacetype = IPTR_IOP
    IPTR_PROCESSOR: ghidra.pcodeCPort.space.spacetype = IPTR_PROCESSOR
    IPTR_SPACEBASE: ghidra.pcodeCPort.space.spacetype = IPTR_SPACEBASE







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
    def valueOf(__a0: unicode) -> ghidra.pcodeCPort.space.spacetype: ...

    @overload
    @staticmethod
    def valueOf(__a0: java.lang.Class, __a1: unicode) -> java.lang.Enum: ...

    @staticmethod
    def values() -> List[ghidra.pcodeCPort.space.spacetype]: ...

    @overload
    def wait(self) -> None: ...

    @overload
    def wait(self, __a0: long) -> None: ...

    @overload
    def wait(self, __a0: long, __a1: int) -> None: ...
