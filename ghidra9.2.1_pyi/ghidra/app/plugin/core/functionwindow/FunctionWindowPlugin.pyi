from typing import List
import docking
import ghidra.app.plugin
import ghidra.framework.model
import ghidra.framework.options
import ghidra.framework.plugintool
import ghidra.framework.plugintool.util
import ghidra.program.model.listing
import ghidra.program.util
import java.lang


class FunctionWindowPlugin(ghidra.app.plugin.ProgramPlugin, ghidra.framework.model.DomainObjectListener, docking.ComponentProviderActivationListener):




    def __init__(self, __a0: ghidra.framework.plugintool.PluginTool): ...



    def acceptData(self, __a0: List[ghidra.framework.model.DomainFile]) -> bool: ...

    def componentProviderActivated(self, __a0: docking.ComponentProvider) -> None: ...

    def componentProviderDeactivated(self, __a0: docking.ComponentProvider) -> None: ...

    def dataStateRestoreCompleted(self) -> None: ...

    def dependsUpon(self, __a0: ghidra.framework.plugintool.Plugin) -> bool: ...

    def dispose(self) -> None: ...

    def domainObjectChanged(self, __a0: ghidra.framework.model.DomainObjectChangedEvent) -> None: ...

    def equals(self, __a0: object) -> bool: ...

    def eventSent(self, __a0: ghidra.framework.plugintool.PluginEvent) -> None: ...

    def firePluginEvent(self, __a0: ghidra.framework.plugintool.PluginEvent) -> None: ...

    def getClass(self) -> java.lang.Class: ...

    def getCurrentProgram(self) -> ghidra.program.model.listing.Program: ...

    def getData(self) -> List[ghidra.framework.model.DomainFile]: ...

    def getMissingRequiredServices(self) -> List[object]: ...

    def getName(self) -> unicode: ...

    def getPluginDescription(self) -> ghidra.framework.plugintool.util.PluginDescription: ...

    @staticmethod
    def getPluginName(__a0: java.lang.Class) -> unicode: ...

    def getProgramHighlight(self) -> ghidra.program.util.ProgramSelection: ...

    def getProgramLocation(self) -> ghidra.program.util.ProgramLocation: ...

    def getProgramSelection(self) -> ghidra.program.util.ProgramSelection: ...

    def getSupportedDataTypes(self) -> List[java.lang.Class]: ...

    def getTool(self) -> ghidra.framework.plugintool.PluginTool: ...

    def getTransientState(self) -> object: ...

    def getUndoRedoState(self, __a0: ghidra.framework.model.DomainObject) -> object: ...

    def hasMissingRequiredService(self) -> bool: ...

    def hashCode(self) -> int: ...

    def init(self) -> None: ...

    def isDisposed(self) -> bool: ...

    def notify(self) -> None: ...

    def notifyAll(self) -> None: ...

    def processEvent(self, __a0: ghidra.framework.plugintool.PluginEvent) -> None: ...

    def readConfigState(self, __a0: ghidra.framework.options.SaveState) -> None: ...

    def readDataState(self, __a0: ghidra.framework.options.SaveState) -> None: ...

    def restoreTransientState(self, __a0: object) -> None: ...

    def restoreUndoRedoState(self, __a0: ghidra.framework.model.DomainObject, __a1: object) -> None: ...

    def serviceAdded(self, __a0: java.lang.Class, __a1: object) -> None: ...

    def serviceRemoved(self, __a0: java.lang.Class, __a1: object) -> None: ...

    def toString(self) -> unicode: ...

    @overload
    def wait(self) -> None: ...

    @overload
    def wait(self, __a0: long) -> None: ...

    @overload
    def wait(self, __a0: long, __a1: int) -> None: ...

    def writeConfigState(self, __a0: ghidra.framework.options.SaveState) -> None: ...

    def writeDataState(self, __a0: ghidra.framework.options.SaveState) -> None: ...
