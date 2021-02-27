import ghidra.framework.plugintool
import java.lang


class ToolListener(object):
    """
    Interface to be implemented by objects that want to receive PluginEvents.
     Tools must be registered for a particular event to actually receive it.
    """









    def equals(self, __a0: object) -> bool: ...

    def getClass(self) -> java.lang.Class: ...

    def hashCode(self) -> int: ...

    def notify(self) -> None: ...

    def notifyAll(self) -> None: ...

    def processToolEvent(self, toolEvent: ghidra.framework.plugintool.PluginEvent) -> None:
        """
        This method is invoked when the registered PluginEvent event occurs.
        @param toolEvent The cross-tool PluginEvent.
        """
        ...

    def toString(self) -> unicode: ...

    @overload
    def wait(self) -> None: ...

    @overload
    def wait(self, __a0: long) -> None: ...

    @overload
    def wait(self, __a0: long, __a1: int) -> None: ...
