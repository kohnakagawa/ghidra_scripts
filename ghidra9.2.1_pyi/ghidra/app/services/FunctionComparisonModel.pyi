from typing import List
import ghidra.app.plugin.core.functioncompare
import ghidra.program.model.listing
import java.lang
import java.util


class FunctionComparisonModel(object):
    """
    A collection of FunctionComparison
     objects that describe how functions may be compared. Each comparison object
     is a mapping of a function (source) to a list of functions (targets).

     This model is intended to be used by the FunctionComparisonProvider
     as the basis for its display. It should never be created manually, and should
     only be accessed via the FunctionComparisonService.

     Note: Subscribers may register to be informed of changes to this model via the
     FunctionComparisonModelListener interface.
    """





    def __init__(self): ...



    def addComparison(self, comparison: ghidra.app.plugin.core.functioncompare.FunctionComparison) -> None:
        """
        Adds a single comparison to the model
        @param comparison the comparison to add
        """
        ...

    def addFunctionComparisonModelListener(self, listener: ghidra.app.plugin.core.functioncompare.FunctionComparisonModelListener) -> None:
        """
        Adds the given subscriber to the list of those to be notified of model
         changes
        @param listener the model change subscriber
        """
        ...

    @overload
    def compareFunctions(self, functions: java.util.Set) -> None:
        """
        Updates the model with a set of functions to compare. This will add the
         functions to any existing {@link FunctionComparison comparisons} in the
         model and create new comparisons for functions not represented.
         <p>
         Note: It is assumed that when using this method, all functions can be
         compared with all other functions; meaning each function will be added as
         both a source AND a target. To specify a specific source/target
         relationship, use {@link #compareFunctions(Function, Function)}.
        @param functions the set of functions to compare
        """
        ...

    @overload
    def compareFunctions(self, source: ghidra.program.model.listing.Function, target: ghidra.program.model.listing.Function) -> None:
        """
        Compares two functions. If a comparison already exists in the model for
         the given source, the target will simply be added to it; otherwise a
         new comparison will be created.
        @param source the source function
        @param target the target function
        """
        ...

    def equals(self, __a0: object) -> bool: ...

    def getClass(self) -> java.lang.Class: ...

    def getComparisons(self) -> List[ghidra.app.plugin.core.functioncompare.FunctionComparison]:
        """
        Returns a list of all comparisons in the model, in sorted order by
         source function name
        @return a list of all comparisons in the model
        """
        ...

    def getSourceFunctions(self) -> java.util.Set:
        """
        Returns all source functions in the model
        @return a set of all source functions
        """
        ...

    @overload
    def getTargetFunctions(self) -> java.util.Set:
        """
        Returns all target functions in the model
        @return a set of all target functions
        """
        ...

    @overload
    def getTargetFunctions(self, source: ghidra.program.model.listing.Function) -> java.util.Set:
        """
        Returns a set of all target functions for a given source
        @param source the source function to search for
        @return the set of associated target functions
        """
        ...

    def getTargets(self, source: ghidra.program.model.listing.Function) -> java.util.Set:
        """
        Returns a list of all targets in the model (across all comparisons) for
         a given source function
        @param source the source function
        @return list of associated target functions
        """
        ...

    def hashCode(self) -> int: ...

    def notify(self) -> None: ...

    def notifyAll(self) -> None: ...

    def removeFunction(self, function: ghidra.program.model.listing.Function) -> None:
        """
        Removes the given function from all comparisons in the model, whether
         stored as a source or target
        @param function the function to remove
        """
        ...

    def removeFunctions(self, program: ghidra.program.model.listing.Program) -> None:
        """
        Removes all functions in the model that come from the given
         program
        @param program the program to remove functions from
        """
        ...

    def setComparisons(self, __a0: List[object]) -> None: ...

    def toString(self) -> unicode: ...

    @overload
    def wait(self) -> None: ...

    @overload
    def wait(self, __a0: long) -> None: ...

    @overload
    def wait(self, __a0: long, __a1: int) -> None: ...

    @property
    def comparisons(self) -> List[object]: ...

    @comparisons.setter
    def comparisons(self, value: List[object]) -> None: ...

    @property
    def sourceFunctions(self) -> java.util.Set: ...

    @property
    def targetFunctions(self) -> java.util.Set: ...
