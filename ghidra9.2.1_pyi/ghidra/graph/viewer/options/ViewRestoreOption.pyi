from typing import List
import ghidra.graph.viewer.options
import java.lang


class ViewRestoreOption(java.lang.Enum):
    REMEMBER_SETTINGS: ghidra.graph.viewer.options.ViewRestoreOption = Remember User Settings
    START_FULLY_ZOOMED_IN: ghidra.graph.viewer.options.ViewRestoreOption = Start Fully Zoomed In
    START_FULLY_ZOOMED_OUT: ghidra.graph.viewer.options.ViewRestoreOption = Start Fully Zoomed Out







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
    def valueOf(__a0: unicode) -> ghidra.graph.viewer.options.ViewRestoreOption: ...

    @overload
    @staticmethod
    def valueOf(__a0: java.lang.Class, __a1: unicode) -> java.lang.Enum: ...

    @staticmethod
    def values() -> List[ghidra.graph.viewer.options.ViewRestoreOption]: ...

    @overload
    def wait(self) -> None: ...

    @overload
    def wait(self, __a0: long) -> None: ...

    @overload
    def wait(self, __a0: long, __a1: int) -> None: ...
