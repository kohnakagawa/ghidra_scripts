from typing import Iterator
from typing import List
import ghidra.program.model.address
import ghidra.program.model.block
import ghidra.program.model.symbol
import ghidra.util.task
import java.lang
import java.util
import java.util.function


class CodeBlockImpl(object, ghidra.program.model.block.CodeBlock):
    """
    CodeBlockImpl is an implementation of a CodeBlock.
     These are produced by a particular CodeBlockModel and are associated
     with only that model.  Most methods simply delegate any work that
     is specific to a particular CodeBlockModel to that model.
    """





    def __init__(self, model: ghidra.program.model.block.CodeBlockModel, starts: List[ghidra.program.model.address.Address], body: ghidra.program.model.address.AddressSetView):
        """
        Construct a multi-entry CodeBlock associated with a CodeBlockModel. The
         significance of the start Addresses is model dependent.
        @param model the model instance which produced this block.
        @param starts the entry points for the block. Any of these addresses may
         be used to identify this block within the model that produced it.
        @param body the address set which makes-up the body of this block.
        """
        ...

    def __iter__(self): ...

    @overload
    def contains(self, a: ghidra.program.model.address.Address) -> bool:
        """
        @see ghidra.program.model.address.AddressSetView#contains(ghidra.program.model.address.Address)
        """
        ...

    @overload
    def contains(self, rangeSet: ghidra.program.model.address.AddressSetView) -> bool:
        """
        @see ghidra.program.model.address.AddressSetView#contains(ghidra.program.model.address.AddressSetView)
        """
        ...

    @overload
    def contains(self, start: ghidra.program.model.address.Address, end: ghidra.program.model.address.Address) -> bool:
        """
        @see ghidra.program.model.address.AddressSetView#contains(ghidra.program.model.address.Address, ghidra.program.model.address.Address)
        """
        ...

    def equals(self, obj: object) -> bool:
        """
        @see java.lang.Object#equals(java.lang.Object)
        """
        ...

    def findFirstAddressInCommon(self, otherSet: ghidra.program.model.address.AddressSetView) -> ghidra.program.model.address.Address: ...

    def forEach(self, __a0: java.util.function.Consumer) -> None: ...

    @overload
    def getAddressRanges(self) -> ghidra.program.model.address.AddressRangeIterator:
        """
        @see ghidra.program.model.address.AddressSetView#getAddressRanges()
        """
        ...

    @overload
    def getAddressRanges(self, startAtFront: bool) -> ghidra.program.model.address.AddressRangeIterator:
        """
        @see ghidra.program.model.address.AddressSetView#getAddressRanges(boolean)
        """
        ...

    @overload
    def getAddressRanges(self, start: ghidra.program.model.address.Address, forward: bool) -> ghidra.program.model.address.AddressRangeIterator: ...

    @overload
    def getAddresses(self, forward: bool) -> ghidra.program.model.address.AddressIterator:
        """
        @see ghidra.program.model.address.AddressSetView#getAddresses(boolean)
        """
        ...

    @overload
    def getAddresses(self, start: ghidra.program.model.address.Address, forward: bool) -> ghidra.program.model.address.AddressIterator:
        """
        @see ghidra.program.model.address.AddressSetView#getAddresses(ghidra.program.model.address.Address, boolean)
        """
        ...

    def getClass(self) -> java.lang.Class: ...

    def getDestinations(self, monitor: ghidra.util.task.TaskMonitor) -> ghidra.program.model.block.CodeBlockReferenceIterator:
        """
        @see ghidra.program.model.block.CodeBlock#getDestinations(ghidra.util.task.TaskMonitor)
        """
        ...

    def getFirstRange(self) -> ghidra.program.model.address.AddressRange: ...

    def getFirstStartAddress(self) -> ghidra.program.model.address.Address:
        """
        @see ghidra.program.model.block.CodeBlock#getFirstStartAddress()
        """
        ...

    def getFlowType(self) -> ghidra.program.model.symbol.FlowType:
        """
        @see ghidra.program.model.block.CodeBlock#getFlowType()
        """
        ...

    def getLastRange(self) -> ghidra.program.model.address.AddressRange: ...

    def getMaxAddress(self) -> ghidra.program.model.address.Address:
        """
        @see ghidra.program.model.address.AddressSetView#getMaxAddress()
        """
        ...

    def getMinAddress(self) -> ghidra.program.model.address.Address:
        """
        @see ghidra.program.model.address.AddressSetView#getMinAddress()
        """
        ...

    def getModel(self) -> ghidra.program.model.block.CodeBlockModel:
        """
        @see ghidra.program.model.block.CodeBlock#getModel()
        """
        ...

    def getName(self) -> unicode:
        """
        @see ghidra.program.model.block.CodeBlock#getName()
        """
        ...

    def getNumAddressRanges(self) -> int:
        """
        @see ghidra.program.model.address.AddressSetView#getNumAddressRanges()
        """
        ...

    def getNumAddresses(self) -> long:
        """
        @see ghidra.program.model.address.AddressSetView#getNumAddresses()
        """
        ...

    def getNumDestinations(self, monitor: ghidra.util.task.TaskMonitor) -> int:
        """
        @see ghidra.program.model.block.CodeBlock#getNumDestinations(ghidra.util.task.TaskMonitor)
        """
        ...

    def getNumSources(self, monitor: ghidra.util.task.TaskMonitor) -> int:
        """
        @see ghidra.program.model.block.CodeBlock#getNumSources(ghidra.util.task.TaskMonitor)
        """
        ...

    def getRangeContaining(self, address: ghidra.program.model.address.Address) -> ghidra.program.model.address.AddressRange: ...

    def getSources(self, monitor: ghidra.util.task.TaskMonitor) -> ghidra.program.model.block.CodeBlockReferenceIterator:
        """
        @see ghidra.program.model.block.CodeBlock#getSources(ghidra.util.task.TaskMonitor)
        """
        ...

    def getStartAddresses(self) -> List[ghidra.program.model.address.Address]:
        """
        @see ghidra.program.model.block.CodeBlock#getStartAddresses()
        """
        ...

    def hasSameAddresses(self, view: ghidra.program.model.address.AddressSetView) -> bool:
        """
        @see ghidra.program.model.address.AddressSetView#hasSameAddresses(ghidra.program.model.address.AddressSetView)
        """
        ...

    def hashCode(self) -> int:
        """
        @see java.lang.Object#hashCode()
        """
        ...

    def intersect(self, view: ghidra.program.model.address.AddressSetView) -> ghidra.program.model.address.AddressSet:
        """
        @see ghidra.program.model.address.AddressSetView#intersect(ghidra.program.model.address.AddressSetView)
        """
        ...

    def intersectRange(self, start: ghidra.program.model.address.Address, end: ghidra.program.model.address.Address) -> ghidra.program.model.address.AddressSet:
        """
        @see ghidra.program.model.address.AddressSetView#intersectRange(ghidra.program.model.address.Address, ghidra.program.model.address.Address)
        """
        ...

    @overload
    def intersects(self, addrSet: ghidra.program.model.address.AddressSetView) -> bool:
        """
        @see ghidra.program.model.address.AddressSetView#intersects(ghidra.program.model.address.AddressSetView)
        """
        ...

    @overload
    def intersects(self, start: ghidra.program.model.address.Address, end: ghidra.program.model.address.Address) -> bool:
        """
        @see ghidra.program.model.address.AddressSetView#intersects(ghidra.program.model.address.Address, ghidra.program.model.address.Address)
        """
        ...

    def isEmpty(self) -> bool:
        """
        @see ghidra.program.model.address.AddressSetView#isEmpty()
        """
        ...

    @overload
    def iterator(self) -> Iterator[ghidra.program.model.address.AddressRange]: ...

    @overload
    def iterator(self, forward: bool) -> Iterator[ghidra.program.model.address.AddressRange]: ...

    @overload
    def iterator(self, start: ghidra.program.model.address.Address, forward: bool) -> Iterator[ghidra.program.model.address.AddressRange]: ...

    def notify(self) -> None: ...

    def notifyAll(self) -> None: ...

    def spliterator(self) -> java.util.Spliterator: ...

    def subtract(self, addrSet: ghidra.program.model.address.AddressSetView) -> ghidra.program.model.address.AddressSet:
        """
        @see ghidra.program.model.address.AddressSetView#subtract(ghidra.program.model.address.AddressSetView)
        """
        ...

    def toString(self) -> unicode:
        """
        @see java.lang.Object#toString()
        """
        ...

    @staticmethod
    def trimEnd(__a0: ghidra.program.model.address.AddressSetView, __a1: ghidra.program.model.address.Address) -> ghidra.program.model.address.AddressSetView: ...

    @staticmethod
    def trimStart(__a0: ghidra.program.model.address.AddressSetView, __a1: ghidra.program.model.address.Address) -> ghidra.program.model.address.AddressSetView: ...

    def union(self, addrSet: ghidra.program.model.address.AddressSetView) -> ghidra.program.model.address.AddressSet:
        """
        @see ghidra.program.model.address.AddressSetView#union(ghidra.program.model.address.AddressSetView)
        """
        ...

    @overload
    def wait(self) -> None: ...

    @overload
    def wait(self, __a0: long) -> None: ...

    @overload
    def wait(self, __a0: long, __a1: int) -> None: ...

    def xor(self, addrSet: ghidra.program.model.address.AddressSetView) -> ghidra.program.model.address.AddressSet:
        """
        @see ghidra.program.model.address.AddressSetView#xor(ghidra.program.model.address.AddressSetView)
        """
        ...

    @property
    def addressRanges(self) -> ghidra.program.model.address.AddressRangeIterator: ...

    @property
    def empty(self) -> bool: ...

    @property
    def firstRange(self) -> ghidra.program.model.address.AddressRange: ...

    @property
    def firstStartAddress(self) -> ghidra.program.model.address.Address: ...

    @property
    def flowType(self) -> ghidra.program.model.symbol.FlowType: ...

    @property
    def lastRange(self) -> ghidra.program.model.address.AddressRange: ...

    @property
    def maxAddress(self) -> ghidra.program.model.address.Address: ...

    @property
    def minAddress(self) -> ghidra.program.model.address.Address: ...

    @property
    def model(self) -> ghidra.program.model.block.CodeBlockModel: ...

    @property
    def name(self) -> unicode: ...

    @property
    def numAddressRanges(self) -> int: ...

    @property
    def numAddresses(self) -> long: ...

    @property
    def startAddresses(self) -> List[ghidra.program.model.address.Address]: ...
