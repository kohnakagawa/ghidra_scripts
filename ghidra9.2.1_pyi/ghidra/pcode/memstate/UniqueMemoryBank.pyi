from typing import List
import ghidra.pcode.memstate
import ghidra.program.model.address
import java.lang


class UniqueMemoryBank(ghidra.pcode.memstate.MemoryBank):
    """
    An subclass of MemoryBank intended for modeling the "unique" memory
     space.  The space is byte-addressable and paging is not supported.
    """






    class WordInfo(object):
        initialized: int
        word: long



        def __init__(self): ...



        def equals(self, __a0: object) -> bool: ...

        def getByte(self, __a0: int) -> int: ...

        def getClass(self) -> java.lang.Class: ...

        def getWord(self, __a0: List[int]) -> None: ...

        def hashCode(self) -> int: ...

        def notify(self) -> None: ...

        def notifyAll(self) -> None: ...

        def setByte(self, __a0: int, __a1: int) -> None: ...

        def toString(self) -> unicode: ...

        @overload
        def wait(self) -> None: ...

        @overload
        def wait(self, __a0: long) -> None: ...

        @overload
        def wait(self, __a0: long, __a1: int) -> None: ...



    def __init__(self, spc: ghidra.program.model.address.AddressSpace, isBigEndian: bool): ...



    def clear(self) -> None:
        """
        Clear unique storage at the start of an instruction
        """
        ...

    @staticmethod
    def constructValue(ptr: List[int], offset: int, size: int, bigendian: bool) -> long: ...

    @staticmethod
    def deconstructValue(ptr: List[int], offset: int, val: long, size: int, bigendian: bool) -> None: ...

    def equals(self, __a0: object) -> bool: ...

    def getChunk(self, offset: long, size: int, dest: List[int], stopOnUninitialized: bool) -> int: ...

    def getClass(self) -> java.lang.Class: ...

    def getInitializedMaskSize(self) -> int:
        """
        @return the size of a page initialized mask in bytes.  Each bit within the
         mask corresponds to a data byte within a page.
        """
        ...

    def getMemoryFaultHandler(self) -> ghidra.pcode.memstate.MemoryFaultHandler:
        """
        @return memory fault handler (may be null)
        """
        ...

    def getPageSize(self) -> int:
        """
        A MemoryBank is instantiated with a \e natural page size. Requests for large chunks of data
         may be broken down into units of this size.
        @return the number of bytes in a page.
        """
        ...

    def getSpace(self) -> ghidra.program.model.address.AddressSpace:
        """
        @return the AddressSpace associated with this bank.
        """
        ...

    def hashCode(self) -> int: ...

    def isBigEndian(self) -> bool:
        """
        @return true if memory bank is big endian
        """
        ...

    def notify(self) -> None: ...

    def notifyAll(self) -> None: ...

    def setChunk(self, offset: long, size: int, src: List[int]) -> None: ...

    def setInitialized(self, offset: long, size: int, initialized: bool) -> None: ...

    def toString(self) -> unicode: ...

    @overload
    def wait(self) -> None: ...

    @overload
    def wait(self, __a0: long) -> None: ...

    @overload
    def wait(self, __a0: long, __a1: int) -> None: ...
