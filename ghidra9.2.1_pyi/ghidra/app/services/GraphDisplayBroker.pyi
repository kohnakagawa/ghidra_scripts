import ghidra.app.plugin.core.graph
import ghidra.service.graph
import ghidra.util.task
import java.lang


class GraphDisplayBroker(object):
    """
    Ghidra service interface for managing and directing graph output.  It purpose is to discover
     available graphing display providers and (if more than one) allow the user to select the currently
     active graph consumer.  Clients that generate graphs don't have to worry about how to display them
     or export graphs. They simply send their graphs to the broker and register for graph events if
     they want interactive support.
    """









    def addGraphDisplayBrokerListener(self, listener: ghidra.app.plugin.core.graph.GraphDisplayBrokerListener) -> None:
        """
        Adds a listener for notification when the set of graph display providers change or the currently
         active graph display provider changes
        @param listener the listener to be notified
        """
        ...

    def equals(self, __a0: object) -> bool: ...

    def getClass(self) -> java.lang.Class: ...

    def getDefaultGraphDisplay(self, reuseGraph: bool, monitor: ghidra.util.task.TaskMonitor) -> ghidra.service.graph.GraphDisplay:
        """
        A convenience method for getting a {@link GraphDisplay} from the currently active provider
        @param reuseGraph if true, the provider will attempt to re-use a current graph display
        @param monitor the {@link TaskMonitor} that can be used to cancel the operation
        @return a {@link GraphDisplay} object to sends graphs to be displayed or exported.
        @throws GraphException thrown if an error occurs trying to get a graph display
        """
        ...

    def getDefaultGraphDisplayProvider(self) -> ghidra.service.graph.GraphDisplayProvider:
        """
        Gets the currently active GraphDisplayProvider that will be used to display/export graphs
        @return the currently active GraphDisplayProvider
        """
        ...

    def getGraphDisplayProvider(self, name: unicode) -> ghidra.service.graph.GraphDisplayProvider:
        """
        Gets the {@link GraphDisplayProvider} with the given name
        @param name the name of the GraphDisplayProvider to get
        @return the GraphDisplayProvider with the given name or null if none with that name exists.
        """
        ...

    def hasDefaultGraphDisplayProvider(self) -> bool:
        """
        Checks if there is at least one {@link GraphDisplayProvider} in the system.
        @return true if there is at least one {@link GraphDisplayProvider}
        """
        ...

    def hashCode(self) -> int: ...

    def notify(self) -> None: ...

    def notifyAll(self) -> None: ...

    def removeGraphDisplayBrokerLisetener(self, listener: ghidra.app.plugin.core.graph.GraphDisplayBrokerListener) -> None:
        """
        Removes the given listener
        @param listener the listener to no longer be notified of changes
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
    def defaultGraphDisplayProvider(self) -> ghidra.service.graph.GraphDisplayProvider: ...
