import ghidra.program.model.listing
import java.lang


class HashCalculator(object):
    """
    Interface for hashing across sequences of Instructions in different ways
    """









    def calcHash(self, startHash: int, inst: ghidra.program.model.listing.Instruction) -> int:
        """
        Calculate a (partial) hash across a single instruction
        @param startHash is initial hash value
        @param inst is the instruction to fold into the hash
        @return the final hash value
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
