from typing import Iterator
from typing import List
import ghidra.program.model.address
import ghidra.program.model.lang
import ghidra.program.model.listing
import java.lang
import java.util
import java.util.function


class InstructionSet(object, java.lang.Iterable):
    """
    A set of instructions organized as a graph of basic blocks.
    """





    def __init__(self, addrFactory: ghidra.program.model.address.AddressFactory): ...

    def __iter__(self): ...

    def addBlock(self, block: ghidra.program.model.lang.InstructionBlock) -> None:
        """
        Add an Instruction block to this Instruction Set.
         If the block is empty it will only be added to the empty-list and will not
         be added to the maps or block iterator
        @param block the block to add.
        """
        ...

    def containsBlockAt(self, blockAddr: ghidra.program.model.address.Address) -> bool: ...

    def emptyBlockIterator(self) -> Iterator[ghidra.program.model.lang.InstructionBlock]:
        """
        Returns an iterator over all empty blocks which likely contain a conflict error.
        @return empty block iterator
        """
        ...

    def equals(self, __a0: object) -> bool: ...

    def findFirstIntersectingBlock(self, min: ghidra.program.model.address.Address, max: ghidra.program.model.address.Address) -> ghidra.program.model.lang.InstructionBlock:
        """
        Find the first block within this InstructionSet which intersects the specified range.
         This method should be used sparingly since it uses a brute-force search.
        @param min the minimum intersection address
        @param max the maximum intersection address
        @return block within this InstructionSet which intersects the specified range or null
         if not found
        """
        ...

    def forEach(self, __a0: java.util.function.Consumer) -> None: ...

    def getAddressSet(self) -> ghidra.program.model.address.AddressSetView:
        """
        Returns the address set that makes up all the instructions contained in this set.
        @return the address set that makes up all the instructions contained in this set.
        """
        ...

    def getClass(self) -> java.lang.Class: ...

    def getConflicts(self) -> List[ghidra.program.model.lang.InstructionError]:
        """
        Returns a list of conflicts for this set.  If a block is not reachable from a non-conflicted
         block, it's conflicts(if any) will not be included.
        @return the list of conflicts for this set.
        """
        ...

    def getInstructionAt(self, address: ghidra.program.model.address.Address) -> ghidra.program.model.listing.Instruction:
        """
        Returns the instruction at the specified address within this instruction set
        @param address
        @return instruction at the specified address within this instruction set or null if not found
        """
        ...

    def getInstructionBlockContaining(self, address: ghidra.program.model.address.Address) -> ghidra.program.model.lang.InstructionBlock:
        """
        Returns the non-empty InstructionBlock containing the specified address
        @param address
        @return the InstructionBlock containing the specified address or null if not found
        """
        ...

    def getInstructionCount(self) -> int:
        """
        Returns the number of instructions in this instruction set.
        @return the number of instructions in this instruction set.
        """
        ...

    def getMinAddress(self) -> ghidra.program.model.address.Address:
        """
        Returns the minimum address for this Instruction set;
        @return the minimum address for this Instruction set;
        """
        ...

    def hashCode(self) -> int: ...

    def intersects(self, minAddress: ghidra.program.model.address.Address, maxAddress: ghidra.program.model.address.Address) -> bool:
        """
        Returns true if this instruction set intersects the specified range
        @param minAddress
        @param maxAddress
        @return true if this instruction set intersects the specified range
        """
        ...

    def iterator(self) -> Iterator[ghidra.program.model.lang.InstructionBlock]:
        """
        Returns an iterator over the blocks in this Instruction set, giving preference to fall
         through flows.  This iterator will not follow any flows from a block that has a conflict.
         If the last block returned from the iterator is marked as a conflict before the next() or
         hasNext() methods are called, then this iterator will respect the conflict.  In other words,
         this iterator follows block flows on the fly and doesn't pre-compute the blocks to return.
         Also, if any blocks in this set don't have a flow to path from the start block, it will
         not be included in this iterator.
        """
        ...

    def notify(self) -> None: ...

    def notifyAll(self) -> None: ...

    def spliterator(self) -> java.util.Spliterator: ...

    def toString(self) -> unicode: ...

    @overload
    def wait(self) -> None: ...

    @overload
    def wait(self, __a0: long) -> None: ...

    @overload
    def wait(self, __a0: long, __a1: int) -> None: ...

    @property
    def addressSet(self) -> ghidra.program.model.address.AddressSetView: ...

    @property
    def conflicts(self) -> List[object]: ...

    @property
    def instructionCount(self) -> int: ...

    @property
    def minAddress(self) -> ghidra.program.model.address.Address: ...
