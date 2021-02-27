from typing import List
import ghidra.framework.model
import ghidra.framework.plugintool
import java.lang


class ToolConnectionImpl(object, ghidra.framework.model.ToolConnection, ghidra.framework.model.ToolListener):
    """
    Implementation for representing connections between two tools.
     Acts as the middle man for the connection in order to filter the
     events.
    """









    def connect(self, eventName: unicode) -> None: ...

    def disconnect(self, eventName: unicode) -> None: ...

    def equals(self, obj: object) -> bool:
        """
        Indicates whether some other object is "equal to" this one.
        """
        ...

    def getClass(self) -> java.lang.Class: ...

    def getConsumer(self) -> ghidra.framework.plugintool.PluginTool: ...

    def getEvents(self) -> List[unicode]: ...

    def getProducer(self) -> ghidra.framework.plugintool.PluginTool: ...

    def hashCode(self) -> int:
        """
        Returns a hash code value for the object. This method is
         supported for the benefit of hashtables such as those provided by
         <code>java.util.Hashtable</code>.
        """
        ...

    def isConnected(self, eventName: unicode) -> bool: ...

    def notify(self) -> None: ...

    def notifyAll(self) -> None: ...

    def processToolEvent(self, toolEvent: ghidra.framework.plugintool.PluginEvent) -> None: ...

    def toString(self) -> unicode:
        """
        Returns a string representation of the object. In general, the
         <code>toString</code> method returns a string that
         "textually represents" this object. The result should
         be a concise but informative representation that is easy for a
         person to read.
        """
        ...

    @overload
    def wait(self) -> None: ...

    @overload
    def wait(self, __a0: long) -> None: ...

    @overload
    def wait(self, __a0: long, __a1: int) -> None: ...
