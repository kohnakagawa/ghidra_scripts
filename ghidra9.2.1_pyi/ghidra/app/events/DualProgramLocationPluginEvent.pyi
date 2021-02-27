import ghidra.framework.plugintool
import ghidra.program.util
import java.lang


class DualProgramLocationPluginEvent(ghidra.framework.plugintool.PluginEvent):
    """
    This plugin event class provides program location information for
     plugins that send information to two or more tools containing associated addresses.
    """

    NAME: unicode = u'DualProgramLocation'



    @overload
    def __init__(self, src: unicode, loc: ghidra.program.util.ProgramLocation, programName: unicode):
        """
        Construct a new DualProgramLocationPluginEvent.
        @param src the name of the plugin that generated this event.
        @param loc the ProgramLocation object that contains the new location.
        @param programName the name of the program for which the loc object refers.
        """
        ...

    @overload
    def __init__(self, src: unicode, loc: ghidra.program.util.ProgramLocation, program: ghidra.program.model.listing.Program):
        """
        Construct a new DualProgramLocationPluginEvent.
        @param src the name of the plugin that generated this event.
        @param loc the ProgramLocation object that contains the new location.
        @param program the program for which the loc object refers.
        """
        ...



    def equals(self, __a0: object) -> bool: ...

    def getClass(self) -> java.lang.Class: ...

    def getEventName(self) -> unicode:
        """
        Get the plugin event name.
        """
        ...

    def getLocation(self) -> ghidra.program.util.ProgramLocation:
        """
        Returns the ProgramLocation stored in this event.
        """
        ...

    def getProgramName(self) -> unicode:
        """
        Returns the Program object that the location refers to.
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
    def location(self) -> ghidra.program.util.ProgramLocation: ...

    @property
    def programName(self) -> unicode: ...
