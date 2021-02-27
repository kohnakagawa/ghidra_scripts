from typing import List
import ghidra.program.model.correlate
import java.lang


class DisambiguateStrategy(object):








    def calcHashes(self, instHash: ghidra.program.model.correlate.InstructHash, matchSize: int, store: ghidra.program.model.correlate.HashStore) -> List[ghidra.program.model.correlate.Hash]:
        """
        Generate (possibly multiple) hashes that can be used to disambiguate an n-gram and its block from other
         blocks with similar instructions.  Hashes are attached to the block's disambigHash list.
        @param instHash the instruction hash
        @param matchSize the number of instructions to match
        @param store is the HashStore used to store the disambiguating hashes
        @return the list of disambiguating hashes
        @throws CancelledException
        @throws MemoryAccessException
        """
        ...

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
