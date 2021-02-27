from typing import List
import ghidra.framework.plugintool
import java.lang


class ToolConnection(object):
    """
    Represents a connection between a producer tool and a
     consumer tool.
    """









    def connect(self, eventName: unicode) -> None:
        """
        Connect the tools for the given event name.
        @param eventName name of event to connect
        @throws IllegalArgumentException if eventName is not valid for this
         producer/consumer pair.
        """
        ...

    def disconnect(self, eventName: unicode) -> None:
        """
        Break the connection between the tools for the
         given event name.
        @param eventName name of event to disconnect
        @throws IllegalArgumentException if eventName is not valid for this
         producer/consumer pair.
        """
        ...

    def equals(self, __a0: object) -> bool: ...

    def getClass(self) -> java.lang.Class: ...

    def getConsumer(self) -> ghidra.framework.plugintool.PluginTool:
        """
        Get the tool that consumes an event
        @return the tool
        """
        ...

    def getEvents(self) -> List[unicode]:
        """
        Get the list of event names that is an intersection
         between what the producer produces and what the
         consumers consumes.
        @return an array of event names
        """
        ...

    def getProducer(self) -> ghidra.framework.plugintool.PluginTool:
        """
        Get the tool that produces an event
        @return the tool
        """
        ...

    def hashCode(self) -> int: ...

    def isConnected(self, eventName: unicode) -> bool:
        """
        Return whether the tools are connected for the
         given event name.
        @param eventName name of event to check
        @return true if the tools are connected by eventName.
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
    def consumer(self) -> ghidra.framework.plugintool.PluginTool: ...

    @property
    def events(self) -> List[unicode]: ...

    @property
    def producer(self) -> ghidra.framework.plugintool.PluginTool: ...
