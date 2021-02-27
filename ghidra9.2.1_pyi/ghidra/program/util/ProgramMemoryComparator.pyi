import ghidra.program.model.address
import ghidra.program.model.listing
import java.lang


class ProgramMemoryComparator(object):
    """
    ProgramMemoryComparator is a class for comparing two programs and
     determining the address differences between them.
    """





    def __init__(self, program1: ghidra.program.model.listing.Program, program2: ghidra.program.model.listing.Program):
        """
        <CODE>ProgramMemoryComparator</CODE> is used to determine the memory
         address differences between two programs.
        @param program1 the first program
        @param program2 the second program
        @throws ProgramConflictException if the two programs can't be compared.
        """
        ...



    @staticmethod
    def compareAddressTypes(program1: ghidra.program.model.listing.Program, program2: ghidra.program.model.listing.Program) -> None:
        """
        Check each program to see if the memory blocks have the same address types.
        @param program1 the first program
        @param program2 the second program
        @throws ProgramConflictException if the address types for the two programs
         do not match.
        """
        ...

    def equals(self, __a0: object) -> bool: ...

    def getAddressRanges(self) -> ghidra.program.model.address.AddressRangeIterator:
        """
        Returns an iterator for the address ranges in the set containing the combined addresses
          in program1 and program2.
          Address ranges from this iterator are derived using program1.
        @return the addresses for both program1 and program2.
        """
        ...

    def getAddressesInCommon(self) -> ghidra.program.model.address.AddressSet:
        """
        Returns the addresses in common between program1 and program2.
          The returned address set is derived using program1.
        @return the addresses in common between program1 and program2.
        """
        ...

    def getAddressesOnlyInOne(self) -> ghidra.program.model.address.AddressSet:
        """
        Returns the addresses that are in program1, but not in program2
          The returned address set is derived using program1.
        @return the addresses that are in program1, but not in program2.
        """
        ...

    def getAddressesOnlyInTwo(self) -> ghidra.program.model.address.AddressSet:
        """
        Returns the addresses that are in program2, but not in program1
          The returned address set is derived using program2.
        @return the addresses that are in program2, but not in program1.
        """
        ...

    def getClass(self) -> java.lang.Class: ...

    @staticmethod
    def getCombinedAddresses(program1: ghidra.program.model.listing.Program, program2: ghidra.program.model.listing.Program) -> ghidra.program.model.address.AddressSet:
        """
        Returns the addresses from combining the address sets in program1 and program2.
          Addresses in the returned address set are derived from program1.
        @return the addresses for both program1 and program2.
        """
        ...

    def getCompatibleAddressesOnlyInTwo(self) -> ghidra.program.model.address.AddressSet:
        """
        Returns the set of addresses that are in program2, but not in program1
         and that are compatible with program1.
          The returned address set is derived using program1.
        @return the addresses that are in program2, but not in program1.
        """
        ...

    def getInitializedAddressesInCommon(self) -> ghidra.program.model.address.AddressSet:
        """
        Returns the addresses of initialized memory in common between
         program1 and program2. This includes bit memory and live memory.
         The returned address set is derived using program1.
        @return the addresses in common between program1 and program2.
        """
        ...

    def getProgramOne(self) -> ghidra.program.model.listing.Program:
        """
        Gets the first program being compared by the ProgramMemoryComparator.
        @return program1.
        """
        ...

    def getProgramTwo(self) -> ghidra.program.model.listing.Program:
        """
        Gets the second program being compared by the ProgramMemoryComparator.
        @return program2.
        """
        ...

    def getSameMemTypeAddressesInCommon(self) -> ghidra.program.model.address.AddressSet:
        """
        Returns the addresses with the same memory types in common between
         program1 and program2.
         The returned address set is derived using program1.
        @return the addresses in common between program1 and program2.
        """
        ...

    def hasMemoryDifferences(self) -> bool:
        """
        Return whether or not the memory addresses for the two Programs are different.
        """
        ...

    def hashCode(self) -> int: ...

    def notify(self) -> None: ...

    def notifyAll(self) -> None: ...

    @staticmethod
    def sameProgramContextRegisterNames(program1: ghidra.program.model.listing.Program, program2: ghidra.program.model.listing.Program) -> bool:
        """
        Returns true if the register names are the same in both programs.
        @param program1 the first program
        @param program2 the second program
        @return true if the register names are the same
        """
        ...

    @staticmethod
    def similarPrograms(p1: ghidra.program.model.listing.Program, p2: ghidra.program.model.listing.Program) -> bool:
        """
        Return whether or not the two specified programs are alike
         (their language name or address spaces are the same).
        @param p1 the first program
        @param p2 the second program
        @return true if the programs are alike (their language name or address spaces are the same).
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
    def addressRanges(self) -> ghidra.program.model.address.AddressRangeIterator: ...

    @property
    def addressesInCommon(self) -> ghidra.program.model.address.AddressSet: ...

    @property
    def addressesOnlyInOne(self) -> ghidra.program.model.address.AddressSet: ...

    @property
    def addressesOnlyInTwo(self) -> ghidra.program.model.address.AddressSet: ...

    @property
    def compatibleAddressesOnlyInTwo(self) -> ghidra.program.model.address.AddressSet: ...

    @property
    def initializedAddressesInCommon(self) -> ghidra.program.model.address.AddressSet: ...

    @property
    def programOne(self) -> ghidra.program.model.listing.Program: ...

    @property
    def programTwo(self) -> ghidra.program.model.listing.Program: ...

    @property
    def sameMemTypeAddressesInCommon(self) -> ghidra.program.model.address.AddressSet: ...
