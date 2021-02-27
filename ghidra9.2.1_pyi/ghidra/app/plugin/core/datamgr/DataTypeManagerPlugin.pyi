from typing import List
import docking
import docking.actions
import generic.jar
import ghidra.app.plugin
import ghidra.app.plugin.core.datamgr
import ghidra.app.plugin.core.datamgr.archive
import ghidra.app.plugin.core.datamgr.editor
import ghidra.app.services
import ghidra.framework.model
import ghidra.framework.options
import ghidra.framework.plugintool
import ghidra.framework.plugintool.util
import ghidra.program.model.address
import ghidra.program.model.data
import ghidra.program.model.listing
import ghidra.program.util
import ghidra.util
import java.awt
import java.awt.datatransfer
import java.io
import java.lang
import java.util
import javax.swing.tree


class DataTypeManagerPlugin(ghidra.app.plugin.ProgramPlugin, ghidra.framework.model.DomainObjectListener, ghidra.app.services.DataTypeManagerService, docking.actions.PopupActionProvider):




    def __init__(self, __a0: ghidra.framework.plugintool.PluginTool): ...



    def acceptData(self, __a0: List[ghidra.framework.model.DomainFile]) -> bool: ...

    def addDataTypeManagerChangeListener(self, __a0: ghidra.program.model.data.DataTypeManagerChangeListener) -> None: ...

    def addRecentlyOpenedArchiveFile(self, __a0: generic.jar.ResourceFile) -> None: ...

    @overload
    def addRecentlyOpenedProjectArchive(self, __a0: ghidra.app.plugin.core.datamgr.archive.ProjectArchive) -> None: ...

    @overload
    def addRecentlyOpenedProjectArchive(self, __a0: unicode, __a1: unicode) -> None: ...

    def closeArchive(self, __a0: ghidra.program.model.data.DataTypeManager) -> None: ...

    def closeProvider(self, __a0: ghidra.app.plugin.core.datamgr.DataTypesProvider) -> None: ...

    def commit(self, __a0: ghidra.program.model.data.DataType) -> bool: ...

    def createProvider(self) -> ghidra.app.plugin.core.datamgr.DataTypesProvider: ...

    def dataStateRestoreCompleted(self) -> None: ...

    def dependsUpon(self, __a0: ghidra.framework.plugintool.Plugin) -> bool: ...

    def disassociate(self, __a0: ghidra.program.model.data.DataType) -> None: ...

    def dispose(self) -> None: ...

    def domainObjectChanged(self, __a0: ghidra.framework.model.DomainObjectChangedEvent) -> None: ...

    def edit(self, __a0: ghidra.program.model.data.DataType) -> None: ...

    def equals(self, __a0: object) -> bool: ...

    def eventSent(self, __a0: ghidra.framework.plugintool.PluginEvent) -> None: ...

    def firePluginEvent(self, __a0: ghidra.framework.plugintool.PluginEvent) -> None: ...

    def getBuiltInDataTypesManager(self) -> ghidra.program.model.data.DataTypeManager: ...

    def getClass(self) -> java.lang.Class: ...

    def getClipboard(self) -> java.awt.datatransfer.Clipboard: ...

    def getConflictHandler(self) -> ghidra.program.model.data.DataTypeConflictHandler: ...

    def getCurrentProgram(self) -> ghidra.program.model.listing.Program: ...

    def getCurrentSelection(self) -> ghidra.program.model.address.AddressSetView: ...

    def getData(self) -> List[ghidra.framework.model.DomainFile]: ...

    @overload
    def getDataType(self, __a0: unicode) -> ghidra.program.model.data.DataType: ...

    @overload
    def getDataType(self, __a0: javax.swing.tree.TreePath) -> ghidra.program.model.data.DataType: ...

    def getDataTypeManagerHandler(self) -> ghidra.app.plugin.core.datamgr.archive.DataTypeManagerHandler: ...

    def getDataTypeManagers(self) -> List[ghidra.program.model.data.DataTypeManager]: ...

    def getEditorHelpLocation(self, __a0: ghidra.program.model.data.DataType) -> ghidra.util.HelpLocation: ...

    def getEditorManager(self) -> ghidra.app.plugin.core.datamgr.editor.DataTypeEditorManager: ...

    def getFavorites(self) -> List[object]: ...

    def getMissingRequiredServices(self) -> List[object]: ...

    def getName(self) -> unicode: ...

    def getPluginDescription(self) -> ghidra.framework.plugintool.util.PluginDescription: ...

    @staticmethod
    def getPluginName(__a0: java.lang.Class) -> unicode: ...

    def getPopupActions(self, __a0: docking.Tool, __a1: docking.ActionContext) -> List[object]: ...

    def getPossibleEquateNames(self, __a0: long) -> java.util.Set: ...

    def getProgram(self) -> ghidra.program.model.listing.Program: ...

    def getProgramDataTypeManager(self) -> ghidra.program.model.data.DataTypeManager: ...

    def getProgramHighlight(self) -> ghidra.program.util.ProgramSelection: ...

    def getProgramLocation(self) -> ghidra.program.util.ProgramLocation: ...

    def getProgramSelection(self) -> ghidra.program.util.ProgramSelection: ...

    def getProjectArchiveFile(self, __a0: unicode, __a1: unicode) -> ghidra.framework.model.DomainFile: ...

    def getProvider(self) -> ghidra.app.plugin.core.datamgr.DataTypesProvider: ...

    def getRecentlyOpenedArchives(self) -> java.util.Collection: ...

    def getRecentlyUsed(self) -> ghidra.program.model.data.DataType: ...

    def getSortedDataTypeList(self) -> List[object]: ...

    def getSupportedDataTypes(self) -> List[java.lang.Class]: ...

    def getTool(self) -> ghidra.framework.plugintool.PluginTool: ...

    def getTransientState(self) -> object: ...

    def getUndoRedoState(self, __a0: ghidra.framework.model.DomainObject) -> object: ...

    def hasMissingRequiredService(self) -> bool: ...

    def hashCode(self) -> int: ...

    def includeDataMembersInSearch(self) -> bool: ...

    def isDisposed(self) -> bool: ...

    def isEditable(self, __a0: ghidra.program.model.data.DataType) -> bool: ...

    @staticmethod
    def isValidTypeDefBaseType(__a0: java.awt.Component, __a1: ghidra.program.model.data.DataType) -> bool: ...

    def notify(self) -> None: ...

    def notifyAll(self) -> None: ...

    @overload
    def openArchive(self, __a0: ghidra.framework.model.DomainFile) -> ghidra.program.model.listing.DataTypeArchive: ...

    @overload
    def openArchive(self, __a0: ghidra.program.model.listing.DataTypeArchive) -> ghidra.app.plugin.core.datamgr.archive.Archive: ...

    @overload
    def openArchive(self, __a0: ghidra.framework.model.DomainFile, __a1: int) -> ghidra.program.model.listing.DataTypeArchive: ...

    @overload
    def openArchive(self, __a0: java.io.File, __a1: bool) -> ghidra.app.plugin.core.datamgr.archive.Archive: ...

    def openDataTypeArchive(self, __a0: unicode) -> ghidra.program.model.data.DataTypeManager: ...

    def openProjectDataTypeArchive(self) -> None: ...

    def processEvent(self, __a0: ghidra.framework.plugintool.PluginEvent) -> None: ...

    def readConfigState(self, __a0: ghidra.framework.options.SaveState) -> None: ...

    def readDataState(self, __a0: ghidra.framework.options.SaveState) -> None: ...

    def removeDataTypeManagerChangeListener(self, __a0: ghidra.program.model.data.DataTypeManagerChangeListener) -> None: ...

    def restoreTransientState(self, __a0: object) -> None: ...

    def restoreUndoRedoState(self, __a0: ghidra.framework.model.DomainObject, __a1: object) -> None: ...

    def revert(self, __a0: ghidra.program.model.data.DataType) -> bool: ...

    def serviceAdded(self, __a0: java.lang.Class, __a1: object) -> None: ...

    def serviceRemoved(self, __a0: java.lang.Class, __a1: object) -> None: ...

    def setDataTypeSelected(self, __a0: ghidra.program.model.data.DataType) -> None: ...

    def setRecentlyUsed(self, __a0: ghidra.program.model.data.DataType) -> None: ...

    def toString(self) -> unicode: ...

    def update(self, __a0: ghidra.program.model.data.DataType) -> bool: ...

    @overload
    def wait(self) -> None: ...

    @overload
    def wait(self, __a0: long) -> None: ...

    @overload
    def wait(self, __a0: long, __a1: int) -> None: ...

    def writeConfigState(self, __a0: ghidra.framework.options.SaveState) -> None: ...

    def writeDataState(self, __a0: ghidra.framework.options.SaveState) -> None: ...

    @property
    def builtInDataTypesManager(self) -> ghidra.program.model.data.DataTypeManager: ...

    @property
    def clipboard(self) -> java.awt.datatransfer.Clipboard: ...

    @property
    def conflictHandler(self) -> ghidra.program.model.data.DataTypeConflictHandler: ...

    @property
    def currentSelection(self) -> ghidra.program.model.address.AddressSetView: ...

    @property
    def data(self) -> List[ghidra.framework.model.DomainFile]: ...

    @property
    def dataTypeManagerHandler(self) -> ghidra.app.plugin.core.datamgr.archive.DataTypeManagerHandler: ...

    @property
    def dataTypeManagers(self) -> List[ghidra.program.model.data.DataTypeManager]: ...

    @property
    def dataTypeSelected(self) -> None: ...  # No getter available.

    @dataTypeSelected.setter
    def dataTypeSelected(self, value: ghidra.program.model.data.DataType) -> None: ...

    @property
    def editorManager(self) -> ghidra.app.plugin.core.datamgr.editor.DataTypeEditorManager: ...

    @property
    def favorites(self) -> List[object]: ...

    @property
    def program(self) -> ghidra.program.model.listing.Program: ...

    @property
    def programDataTypeManager(self) -> ghidra.program.model.data.DataTypeManager: ...

    @property
    def provider(self) -> ghidra.app.plugin.core.datamgr.DataTypesProvider: ...

    @property
    def recentlyOpenedArchives(self) -> java.util.Collection: ...

    @property
    def recentlyUsed(self) -> ghidra.program.model.data.DataType: ...

    @recentlyUsed.setter
    def recentlyUsed(self, value: ghidra.program.model.data.DataType) -> None: ...

    @property
    def sortedDataTypeList(self) -> List[object]: ...

    @property
    def supportedDataTypes(self) -> List[java.lang.Class]: ...
