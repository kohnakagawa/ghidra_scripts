from typing import List
import ghidra.feature.vt.gui.util
import java.lang


class MungedAssocationAndMarkupItemStatus(java.lang.Enum):
    ACCEPTED_FULLY_APPLIED: ghidra.feature.vt.gui.util.MungedAssocationAndMarkupItemStatus = ACCEPTED_FULLY_APPLIED
    ACCEPTED_HAS_ERRORS: ghidra.feature.vt.gui.util.MungedAssocationAndMarkupItemStatus = ACCEPTED_HAS_ERRORS
    ACCEPTED_NO_UNEXAMINED: ghidra.feature.vt.gui.util.MungedAssocationAndMarkupItemStatus = ACCEPTED_NO_UNEXAMINED
    ACCEPTED_SOME_UNEXAMINED: ghidra.feature.vt.gui.util.MungedAssocationAndMarkupItemStatus = ACCEPTED_SOME_UNEXAMINED
    AVAILABLE: ghidra.feature.vt.gui.util.MungedAssocationAndMarkupItemStatus = AVAILABLE
    BLOCKED: ghidra.feature.vt.gui.util.MungedAssocationAndMarkupItemStatus = BLOCKED
    REJECTED: ghidra.feature.vt.gui.util.MungedAssocationAndMarkupItemStatus = REJECTED







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
    def valueOf(__a0: unicode) -> ghidra.feature.vt.gui.util.MungedAssocationAndMarkupItemStatus: ...

    @overload
    @staticmethod
    def valueOf(__a0: java.lang.Class, __a1: unicode) -> java.lang.Enum: ...

    @staticmethod
    def values() -> List[ghidra.feature.vt.gui.util.MungedAssocationAndMarkupItemStatus]: ...

    @overload
    def wait(self) -> None: ...

    @overload
    def wait(self, __a0: long) -> None: ...

    @overload
    def wait(self, __a0: long, __a1: int) -> None: ...

    @property
    def description(self) -> unicode: ...
