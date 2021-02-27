from typing import Iterator
from typing import List
import ghidra.program.model.address
import ghidra.program.model.listing
import ghidra.program.util
import java.lang
import java.util
import java.util.function


class DefinedDataIterator(object, ghidra.program.model.listing.DataIterator):
    """
    Iterator that visits each defined data instance in the initialized memory of a Program or in the footprint of
     a specified data element.

     Data elements that are nested inside of composites or arrays are visited, not just the
     parent/containing data element.
    """

    EMPTY: ghidra.program.model.listing.DataIterator = ghidra.program.model.listing.DataIterator$IteratorWrapper@5433d286





    def __iter__(self) -> Iterator[ghidra.program.model.listing.Data]: ...

    @staticmethod
    def byDataInstance(program: ghidra.program.model.listing.Program, dataInstancePredicate: java.util.function.Predicate) -> ghidra.program.util.DefinedDataIterator:
        """
        Creates a new iterator that traverses the entire Program's address space, returning
         data instances that successfully match the predicate.
        @param program Program to search
        @param dataInstancePredicate {@link Predicate} that tests each data instance's properties
        @return new iterator
        """
        ...

    @staticmethod
    def byDataType(program: ghidra.program.model.listing.Program, dataTypePredicate: java.util.function.Predicate) -> ghidra.program.util.DefinedDataIterator:
        """
        Creates a new iterator that traverses the entire Program's address space, returning
         data instances that successfully match the predicate.
        @param program Program to search
        @param dataTypePredicate {@link Predicate} that tests each data instance's {@link DataType}
        @return new iterator
        """
        ...

    @overload
    @staticmethod
    def definedStrings(singleDataInstance: ghidra.program.model.listing.Data) -> ghidra.program.util.DefinedDataIterator:
        """
        Creates a new iterator that traverses the address space of a single data item (ie. a
         composite or array data instance that needs to be recursed into).
        @param singleDataInstance Data instance
        @return new iterator
        """
        ...

    @overload
    @staticmethod
    def definedStrings(program: ghidra.program.model.listing.Program) -> ghidra.program.util.DefinedDataIterator:
        """
        Creates a new iterator that traverses the entire Program's address space returning
         data instances that are strings.
        @param program Ghidra {@link Program} to search
        @return new iterator
        """
        ...

    @overload
    @staticmethod
    def definedStrings(program: ghidra.program.model.listing.Program, addrs: ghidra.program.model.address.AddressSetView) -> ghidra.program.util.DefinedDataIterator:
        """
        Creates a new iterator that traverses a portion of the Program's address space returning
         data instances that are strings.
        @param program Ghidra {@link Program} to search
        @param addrs addresses to limit the iteration to
        @return new iterator
        """
        ...

    def equals(self, __a0: object) -> bool: ...

    def forEach(self, __a0: java.util.function.Consumer) -> None: ...

    def forEachRemaining(self, __a0: java.util.function.Consumer) -> None: ...

    def getClass(self) -> java.lang.Class: ...

    def hasNext(self) -> bool: ...

    def hashCode(self) -> int: ...

    def iterator(self) -> java.util.Iterator: ...

    def next(self) -> ghidra.program.model.listing.Data: ...

    def notify(self) -> None: ...

    def notifyAll(self) -> None: ...

    @staticmethod
    def of(__a0: List[ghidra.program.model.listing.Data]) -> ghidra.program.model.listing.DataIterator: ...

    def remove(self) -> None: ...

    def spliterator(self) -> java.util.Spliterator: ...

    def toString(self) -> unicode: ...

    @overload
    def wait(self) -> None: ...

    @overload
    def wait(self, __a0: long) -> None: ...

    @overload
    def wait(self, __a0: long, __a1: int) -> None: ...
