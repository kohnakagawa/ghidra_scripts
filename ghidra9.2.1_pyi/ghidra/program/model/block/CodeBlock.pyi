from typing import Iterator
from typing import List
import ghidra.program.model.address
import ghidra.program.model.block
import ghidra.program.model.symbol
import ghidra.util.task
import java.lang
import java.util
import java.util.function


class CodeBlock(ghidra.program.model.address.AddressSetView, object):
    """
    CodeBlock represents some group of Instructions/Data.  Each block
     has some set of source blocks that flow into it and some
     set of destination blocks that flow out of it.  A BlockModel
     is used to produce CodeBlocks.  Each model produces blocks
     based on its interpretation of Instruction/Data grouping and flow
     between those groups.
    """







    def __iter__(self): ...

    @overload
    def contains(self, __a0: ghidra.program.model.address.Address) -> bool: ...

    @overload
    def contains(self, __a0: ghidra.program.model.address.AddressSetView) -> bool: ...

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

    def getDestinations(self, monitor: ghidra.util.task.TaskMonitor) -> ghidra.program.model.block.CodeBlockReferenceIterator:
        """
        Get an Iterator over the CodeBlocks that are flowed to from this
         CodeBlock.
        @param monitor task monitor which allows user to cancel operation.
        @return An iterator over CodeBlocks referred to by this Block.
        @throws CancelledException if the monitor cancels the operation.
        """
        ...

    def getFirstRange(self) -> ghidra.program.model.address.AddressRange: ...

    def getFirstStartAddress(self) -> ghidra.program.model.address.Address:
        """
        Return the first start address of the CodeBlock.
         Depending on the model used to generate the CodeBlock,
         there may be multiple entry points to the block.  This will
         return the first start address for the block.  It should
         always return the same address for a given block if there
         is more than one entry point.
        @return the first start address of the block.
        """
        ...

    def getFlowType(self) -> ghidra.program.model.symbol.FlowType:
        """
        Return, in theory, how things flow out of this node.
         If there are any abnormal ways to flow out of this node,
         (ie: jump, call, etc...) then the flow type of the node
         takes on that type.
         If there are multiple unique ways out of the node, then we
         should return FlowType.UNKNOWN.
         Fallthrough is returned if that is the only way out.
        @return flow type of this node
        """
        ...

    def getLastRange(self) -> ghidra.program.model.address.AddressRange: ...

    def getMaxAddress(self) -> ghidra.program.model.address.Address: ...

    def getMinAddress(self) -> ghidra.program.model.address.Address: ...

    def getModel(self) -> ghidra.program.model.block.CodeBlockModel:
        """
        Get the model instance which was used to generate this block.
        @return the model used to build this CodeBlock
        """
        ...

    def getName(self) -> unicode:
        """
        Return the name of the block.
        @return name of block,
          normally the symbol at the starting address
        """
        ...

    def getNumAddressRanges(self) -> int: ...

    def getNumAddresses(self) -> long: ...

    def getNumDestinations(self, monitor: ghidra.util.task.TaskMonitor) -> int:
        """
        Get the number of CodeBlocks this block flows to.
         Note that this is almost as much work as getting the actual destination references.
        @param monitor task monitor which allows user to cancel operation.
        @return number of destination CodeBlocks.
        @throws CancelledException if the monitor cancels the operation.
        @see #getDestinations(ghidra.util.task.TaskMonitor)
        """
        ...

    def getNumSources(self, monitor: ghidra.util.task.TaskMonitor) -> int:
        """
        Get the number of CodeBlocks that flow into this CodeBlock.
         Note that this is almost as much work as getting the actual source references.
        @param monitor task monitor which allows user to cancel operation.
        @return number of source CodeBlocks.
        @throws CancelledException if the monitor cancels the operation.
        @see #getSources(ghidra.util.task.TaskMonitor)
        """
        ...

    def getRangeContaining(self, __a0: ghidra.program.model.address.Address) -> ghidra.program.model.address.AddressRange: ...

    def getSources(self, monitor: ghidra.util.task.TaskMonitor) -> ghidra.program.model.block.CodeBlockReferenceIterator:
        """
        Get an Iterator over the CodeBlocks that flow into this CodeBlock.
        @param monitor task monitor which allows user to cancel operation.
        @return An iterator over CodeBlocks referencing this Block.
        @throws CancelledException if the monitor cancels the operation.
        """
        ...

    def getStartAddresses(self) -> List[ghidra.program.model.address.Address]:
        """
        Get all the entry points to this block.  Depending on the
         model, there may be more than one entry point.
         Entry points will be returned in natural sorted order.
        @return an array of entry points to this block.
         a zero length array if there are no entry points.
        """
        ...

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

    def notify(self) -> None: ...

    def notifyAll(self) -> None: ...

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
