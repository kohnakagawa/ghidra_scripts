import ghidra.framework.cmd
import java.lang


class BackgroundCommandListener(object):
    """
    Listener that is notified when a BackgroundCommand completes.
    """









    def commandCompleted(self, cmd: ghidra.framework.cmd.BackgroundCommand) -> None:
        """
        Notification that the given BackgroundCommand has completed.
        @param cmd background command that has completed
        """
        ...

    def equals(self, __a0: object) -> bool: ...

    def getClass(self) -> java.lang.Class: ...

    def hashCode(self) -> int: ...

    def notify(self) -> None: ...

    def notifyAll(self) -> None: ...

    def toString(self) -> unicode: ...

    @overload
    def wait(self) -> None: ...

    @overload
    def wait(self, __a0: long) -> None: ...

    @overload
    def wait(self, __a0: long, __a1: int) -> None: ...
