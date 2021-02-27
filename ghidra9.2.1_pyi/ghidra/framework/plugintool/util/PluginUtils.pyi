from typing import List
import ghidra.framework.plugintool
import java.lang
import java.util


class PluginUtils(object):
    """
    Utility class for plugin-related methods.
    """





    def __init__(self): ...



    @staticmethod
    def assertUniquePluginName(pluginClass: java.lang.Class) -> None:
        """
        Ensures the specified Plugin has a unique name among all Plugin classes
         found in the current ClassSearcher's reach.
        @param pluginClass Class
        @throws PluginException throws exception if Plugin class is not uniquely named
        """
        ...

    def equals(self, __a0: object) -> bool: ...

    @staticmethod
    def findLoadedPlugins(extensions: java.util.Set) -> List[java.lang.Class]:
        """
        Finds all plugin classes loaded from a given set of extensions.
        @param extensions set of extensions to search
        @return list of loaded plugin classes, or empty list if none found
        """
        ...

    @staticmethod
    def forName(pluginClassName: unicode) -> java.lang.Class:
        """
        Returns the Class for a Plugin, by class name.
        @param pluginClassName String class name
        @return Class that is a Plugin, never null.
        @throws PluginException if specified class does not exist or is not a Plugin.
        """
        ...

    def getClass(self) -> java.lang.Class: ...

    @staticmethod
    def getDefaultProviderForServiceClass(serviceClass: java.lang.Class) -> java.lang.Class:
        """
        Returns the Plugin Class that is specified as being the defaultProvider for a
         Service, or null if no default provider is specified.
         <p>
        @param serviceClass Service interface class
        @return Plugin class that provides the specified service
        """
        ...

    @staticmethod
    def getPluginDescriptions(__a0: ghidra.framework.plugintool.PluginTool, __a1: List[object]) -> List[object]: ...

    @staticmethod
    def getPluginNameFromClass(pluginClass: java.lang.Class) -> unicode:
        """
        Returns the name of a Plugin based on its class.
        @param pluginClass Class to get name from
        @return String name, based on Class's getSimpleName()
        """
        ...

    def hashCode(self) -> int: ...

    @staticmethod
    def instantiatePlugin(pluginClass: java.lang.Class, tool: ghidra.framework.plugintool.PluginTool) -> object:
        """
        Returns a new instance of a {@link Plugin}.
        @param pluginClass Specific Plugin Class
        @param tool The {@link PluginTool} that is the parent of the new Plugin
        @return a new Plugin instance, never NULL.
        @throws PluginException if problem constructing the Plugin instance.
        """
        ...

    @staticmethod
    def isValidPluginClass(pluginClass: java.lang.Class) -> bool:
        """
        Returns true if the specified Plugin class is well-formed and meets requirements for
         Ghidra Plugins:
         <ul>
         	<li>Has a constructor with a signature of <code>ThePlugin(PluginTool tool)</code>
         	<li>Has a {@link PluginInfo @PluginInfo} annotation.
         </ul>
         <p>
         See {@link Plugin}.
         <p>
        @param pluginClass Class to examine.
        @return boolean true if well formed.
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
