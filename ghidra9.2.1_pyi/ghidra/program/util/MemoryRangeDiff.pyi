import ghidra.program.util
import java.lang


class MemoryRangeDiff(ghidra.program.util.MemoryBlockDiff):
    """
    MemoryBlockDiff determines the types of differences between two memory blocks.
    """





    def __init__(self, memory1: ghidra.program.model.mem.Memory, memory2: ghidra.program.model.mem.Memory, range: ghidra.program.model.address.AddressRange):
        """
        Constructor. <CODE>MemoryRangeDiff</CODE> determines the types of differences
         between two memory blocks.
        @param memory1 the first program's memory
        @param memory2 the second program's memory
        @param range the address range where the two programs differ
        """
        ...



    def equals(self, __a0: object) -> bool: ...

    def getClass(self) -> java.lang.Class: ...

    def getDifferencesAsString(self) -> unicode:
        """
        Gets a string representation of the types of memory differences for this MemoryBlockDiff.
        """
        ...

    def hashCode(self) -> int: ...

    def isCommentDifferent(self) -> bool:
        """
        Returns true if the comments on the memory blocks differ.
        """
        ...

    def isEndAddressDifferent(self) -> bool:
        """
        Returns true if the end addresses of the memory blocks differ.
        """
        ...

    def isExecDifferent(self) -> bool:
        """
        Returns true if the memory blocks Execute flags differ.
        """
        ...

    def isInitDifferent(self) -> bool:
        """
        Returns true if the initialization of the memory blocks isn't the same.
        """
        ...

    def isNameDifferent(self) -> bool:
        """
        Returns true if the memory block names differ.
        """
        ...

    def isReadDifferent(self) -> bool:
        """
        Returns true if the memory blocks Read flags differ.
        """
        ...

    def isSizeDifferent(self) -> bool:
        """
        Returns true if the sizes of the memory blocks differ.
        """
        ...

    def isSourceDifferent(self) -> bool:
        """
        Returns true if the source for the memory blocks differ.
        """
        ...

    def isStartAddressDifferent(self) -> bool:
        """
        Returns true if the start addresses of the memory blocks differ.
        """
        ...

    def isTypeDifferent(self) -> bool:
        """
        Returns true if the type for the memory blocks differ.
        """
        ...

    def isVolatileDifferent(self) -> bool:
        """
        Returns true if the memory blocks Volatile flags differ.
        """
        ...

    def isWriteDifferent(self) -> bool:
        """
        Returns true if the memory blocks Write flags differ.
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
