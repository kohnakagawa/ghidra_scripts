from typing import List
import ghidra.program.model.address
import ghidra.program.model.listing
import ghidra.program.util
import ghidra.util.task
import java.lang


class MemoryDiff(object):
    """
    MemoryDiff determines where the memory differs between two programs as well as the
     types of differences.
    """





    def __init__(self, p1: ghidra.program.model.listing.Program, p2: ghidra.program.model.listing.Program):
        """
        Constructs an object for determining memory differences between two programs.
        @param p1 the first program
        @param p2 the second program
        @throws ProgramConflictException if the program memory can't be compared because the programs
         are based on different languages.
        """
        ...



    def equals(self, __a0: object) -> bool: ...

    def getClass(self) -> java.lang.Class: ...

    def getDifferenceInfo(self, index: int) -> ghidra.program.util.MemoryBlockDiff:
        """
        Gets the memory difference flags for the address range as indicated by index.
        @param index the index of the address range to get the difference flags for.
        @return the difference flags for the indicated address range.
        """
        ...

    def getDifferences(self, p1Address: ghidra.program.model.address.Address) -> unicode:
        """
        Gets a string representation of the types of memory differences that exist for the memory
         block that contains the indicated address.
        @param p1Address address that is obtained via the first program.
        @return a string indicating the types of memory differences.
        """
        ...

    def getDifferentAddressRanges(self) -> List[ghidra.program.model.address.AddressRange]:
        """
        Returns an array of address ranges where there are memory differences.
        @return address ranges with differences.
        """
        ...

    def getNumRanges(self) -> int:
        """
        Gets the number of address ranges that the two programs memories are broken into for
         comparing the programs.
        @return the number of address ranges.
        """
        ...

    def getProgram1(self) -> ghidra.program.model.listing.Program:
        """
        Gets the first program that is part of this MemoryDiff.
        @return the first program
        """
        ...

    def getProgram2(self) -> ghidra.program.model.listing.Program:
        """
        Gets the second program that is part of this MemoryDiff.
        @return the second program
        """
        ...

    def getRange(self, index: int) -> ghidra.program.model.address.AddressRange:
        """
        Gets the address range as indicated by index. The index is zero based. Address ranges are
         in order from the minimum address to the maximum address range.
        @param index the index of the address range to get.
        @return the address range.
        """
        ...

    def hashCode(self) -> int: ...

    def merge(self, row: int, mergeFields: int, monitor: ghidra.util.task.TaskMonitor) -> bool: ...

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
    def differentAddressRanges(self) -> List[ghidra.program.model.address.AddressRange]: ...

    @property
    def numRanges(self) -> int: ...

    @property
    def program1(self) -> ghidra.program.model.listing.Program: ...

    @property
    def program2(self) -> ghidra.program.model.listing.Program: ...
