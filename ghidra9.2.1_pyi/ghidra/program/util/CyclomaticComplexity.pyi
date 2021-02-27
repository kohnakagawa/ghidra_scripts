import ghidra.program.model.listing
import ghidra.util.task
import java.lang


class CyclomaticComplexity(object):
    """
    Class with a utility function to calculate the cyclomatic complexity of a function.
    """





    def __init__(self): ...



    def calculateCyclomaticComplexity(self, function: ghidra.program.model.listing.Function, monitor: ghidra.util.task.TaskMonitor) -> int:
        """
        Calculates the cyclomatic complexity of a function by decomposing it into a flow
         graph using a BasicBlockModel.
        @param function the function
        @param monitor a monitor
        @return the cyclomatic complexity
        @throws CancelledException
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
