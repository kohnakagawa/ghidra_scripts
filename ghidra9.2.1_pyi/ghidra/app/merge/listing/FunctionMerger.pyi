import ghidra.app.merge.listing
import java.lang


class FunctionMerger(ghidra.app.merge.listing.AbstractFunctionMerger, ghidra.app.merge.listing.ListingMerger):
    """
    Class for merging function changes. This class can merge function changes
     that were made to the checked out version. It can determine
     where there are conflicts between the latest checked in version and my
     checked out version. It can then manually merge the conflicting functions.
     The FunctionMerger merges entire functions wherever the function bodies are
     potentially in conflict between Latest and My. It then merges individual
     parts that make up functions with matching bodies.
     Note: Function name differences are not resolved by this merger. Instead,
     they are resolved by the SymbolMerger.
     Important: This class is intended to be used only for a single program
     version merge. It should be constructed, followed by an autoMerge(), and lastly
     each address with a conflict should have mergeConflicts() called on it.
    """









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
