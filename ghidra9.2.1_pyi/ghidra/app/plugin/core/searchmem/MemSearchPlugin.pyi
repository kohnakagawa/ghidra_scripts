from typing import List
import docking
import ghidra.app.context
import ghidra.app.nav
import ghidra.app.services
import ghidra.framework.model
import ghidra.framework.options
import ghidra.framework.plugintool
import ghidra.framework.plugintool.util
import java.lang


class MemSearchPlugin(ghidra.framework.plugintool.Plugin, ghidra.framework.options.OptionsChangeListener, docking.DockingContextListener, ghidra.app.nav.NavigatableRemovalListener, ghidra.app.services.MemorySearchService):




    def __init__(self, __a0: ghidra.framework.plugintool.PluginTool): ...



    def acceptData(self, __a0: List[ghidra.framework.model.DomainFile]) -> bool: ...

    def contextChanged(self, __a0: docking.ActionContext) -> None: ...

    def dataStateRestoreCompleted(self) -> None: ...

    def dependsUpon(self, __a0: ghidra.framework.plugintool.Plugin) -> bool: ...

    def dispose(self) -> None: ...

    def equals(self, __a0: object) -> bool: ...

    def eventSent(self, __a0: ghidra.framework.plugintool.PluginEvent) -> None: ...

    def firePluginEvent(self, __a0: ghidra.framework.plugintool.PluginEvent) -> None: ...

    def getClass(self) -> java.lang.Class: ...

    def getData(self) -> List[ghidra.framework.model.DomainFile]: ...

    def getMissingRequiredServices(self) -> List[object]: ...

    def getName(self) -> unicode: ...

    def getPluginDescription(self) -> ghidra.framework.plugintool.util.PluginDescription: ...

    @staticmethod
    def getPluginName(__a0: java.lang.Class) -> unicode: ...

    def getSupportedDataTypes(self) -> List[java.lang.Class]: ...

    def getTool(self) -> ghidra.framework.plugintool.PluginTool: ...

    def getTransientState(self) -> object: ...

    def getUndoRedoState(self, __a0: ghidra.framework.model.DomainObject) -> object: ...

    def hasMissingRequiredService(self) -> bool: ...

    def hashCode(self) -> int: ...

    def isDisposed(self) -> bool: ...

    def navigatableRemoved(self, __a0: ghidra.app.nav.Navigatable) -> None: ...

    def notify(self) -> None: ...

    def notifyAll(self) -> None: ...

    def optionsChanged(self, __a0: ghidra.framework.options.ToolOptions, __a1: unicode, __a2: object, __a3: object) -> None: ...

    def processEvent(self, __a0: ghidra.framework.plugintool.PluginEvent) -> None: ...

    def readConfigState(self, __a0: ghidra.framework.options.SaveState) -> None: ...

    def readDataState(self, __a0: ghidra.framework.options.SaveState) -> None: ...

    def restoreTransientState(self, __a0: object) -> None: ...

    def restoreUndoRedoState(self, __a0: ghidra.framework.model.DomainObject, __a1: object) -> None: ...

    def search(self, __a0: List[int], __a1: ghidra.app.context.NavigatableActionContext) -> None: ...

    def serviceAdded(self, __a0: java.lang.Class, __a1: object) -> None: ...

    def serviceRemoved(self, __a0: java.lang.Class, __a1: object) -> None: ...

    def setIsMnemonic(self, __a0: bool) -> None: ...

    def setSearchText(self, __a0: unicode) -> None: ...

    def toString(self) -> unicode: ...

    @overload
    def wait(self) -> None: ...

    @overload
    def wait(self, __a0: long) -> None: ...

    @overload
    def wait(self, __a0: long, __a1: int) -> None: ...

    def writeConfigState(self, __a0: ghidra.framework.options.SaveState) -> None: ...

    def writeDataState(self, __a0: ghidra.framework.options.SaveState) -> None: ...

    @property
    def isMnemonic(self) -> None: ...  # No getter available.

    @isMnemonic.setter
    def isMnemonic(self, value: bool) -> None: ...

    @property
    def searchText(self) -> None: ...  # No getter available.

    @searchText.setter
    def searchText(self, value: unicode) -> None: ...