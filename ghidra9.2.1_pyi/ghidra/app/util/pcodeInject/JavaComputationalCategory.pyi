from typing import List
import ghidra.app.util.pcodeInject
import java.lang


class JavaComputationalCategory(java.lang.Enum):
    CAT_1: ghidra.app.util.pcodeInject.JavaComputationalCategory = CAT_1
    CAT_2: ghidra.app.util.pcodeInject.JavaComputationalCategory = CAT_2
    VOID: ghidra.app.util.pcodeInject.JavaComputationalCategory = VOID







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
    def valueOf(__a0: unicode) -> ghidra.app.util.pcodeInject.JavaComputationalCategory: ...

    @overload
    @staticmethod
    def valueOf(__a0: java.lang.Class, __a1: unicode) -> java.lang.Enum: ...

    @staticmethod
    def values() -> List[ghidra.app.util.pcodeInject.JavaComputationalCategory]: ...

    @overload
    def wait(self) -> None: ...

    @overload
    def wait(self, __a0: long) -> None: ...

    @overload
    def wait(self, __a0: long, __a1: int) -> None: ...
