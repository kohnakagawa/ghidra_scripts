from typing import Iterator
from typing import List
import ghidra.app.plugin.assembler.sleigh.grammars
import ghidra.app.plugin.assembler.sleigh.symbol
import java.lang
import java.util
import java.util.function
import java.util.stream


class AssemblyExtendedProduction(ghidra.app.plugin.assembler.sleigh.grammars.AbstractAssemblyProduction):
    """
    Defines a production of an "extended" grammar
    """





    def __init__(self, lhs: ghidra.app.plugin.assembler.sleigh.symbol.AssemblyExtendedNonTerminal, rhs: ghidra.app.plugin.assembler.sleigh.grammars.AssemblySentential, finalState: int, ancestor: ghidra.app.plugin.assembler.sleigh.grammars.AssemblyProduction):
        """
        Construct an extended production based on the given ancestor
        @param lhs the extended left-hand side
        @param rhs the extended right-hand side
        @param finalState the end state of the final symbol of the RHS
        @param ancestor the original production from which this extended production is derived
        """
        ...

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

    @overload
    def compareTo(self, that: ghidra.app.plugin.assembler.sleigh.grammars.AbstractAssemblyProduction) -> int: ...

    @overload
    def compareTo(self, __a0: object) -> int: ...

    def contains(self, __a0: object) -> bool: ...

    def containsAll(self, __a0: java.util.Collection) -> bool: ...

    @staticmethod
    def copyOf(__a0: java.util.Collection) -> List[object]: ...

    def equals(self, that: object) -> bool: ...

    def forEach(self, __a0: java.util.function.Consumer) -> None: ...

    def get(self, __a0: int) -> object: ...

    def getAncestor(self) -> ghidra.app.plugin.assembler.sleigh.grammars.AssemblyProduction:
        """
        Get the original production from which this production was derived
        @return the original production
        """
        ...

    def getClass(self) -> java.lang.Class: ...

    def getFinalState(self) -> int:
        """
        Get the final state of this production
        @return the end state of the last symbol of the RHS
        """
        ...

    def getIndex(self) -> int:
        """
        Get the index of the production

         Instead of using deep comparison, the index is often used as the identify of the production
         within a grammar.
        @return the index
        """
        ...

    def getLHS(self) -> ghidra.app.plugin.assembler.sleigh.symbol.AssemblyExtendedNonTerminal: ...

    def getName(self) -> unicode:
        """
        Get the "name" of this production

         This is mostly just notional and for debugging. The name is taken as the name of the LHS.
        @return the name of the LHS
        """
        ...

    def getRHS(self) -> ghidra.app.plugin.assembler.sleigh.grammars.AssemblySentential:
        """
        Get the right-hand side
        @return the RHS
        """
        ...

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

    def subList(self, fromIndex: int, toIndex: int) -> ghidra.app.plugin.assembler.sleigh.grammars.AssemblySentential: ...

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
    def LHS(self) -> ghidra.app.plugin.assembler.sleigh.symbol.AssemblyExtendedNonTerminal: ...

    @property
    def ancestor(self) -> ghidra.app.plugin.assembler.sleigh.grammars.AssemblyProduction: ...

    @property
    def finalState(self) -> int: ...
