import ghidra.framework.plugintool.util
import ghidra.util.classfinder
import java.lang
import javax.swing


class PluginPackage(object, ghidra.util.classfinder.ExtensionPoint, java.lang.Comparable):
    CORE_PRIORITY: int = 0
    DEVELOPER_PRIORITY: int = 8
    EXAMPLES_PRIORITY: int = 10
    EXPERIMENTAL_PRIORITY: int = 12
    FEATURE_PRIORITY: int = 4
    MISCELLANIOUS_PRIORITY: int = 6







    @overload
    def compareTo(self, other: ghidra.framework.plugintool.util.PluginPackage) -> int: ...

    @overload
    def compareTo(self, __a0: object) -> int: ...

    def equals(self, __a0: object) -> bool: ...

    def getClass(self) -> java.lang.Class: ...

    def getDescription(self) -> unicode: ...

    def getIcon(self) -> javax.swing.Icon: ...

    def getName(self) -> unicode: ...

    @staticmethod
    def getPluginPackage(packageName: unicode) -> ghidra.framework.plugintool.util.PluginPackage: ...

    def hashCode(self) -> int: ...

    def isfullyAddable(self) -> bool: ...

    def notify(self) -> None: ...

    def notifyAll(self) -> None: ...

    def toString(self) -> unicode: ...

    @overload
    def wait(self) -> None: ...

    @overload
    def wait(self, __a0: long) -> None: ...

    @overload
    def wait(self, __a0: long, __a1: int) -> None: ...

    @property
    def description(self) -> unicode: ...

    @property
    def fullyAddable(self) -> bool: ...

    @property
    def icon(self) -> javax.swing.Icon: ...

    @property
    def name(self) -> unicode: ...
