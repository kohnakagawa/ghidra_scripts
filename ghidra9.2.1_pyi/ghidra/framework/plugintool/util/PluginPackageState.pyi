from typing import List
import ghidra.framework.plugintool.util
import java.lang


class PluginPackageState(java.lang.Enum):
    ALL_PLUGINS_LOADED: ghidra.framework.plugintool.util.PluginPackageState = ALL_PLUGINS_LOADED
    NO_PLUGINS_LOADED: ghidra.framework.plugintool.util.PluginPackageState = NO_PLUGINS_LOADED
    SOME_PLUGINS_LOADED: ghidra.framework.plugintool.util.PluginPackageState = SOME_PLUGINS_LOADED







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
    def valueOf(__a0: unicode) -> ghidra.framework.plugintool.util.PluginPackageState: ...

    @overload
    @staticmethod
    def valueOf(__a0: java.lang.Class, __a1: unicode) -> java.lang.Enum: ...

    @staticmethod
    def values() -> List[ghidra.framework.plugintool.util.PluginPackageState]: ...

    @overload
    def wait(self) -> None: ...

    @overload
    def wait(self, __a0: long) -> None: ...

    @overload
    def wait(self, __a0: long, __a1: int) -> None: ...
