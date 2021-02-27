from typing import Iterator
from typing import List
import ghidra.app.plugin.match
import ghidra.program.model.address
import ghidra.program.model.listing
import java.lang
import java.util
import java.util.function
import java.util.stream


class FunctionMatchSet(java.util.ArrayList):
    aProgram: ghidra.program.model.listing.Program
    bProgram: ghidra.program.model.listing.Program



    def __init__(self, __a0: ghidra.program.model.listing.Program, __a1: ghidra.program.model.listing.Program): ...

    def __iter__(self): ...

    @overload
    def add(self, __a0: object) -> bool: ...

    @overload
    def add(self, __a0: int, __a1: object) -> None: ...

    @overload
    def addAll(self, __a0: java.util.Collection) -> bool: ...

    @overload
    def addAll(self, __a0: int, __a1: java.util.Collection) -> bool: ...

    def clear(self) -> None: ...

    def clone(self) -> object: ...

    def contains(self, __a0: object) -> bool: ...

    def containsAll(self, __a0: java.util.Collection) -> bool: ...

    @staticmethod
    def copyOf(__a0: java.util.Collection) -> List[object]: ...

    def ensureCapacity(self, __a0: int) -> None: ...

    def equals(self, __a0: object) -> bool: ...

    def forEach(self, __a0: java.util.function.Consumer) -> None: ...

    def get(self, __a0: int) -> object: ...

    def getClass(self) -> java.lang.Class: ...

    @overload
    def getLength(self, __a0: ghidra.program.model.address.Address) -> int: ...

    @overload
    def getLength(self, __a0: ghidra.program.model.address.Address, __a1: ghidra.program.model.listing.Program) -> int: ...

    def getMatches(self) -> List[ghidra.app.plugin.match.SubroutineMatch]: ...

    def hashCode(self) -> int: ...

    def indexOf(self, __a0: object) -> int: ...

    def isEmpty(self) -> bool: ...

    def iterator(self) -> java.util.Iterator: ...

    def lastIndexOf(self, __a0: object) -> int: ...

    @overload
    def listIterator(self) -> java.util.ListIterator: ...

    @overload
    def listIterator(self, __a0: int) -> java.util.ListIterator: ...

    def notify(self) -> None: ...

    def notifyAll(self) -> None: ...

    @overload
    @staticmethod
    def of() -> List[object]: ...

    @overload
    @staticmethod
    def of(__a0: List[object]) -> List[object]: ...

    @overload
    @staticmethod
    def of(__a0: object) -> List[object]: ...

    @overload
    @staticmethod
    def of(__a0: object, __a1: object) -> List[object]: ...

    @overload
    @staticmethod
    def of(__a0: object, __a1: object, __a2: object) -> List[object]: ...

    @overload
    @staticmethod
    def of(__a0: object, __a1: object, __a2: object, __a3: object) -> List[object]: ...

    @overload
    @staticmethod
    def of(__a0: object, __a1: object, __a2: object, __a3: object, __a4: object) -> List[object]: ...

    @overload
    @staticmethod
    def of(__a0: object, __a1: object, __a2: object, __a3: object, __a4: object, __a5: object) -> List[object]: ...

    @overload
    @staticmethod
    def of(__a0: object, __a1: object, __a2: object, __a3: object, __a4: object, __a5: object, __a6: object) -> List[object]: ...

    @overload
    @staticmethod
    def of(__a0: object, __a1: object, __a2: object, __a3: object, __a4: object, __a5: object, __a6: object, __a7: object) -> List[object]: ...

    @overload
    @staticmethod
    def of(__a0: object, __a1: object, __a2: object, __a3: object, __a4: object, __a5: object, __a6: object, __a7: object, __a8: object) -> List[object]: ...

    @overload
    @staticmethod
    def of(__a0: object, __a1: object, __a2: object, __a3: object, __a4: object, __a5: object, __a6: object, __a7: object, __a8: object, __a9: object) -> List[object]: ...

    def parallelStream(self) -> java.util.stream.Stream: ...

    def removeAll(self, __a0: java.util.Collection) -> bool: ...

    def removeIf(self, __a0: java.util.function.Predicate) -> bool: ...

    def replaceAll(self, __a0: java.util.function.UnaryOperator) -> None: ...

    def retainAll(self, __a0: java.util.Collection) -> bool: ...

    def set(self, __a0: int, __a1: object) -> object: ...

    def size(self) -> int: ...

    def spliterator(self) -> java.util.Spliterator: ...

    def stream(self) -> java.util.stream.Stream: ...

    def subList(self, __a0: int, __a1: int) -> List[object]: ...

    @overload
    def toArray(self) -> List[object]: ...

    @overload
    def toArray(self, __a0: List[object]) -> List[object]: ...

    @overload
    def toArray(self, __a0: java.util.function.IntFunction) -> List[object]: ...

    def toString(self) -> unicode: ...

    def trimToSize(self) -> None: ...

    @overload
    def wait(self) -> None: ...

    @overload
    def wait(self, __a0: long) -> None: ...

    @overload
    def wait(self, __a0: long, __a1: int) -> None: ...

    @property
    def matches(self) -> List[ghidra.app.plugin.match.SubroutineMatch]: ...