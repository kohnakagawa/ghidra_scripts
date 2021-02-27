from typing import List
import generic.stl
import ghidra.app.util.opinion
import java.lang
import java.util.function


class SingleLoaderFilter(object, java.util.function.Predicate):




    @overload
    def __init__(self, single: java.lang.Class):
        """
        Create a new single loader filter from the given loader class.
        @param single The loader class used for this filter.
        """
        ...

    @overload
    def __init__(self, __a0: java.lang.Class, __a1: List[object]): ...



    def and(self, __a0: java.util.function.Predicate) -> java.util.function.Predicate: ...

    def equals(self, __a0: object) -> bool: ...

    def getClass(self) -> java.lang.Class: ...

    def getLoaderArgs(self) -> List[generic.stl.Pair]:
        """
        Gets the loader arguments tied to the loader in this filter.
        @return The loader arguments tied to the loader in this filter.  Could be null if there
                 are no arguments.
        """
        ...

    def hashCode(self) -> int: ...

    @staticmethod
    def isEqual(__a0: object) -> java.util.function.Predicate: ...

    def negate(self) -> java.util.function.Predicate: ...

    @staticmethod
    def not(__a0: java.util.function.Predicate) -> java.util.function.Predicate: ...

    def notify(self) -> None: ...

    def notifyAll(self) -> None: ...

    def or(self, __a0: java.util.function.Predicate) -> java.util.function.Predicate: ...

    @overload
    def test(self, loader: ghidra.app.util.opinion.Loader) -> bool: ...

    @overload
    def test(self, __a0: object) -> bool: ...

    def toString(self) -> unicode: ...

    @overload
    def wait(self) -> None: ...

    @overload
    def wait(self, __a0: long) -> None: ...

    @overload
    def wait(self, __a0: long, __a1: int) -> None: ...

    @property
    def loaderArgs(self) -> List[object]: ...
