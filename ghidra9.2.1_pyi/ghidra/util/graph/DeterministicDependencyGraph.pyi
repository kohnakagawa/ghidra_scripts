import ghidra.util.graph
import java.lang
import java.util


class DeterministicDependencyGraph(ghidra.util.graph.AbstractDependencyGraph):
    """
    Dependency Graph that uses TreeMaps and ListOrderedSets to provide
     determinism in pulling (#pop()) from the graph.  This class seems to consume more
     memory than DependencyGraph, and if memory is not an issue, it also seems to be
     slightly faster as well.

     This class was implemented to provide determinism while doing
     developmental debugging.
    """





    @overload
    def __init__(self): ...

    @overload
    def __init__(self, other: ghidra.util.graph.DeterministicDependencyGraph):
        """
        Copy constructor
        @param other the other DependencyGraph to copy
        """
        ...



    def addDependency(self, value1: object, value2: object) -> None:
        """
        Add a dependency such that value1 depends on value2.  Both value1 and value2 will be
         added to the graph if they are not already in the graph.
        @param value1 the value that depends on value2
        @param value2 the value that value1 is depending on
        """
        ...

    def addValue(self, value: object) -> None:
        """
        Adds the value to this graph.
        @param value the value to add
        """
        ...

    def contains(self, value: object) -> bool:
        """
        Returns true if this graph has the given key.
        @param value the value to check if its in this graph
        @return true if this graph has the given key.
        """
        ...

    def copy(self) -> ghidra.util.graph.DeterministicDependencyGraph: ...

    def equals(self, __a0: object) -> bool: ...

    def getAllIndependentValues(self) -> java.util.Set:
        """
        Returns the set of all values that have no dependencies regardless of whether or not
         they have been "visited" (by the getUnvisitedIndependentValues() method.
        @return return the set of all values that have no dependencies.
        """
        ...

    def getClass(self) -> java.lang.Class: ...

    def getDependentValues(self, value: object) -> java.util.Set:
        """
        Returns a set of values that depend on the given value.
        @param value the value that other values may depend on.
        @return a set of values that depend on the given value.
        """
        ...

    def getNodeMap(self) -> java.util.Map: ...

    def getNodeMapValues(self) -> java.util.Set: ...

    def getUnvisitedIndependentValues(self) -> java.util.Set:
        """
        Returns a set of all values that have no dependencies.  As values are removed from the
         graph, dependencies will be removed and additional values will be eligible to be returned
         by this method.  Once a value has been retrieved using this method, it will be considered
         "visited" and future calls to this method will not include those values.  To continue
         processing the values in the graph, all values return from this method should eventually
         be deleted from the graph to "free up" other values.  NOTE: values retrieved by this method
         will no longer be eligible for return by the pop() method.
        @return the set of values without dependencies that have never been returned by this method
         before.
        """
        ...

    def getValues(self) -> java.util.Set:
        """
        Returns the set of values in this graph.
        @return the set of values in this graph.
        """
        ...

    def hasCycles(self) -> bool:
        """
        Checks if this graph has cycles.  Normal processing of this graph will eventually reveal
         a cycle and throw an exception at the time it is detected.  This method allows for a
         "fail fast" way to detect cycles.
        @return true if cycles exist in the graph.
        """
        ...

    def hasUnVisitedIndependentValues(self) -> bool:
        """
        Returns true if there are unvisited values ready (no dependencies) for processing.
        @return true if there are unvisited values ready for processing.
        @exception IllegalStateException is thrown if the graph is not empty and there are no nodes
         without dependency which indicates there is a cycle in the graph.
        """
        ...

    def hashCode(self) -> int: ...

    def isEmpty(self) -> bool:
        """
        Returns true if the graph has no values;
        @return true if the graph has no values;
        """
        ...

    def notify(self) -> None: ...

    def notifyAll(self) -> None: ...

    def pop(self) -> object:
        """
        Removes and returns a value that has no dependencies from the graph.  If the graph is empty
         or all the nodes without dependencies are currently visited, then null will be returned.
         NOTE: If the getUnvisitedIndependentValues() method has been called(), this method may
         return null until all those "visited" nodes are removed from the graph.
        @return return an arbitrary value that has no dependencies and hasn't been visited or null.
        """
        ...

    def remove(self, value: object) -> None:
        """
        Removes the value from the graph.  Any dependency from this node to another will be removed,
         possible allowing nodes that depend on this node to be eligible for processing.
        @param value the value to remove from the graph.
        """
        ...

    def size(self) -> int:
        """
        Returns the number of values in this graph.
        @return the number of values in this graph.
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
    def nodeMapValues(self) -> java.util.Set: ...
