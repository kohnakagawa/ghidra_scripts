import ghidra.app.cmd.function
import java.lang


class CaptureFunctionDataTypesListener(object):
    """
    Listener that is notified when the CaptureFunctionDataTypesCmd completes.
    """









    def captureFunctionDataTypesCompleted(self, cmd: ghidra.app.cmd.function.CaptureFunctionDataTypesCmd) -> None:
        """
        Notification that the capture function data types command completed
        @param cmd command that was completed; the command has the
         status as to whether the capture was successful
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
