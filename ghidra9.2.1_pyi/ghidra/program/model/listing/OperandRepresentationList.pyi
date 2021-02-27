from typing import Iterator
from typing import List
import java.lang
import java.util
import java.util.function
import java.util.stream


class OperandRepresentationList(java.util.ArrayList):
    """
    OperandRepresentation provides a list for operand sub-elements.
     The number of elements are expected to remain constant for a given code unit
     operand regardless of its format.

     The list may contain various Objects including any combination of Character,
     String, VariableOffset, Register, Address, Scalar, LabelString, and
     nesting of other OperandRepresentationList objects.

     All objects returned must support the toString() method for producing
     an appropriate listing representation.
    """







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

    def hasError(self) -> bool:
        """
        Returns true if the representation encountered an error.
         Error will be reflected within the representation as a String.
        """
        ...

    def hashCode(self) -> int: ...

    def indexOf(self, __a0: object) -> int: ...

    def isEmpty(self) -> bool: ...

    def isPrimaryReferenceHidden(self) -> bool:
        """
        Returns true if the primary reference is not reflected in the representation.
        """
        ...

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

    def toString(self) -> unicode:
        """
        Returns a formatted string representation of the specified code unit operand.
        @return formatted code unit representation
        """
        ...

    def trimToSize(self) -> None: ...

    @overload
    def wait(self) -> None: ...

    @overload
    def wait(self, __a0: long) -> None: ...

    @overload
    def wait(self, __a0: long, __a1: int) -> None: ...

    @property
    def primaryReferenceHidden(self) -> bool: ...
