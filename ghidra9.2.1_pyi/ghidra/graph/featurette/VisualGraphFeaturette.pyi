import ghidra.framework.options
import ghidra.graph
import java.lang


class VisualGraphFeaturette(object):
    """
    An interface that represents a sub-feature of a VisualGraphComponentProvider.  This
     allows the base provider to have a set of features ready to be installed by subclasses.
    """









    def equals(self, __a0: object) -> bool: ...

    def getClass(self) -> java.lang.Class: ...

    def hashCode(self) -> int: ...

    def init(self, provider: ghidra.graph.VisualGraphComponentProvider) -> None:
        """
        Called to initialize this feature when the provider and view are ready
        @param provider the provider associated with this feature
        """
        ...

    def notify(self) -> None: ...

    def notifyAll(self) -> None: ...

    def providerClosed(self, provider: ghidra.graph.VisualGraphComponentProvider) -> None:
        """
        Called when the client provider is closed
        @param provider the provider
        """
        ...

    def providerOpened(self, provider: ghidra.graph.VisualGraphComponentProvider) -> None:
        """
        Called when the client provider is opened
        @param provider the provider
        """
        ...

    def readConfigState(self, saveState: ghidra.framework.options.SaveState) -> None:
        """
        Called when the client wishes to restore configuration state.  Features can read state
         previously saved from a call to {@link #writeConfigState(SaveState)}.
        @param saveState the container for state information
        """
        ...

    def remove(self) -> None:
        """
        Called when the provider is being disposed
        """
        ...

    def toString(self) -> unicode: ...

    @overload
    def wait(self) -> None: ...

    @overload
    def wait(self, __a0: long) -> None: ...

    @overload
    def wait(self, __a0: long, __a1: int) -> None: ...

    def writeConfigState(self, state: ghidra.framework.options.SaveState) -> None:
        """
        Called when the client wishes to save configuration state.  Features can add any state
         they wish to be persisted over tool launches.
        @param state the container for state information
        """
        ...
