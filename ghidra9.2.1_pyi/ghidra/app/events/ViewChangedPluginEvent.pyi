import ghidra.framework.plugintool
import ghidra.program.model.address
import java.lang


class ViewChangedPluginEvent(ghidra.framework.plugintool.PluginEvent):
    """
    Event for notifying plugins when the program view changes (what the
     Code Browser shows in the listing window).
    """

    NAME: unicode = u'ViewChanged'



    def __init__(self, source: unicode, treeName: unicode, viewSet: ghidra.program.model.address.AddressSet):
        """
        Constructor for ViewChangedPluginEvent.
        @param source name of the plugin that created this event
        @param treeName name of the tree in the program
        @param viewSet set of addresses in the view
        """
        ...



    def equals(self, __a0: object) -> bool: ...

    def getClass(self) -> java.lang.Class: ...

    def getEventName(self) -> unicode:
        """
        Get the plugin event name.
        """
        ...

    def getSourceName(self) -> unicode:
        """
        Returns the name of the plugin immediately responsible for firing this
         event.
        """
        ...

    def getToolEventName(self) -> unicode:
        """
        Get the optional cross-tool event name which has been established via
         a {@link ToolEventName} annotation which makes it available for
         passing as an external tool via a {@link ToolConnection}.
         This name may differ from the {@link #getEventName()}.s
        @return tool event name or null if not permitted as a cross-tool event
        """
        ...

    def getTreeName(self) -> unicode:
        """
        Get the name of the tree where the view is from.
        """
        ...

    def getTriggerEvent(self) -> ghidra.framework.plugintool.PluginEvent: ...

    def getView(self) -> ghidra.program.model.address.AddressSet:
        """
        Get the address set in the view.
        """
        ...

    def hashCode(self) -> int: ...

    def isToolEvent(self) -> bool:
        """
        Determine if this event has been annotated with a {@link ToolEventName} which
         makes it available for passing to another tool via a {@link ToolConnection}.
        @return true if event can be utilized as a cross-tool event
        """
        ...

    @staticmethod
    def lookupToolEventName(pluginEventClass: java.lang.Class) -> unicode:
        """
        Returns the tool event name corresponding to the given pluginEventClass.
         If no corresponding tool event exists, null will be returned.
        """
        ...

    def notify(self) -> None: ...

    def notifyAll(self) -> None: ...

    def setSourceName(self, s: unicode) -> None: ...

    def setTriggerEvent(self, triggerEvent: ghidra.framework.plugintool.PluginEvent) -> None: ...

    def toString(self) -> unicode:
        """
        Returns a string for debugging purposes.
        @see java.lang.Object#toString()
        """
        ...

    @overload
    def wait(self) -> None: ...

    @overload
    def wait(self, __a0: long) -> None: ...

    @overload
    def wait(self, __a0: long, __a1: int) -> None: ...

    @property
    def treeName(self) -> unicode: ...

    @property
    def view(self) -> ghidra.program.model.address.AddressSet: ...
