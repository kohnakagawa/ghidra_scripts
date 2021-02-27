from typing import List
import ghidra.program.model.address
import ghidra.program.model.correlate
import ghidra.program.model.correlate.HashStore
import ghidra.program.model.listing
import ghidra.util.task
import java.lang


class HashStore(object):
    """
    HashStore is a sorted, basic-block aware, store for Instruction "n-grams" to help quickly match similar
     sequences of Instructions between two functions.  The Instructions comprising a single n-gram are hashed
     for quick lookup by the main matching algorithm (HashedFunctionAddressCorrelation).  Hash diversity is
     important to minimize collisions, even though the number of hashes calculated for a single function pair
     match is small.

     Hashes are built and sorted respectively using the calcHashes() and insertHashes() methods. The main sort
     is on the number of collisions for a hash (indicating that there are duplicate or near duplicate instruction
     sequences), the hashes with fewer (or no) duplicates come first. The secondary sort is on
     "n", the number of Instructions in the n-gram, which effectively describes the significance of the match, or how
     unlikely the match is to occur at random.  The main matching algorithm effectively creates a HashSort for both
     functions, and then in a loop calls
        hash = getFirstEntry()    on one side to get the most significant possible match
        getEntry(has)             to see if there is a matching n-gram on the other side

     If there is a match it is declared to the sort with the matchHash() call, allowing overlapping n-grams to be
     removed and deconflicting information to be updated.  If there is no match, hashes can be removed with the
     removeHash() method to allow new hashes to move to the top of the sort.

     The store uses a couple of methods to help deconflict very similar sequences of instructions within the same function.
     Primarily, the sort is basic-block aware.  All n-grams are contained within a single basic block, and when an initial
     match is found, hashes for other n-grams within that block (and its matching block on the other side) are modified
     so that n-grams within that block pair can only match each other.
    """






    class NgramMatch(object):
        block: ghidra.program.model.correlate.Block
        endindex: int
        startindex: int



        def __init__(self): ...



        def equals(self, __a0: object) -> bool: ...

        def getClass(self) -> java.lang.Class: ...

        def hashCode(self) -> int: ...

        def notify(self) -> None: ...

        def notifyAll(self) -> None: ...

        def toString(self) -> unicode: ...

        @overload
        def wait(self) -> None: ...

        @overload
        def wait(self, __a0: long) -> None: ...

        @overload
        def wait(self, __a0: long, __a1: int) -> None: ...



    def __init__(self, a: ghidra.program.model.listing.Function, mon: ghidra.util.task.TaskMonitor): ...



    def calcHashes(self, minLength: int, maxLength: int, wholeBlock: bool, matchOnly: bool, hashCalc: ghidra.program.model.correlate.HashCalculator) -> None:
        """
        Calculate hashes for all blocks
        @param minLength is the minimum length of an n-gram for these passes
        @param maxLength is the maximum length of an n-gram for these passes
        @param wholeBlock if true, allows blocks that are smaller than the minimum length to be considered as 1 n-gram.
        @param matchOnly if true, only generates n-grams for sequences in previously matched blocks
        @param hashCalc is the hash function
        @throws MemoryAccessException
        """
        ...

    def clearSort(self) -> None:
        """
        Clear the main sort structures, but preserve blocks and instructions
        """
        ...

    def equals(self, __a0: object) -> bool: ...

    @staticmethod
    def extendMatch(nGramSize: int, srcInstruct: ghidra.program.model.correlate.InstructHash, srcMatch: ghidra.program.model.correlate.HashStore.NgramMatch, destInstruct: ghidra.program.model.correlate.InstructHash, destMatch: ghidra.program.model.correlate.HashStore.NgramMatch, hashCalc: ghidra.program.model.correlate.HashCalculator) -> None:
        """
        Try to extend a match on a pair of n-grams to the Instructions right before and right after the n-gram.
         The match is extended if the Instruction adjacent to the n-gram, and its corresponding pair on the other side,
         hash to the same value using the hash function. The NgramMatch objects are updated to reflect the
         original n-gram match plus any additional extension.
        @param nGramSize is the original size of the matching n-gram.
        @param srcInstruct is the first Instruction in the "source" n-gram
        @param srcMatch is the "source" NgramMatch object to be populate
        @param destInstruct is the first Instruction in the "destination" n-gram
        @param destMatch is the "destination" NgramMatch object to populate
        @param hashCalc is the hash function object
        @throws MemoryAccessException
        """
        ...

    def getBlock(self, addr: ghidra.program.model.address.Address) -> ghidra.program.model.correlate.Block:
        """
        Get the basic-block with the corresponding start Address
        @param addr is the starting address
        @return the Block object
        """
        ...

    def getClass(self) -> java.lang.Class: ...

    def getEntry(self, hash: ghidra.program.model.correlate.Hash) -> ghidra.program.model.correlate.HashEntry:
        """
        Get the HashEntry corresponding to a given hash
        @param hash is the Hash to match
        @return the set of n-grams (HashEntry) matching this hash
        """
        ...

    def getFirstEntry(self) -> ghidra.program.model.correlate.HashEntry:
        """
        @return the first HashEntry in the sort.  The least number of matching n-grams and the biggest n-gram.
        """
        ...

    def getMonitor(self) -> ghidra.util.task.TaskMonitor:
        """
        @return the TaskMonitor for this store
        """
        ...

    def getTotalInstructions(self) -> int:
        """
        @return total number of Instructions in the whole function
        """
        ...

    def getUnmatchedInstructions(self) -> List[ghidra.program.model.listing.Instruction]:
        """
        @return list of unmatched instructions across the whole function
        """
        ...

    def hashCode(self) -> int: ...

    def insertHashes(self) -> None:
        """
        Insert all hashes associated with unknown (i.e not matched) blocks and instructions
        """
        ...

    def isEmpty(self) -> bool:
        """
        @return true if there are no n-grams left in the sort
        """
        ...

    def matchHash(self, __a0: ghidra.program.model.correlate.HashStore.NgramMatch, __a1: List[object], __a2: List[object]) -> None: ...

    def notify(self) -> None: ...

    def notifyAll(self) -> None: ...

    def numMatchedInstructions(self) -> int:
        """
        @return number of instructions that have been matched so far
        """
        ...

    def removeHash(self, hashEntry: ghidra.program.model.correlate.HashEntry) -> None:
        """
        Remove a particular HashEntry.  This may affect multiple instructions.
        @param hashEntry is the entry
        """
        ...

    def toString(self) -> unicode: ...

    @overload
    def wait(self) -> None: ...

    @overload
    def wait(self, __a0: long) -> None: ...

    @overload
    def wait(self, __a0: long, __a1: int) -> None: ...

    @property
    def empty(self) -> bool: ...

    @property
    def firstEntry(self) -> ghidra.program.model.correlate.HashEntry: ...

    @property
    def monitor(self) -> ghidra.util.task.TaskMonitor: ...

    @property
    def totalInstructions(self) -> int: ...

    @property
    def unmatchedInstructions(self) -> List[object]: ...
