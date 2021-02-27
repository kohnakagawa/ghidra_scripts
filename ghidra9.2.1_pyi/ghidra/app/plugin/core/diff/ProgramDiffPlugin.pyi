from typing import List
import docking.widgets
import ghidra.app.plugin
import ghidra.app.plugin.core.diff
import ghidra.app.services
import ghidra.app.util.viewer.listingpanel
import ghidra.framework.model
import ghidra.framework.options
import ghidra.framework.plugintool
import ghidra.framework.plugintool.util
import ghidra.program.model.address
import ghidra.program.model.listing
import ghidra.program.util
import java.lang


class ProgramDiffPlugin(ghidra.app.plugin.ProgramPlugin, ghidra.app.util.viewer.listingpanel.ProgramLocationListener, ghidra.app.util.viewer.listingpanel.ProgramSelectionListener, ghidra.app.plugin.core.diff.DiffControllerListener, ghidra.app.services.DiffService, ghidra.framework.options.OptionsChangeListener, ghidra.framework.model.DomainObjectListener):




    def __init__(self, __a0: ghidra.framework.plugintool.PluginTool): ...



    def acceptData(self, __a0: List[ghidra.framework.model.DomainFile]) -> bool: ...

    def dataStateRestoreCompleted(self) -> None: ...

    def dependsUpon(self, __a0: ghidra.framework.plugintool.Plugin) -> bool: ...

    def diffLocationChanged(self, __a0: ghidra.app.plugin.core.diff.DiffController, __a1: ghidra.program.model.address.Address) -> None: ...

    def differencesChanged(self, __a0: ghidra.app.plugin.core.diff.DiffController) -> None: ...

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

    def inProgress(self) -> bool: ...

    def isDisposed(self) -> bool: ...

    @overload
    def launchDiff(self, __a0: ghidra.framework.model.DomainFile) -> bool: ...

    @overload
    def launchDiff(self, __a0: ghidra.program.model.listing.Program) -> bool: ...

    def notify(self) -> None: ...

    def notifyAll(self) -> None: ...

    def optionsChanged(self, __a0: ghidra.framework.options.ToolOptions, __a1: unicode, __a2: object, __a3: object) -> None: ...

    def processEvent(self, __a0: ghidra.framework.plugintool.PluginEvent) -> None: ...

    def programLocationChanged(self, __a0: ghidra.program.util.ProgramLocation, __a1: docking.widgets.EventTrigger) -> None: ...

    def programSelectionChanged(self, __a0: ghidra.program.util.ProgramSelection) -> None: ...

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