import ghidra.framework.options
import ghidra.framework.plugintool
import ghidra.service.graph
import ghidra.util
import ghidra.util.classfinder
import ghidra.util.task
import java.lang


class GraphDisplayProvider(ghidra.util.classfinder.ExtensionPoint, object):
    """
    Basic interface for objects that can display or otherwise consume a generic graph
    """









    def dispose(self) -> None:
        """
        Disposes this GraphDisplayProvider
        """
        ...

    def equals(self, __a0: object) -> bool: ...

    def getClass(self) -> java.lang.Class: ...

    def getGraphDisplay(self, reuseGraph: bool, monitor: ghidra.util.task.TaskMonitor) -> ghidra.service.graph.GraphDisplay:
        """
        Returns a GraphDisplay that can be used to "display" a graph
        @param reuseGraph if true, this provider will attempt to re-use an existing GraphDisplay
        @param monitor the {@link TaskMonitor} that can be used to monitor and cancel the operation
        @return A GraphDisplay that can be used to display (or otherwise consume - e.g. export) the graph
        @throws GraphException thrown if there is a problem creating a GraphDisplay
        """
        ...

    def getHelpLocation(self) -> ghidra.util.HelpLocation:
        """
        Gets the help location for this GraphDisplayProvider
        @return help location for this GraphDisplayProvider
        """
        ...

    def getName(self) -> unicode:
        """
        The name of this provider (for displaying as menu option when graphing)
        @return the name of this provider.
        """
        ...

    def hashCode(self) -> int: ...

    def initialize(self, tool: ghidra.framework.plugintool.PluginTool, options: ghidra.framework.options.Options) -> None:
        """
        Provides an opportunity for this provider to register and read tool options
        @param tool the tool hosting this display
        @param options the tool options for graphing
        """
        ...

    def notify(self) -> None: ...

    def notifyAll(self) -> None: ...

    def optionsChanged(self, options: ghidra.framework.options.Options) -> None:
        """
        Called if the graph options change
        @param options the current tool options
        """
        ...

    def toString(self) -> unicode: ...

    @overload
    def wait(self) -> None: ...

    @overload
    def wait(self, __a0: long) -> None: ...

    @overload
    def wait(self, __a0: long, __a1: int) -> None: ...

    @property
    def helpLocation(self) -> ghidra.util.HelpLocation: ...

    @property
    def name(self) -> unicode: ...
