from typing import Iterator
from typing import List
import ghidra.program.model.address
import ghidra.program.model.block
import ghidra.program.model.listing
import ghidra.program.model.symbol
import ghidra.util.task
import java.lang
import java.util
import java.util.function


class ExtCodeBlockImpl(ghidra.program.model.address.AddressSet, ghidra.program.model.block.CodeBlock):




    def __init__(self, model: ghidra.program.model.block.CodeBlockModel, extAddr: ghidra.program.model.address.Address): ...

    def __iter__(self): ...

    @overload
    def add(self, address: ghidra.program.model.address.Address) -> None:
        """
        Adds the given address to this set.
        @param address the address to add
        """
        ...

    @overload
    def add(self, range: ghidra.program.model.address.AddressRange) -> None:
        """
        Add an address range to this set.
        @param range the range to add.
        """
        ...

    @overload
    def add(self, addressSet: ghidra.program.model.address.AddressSetView) -> None:
        """
        Add all addresses of the given AddressSet to this set.
        @param addressSet set of addresses to add.
        """
        ...

    @overload
    def add(self, start: ghidra.program.model.address.Address, end: ghidra.program.model.address.Address) -> None:
        """
        Adds the range to this set
        @param start the start address of the range to add
        @param end the end address of the range to add
        """
        ...

    @overload
    def addRange(self, start: ghidra.program.model.address.Address, end: ghidra.program.model.address.Address) -> None:
        """
        Adds the range to this set
        @param start the start address of the range to add
        @param end the end address of the range to add
        @throws IllegalArgumentException if the start and end addresses are in different spaces.  To
         avoid this, use the constructor  {@link #addRange(Program, Address, Address)}
        """
        ...

    @overload
    def addRange(self, program: ghidra.program.model.listing.Program, start: ghidra.program.model.address.Address, end: ghidra.program.model.address.Address) -> None:
        """
        Adds a range of addresses to this set.
        @param program program whose AddressFactory is used to resolve address ranges that span
         multiple address spaces.
        @param start the start address of the range to add
        @param end the end address of the range to add
        """
        ...

    def clear(self) -> None:
        """
        Removes all addresses from the set.
        """
        ...

    @overload
    def contains(self, address: ghidra.program.model.address.Address) -> bool: ...

    @overload
    def contains(self, addrSet: ghidra.program.model.address.AddressSetView) -> bool: ...

    @overload
    def contains(self, start: ghidra.program.model.address.Address, end: ghidra.program.model.address.Address) -> bool: ...

    @overload
    def delete(self, range: ghidra.program.model.address.AddressRange) -> None:
        """
        Deletes an address range from this set.
        @param range AddressRange to remove from this set
        """
        ...

    @overload
    def delete(self, addressSet: ghidra.program.model.address.AddressSetView) -> None:
        """
        Delete all addresses in the given AddressSet from this set.
        @param addressSet set of addresses to remove from this set.
        """
        ...

    @overload
    def delete(self, start: ghidra.program.model.address.Address, end: ghidra.program.model.address.Address) -> None:
        """
        Deletes a range of addresses from this set
        @param start the starting address of the range to be removed
        @param end the ending address of the range to be removed (inclusive)
        """
        ...

    def deleteRange(self, start: ghidra.program.model.address.Address, end: ghidra.program.model.address.Address) -> None:
        """
        Deletes a range of addresses from this set
        @param start the starting address of the range to be removed
        @param end the ending address of the range to be removed
        """
        ...

    def equals(self, obj: object) -> bool: ...

    def findFirstAddressInCommon(self, set: ghidra.program.model.address.AddressSetView) -> ghidra.program.model.address.Address: ...

    def forEach(self, __a0: java.util.function.Consumer) -> None: ...

    @overload
    def getAddressRanges(self) -> ghidra.program.model.address.AddressRangeIterator: ...

    @overload
    def getAddressRanges(self, forward: bool) -> ghidra.program.model.address.AddressRangeIterator: ...

    @overload
    def getAddressRanges(self, start: ghidra.program.model.address.Address, forward: bool) -> ghidra.program.model.address.AddressRangeIterator: ...

    @overload
    def getAddresses(self, forward: bool) -> ghidra.program.model.address.AddressIterator: ...

    @overload
    def getAddresses(self, start: ghidra.program.model.address.Address, forward: bool) -> ghidra.program.model.address.AddressIterator: ...

    def getClass(self) -> java.lang.Class: ...

    def getDestinations(self, monitor: ghidra.util.task.TaskMonitor) -> ghidra.program.model.block.CodeBlockReferenceIterator: ...

    def getFirstRange(self) -> ghidra.program.model.address.AddressRange: ...

    def getFirstStartAddress(self) -> ghidra.program.model.address.Address: ...

    def getFlowType(self) -> ghidra.program.model.symbol.FlowType: ...

    def getLastRange(self) -> ghidra.program.model.address.AddressRange: ...

    def getMaxAddress(self) -> ghidra.program.model.address.Address: ...

    def getMinAddress(self) -> ghidra.program.model.address.Address: ...

    def getModel(self) -> ghidra.program.model.block.CodeBlockModel: ...

    def getName(self) -> unicode: ...

    def getNumAddressRanges(self) -> int: ...

    def getNumAddresses(self) -> long: ...

    def getNumDestinations(self, monitor: ghidra.util.task.TaskMonitor) -> int: ...

    def getNumSources(self, monitor: ghidra.util.task.TaskMonitor) -> int: ...

    def getRangeContaining(self, address: ghidra.program.model.address.Address) -> ghidra.program.model.address.AddressRange: ...

    def getSources(self, monitor: ghidra.util.task.TaskMonitor) -> ghidra.program.model.block.CodeBlockReferenceIterator: ...

    def getStartAddresses(self) -> List[ghidra.program.model.address.Address]: ...

    def hasSameAddresses(self, addrSet: ghidra.program.model.address.AddressSetView) -> bool: ...

    def hashCode(self) -> int:
        """
        @see java.lang.Object#hashCode()
        """
        ...

    def intersect(self, addrSet: ghidra.program.model.address.AddressSetView) -> ghidra.program.model.address.AddressSet: ...

    def intersectRange(self, start: ghidra.program.model.address.Address, end: ghidra.program.model.address.Address) -> ghidra.program.model.address.AddressSet: ...

    @overload
    def intersects(self, addrSet: ghidra.program.model.address.AddressSetView) -> bool: ...

    @overload
    def intersects(self, start: ghidra.program.model.address.Address, end: ghidra.program.model.address.Address) -> bool: ...

    def isEmpty(self) -> bool: ...

    @overload
    def iterator(self) -> Iterator[ghidra.program.model.address.AddressRange]: ...

    @overload
    def iterator(self, forward: bool) -> Iterator[ghidra.program.model.address.AddressRange]: ...

    @overload
    def iterator(self, start: ghidra.program.model.address.Address, forward: bool) -> Iterator[ghidra.program.model.address.AddressRange]: ...

    def notify(self) -> None: ...

    def notifyAll(self) -> None: ...

    def printRanges(self) -> unicode:
        """
        Returns a string displaying the ranges in this set.
        @return a string displaying the ranges in this set.
        """
        ...

    def spliterator(self) -> java.util.Spliterator: ...

    def subtract(self, addrSet: ghidra.program.model.address.AddressSetView) -> ghidra.program.model.address.AddressSet: ...

    def toList(self) -> List[ghidra.program.model.address.AddressRange]:
        """
        Returns a list of the AddressRanges in this set.
        @return a list of the AddressRanges in this set.
        """
        ...

    def toString(self) -> unicode: ...

    @staticmethod
    def trimEnd(__a0: ghidra.program.model.address.AddressSetView, __a1: ghidra.program.model.address.Address) -> ghidra.program.model.address.AddressSetView: ...

    @staticmethod
    def trimStart(__a0: ghidra.program.model.address.AddressSetView, __a1: ghidra.program.model.address.Address) -> ghidra.program.model.address.AddressSetView: ...

    def union(self, addrSet: ghidra.program.model.address.AddressSetView) -> ghidra.program.model.address.AddressSet: ...

    @overload
    def wait(self) -> None: ...

    @overload
    def wait(self, __a0: long) -> None: ...

    @overload
    def wait(self, __a0: long, __a1: int) -> None: ...

    def xor(self, addrSet: ghidra.program.model.address.AddressSetView) -> ghidra.program.model.address.AddressSet: ...

    @property
    def firstStartAddress(self) -> ghidra.program.model.address.Address: ...

    @property
    def flowType(self) -> ghidra.program.model.symbol.FlowType: ...

    @property
    def model(self) -> ghidra.program.model.block.CodeBlockModel: ...

    @property
    def name(self) -> unicode: ...

    @property
    def startAddresses(self) -> List[ghidra.program.model.address.Address]: ...
