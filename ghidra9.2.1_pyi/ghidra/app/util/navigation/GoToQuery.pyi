import java.lang


class GoToQuery(object):




    def __init__(self, navigatable: ghidra.app.nav.Navigatable, plugin: ghidra.framework.plugintool.Plugin, goToService: ghidra.app.services.GoToService, queryData: ghidra.app.services.QueryData, fromAddr: ghidra.program.model.address.Address, listener: ghidra.app.services.GoToServiceListener, navigationOptions: ghidra.app.plugin.core.navigation.NavigationOptions, monitor: ghidra.util.task.TaskMonitor): ...



    def equals(self, __a0: object) -> bool: ...

    def getClass(self) -> java.lang.Class: ...

    def hashCode(self) -> int: ...

    def isWildCard(self) -> bool: ...

    def notify(self) -> None: ...

    def notifyAll(self) -> None: ...

    def processQuery(self) -> bool: ...

    def toString(self) -> unicode: ...

    @overload
    def wait(self) -> None: ...

    @overload
    def wait(self, __a0: long) -> None: ...

    @overload
    def wait(self, __a0: long, __a1: int) -> None: ...

    @property
    def wildCard(self) -> bool: ...
