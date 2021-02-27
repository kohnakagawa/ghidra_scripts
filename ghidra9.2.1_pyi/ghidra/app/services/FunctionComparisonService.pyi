import docking
import ghidra.app.plugin.core.functioncompare
import ghidra.program.model.listing
import java.lang
import java.util


class FunctionComparisonService(object):
    """
    Allows users to create comparisons between functions which will be displayed
     side-by-side in a FunctionComparisonProvider. Each side in the
     display will allow the user to select one or more functions

     Concurrent usage: All work performed by this service will be done on the Swing thread.
     Further, all calls that do not return a value will be run immediately if the caller is on
     the Swing thread; otherwise, the work will be done on the Swing thread at a later time.
     Contrastingly, any method on this interface that returns a value will be run immediately,
     regardless of whether the call is on the Swing thread.  Thus, the methods that return a value
     will always be blocking calls; methods that do not return a value may or may not block,
     depending on the client's thread.
    """









    def addFunctionComparisonProviderListener(self, listener: docking.ComponentProviderActivationListener) -> None:
        """
        Adds the given listener to the list of subscribers who wish to be
         notified of provider activation events (eg: provider open/close)
        @param listener the listener to be added
        """
        ...

    @overload
    def compareFunctions(self, functions: java.util.Set) -> ghidra.app.plugin.core.functioncompare.FunctionComparisonProvider:
        """
        Creates a comparison between a set of functions, where each function
         in the list can be compared against any other.
         <p>
         eg: Given a set of 3 functions (f1, f2, f3), the comparison dialog will
         allow the user to display either f1, f2 or f3 on EITHER side of the
         comparison.
         <p>
         Note that this method will always create a new provider; if you want to
         add functions to an existing comparison, use
         {@link #compareFunctions(Set, FunctionComparisonProvider) this}
         variant that takes a provider.
        @param functions the functions to compare
        @return the new comparison provider
        """
        ...

    @overload
    def compareFunctions(self, source: ghidra.program.model.listing.Function, target: ghidra.program.model.listing.Function) -> ghidra.app.plugin.core.functioncompare.FunctionComparisonProvider:
        """
        Creates a comparison between two functions, where the source function
         will be shown on the left side of the comparison dialog and the target
         on the right.
         <p>
         Note that this will always create a new provider; if you want to add
         functions to an existing comparison, use
         {@link #compareFunctions(Function, Function, FunctionComparisonProvider) this}
         variant that takes a provider.
        @param source a function in the comparison
        @param target a function in the comparison
        @return the new comparison provider
        """
        ...

    @overload
    def compareFunctions(self, functions: java.util.Set, provider: ghidra.app.plugin.core.functioncompare.FunctionComparisonProvider) -> None:
        """
        Creates a comparison between a set of functions, adding them to the
         given comparison provider. Each function in the given set will be added
         to both sides of the comparison, allowing users to compare any functions
         in the existing provider with the new set.
        @see #compareFunctions(Set)
        @param functions the functions to compare
        @param provider the provider to add the comparisons to
        """
        ...

    @overload
    def compareFunctions(self, source: ghidra.program.model.listing.Function, target: ghidra.program.model.listing.Function, provider: ghidra.app.plugin.core.functioncompare.FunctionComparisonProvider) -> None:
        """
        Creates a comparison between two functions and adds it to a given
         comparison provider. The existing comparisons in the provider will not
         be affected, unless the provider already contains a comparison with
         the same source function; in this case the given target will be added
         to that comparisons' list of targets.
        @see #compareFunctions(Function, Function)
        @param source a function in the comparison
        @param target a function in the comparison
        @param provider the provider to add the comparison to
        """
        ...

    def equals(self, __a0: object) -> bool: ...

    def getClass(self) -> java.lang.Class: ...

    def hashCode(self) -> int: ...

    def notify(self) -> None: ...

    def notifyAll(self) -> None: ...

    @overload
    def removeFunction(self, function: ghidra.program.model.listing.Function) -> None:
        """
        Removes a given function from all comparisons across all comparison
         providers
        @param function the function to remove
        """
        ...

    @overload
    def removeFunction(self, function: ghidra.program.model.listing.Function, provider: ghidra.app.plugin.core.functioncompare.FunctionComparisonProvider) -> None:
        """
        Removes a given function from all comparisons in the given comparison
         provider only
        @param function the function to remove
        @param provider the comparison provider to remove functions from
        """
        ...

    def removeFunctionComparisonProviderListener(self, listener: docking.ComponentProviderActivationListener) -> None:
        """
        Removes a listener from the list of provider activation event subscribers
        @param listener the listener to remove
        """
        ...

    def toString(self) -> unicode: ...

    @overload
    def wait(self) -> None: ...

    @overload
    def wait(self, __a0: long) -> None: ...

    @overload
    def wait(self, __a0: long, __a1: int) -> None: ...
