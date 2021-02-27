from typing import List
import ghidra.framework.model
import ghidra.framework.plugintool
import ghidra.framework.plugintool.util
import java.lang


class EventManager(object):
    """
    Helper class to manage the events that plugins consume and produce.  This class keeps
     track of the last events that went out so that when a plugin is added, it receives those events.
    """





    def __init__(self, tool: ghidra.framework.plugintool.PluginTool):
        """
        Construct a new EventManager.
        @param tool plugin tool associated with this EventManager
        """
        ...



    def addAllEventListener(self, listener: ghidra.framework.plugintool.util.PluginEventListener) -> None: ...

    def addEventListener(self, eventClass: java.lang.Class, listener: ghidra.framework.plugintool.util.PluginEventListener) -> None:
        """
        Add a plugin event listener that will be notified when an event of
         the given event class is generated.
        @param eventClass class of the event of interest
        @param listener listener to notify
        """
        ...

    def addEventProducer(self, eventClass: java.lang.Class) -> None:
        """
        Add the class for the PluginEvent that a plugin will produce
        @param eventClass class for the PluginEvent
        """
        ...

    def addToolListener(self, listener: ghidra.framework.model.ToolListener) -> None:
        """
        Add the given tool listener to be notified notified when tool events are generated
        @param listener listener to add
        """
        ...

    def clearLastEvents(self) -> None:
        """
        Clear the list of last plugin events fired
        """
        ...

    def equals(self, __a0: object) -> bool: ...

    def fireEvent(self, event: ghidra.framework.plugintool.PluginEvent) -> None:
        """
        Notify all plugin listeners that are registered to consume the given
         event. Events are fired in the SwingThread.
        @param event event to fire
        """
        ...

    def getClass(self) -> java.lang.Class: ...

    def getEventsConsumed(self) -> List[unicode]:
        """
        Get the names of all events consumed by plugins in the tool.
        @return array of PluginEvent names
        """
        ...

    def getEventsProduced(self) -> List[unicode]:
        """
        Get the names of all events produced by plugins in the tool.
        @return array of PluginEvent names
        """
        ...

    def getLastEvents(self) -> List[ghidra.framework.plugintool.PluginEvent]:
        """
        Return an array of the last plugin events fired. EventManager maps the event class to the
         last event fired.
        @return array of plugin events
        """
        ...

    def hasToolListeners(self) -> bool:
        """
        Return whether there are any registered tool listeners for the tool associated with class
        @return true if there are any listeners
        """
        ...

    def hashCode(self) -> int: ...

    def notify(self) -> None: ...

    def notifyAll(self) -> None: ...

    def processToolEvent(self, event: ghidra.framework.plugintool.PluginEvent) -> None:
        """
        Convert the given tool event to a plugin event; notify the appropriate plugin listeners.
         This method allows one tool's event manager to send events to another connected tool.
        @param event tool event
        """
        ...

    def removeAllEventListener(self, listener: ghidra.framework.plugintool.util.PluginEventListener) -> None: ...

    @overload
    def removeEventListener(self, className: unicode) -> None:
        """
        Remove the event listener by className; the plugin registered for
         events, but the construction failed.
        @param className class name of the plugin (event listener)
        """
        ...

    @overload
    def removeEventListener(self, eventClass: java.lang.Class, listener: ghidra.framework.plugintool.util.PluginEventListener) -> None:
        """
        Remove the plugin event listener from the list of listeners notified
         when an event of the given event class is generated.
        @param eventClass class of the event of interest
        @param listener listener to remove
        """
        ...

    def removeEventProducer(self, eventClass: java.lang.Class) -> None:
        """
        Remove the class of a PluginEvent that a plugin produces.
        @param eventClass class for the PluginEvent
        """
        ...

    def removeToolListener(self, listener: ghidra.framework.model.ToolListener) -> None:
        """
        Remove the given tool listener from the list of tool listeners
        @param listener listener to remove
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
    def eventsConsumed(self) -> List[unicode]: ...

    @property
    def eventsProduced(self) -> List[unicode]: ...

    @property
    def lastEvents(self) -> List[ghidra.framework.plugintool.PluginEvent]: ...
