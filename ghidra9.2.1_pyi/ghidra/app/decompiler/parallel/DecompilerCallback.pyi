import generic.concurrent
import ghidra.app.decompiler
import ghidra.program.model.listing
import ghidra.util.task
import java.lang


class DecompilerCallback(object, generic.concurrent.QCallback):
    """
    An implementation of QCallback that performs the management of the
     DecompInterface instances using a Pool.

     Clients will get a chance to configure each newly created decompiler via the passed-in
     DecompileConfigurer.

     Clients must implement #process(DecompileResults, TaskMonitor), which will be
     called for each function that is decompiled.
    """





    def __init__(self, program: ghidra.program.model.listing.Program, configurer: ghidra.app.decompiler.parallel.DecompileConfigurer): ...



    def dispose(self) -> None:
        """
        Call this when all work is done so that the pooled decompilers can be disposed
        """
        ...

    def equals(self, __a0: object) -> bool: ...

    def getClass(self) -> java.lang.Class: ...

    def hashCode(self) -> int: ...

    def notify(self) -> None: ...

    def notifyAll(self) -> None: ...

    @overload
    def process(self, results: ghidra.app.decompiler.DecompileResults, monitor: ghidra.util.task.TaskMonitor) -> R:
        """
        This is called when a function is decompiled.
        @param results the decompiled results
        @param monitor the task monitor
        @return the client result
        @throws Exception if there is any issue processing the given results
        """
        ...

    @overload
    def process(self, f: ghidra.program.model.listing.Function, monitor: ghidra.util.task.TaskMonitor) -> R: ...

    @overload
    def process(self, __a0: object, __a1: ghidra.util.task.TaskMonitor) -> object: ...

    def setTimeout(self, timeoutSecs: int) -> None:
        """
        Sets the timeout for each decompile
        @param timeoutSecs the timeout in seconds
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
    def timeout(self) -> None: ...  # No getter available.

    @timeout.setter
    def timeout(self, value: int) -> None: ...
