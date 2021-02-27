from typing import List
import ghidra.feature.vt.api.main
import java.lang


class VTMarkupItemApplyActionType(java.lang.Enum):
    ADD: ghidra.feature.vt.api.main.VTMarkupItemApplyActionType = ADD
    ADD_AS_PRIMARY: ghidra.feature.vt.api.main.VTMarkupItemApplyActionType = ADD_AS_PRIMARY
    REPLACE: ghidra.feature.vt.api.main.VTMarkupItemApplyActionType = REPLACE
    REPLACE_DEFAULT_ONLY: ghidra.feature.vt.api.main.VTMarkupItemApplyActionType = REPLACE_DEFAULT_ONLY
    REPLACE_FIRST_ONLY: ghidra.feature.vt.api.main.VTMarkupItemApplyActionType = REPLACE_FIRST_ONLY







    @overload
    def compareTo(self, __a0: java.lang.Enum) -> int: ...

    @overload
    def compareTo(self, __a0: object) -> int: ...

    def equals(self, __a0: object) -> bool: ...

    def getApplyStatus(self) -> ghidra.feature.vt.api.main.VTMarkupItemStatus: ...

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
    def valueOf(__a0: unicode) -> ghidra.feature.vt.api.main.VTMarkupItemApplyActionType: ...

    @overload
    @staticmethod
    def valueOf(__a0: java.lang.Class, __a1: unicode) -> java.lang.Enum: ...

    @staticmethod
    def values() -> List[ghidra.feature.vt.api.main.VTMarkupItemApplyActionType]: ...

    @overload
    def wait(self) -> None: ...

    @overload
    def wait(self, __a0: long) -> None: ...

    @overload
    def wait(self, __a0: long, __a1: int) -> None: ...

    @property
    def applyStatus(self) -> ghidra.feature.vt.api.main.VTMarkupItemStatus: ...
