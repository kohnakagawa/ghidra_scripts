from typing import List
import ghidra.app.util
import ghidra.app.util.viewer.field
import ghidra.framework.model
import ghidra.framework.options
import ghidra.framework.plugintool
import ghidra.framework.plugintool.util
import ghidra.program.model.address
import ghidra.program.model.listing
import ghidra.program.model.symbol
import java.lang


class ReferencesPlugin(ghidra.framework.plugintool.Plugin):




    def __init__(self, __a0: ghidra.framework.plugintool.PluginTool): ...



    def acceptData(self, __a0: List[ghidra.framework.model.DomainFile]) -> bool: ...

    @overload
    def addReference(self, __a0: ghidra.program.model.listing.CodeUnit, __a1: int, __a2: int, __a3: ghidra.program.model.symbol.RefType) -> bool: ...

    @overload
    def addReference(self, __a0: ghidra.program.model.listing.CodeUnit, __a1: int, __a2: unicode, __a3: unicode, __a4: ghidra.program.model.address.Address, __a5: unicode) -> bool: ...

    def dataStateRestoreCompleted(self) -> None: ...

    def dependsUpon(self, __a0: ghidra.framework.plugintool.Plugin) -> bool: ...

    def dispose(self) -> None: ...

    def equals(self, __a0: object) -> bool: ...

    def eventSent(self, __a0: ghidra.framework.plugintool.PluginEvent) -> None: ...

    def firePluginEvent(self, __a0: ghidra.framework.plugintool.PluginEvent) -> None: ...

    def getClass(self) -> java.lang.Class: ...

    def getCodeUnitFormat(self) -> ghidra.app.util.viewer.field.BrowserCodeUnitFormat: ...

    def getData(self) -> List[ghidra.framework.model.DomainFile]: ...

    def getMissingRequiredServices(self) -> List[object]: ...

    def getName(self) -> unicode: ...

    def getPluginDescription(self) -> ghidra.framework.plugintool.util.PluginDescription: ...

    @staticmethod
    def getPluginName(__a0: java.lang.Class) -> unicode: ...

    def getSupportedDataTypes(self) -> List[java.lang.Class]: ...

    def getSymbolInspector(self) -> ghidra.app.util.SymbolInspector: ...

    def getTool(self) -> ghidra.framework.plugintool.PluginTool: ...

    def getTransientState(self) -> object: ...

    def getUndoRedoState(self, __a0: ghidra.framework.model.DomainObject) -> object: ...

    def hasMissingRequiredService(self) -> bool: ...

    def hashCode(self) -> int: ...

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
    def updateReference(self, __a0: ghidra.program.model.symbol.StackReference, __a1: ghidra.program.model.listing.CodeUnit, __a2: int, __a3: ghidra.program.model.symbol.RefType) -> bool: ...

    @overload
    def updateReference(self, __a0: ghidra.program.model.symbol.ExternalReference, __a1: ghidra.program.model.listing.CodeUnit, __a2: unicode, __a3: unicode, __a4: ghidra.program.model.address.Address, __a5: unicode) -> bool: ...

    @overload
    def wait(self) -> None: ...

    @overload
    def wait(self, __a0: long) -> None: ...

    @overload
    def wait(self, __a0: long, __a1: int) -> None: ...

    def writeConfigState(self, __a0: ghidra.framework.options.SaveState) -> None: ...

    def writeDataState(self, __a0: ghidra.framework.options.SaveState) -> None: ...

    @property
    def codeUnitFormat(self) -> ghidra.app.util.viewer.field.BrowserCodeUnitFormat: ...

    @property
    def symbolInspector(self) -> ghidra.app.util.SymbolInspector: ...
