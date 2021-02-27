from typing import Iterator
from typing import List
import ghidra.program.model.address
import ghidra.program.model.listing
import java.lang
import java.util
import java.util.function


class ProgramFragment(ghidra.program.model.listing.Group, ghidra.program.model.address.AddressSetView, object):
    """
    A ProgramFragment is a set of CodeUnits that have been
     bundled together with some additional information such as a name, comment,
     alias, etc. Every code unit in the program is in one and only one fragment
     so the fragments form a partition of the program. Fragments in turn are the
     building blocks of ProgramModules. Program fragments and modules
     allow the user to overlay a hierarchical structure upon the program which can then
     be used to control viewing and navigating the program.
    """







    def __iter__(self): ...

    @overload
    def contains(self, __a0: ghidra.program.model.address.Address) -> bool: ...

    @overload
    def contains(self, __a0: ghidra.program.model.address.AddressSetView) -> bool: ...

    @overload
    def contains(self, codeUnit: ghidra.program.model.listing.CodeUnit) -> bool:
        """
        Returns whether this fragment contains the given code unit.<P>
        @param codeUnit the code unit being tested.
        @return true if the code unit is in the fragment, false otherwise.
        """
        ...

    @overload
    def contains(self, __a0: ghidra.program.model.address.Address, __a1: ghidra.program.model.address.Address) -> bool: ...

    def equals(self, __a0: object) -> bool: ...

    def findFirstAddressInCommon(self, __a0: ghidra.program.model.address.AddressSetView) -> ghidra.program.model.address.Address: ...

    def forEach(self, __a0: java.util.function.Consumer) -> None: ...

    @overload
    def getAddressRanges(self) -> ghidra.program.model.address.AddressRangeIterator: ...

    @overload
    def getAddressRanges(self, __a0: bool) -> ghidra.program.model.address.AddressRangeIterator: ...

    @overload
    def getAddressRanges(self, __a0: ghidra.program.model.address.Address, __a1: bool) -> ghidra.program.model.address.AddressRangeIterator: ...

    @overload
    def getAddresses(self, __a0: bool) -> ghidra.program.model.address.AddressIterator: ...

    @overload
    def getAddresses(self, __a0: ghidra.program.model.address.Address, __a1: bool) -> ghidra.program.model.address.AddressIterator: ...

    def getClass(self) -> java.lang.Class: ...

    def getCodeUnits(self) -> ghidra.program.model.listing.CodeUnitIterator:
        """
        Returns a forward iterator over the code units making up this fragment.
        """
        ...

    def getComment(self) -> unicode: ...

    def getFirstRange(self) -> ghidra.program.model.address.AddressRange: ...

    def getLastRange(self) -> ghidra.program.model.address.AddressRange: ...

    def getMaxAddress(self) -> ghidra.program.model.address.Address: ...

    def getMinAddress(self) -> ghidra.program.model.address.Address: ...

    def getName(self) -> unicode: ...

    def getNumAddressRanges(self) -> int: ...

    def getNumAddresses(self) -> long: ...

    def getNumParents(self) -> int: ...

    def getParentNames(self) -> List[unicode]: ...

    def getParents(self) -> List[ghidra.program.model.listing.ProgramModule]: ...

    def getRangeContaining(self, __a0: ghidra.program.model.address.Address) -> ghidra.program.model.address.AddressRange: ...

    def getTreeName(self) -> unicode: ...

    def hasSameAddresses(self, __a0: ghidra.program.model.address.AddressSetView) -> bool: ...

    def hashCode(self) -> int: ...

    def intersect(self, __a0: ghidra.program.model.address.AddressSetView) -> ghidra.program.model.address.AddressSet: ...

    def intersectRange(self, __a0: ghidra.program.model.address.Address, __a1: ghidra.program.model.address.Address) -> ghidra.program.model.address.AddressSet: ...

    @overload
    def intersects(self, __a0: ghidra.program.model.address.AddressSetView) -> bool: ...

    @overload
    def intersects(self, __a0: ghidra.program.model.address.Address, __a1: ghidra.program.model.address.Address) -> bool: ...

    def isEmpty(self) -> bool: ...

    @overload
    def iterator(self) -> java.util.Iterator: ...

    @overload
    def iterator(self, __a0: bool) -> java.util.Iterator: ...

    @overload
    def iterator(self, __a0: ghidra.program.model.address.Address, __a1: bool) -> java.util.Iterator: ...

    def move(self, min: ghidra.program.model.address.Address, max: ghidra.program.model.address.Address) -> None:
        """
        Moves all of the code units in a given range into this fragment.
         Note that <CODE>min</CODE> must the starting address of a code unit
         and <CODE>max</CODE> must be the ending address of a code unit.
         Furthermore every address in the given range must exist in program
         memory.<P>
        @param min min address of range specifying the code units to move
        @param max max address of range specifying the code units to move
        @exception NotFoundException thrown if any address between <CODE>min</CODE>
         and <CODE>max</CODE> (inclusive) does not belong to program memory.
        """
        ...

    def notify(self) -> None: ...

    def notifyAll(self) -> None: ...

    def setComment(self, __a0: unicode) -> None: ...

    def setName(self, __a0: unicode) -> None: ...

    def spliterator(self) -> java.util.Spliterator: ...

    def subtract(self, __a0: ghidra.program.model.address.AddressSetView) -> ghidra.program.model.address.AddressSet: ...

    def toString(self) -> unicode: ...

    @staticmethod
    def trimEnd(__a0: ghidra.program.model.address.AddressSetView, __a1: ghidra.program.model.address.Address) -> ghidra.program.model.address.AddressSetView: ...

    @staticmethod
    def trimStart(__a0: ghidra.program.model.address.AddressSetView, __a1: ghidra.program.model.address.Address) -> ghidra.program.model.address.AddressSetView: ...

    def union(self, __a0: ghidra.program.model.address.AddressSetView) -> ghidra.program.model.address.AddressSet: ...

    @overload
    def wait(self) -> None: ...

    @overload
    def wait(self, __a0: long) -> None: ...

    @overload
    def wait(self, __a0: long, __a1: int) -> None: ...

    def xor(self, __a0: ghidra.program.model.address.AddressSetView) -> ghidra.program.model.address.AddressSet: ...

    @property
    def addressRanges(self) -> ghidra.program.model.address.AddressRangeIterator: ...

    @property
    def codeUnits(self) -> ghidra.program.model.listing.CodeUnitIterator: ...

    @property
    def comment(self) -> unicode: ...

    @comment.setter
    def comment(self, value: unicode) -> None: ...

    @property
    def empty(self) -> bool: ...

    @property
    def firstRange(self) -> ghidra.program.model.address.AddressRange: ...

    @property
    def lastRange(self) -> ghidra.program.model.address.AddressRange: ...

    @property
    def maxAddress(self) -> ghidra.program.model.address.Address: ...

    @property
    def minAddress(self) -> ghidra.program.model.address.Address: ...

    @property
    def name(self) -> unicode: ...

    @name.setter
    def name(self, value: unicode) -> None: ...

    @property
    def numAddressRanges(self) -> int: ...

    @property
    def numAddresses(self) -> long: ...

    @property
    def numParents(self) -> int: ...

    @property
    def parentNames(self) -> List[unicode]: ...

    @property
    def parents(self) -> List[ghidra.program.model.listing.ProgramModule]: ...

    @property
    def treeName(self) -> unicode: ...