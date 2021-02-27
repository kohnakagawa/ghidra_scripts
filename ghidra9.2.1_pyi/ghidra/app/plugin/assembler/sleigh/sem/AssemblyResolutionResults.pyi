from typing import Iterator
from typing import List
import ghidra.app.plugin.assembler.sleigh.sem
import java.lang
import java.util
import java.util.function
import java.util.stream
import org.apache.commons.collections4.set


class AssemblyResolutionResults(org.apache.commons.collections4.set.AbstractSetDecorator):
    """
    A set of possible assembly resolutions for a single SLEIGH constructor

     Since the assembler works from the leaves up, it unclear in what context a given token appears.
     Thus, every possible encoding is collected and passed upward. As resolution continues, many of
     the possible encodings are pruned out. When the resolver reaches the root, we end up with every
     possible encoding (less some prefixes) of an instruction. This object stores the possible
     encodings, including error records describing the pruned intermediate results.
    """





    def __init__(self):
        """
        Construct a new (mutable) empty set of resolutions
        """
        ...

    def __iter__(self): ...

    def absorb(self, that: ghidra.app.plugin.assembler.sleigh.sem.AssemblyResolutionResults) -> None:
        """
        A synonym for {@link #addAll(Collection)} that accepts only another resolution set
        @param that the other set
        """
        ...

    @overload
    def add(self, ar: ghidra.app.plugin.assembler.sleigh.sem.AssemblyResolution) -> bool: ...

    @overload
    def add(self, __a0: object) -> bool: ...

    def addAll(self, c: java.util.Collection) -> bool: ...

    def clear(self) -> None: ...

    def contains(self, __a0: object) -> bool: ...

    def containsAll(self, __a0: java.util.Collection) -> bool: ...

    @staticmethod
    def copyOf(__a0: java.util.Collection) -> java.util.Set: ...

    def equals(self, __a0: object) -> bool: ...

    def forEach(self, __a0: java.util.function.Consumer) -> None: ...

    def getClass(self) -> java.lang.Class: ...

    def getResolutions(self) -> java.util.Set:
        """
        Get an unmodifiable reference to this set
        @return the set
        """
        ...

    def hashCode(self) -> int: ...

    def isEmpty(self) -> bool: ...

    def iterator(self) -> java.util.Iterator: ...

    def notify(self) -> None: ...

    def notifyAll(self) -> None: ...

    @overload
    @staticmethod
    def of() -> java.util.Set: ...

    @overload
    @staticmethod
    def of(__a0: List[object]) -> java.util.Set: ...

    @overload
    @staticmethod
    def of(__a0: object) -> java.util.Set: ...

    @overload
    @staticmethod
    def of(__a0: object, __a1: object) -> java.util.Set: ...

    @overload
    @staticmethod
    def of(__a0: object, __a1: object, __a2: object) -> java.util.Set: ...

    @overload
    @staticmethod
    def of(__a0: object, __a1: object, __a2: object, __a3: object) -> java.util.Set: ...

    @overload
    @staticmethod
    def of(__a0: object, __a1: object, __a2: object, __a3: object, __a4: object) -> java.util.Set: ...

    @overload
    @staticmethod
    def of(__a0: object, __a1: object, __a2: object, __a3: object, __a4: object, __a5: object) -> java.util.Set: ...

    @overload
    @staticmethod
    def of(__a0: object, __a1: object, __a2: object, __a3: object, __a4: object, __a5: object, __a6: object) -> java.util.Set: ...

    @overload
    @staticmethod
    def of(__a0: object, __a1: object, __a2: object, __a3: object, __a4: object, __a5: object, __a6: object, __a7: object) -> java.util.Set: ...

    @overload
    @staticmethod
    def of(__a0: object, __a1: object, __a2: object, __a3: object, __a4: object, __a5: object, __a6: object, __a7: object, __a8: object) -> java.util.Set: ...

    @overload
    @staticmethod
    def of(__a0: object, __a1: object, __a2: object, __a3: object, __a4: object, __a5: object, __a6: object, __a7: object, __a8: object, __a9: object) -> java.util.Set: ...

    def parallelStream(self) -> java.util.stream.Stream: ...

    def removeAll(self, __a0: java.util.Collection) -> bool: ...

    def removeIf(self, __a0: java.util.function.Predicate) -> bool: ...

    def retainAll(self, __a0: java.util.Collection) -> bool: ...

    @staticmethod
    def singleton(rc: ghidra.app.plugin.assembler.sleigh.sem.AssemblyResolvedConstructor) -> ghidra.app.plugin.assembler.sleigh.sem.AssemblyResolutionResults:
        """
        Construct an immutable single-entry set consisting of the one given resolution
        @param rc the single resolution entry
        @return the new resolution set
        """
        ...

    def size(self) -> int: ...

    def spliterator(self) -> java.util.Spliterator: ...

    def stream(self) -> java.util.stream.Stream: ...

    @overload
    def toArray(self) -> List[object]: ...

    @overload
    def toArray(self, __a0: List[object]) -> List[object]: ...

    @overload
    def toArray(self, __a0: java.util.function.IntFunction) -> List[object]: ...

    def toString(self) -> unicode: ...

    @overload
    def wait(self) -> None: ...

    @overload
    def wait(self, __a0: long) -> None: ...

    @overload
    def wait(self, __a0: long, __a1: int) -> None: ...

    @property
    def resolutions(self) -> java.util.Set: ...
