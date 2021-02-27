from typing import List
import ghidra.framework.plugintool.util
import java.lang


class PluginDescription(object, java.lang.Comparable):
    """
    Class to hold meta information about a plugin, derived from meta-data attached to
     each Plugin using a PluginInfo annotation.
    """









    @overload
    def compareTo(self, other: ghidra.framework.plugintool.util.PluginDescription) -> int: ...

    @overload
    def compareTo(self, __a0: object) -> int: ...

    @overload
    @staticmethod
    def createPluginDescription(pluginClass: java.lang.Class, status: ghidra.framework.plugintool.util.PluginStatus, pluginPackage: unicode, category: unicode, shortDescription: unicode, description: unicode) -> ghidra.framework.plugintool.util.PluginDescription:
        """
        Constructs a new PluginDescription for the given plugin class.
         <p>
         Deprecated, use {@link PluginInfo @PluginInfo} instead.
        @param pluginClass the class of the plugin
        @param status the status, UNSTABLE, STABLE, RELEASED, DEBUG, or EXAMPLE
        @param pluginPackage the package to which the plugin belongs (see {@link PluginPackage}
                subclasses for examples)
        @param category the category to which the plugin belongs (see {@link PluginCategoryNames}
        @param shortDescription a brief description of what the plugin does
        @param description the long description of what the plugin does
        @return the new (or cached) PluginDescription
        """
        ...

    @overload
    @staticmethod
    def createPluginDescription(pluginClassParam: java.lang.Class, status: ghidra.framework.plugintool.util.PluginStatus, pluginPackage: unicode, category: unicode, shortDescription: unicode, description: unicode, isSlowInstallation: bool) -> ghidra.framework.plugintool.util.PluginDescription:
        """
        Constructs a new PluginDescription for the given plugin class.
         <p>
        @deprecated , use {@link PluginInfo &#64;PluginInfo} instead.
        @param pluginClassParam the class of the plugin
        @param status the status, UNSTABLE, STABLE, RELEASED, DEBUG, or EXAMPLE
        @param pluginPackage the package to which the plugin belongs (see {@link PluginPackage}
                subclasses for examples)
        @param category the category to which the plugin belongs (see {@link PluginCategoryNames}
        @param shortDescription a brief description of what the plugin does
        @param description the long description of what the plugin does
        @param isSlowInstallation true signals that this plugin loads slowly
        @return the new (or cached) PluginDescription
        """
        ...

    def equals(self, obj: object) -> bool: ...

    def getCategory(self) -> unicode:
        """
        Return the category for the plugin.
        @return the category
        """
        ...

    def getClass(self) -> java.lang.Class: ...

    def getDescription(self) -> unicode:
        """
        Return the description of the plugin.
        @return {@code "<None>"} if no description was specified
        """
        ...

    def getEventsConsumed(self) -> List[java.lang.Class]: ...

    def getEventsProduced(self) -> List[java.lang.Class]: ...

    def getModuleName(self) -> unicode:
        """
        Return the type for the plugin: CORE, CONTRIB, PROTOTYPE, or
         DEVELOP. Within a type, plugins are grouped by category.
        @return the type (or null if there is no module)
        """
        ...

    def getName(self) -> unicode:
        """
        Return the name of the plugin.
        """
        ...

    def getPluginClass(self) -> java.lang.Class:
        """
        Return the class of the plugin.
        @return plugin class object
        """
        ...

    @staticmethod
    def getPluginDescription(c: java.lang.Class) -> ghidra.framework.plugintool.util.PluginDescription:
        """
        Fetches the {@link PluginDescription} for the specified Plugin class.
         <p>
         If the PluginDescription is found in the static cache, it is returned directly,
         otherwise a new instance is created (using annotation data attached to the Plugin
         class) and it is cached for later use.
        @param c Plugin's class
        @return {@link PluginDescription}
        """
        ...

    def getPluginPackage(self) -> ghidra.framework.plugintool.util.PluginPackage: ...

    def getServicesProvided(self) -> List[java.lang.Class]: ...

    def getServicesRequired(self) -> List[java.lang.Class]: ...

    def getShortDescription(self) -> unicode:
        """
        Set the short description for what the plugin does.
        @return short description
        """
        ...

    def getSourceLocation(self) -> unicode:
        """
        Get the location for the source file for the plugin.
        @return path to the source file
        """
        ...

    def getStatus(self) -> ghidra.framework.plugintool.util.PluginStatus:
        """
        Returns the development status of the plugin.
        """
        ...

    def hashCode(self) -> int: ...

    def isInCategory(self, parentCategory: unicode) -> bool:
        """
        Return whether the plugin is in the given category.
        @param parentCategory category to check
        @return true if the plugin is in the category
        """
        ...

    def isSlowInstallation(self) -> bool:
        """
        Returns true if this plugin requires a noticeable amount of time to load when installed.
        @return
        """
        ...

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
    def category(self) -> unicode: ...

    @property
    def description(self) -> unicode: ...

    @property
    def eventsConsumed(self) -> List[object]: ...

    @property
    def eventsProduced(self) -> List[object]: ...

    @property
    def moduleName(self) -> unicode: ...

    @property
    def name(self) -> unicode: ...

    @property
    def pluginClass(self) -> java.lang.Class: ...

    @property
    def pluginPackage(self) -> ghidra.framework.plugintool.util.PluginPackage: ...

    @property
    def servicesProvided(self) -> List[object]: ...

    @property
    def servicesRequired(self) -> List[object]: ...

    @property
    def shortDescription(self) -> unicode: ...

    @property
    def slowInstallation(self) -> bool: ...

    @property
    def sourceLocation(self) -> unicode: ...

    @property
    def status(self) -> ghidra.framework.plugintool.util.PluginStatus: ...
