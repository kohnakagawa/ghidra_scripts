import ghidra.program.model.correlate
import java.lang


class Block(object):
    """
    This class holds basic-block information for matching algorithms. It is used as a node to traverse the
     control-flow graph. It serves as a container for hashing information associated with Instructions in the
     block.  It holds disambiguating hashes (calculated primarily from basic-block parent/child relationships)
     to help separate identical or near identical sequences of Instructions within one function.
    """





    def __init__(self, codeBlock: ghidra.program.model.block.CodeBlock): ...



    def equals(self, __a0: object) -> bool: ...

    def getClass(self) -> java.lang.Class: ...

    def getMatchHash(self) -> int:
        """
        @return the main deconfliction hash feed
        """
        ...

    def hashCode(self) -> int: ...

    def hashGram(self, gramSize: int, instHash: ghidra.program.model.correlate.InstructHash, hashCalc: ghidra.program.model.correlate.HashCalculator) -> int:
        """
        Calculate an n-gram hash, given a particular hash function
        @param gramSize is the size of the n-gram
        @param instHash is the first Instruction in the n-gram
        @param hashCalc is the hash function
        @return the final 32-bit hash
        @throws MemoryAccessException
        """
        ...

    def notify(self) -> None: ...

    def notifyAll(self) -> None: ...

    def toString(self) -> unicode: ...

    @overload
    def wait(self) -> None: ...

    @overload
    def wait(self, __a0: long) -> None: ...

    @overload
    def wait(self, __a0: long, __a1: int) -> None: ...

    @property
    def matchHash(self) -> int: ...
