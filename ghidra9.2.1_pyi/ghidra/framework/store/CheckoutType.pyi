from typing import List
import ghidra.framework.store
import java.lang


class CheckoutType(java.lang.Enum):
    EXCLUSIVE: ghidra.framework.store.CheckoutType = EXCLUSIVE
    NORMAL: ghidra.framework.store.CheckoutType = NORMAL
    TRANSIENT: ghidra.framework.store.CheckoutType = TRANSIENT
    serialVersionUID: long = 0x1L







    @overload
    def compareTo(self, __a0: java.lang.Enum) -> int: ...

    @overload
    def compareTo(self, __a0: object) -> int: ...

    def equals(self, __a0: object) -> bool: ...

    @staticmethod
    def getCheckoutType(__a0: int) -> ghidra.framework.store.CheckoutType: ...

    def getClass(self) -> java.lang.Class: ...

    def getDeclaringClass(self) -> java.lang.Class: ...

    def getID(self) -> int: ...

    def hashCode(self) -> int: ...

    def name(self) -> unicode: ...

    def notify(self) -> None: ...

    def notifyAll(self) -> None: ...

    def ordinal(self) -> int: ...

    def toString(self) -> unicode: ...

    @overload
    @staticmethod
    def valueOf(__a0: unicode) -> ghidra.framework.store.CheckoutType: ...

    @overload
    @staticmethod
    def valueOf(__a0: java.lang.Class, __a1: unicode) -> java.lang.Enum: ...

    @staticmethod
    def values() -> List[ghidra.framework.store.CheckoutType]: ...

    @overload
    def wait(self) -> None: ...

    @overload
    def wait(self, __a0: long) -> None: ...

    @overload
    def wait(self, __a0: long, __a1: int) -> None: ...

    @property
    def ID(self) -> int: ...
