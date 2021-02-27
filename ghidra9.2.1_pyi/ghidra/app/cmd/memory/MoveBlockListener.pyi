import ghidra.app.cmd.memory
import java.lang


class MoveBlockListener(object):
    """
    Listener that is notified when a move block completed or some state
     has changed.
    """









    def equals(self, __a0: object) -> bool: ...

    def getClass(self) -> java.lang.Class: ...

    def hashCode(self) -> int: ...

    def moveBlockCompleted(self, cmd: ghidra.app.cmd.memory.MoveBlockTask) -> None:
        """
        Notification that the move block completed.
        @param cmd the command that was executed to move the block; the
         command has the status of whether the block was moved
         successfully
        """
        ...

    def notify(self) -> None: ...

    def notifyAll(self) -> None: ...

    def stateChanged(self) -> None:
        """
        Notification that something has changed.
        """
        ...

    def toString(self) -> unicode: ...

    @overload
    def wait(self) -> None: ...

    @overload
    def wait(self, __a0: long) -> None: ...

    @overload
    def wait(self, __a0: long, __a1: int) -> None: ...
