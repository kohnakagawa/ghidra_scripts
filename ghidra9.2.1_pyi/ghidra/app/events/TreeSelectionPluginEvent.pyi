from typing import List
import ghidra.framework.plugintool
import ghidra.program.util
import java.lang


class TreeSelectionPluginEvent(ghidra.framework.plugintool.PluginEvent):
    """
    Notification for a new Program Tree selection.
    """

    NAME: unicode = u'ProgramTreeSelection'



    def __init__(self, source: unicode, treeName: unicode, groupPaths: List[ghidra.program.util.GroupPath]):
        """
        Constructor for TreeSelectionPluginEvent.
        @param source name of the plugin that generated this event
        @param treeName name of the tree in the program
        @param groupPaths group paths that are selected in a Program Tree; the
         group path uniquely identifies a Module (folder) or fragment in the
         tree
        """
        ...



    def equals(self, __a0: object) -> bool: ...

    def getClass(self) -> java.lang.Class: ...

    def getEventName(self) -> unicode:
        """
        Get the plugin event name.
        """
        ...

    def getGroupPaths(self) -> List[ghidra.program.util.GroupPath]:
        """
        Get the group paths that are in the tree selection.
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
        Get the tree name associated with this event.
        @return String tree name
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

    def toString(self) -> unicode:
        """
        String representation of this event for debugging purposes.
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
    def groupPaths(self) -> List[ghidra.program.util.GroupPath]: ...

    @property
    def treeName(self) -> unicode: ...
