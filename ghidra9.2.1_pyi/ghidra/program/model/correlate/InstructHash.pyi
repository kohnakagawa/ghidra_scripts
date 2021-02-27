import ghidra.program.model.correlate
import java.lang


class InstructHash(object):
    """
    This class is the container for hashing information about a particular instruction, including all the
     n-grams it is currently involved in within the HashStore.
    """





    def __init__(self, inst: ghidra.program.model.listing.Instruction, bl: ghidra.program.model.correlate.Block, ind: int):
        """
        Build an (unmatched) Instruction, associating it with its position in the basic block
        @param inst is the underlying instruction
        @param bl is the basic-block
        @param ind is the index within the block
        """
        ...



    def allUnknown(self, length: int) -> bool:
        """
        If the -length- instructions, starting with this, are all unmatched, return true;
        @param length is number of instructions to check
        @return true if all checked instructions are unmatched
        """
        ...

    def equals(self, __a0: object) -> bool: ...

    def getBlock(self) -> ghidra.program.model.correlate.Block:
        """
        @return the containing basic block
        """
        ...

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

    @property
    def block(self) -> ghidra.program.model.correlate.Block: ...
