from typing import List
import ghidra.pcode.memstate
import ghidra.program.model.address
import java.lang


class MemoryBank(object):




    def __init__(self, spc: ghidra.program.model.address.AddressSpace, isBigEndian: bool, ps: int, faultHandler: ghidra.pcode.memstate.MemoryFaultHandler):
        """
        A MemoryBank must be associated with a specific address space, have a preferred or natural
         pagesize.  The pagesize must be a power of 2.
        @param spc is the associated address space
        @param isBigEndian memory endianess
        @param ps ps is the number of bytes in a page (must be a power of 2)
        @param faultHandler memory fault handler
        """
        ...



    @staticmethod
    def constructValue(ptr: List[int], offset: int, size: int, bigendian: bool) -> long: ...

    @staticmethod
    def deconstructValue(ptr: List[int], offset: int, val: long, size: int, bigendian: bool) -> None: ...

    def equals(self, __a0: object) -> bool: ...

    def getChunk(self, addrOffset: long, size: int, res: List[int], stopOnUnintialized: bool) -> int: ...

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

    def setChunk(self, offset: long, size: int, val: List[int]) -> None: ...

    def setInitialized(self, offset: long, size: int, initialized: bool) -> None: ...

    def toString(self) -> unicode: ...

    @overload
    def wait(self) -> None: ...

    @overload
    def wait(self, __a0: long) -> None: ...

    @overload
    def wait(self, __a0: long, __a1: int) -> None: ...

    @property
    def bigEndian(self) -> bool: ...

    @property
    def initializedMaskSize(self) -> int: ...

    @property
    def memoryFaultHandler(self) -> ghidra.pcode.memstate.MemoryFaultHandler: ...

    @property
    def pageSize(self) -> int: ...

    @property
    def space(self) -> ghidra.program.model.address.AddressSpace: ...
