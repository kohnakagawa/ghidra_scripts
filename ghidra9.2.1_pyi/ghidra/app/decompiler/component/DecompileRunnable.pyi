import ghidra.util.task
import java.lang


class DecompileRunnable(object, ghidra.util.task.SwingRunnable):








    def equals(self, __a0: object) -> bool: ...

    def getClass(self) -> java.lang.Class: ...

    def hashCode(self) -> int: ...

    def monitoredRun(self, monitor: ghidra.util.task.TaskMonitor) -> None:
        """
        Performs the decompile.
        """
        ...

    def notify(self) -> None: ...

    def notifyAll(self) -> None: ...

    def swingRun(self, isCancelled: bool) -> None:
        """
        Automatically called in the Swing thread by the RunManager after the run() method completes.
         If the decompile wasn't cancelled, it reports the results back to the DecompilerController.
        """
        ...

    def toString(self) -> unicode: ...

    @overload
    def wait(self) -> None: ...

    @overload
    def wait(self, __a0: long) -> None: ...

    @overload
    def wait(self, __a0: long, __a1: int) -> None: ...
