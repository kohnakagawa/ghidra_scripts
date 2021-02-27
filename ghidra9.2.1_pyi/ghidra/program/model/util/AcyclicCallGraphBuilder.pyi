import ghidra.util.graph
import ghidra.util.task
import java.lang


class AcyclicCallGraphBuilder(object):
    """
    Class to build an DependencyGraph base on a acyclic function call graph.  This is useful when
     you want to process functions "bottom up".
    """





    @overload
    def __init__(self, program: ghidra.program.model.listing.Program, killThunks: bool):
        """
        Creates a DependencyGraph of all functions in a program based on the call graph.
        @param program the program to create an acyclic call graph
        @param killThunks true if thunked functions should be eliminated from the graph
        """
        ...

    @overload
    def __init__(self, program: ghidra.program.model.listing.Program, set: ghidra.program.model.address.AddressSetView, killThunks: bool):
        """
        Creates a DependencyGraph of all functions in the given addressSet based on the call graph.
         Calls to or from functions outside the given address set are ignored.
        @param program the program to create an acyclic call graph
        @param set the address to restrict the call graph.
        @param killThunks true if thunked functions should be eliminated from the graph
        """
        ...

    @overload
    def __init__(self, program: ghidra.program.model.listing.Program, functions: java.util.Collection, killThunks: bool):
        """
        Creates a DependencyGraph of all functions in the given set of functions based on the call graph.
         Calls to or from functions not in the given set are ignored.
        @param program the program to create an acyclic call graph
        @param functions the set of functions to include in the call graph.
        @param killThunks true if thunked functions should be eliminated from the graph
        """
        ...



    def equals(self, __a0: object) -> bool: ...

    def getClass(self) -> java.lang.Class: ...

    def getDependencyGraph(self, monitor: ghidra.util.task.TaskMonitor) -> ghidra.util.graph.AbstractDependencyGraph:
        """
        Builds the DependencyGraph for the acyclic call graph represented by this object.
        @param monitor the taskMonitor to use for reporting progress or cancelling.
        @return the DependencyGraph for the acyclic call graph represented by this object.
        @throws CancelledException if the monitor was cancelled.
        """
        ...

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
