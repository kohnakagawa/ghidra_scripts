from typing import List
import ghidra.app.plugin.core.overview.addresstype
import java.lang


class AddressType(java.lang.Enum):
    DATA: ghidra.app.plugin.core.overview.addresstype.AddressType = DATA
    EXTERNAL_REF: ghidra.app.plugin.core.overview.addresstype.AddressType = EXTERNAL_REF
    FUNCTION: ghidra.app.plugin.core.overview.addresstype.AddressType = FUNCTION
    INSTRUCTION: ghidra.app.plugin.core.overview.addresstype.AddressType = INSTRUCTION
    UNDEFINED: ghidra.app.plugin.core.overview.addresstype.AddressType = UNDEFINED
    UNINITIALIZED: ghidra.app.plugin.core.overview.addresstype.AddressType = UNINITIALIZED







    @overload
    def compareTo(self, __a0: java.lang.Enum) -> int: ...

    @overload
    def compareTo(self, __a0: object) -> int: ...

    def equals(self, __a0: object) -> bool: ...

    def getClass(self) -> java.lang.Class: ...

    def getDeclaringClass(self) -> java.lang.Class: ...

    def getDescription(self) -> unicode: ...

    def hashCode(self) -> int: ...

    def name(self) -> unicode: ...

    def notify(self) -> None: ...

    def notifyAll(self) -> None: ...

    def ordinal(self) -> int: ...

    def toString(self) -> unicode: ...

    @overload
    @staticmethod
    def valueOf(__a0: unicode) -> ghidra.app.plugin.core.overview.addresstype.AddressType: ...

    @overload
    @staticmethod
    def valueOf(__a0: java.lang.Class, __a1: unicode) -> java.lang.Enum: ...

    @staticmethod
    def values() -> List[ghidra.app.plugin.core.overview.addresstype.AddressType]: ...

    @overload
    def wait(self) -> None: ...

    @overload
    def wait(self, __a0: long) -> None: ...

    @overload
    def wait(self, __a0: long, __a1: int) -> None: ...

    @property
    def description(self) -> unicode: ...
