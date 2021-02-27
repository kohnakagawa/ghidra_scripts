import ghidra.app.cmd.memory
import java.lang


class DeleteBlockListener(object):
    """
    Listener that is notified when the DeleteBlockCmd completes.
    """









    def deleteBlockCompleted(self, cmd: ghidra.app.cmd.memory.DeleteBlockCmd) -> None:
        """
        Notification that the delete block command completed
        @param cmd command that was completed; the command has the
         status as to whether the delete was successful
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
