from typing import List
import ghidra.app.nav
import ghidra.framework.plugintool
import java.lang


class NavigatableRegistry(object):




    def __init__(self): ...



    def equals(self, __a0: object) -> bool: ...

    def getClass(self) -> java.lang.Class: ...

    @staticmethod
    def getNavigatable(navigationID: long) -> ghidra.app.nav.Navigatable: ...

    @staticmethod
    def getRegisteredNavigatables(tool: ghidra.framework.plugintool.PluginTool) -> List[ghidra.app.nav.Navigatable]: ...

    def hashCode(self) -> int: ...

    def notify(self) -> None: ...

    def notifyAll(self) -> None: ...

    @staticmethod
    def registerNavigatable(tool: ghidra.framework.plugintool.PluginTool, navigatable: ghidra.app.nav.Navigatable) -> None: ...

    def toString(self) -> unicode: ...

    @staticmethod
    def unregisterNavigatable(tool: ghidra.framework.plugintool.PluginTool, navigatable: ghidra.app.nav.Navigatable) -> None: ...

    @overload
    def wait(self) -> None: ...

    @overload
    def wait(self, __a0: long) -> None: ...

    @overload
    def wait(self, __a0: long, __a1: int) -> None: ...
