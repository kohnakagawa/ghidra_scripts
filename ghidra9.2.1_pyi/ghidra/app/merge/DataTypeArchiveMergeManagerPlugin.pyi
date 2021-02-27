from typing import List
import ghidra.app.merge
import ghidra.framework.model
import ghidra.framework.options
import ghidra.framework.plugintool
import ghidra.framework.plugintool.util
import ghidra.program.model.address
import ghidra.program.model.listing
import java.lang


class DataTypeArchiveMergeManagerPlugin(ghidra.app.merge.MergeManagerPlugin):
    """
    Plugin that provides a merge component provider for data type archives.
    """





    def __init__(self, tool: ghidra.framework.plugintool.PluginTool, mergeManager: ghidra.app.merge.DataTypeArchiveMergeManager, dataTypeArchive: ghidra.program.model.listing.DataTypeArchive):
        """
        Constructor for plugin that handles multi-user merge of data type archives.
        @param tool the tool
        @param mergeManager the merge manager that will control the merge process
        @param dataTypeArchive the data type archive
        """
        ...



    def acceptData(self, data: List[ghidra.framework.model.DomainFile]) -> bool:
        """
        Method called if the plugin supports this domain file.
         <p>
        @param data array of {@link DomainFile}s
        @return boolean true if can accept
        """
        ...

    def closeAllDomainObjects(self, ignoreChanges: bool) -> bool: ...

    def closeAllPrograms(self, ignoreChanges: bool) -> bool: ...

    @overload
    def closeDomainObject(self) -> bool: ...

    @overload
    def closeDomainObject(self, domainObject: ghidra.framework.model.UndoableDomainObject, ignoreChanges: bool) -> bool: ...

    @overload
    def closeProgram(self) -> bool: ...

    @overload
    def closeProgram(self, program: ghidra.program.model.listing.Program, ignoreChanges: bool) -> bool: ...

    def createProvider(self) -> ghidra.app.merge.MergeManagerProvider: ...

    def dataStateRestoreCompleted(self) -> None:
        """
        Notification that all plugins have had their data states restored.
        """
        ...

    def dependsUpon(self, plugin: ghidra.framework.plugintool.Plugin) -> bool:
        """
        Check if this plugin depends on the given plugin
        @param plugin the plugin
        @return true if this plugin depends on the given plugin
        """
        ...

    def domainObjectChanged(self, ev: ghidra.framework.model.DomainObjectChangedEvent) -> None: ...

    def equals(self, obj: object) -> bool: ...

    def eventSent(self, event: ghidra.framework.plugintool.PluginEvent) -> None: ...

    def firePluginEvent(self, event: ghidra.framework.plugintool.PluginEvent) -> None:
        """
        Fire the given plugin event; the tool notifies all other plugins
         who are interested in receiving the given event type.
        @param event event to fire
        """
        ...

    def getAllOpenDataTypeArchives(self) -> List[ghidra.program.model.listing.DataTypeArchive]: ...

    def getAllOpenDomainObjects(self) -> List[ghidra.framework.model.UndoableDomainObject]: ...

    @staticmethod
    def getCategory() -> unicode: ...

    def getClass(self) -> java.lang.Class: ...

    def getCurrentDataTypeArchive(self) -> ghidra.program.model.listing.DataTypeArchive: ...

    def getCurrentDomainObject(self) -> ghidra.framework.model.UndoableDomainObject: ...

    def getData(self) -> List[ghidra.framework.model.DomainFile]:
        """
        Get the domain files that this plugin has open.
         <p>
        @return array of {@link DomainFile}s that are open by this Plugin.
        """
        ...

    @staticmethod
    def getDescription() -> unicode: ...

    @staticmethod
    def getDescriptiveName() -> unicode: ...

    def getMissingRequiredServices(self) -> List[java.lang.Class]: ...

    def getName(self) -> unicode:
        """
        Returns this plugin's name.
         <p>
        @return String name, derived from simple class name.
        """
        ...

    def getPluginDescription(self) -> ghidra.framework.plugintool.util.PluginDescription:
        """
        Returns the static {@link PluginDescription} object that was derived from the
         {@link PluginInfo @PluginInfo} annotation at the top of your Plugin.
         <p>
        @return the static/shared {@link PluginDescription} instance that describes this Plugin.
        """
        ...

    @staticmethod
    def getPluginName(pluginClass: java.lang.Class) -> unicode:
        """
        Returns plugin name or null if given class does not extend {@link Plugin}
         <p>
         Deprecated, use {@link PluginUtils#getPluginNameFromClass(Class)}
         <p>
        @param pluginClass the plugin class
        @return the plugin name
        """
        ...

    def getProgram(self, addr: ghidra.program.model.address.Address) -> ghidra.program.model.listing.Program: ...

    @overload
    def getSearchPriority(self, p: ghidra.program.model.listing.Program) -> int: ...

    @overload
    def getSearchPriority(self, domainObject: ghidra.framework.model.UndoableDomainObject) -> int: ...

    def getSupportedDataTypes(self) -> java.lang.Class:
        """
        Return classes of data types that this plugin can support.
         <p>
        @return classes of data types that this plugin can support
        """
        ...

    def getTool(self) -> ghidra.framework.plugintool.PluginTool:
        """
        Get the {@link PluginTool} that hosts/contains this plugin.
        @return PluginTool
        """
        ...

    def getTransientState(self) -> object:
        """
        Returns an object containing the plugins state.  Plugins should override this method if
         they have state that they want to maintain between domain object state transitions (i.e. when the
         user tabs to a different domain object and back) Whatever object is returned will be fed back to
         the plugin after the tool state is switch back to the domain object that was active when the this
         method was called.
        @return Object to be return in the restoreTransientState() method.
        """
        ...

    def getUndoRedoState(self, domainObject: ghidra.framework.model.DomainObject) -> object:
        """
        Returns an object containing the plugin's state as needed to restore itself after an undo
         or redo operation.  Plugins should override this method if they have special undo/redo handling.
        @param domainObject the object that is about to or has had undoable changes made to it.
        @return the state object
        """
        ...

    def hasMissingRequiredService(self) -> bool:
        """
        Checks if this plugin is missing a required service.
        @return boolean true if a required service isn't available via the PluginTool.
        """
        ...

    def hashCode(self) -> int: ...

    def isDisposed(self) -> bool: ...

    @overload
    def isVisible(self, program: ghidra.program.model.listing.Program) -> bool: ...

    @overload
    def isVisible(self, domainObject: ghidra.framework.model.UndoableDomainObject) -> bool: ...

    def notify(self) -> None: ...

    def notifyAll(self) -> None: ...

    @overload
    def openDomainObject(self, domainFile: ghidra.framework.model.DomainFile) -> ghidra.program.model.listing.Program: ...

    @overload
    def openDomainObject(self, domainObject: ghidra.framework.model.UndoableDomainObject) -> None: ...

    @overload
    def openDomainObject(self, df: ghidra.framework.model.DomainFile, version: int) -> ghidra.program.model.listing.Program: ...

    @overload
    def openDomainObject(self, domainObject: ghidra.framework.model.UndoableDomainObject, state: int) -> None: ...

    @overload
    def openDomainObject(self, domainObject: ghidra.framework.model.UndoableDomainObject, current: bool) -> None: ...

    @overload
    def openDomainObject(self, domainFile: ghidra.framework.model.DomainFile, version: int, state: int) -> ghidra.program.model.listing.Program: ...

    @overload
    def openProgram(self, domainFile: ghidra.framework.model.DomainFile) -> ghidra.program.model.listing.Program: ...

    @overload
    def openProgram(self, program: ghidra.program.model.listing.Program) -> None: ...

    @overload
    def openProgram(self, df: ghidra.framework.model.DomainFile, version: int) -> ghidra.program.model.listing.Program: ...

    @overload
    def openProgram(self, program: ghidra.program.model.listing.Program, state: int) -> None: ...

    @overload
    def openProgram(self, program: ghidra.program.model.listing.Program, current: bool) -> None: ...

    @overload
    def openProgram(self, domainFile: ghidra.framework.model.DomainFile, version: int, state: int) -> ghidra.program.model.listing.Program: ...

    def processEvent(self, event: ghidra.framework.plugintool.PluginEvent) -> None: ...

    def readConfigState(self, saveState: ghidra.framework.options.SaveState) -> None:
        """
        Tells the Plugin to read its data-independent (preferences)
         properties from the input stream.
        @param saveState object that holds primitives for state information
        """
        ...

    def readDataState(self, saveState: ghidra.framework.options.SaveState) -> None:
        """
        Tells the Plugin to read its data-dependent state from the
         given SaveState object.
        @param saveState object that holds primitives for state information
        """
        ...

    def releaseDomainObject(self, domainObject: ghidra.framework.model.UndoableDomainObject, persistentOwner: object) -> None: ...

    def releaseProgram(self, program: ghidra.program.model.listing.Program, persistentOwner: object) -> None: ...

    def restoreTransientState(self, state: object) -> None:
        """
        Provides the transient state object that was returned in the corresponding getTransientState()
         call.  Plugins should override this method if they have state that needs to be saved as domain objects
         get switched between active and inactive.
        @param state the state object that was generated by this plugin's getTransientState() method.
        """
        ...

    def restoreUndoRedoState(self, domainObject: ghidra.framework.model.DomainObject, state: object) -> None:
        """
        Updates the plugin's state based on the data stored in the state object.  The state object
         is the object that was returned by this plugin in the {@link #getUndoRedoState(DomainObject)}
        @param domainObject the domain object that has had an undo or redo operation applied to it.
        @param state the state that was recorded before the undo or redo operation.
        """
        ...

    def serviceAdded(self, interfaceClass: java.lang.Class, service: object) -> None:
        """
        Notifies this plugin that a service has been added to
           the plugin tool.
         Plugins should override this method if they update their state
         when a particular service is added.
        @param interfaceClass The <b>interface</b> of the added service
        @param service service that is being added
        """
        ...

    def serviceRemoved(self, interfaceClass: java.lang.Class, service: object) -> None:
        """
        Notifies this plugin that service has been removed from the
           plugin tool.
         Plugins should override this method if they update their state
         when a particular service is removed.
        @param interfaceClass The <b>interface</b> of the added service
        @param service that is being removed.
        """
        ...

    def setCurrentDomainObject(self, domainObject: ghidra.framework.model.UndoableDomainObject) -> None: ...

    def setCurrentProgram(self, p: ghidra.program.model.listing.Program) -> None: ...

    @overload
    def setPersistentOwner(self, program: ghidra.program.model.listing.Program, owner: object) -> bool: ...

    @overload
    def setPersistentOwner(self, domainObject: ghidra.framework.model.UndoableDomainObject, owner: object) -> bool: ...

    @overload
    def setSearchPriority(self, p: ghidra.program.model.listing.Program, priority: int) -> None: ...

    @overload
    def setSearchPriority(self, domainObject: ghidra.framework.model.UndoableDomainObject, priority: int) -> None: ...

    def toString(self) -> unicode: ...

    @overload
    def wait(self) -> None: ...

    @overload
    def wait(self, __a0: long) -> None: ...

    @overload
    def wait(self, __a0: long, __a1: int) -> None: ...

    def writeConfigState(self, saveState: ghidra.framework.options.SaveState) -> None:
        """
        Tells a Plugin to write any data-independent (preferences)
         properties to the output stream.
        @param saveState object that holds primitives for state information
        """
        ...

    def writeDataState(self, saveState: ghidra.framework.options.SaveState) -> None:
        """
        Tells the Plugin to write any data-dependent state to the
         output stream.
        @param saveState object that holds primitives for state information
        """
        ...

    @property
    def allOpenDataTypeArchives(self) -> List[ghidra.program.model.listing.DataTypeArchive]: ...

    @property
    def currentDataTypeArchive(self) -> ghidra.program.model.listing.DataTypeArchive: ...

    @property
    def currentProgram(self) -> None: ...  # No getter available.

    @currentProgram.setter
    def currentProgram(self, value: ghidra.program.model.listing.Program) -> None: ...
