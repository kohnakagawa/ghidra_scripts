import ghidra.framework.plugintool
import ghidra.program.model.symbol
import java.lang


class ExternalReferencePluginEvent(ghidra.framework.plugintool.PluginEvent):
    """
    Plugin event used to navigate to a location in another program when following
     a external reference.
    """

    NAME: unicode = u'ExternalReference'



    def __init__(self, src: unicode, extLoc: ghidra.program.model.symbol.ExternalLocation, programPath: unicode):
        """
        Construct a new plugin event.
        @param src name of the source of this event
        @param extLoc the external location to follow
        @param programPath The ghidra path name of the program file to go to.
        """
        ...



    def equals(self, __a0: object) -> bool: ...

    def getClass(self) -> java.lang.Class: ...

    def getEventName(self) -> unicode:
        """
        Get the plugin event name.
        """
        ...

    def getExternalLocation(self) -> ghidra.program.model.symbol.ExternalLocation:
        """
        Get the external location for this event.
        @return the external location
        """
        ...

    def getProgramPath(self) -> unicode:
        """
        Returns the program path name
        @return String containing the program path name.
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

    def getTriggerEvent(self) -> ghidra.framework.plugintool.PluginEvent: ...

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

    def toString(self) -> unicode: ...

    @overload
    def wait(self) -> None: ...

    @overload
    def wait(self, __a0: long) -> None: ...

    @overload
    def wait(self, __a0: long, __a1: int) -> None: ...

    @property
    def externalLocation(self) -> ghidra.program.model.symbol.ExternalLocation: ...

    @property
    def programPath(self) -> unicode: ...
