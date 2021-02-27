import java.lang


class MemoryBlockDiff(object):
    """
    MemoryBlockDiff determines the types of differences between two memory blocks.
    """

    ALL: int = 4095
    COMMENT: int = 2048
    END_ADDRESS: int = 4
    EXECUTE: int = 64
    INIT: int = 512
    NAME: int = 1
    READ: int = 16
    SIZE: int = 8
    SOURCE: int = 1024
    START_ADDRESS: int = 2
    TYPE: int = 256
    VOLATILE: int = 128
    WRITE: int = 32



    def __init__(self, block1: ghidra.program.model.mem.MemoryBlock, block2: ghidra.program.model.mem.MemoryBlock):
        """
        Constructor. <CODE>MemoryBlockDiff</CODE> determines the types of differences
         between two memory blocks.
        @param block1 the first program's memory block
        @param block2 the second program's memory block
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

    @property
    def commentDifferent(self) -> bool: ...

    @property
    def differencesAsString(self) -> unicode: ...

    @property
    def endAddressDifferent(self) -> bool: ...

    @property
    def execDifferent(self) -> bool: ...

    @property
    def initDifferent(self) -> bool: ...

    @property
    def nameDifferent(self) -> bool: ...

    @property
    def readDifferent(self) -> bool: ...

    @property
    def sizeDifferent(self) -> bool: ...

    @property
    def sourceDifferent(self) -> bool: ...

    @property
    def startAddressDifferent(self) -> bool: ...

    @property
    def typeDifferent(self) -> bool: ...

    @property
    def volatileDifferent(self) -> bool: ...

    @property
    def writeDifferent(self) -> bool: ...
