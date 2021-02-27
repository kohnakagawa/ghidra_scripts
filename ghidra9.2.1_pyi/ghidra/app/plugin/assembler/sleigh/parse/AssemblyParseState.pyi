from typing import Iterator
from typing import List
import ghidra.app.plugin.assembler.sleigh.parse
import java.lang
import java.util
import java.util.function
import java.util.stream
import org.apache.commons.collections4.set


class AssemblyParseState(org.apache.commons.collections4.set.AbstractSetDecorator, java.lang.Comparable):
    """
    A state in an LR(0) parsing machine

     Each item consists of a kernel and an implied closure. Only the kernel is necessary to define
     the item, but the whole closure must be considered when deriving new states.
    """





    @overload
    def __init__(self, grammar: ghidra.app.plugin.assembler.sleigh.grammars.AssemblyGrammar):
        """
        Construct a new state associated with the given grammar
        @param grammar the grammar
        """
        ...

    @overload
    def __init__(self, grammar: ghidra.app.plugin.assembler.sleigh.grammars.AssemblyGrammar, item: ghidra.app.plugin.assembler.sleigh.parse.AssemblyParseStateItem):
        """
        Construct a new state associated with the given grammar, seeded with the given item
        @param grammar the grammar
        @param item an item in the state
        """
        ...

    def __iter__(self): ...

    def add(self, __a0: object) -> bool: ...

    def addAll(self, __a0: java.util.Collection) -> bool: ...

    def clear(self) -> None: ...

    @overload
    def compareTo(self, that: ghidra.app.plugin.assembler.sleigh.parse.AssemblyParseState) -> int: ...

    @overload
    def compareTo(self, __a0: object) -> int: ...

    def contains(self, __a0: object) -> bool: ...

    def containsAll(self, __a0: java.util.Collection) -> bool: ...

    @staticmethod
    def copyOf(__a0: java.util.Collection) -> java.util.Set: ...

    def equals(self, that: object) -> bool: ...

    def forEach(self, __a0: java.util.function.Consumer) -> None: ...

    def getClass(self) -> java.lang.Class: ...

    def getClosure(self) -> java.util.Set:
        """
        Get the closure of this item, caching the result
        @return the closure
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
    def closure(self) -> java.util.Set: ...
