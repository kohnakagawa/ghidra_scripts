from typing import List
import ghidra.framework.model
import ghidra.framework.options
import ghidra.framework.plugintool
import ghidra.framework.plugintool.util
import ghidra.util.classfinder
import java.lang


class Plugin(object, ghidra.util.classfinder.ExtensionPoint, ghidra.framework.plugintool.util.PluginEventListener, ghidra.framework.plugintool.util.ServiceListener):
    """
    Plugins are a basic building block in Ghidra, used to bundle features or capabilities
     into a unit that can be enabled or disabled by the user in their Tool.

     Plugins expose their features or capabilities to users via menu items and buttons that
     the user can click on, and via "service" APIs that other Plugins can programmatically subscribe
     to, and via PluginEvents that are broadcast.

     Well formed Plugins:

     	Derive from Plugin (directly or indirectly).
     	Class name ends with "Plugin" and does not match any other Plugin, regardless of
     	its location in the package tree.
     	Have a PluginInfo annotation.
     	Have a constructor with exactly 1 parameter: PluginTool.

      			public MyPlugin(PluginTool tool) { ... }

      	Usually overrides protected void init().

     Class naming
     All Plugin Classes MUST END IN "Plugin".  If not, the ClassSearcher will not find them.

     Some special Plugins marked with the ProgramaticUseOnly interface are manually
     created and do not follow this naming requirement.

     Plugin Life cycle

     	Your Plugin's constructor is called

     			Plugin base class constructor is called.

     					Services listed in the @PluginInfo annotation are automatically added
     					to dependency list

     			Your Plugin publishes any services listed in PluginInfo using
     			Plugin#registerServiceProvided(Class, Object).
     			(required)
      			Create Actions (optional)
      			Register ghidra.framework.options.Options with the
     PluginTool#getOptions(String). (optional)

     	Other Plugins are constructed, dependencies evaluated, etc.
     	If your dependencies are not available (ie. not installed, threw an exception during their
    	initialization, etc), your Plugin's #dispose() will be called and then your Plugin
    	instance will be discarded.
    	Your Plugin's #init() method is called (when its dependencies are met).

     			Call PluginTool#getService(Class) to get service
     			implementations. (the service class being requested should already be
     			listed in the @PluginInfo)
     			Create Actions (optional)
     			Other initialization stuff.

    	Your Plugin's #readConfigState(SaveState) is called.
     	...user uses Ghidra...

     			Your Plugin's #processEvent(PluginEvent) is called for events.
     			Your Plugin's Action's methods (ie.
     			DockingAction#actionPerformed(docking.ActionContext)) are called.
     			Your Plugin's published service methods are called by other Plugins.
     			Your Plugin's listener methods are called.

     	Plugin is unloaded due to shutdown of the Tool or being disabled by user

    			Your Plugin's #writeConfigState(SaveState) is called - override this
    			method to write configuration info into the Tool definition.
     			Your Plugin's #dispose() is called - override this method to free
     			any resources and perform any needed cleanup.
     			Your Plugin's services and events are de-registered automatically.



     Plugin Service dependency
     All Plugins must be tagged with a PluginInfo annotation.

     The annotation gives you the ability to declare a dependency on another Plugin
     via the PluginInfo#servicesRequired()

     Ghidra will ensure that your Plugin will not be #init() until all
     of its required services are loaded successfully and are available for use when your Plugin
     calls the PluginTool#getService(Class) method.

     Conversely, any services your Plugin advertises in PluginInfo must be published via calls to
     #registerServiceProvided(Class, Object) in your Plugin's
     constructor.

     Cyclic dependencies are not allowed and will cause the Plugin management code to fail to
     load your Plugin. (ie. PluginA requires a service that PluginB provides, which requires a service
     that PluginA provides)

     Plugin Service implementation
     A Plugin may provide a service to other Plugins by advertising in its PluginInfo
     annotation that it PluginInfo#servicesProvided() an interface class.

     Your Plugin can either directly implement the interface in your Plugin class:

     public class MyPlugin extends Plugin implements MyService {....}

     or it may delegate the handling of the service interface to another object during its
     constructor:

     public MyPlugin(PluginTool tool) {
     ...
     MyService serviceObj = new MyService() { ... };
     registerServiceProvided(MyService.class, serviceObj);

     }

     When your Plugin directly implements the advertised service interface, you should not
     call #registerServiceProvided(Class, Object) for that service
     interface.

     Service interface classes are just normal java interface declarations and have no
     preconditions or other requirements to be used as a Plugin's advertised service interface.

     Optionally, service interface classes can be marked with meta-data via a
     ServiceInfo annotation that can have a
     ServiceInfo#defaultProvider() property which specifies a Plugin's
     class (or classname) that should be auto-loaded to provide an implementation of the service
     interface when that service is required by some other Plugin.  Without the defaultProvider
     information, dependent Plugins will fail to load unless the user manually loads a Plugin
     that provides the necessary interface service.

     Multiple Plugins can implement the same service interface.  Plugins that use that
     multi-implemented service will either receive a randomly picked instance if using
     PluginTool#getService(Class) or will receive all implementations if using
     PluginTool#getServices(Class).


     Plugin Events

     	Every type of plugin event should be represented by some class extending PluginEvent.
      One PluginEvent subclass may be used for more than one event type as long as there's some
      natural grouping.


     Component Providers

      A plugin may supply a ComponentProvider that provides a visual component when
      the plugin is added to the tool.


     Important interfaces Plugins often need to implement

     	OptionsChangeListener - to receive notification when a configuration option
     	is changed by the user.
     	FrontEndable - marks this Plugin as being suitable for inclusion in the FrontEnd
     		tool.
     	FrontEndOnly - marks this Plugin as FrontEnd only, not usable in CodeBrowser or
     		other tools.
     	ProgramaticUseOnly - marks this Plugin as special and not for user configuration.

    """









    def acceptData(self, data: List[ghidra.framework.model.DomainFile]) -> bool:
        """
        Method called if the plugin supports this domain file.
         <p>
        @param data array of {@link DomainFile}s
        @return boolean true if can accept
        """
        ...

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

    def equals(self, obj: object) -> bool: ...

    def eventSent(self, event: ghidra.framework.plugintool.PluginEvent) -> None: ...

    def firePluginEvent(self, event: ghidra.framework.plugintool.PluginEvent) -> None:
        """
        Fire the given plugin event; the tool notifies all other plugins
         who are interested in receiving the given event type.
        @param event event to fire
        """
        ...

    def getClass(self) -> java.lang.Class: ...

    def getData(self) -> List[ghidra.framework.model.DomainFile]:
        """
        Get the domain files that this plugin has open.
         <p>
        @return array of {@link DomainFile}s that are open by this Plugin.
        """
        ...

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

    def notify(self) -> None: ...

    def notifyAll(self) -> None: ...

    def processEvent(self, event: ghidra.framework.plugintool.PluginEvent) -> None:
        """
        Method called to process a plugin event.  Plugins should override this method
         if the plugin processes PluginEvents;
        @param event plugin to process
        """
        ...

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
    def data(self) -> List[ghidra.framework.model.DomainFile]: ...

    @property
    def disposed(self) -> bool: ...

    @property
    def missingRequiredServices(self) -> List[object]: ...

    @property
    def name(self) -> unicode: ...

    @property
    def pluginDescription(self) -> ghidra.framework.plugintool.util.PluginDescription: ...

    @property
    def supportedDataTypes(self) -> List[java.lang.Class]: ...

    @property
    def tool(self) -> ghidra.framework.plugintool.PluginTool: ...

    @property
    def transientState(self) -> object: ...
