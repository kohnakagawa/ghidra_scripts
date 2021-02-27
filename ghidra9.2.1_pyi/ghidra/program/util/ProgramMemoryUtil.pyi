from typing import List
import ghidra.program.model.address
import ghidra.program.model.listing
import ghidra.program.model.mem
import ghidra.util.datastruct
import ghidra.util.task
import java.lang
import java.util
import utility.function


class ProgramMemoryUtil(object):
    """
    ProgramMemoryUtil contains some static methods for
     checking Memory block data.
    """





    def __init__(self): ...



    @overload
    @staticmethod
    def copyBytesInRanges(toProgram: ghidra.program.model.listing.Program, fromProgram: ghidra.program.model.listing.Program, minAddr: ghidra.program.model.address.Address, maxAddr: ghidra.program.model.address.Address) -> None:
        """
        Copies the bytes to one program from another for the specified address
         range.
        @param toProgram program that the bytes are copied to.
        @param fromProgram program the bytes are copied from.
        @param minAddr the minimum address of the range to be copied.
         This address should be derived from the toProgram.
        @param maxAddr the maximum address of the range to be copied.
         This address should be derived from the toProgram.
        @throws MemoryAccessException if bytes can't be copied.
        """
        ...

    @overload
    @staticmethod
    def copyBytesInRanges(toProgram: ghidra.program.model.listing.Program, fromProgram: ghidra.program.model.listing.Program, addrSet: ghidra.program.model.address.AddressSetView, monitor: ghidra.util.task.TaskMonitor) -> None:
        """
        Copies the bytes to one program from another for the specified set of
         address ranges.
        @param toProgram program that the bytes are copied to.
        @param fromProgram program the bytes are copied from.
        @param addrSet the set of address ranges to be copied.
         The addresses in this set are derived from the "to program".
        @throws MemoryAccessException if bytes can't be copied.
        @throws CancelledException if user cancels copy bytes via the monitor.
        """
        ...

    def equals(self, __a0: object) -> bool: ...

    @overload
    @staticmethod
    def findDirectReferences(program: ghidra.program.model.listing.Program, alignment: int, toAddress: ghidra.program.model.address.Address, monitor: ghidra.util.task.TaskMonitor) -> java.util.Set:
        """
        Checks a programs memory for direct references to the address indicated.
         Direct references are only found at addresses that match the indicated alignment.
        @param program the program whose memory is to be checked.
        @param alignment direct references are to only be found at the indicated alignment in memory.
        @param toAddress address that we are interested in finding references to.
        @param monitor a task monitor for progress or to allow canceling.
        @return list of addresses referring directly to the toAddress
        @throws CancelledException if the user cancels via the monitor.
        """
        ...

    @overload
    @staticmethod
    def findDirectReferences(__a0: ghidra.program.model.listing.Program, __a1: List[object], __a2: int, __a3: ghidra.program.model.address.Address, __a4: ghidra.util.task.TaskMonitor) -> java.util.Set: ...

    @staticmethod
    def findDirectReferencesCodeUnit(program: ghidra.program.model.listing.Program, alignment: int, codeUnit: ghidra.program.model.listing.CodeUnit, monitor: ghidra.util.task.TaskMonitor) -> List[ghidra.program.model.address.Address]:
        """
        Checks a programs memory for direct references to the CodeUnit indicated.
         Direct references are only found at addresses that match the indicated alignment.
        @param program the program whose memory is to be checked.
        @param alignment direct references are to only be found at the indicated alignment in memory.
        @param codeUnit the code unit to to search for references to.
        @param monitor a task monitor for progress or to allow canceling.
        @return list of addresses referring directly to the toAddress.
        """
        ...

    @staticmethod
    def findImageBaseOffsets32(program: ghidra.program.model.listing.Program, alignment: int, toAddress: ghidra.program.model.address.Address, monitor: ghidra.util.task.TaskMonitor) -> java.util.Set:
        """
        Checks a programs memory for 32 bit image base offset references to the address
         indicated.  These relative references are only found at addresses that match the
         indicated alignment.
        @param program the program whose memory is to be checked.
        @param alignment 32 bit image base offset relative references are to only be found
         at the indicated alignment in memory.
        @param toAddress address that we are interested in finding references to.
        @param monitor a task monitor for progress or to allow canceling.
        @return list of addresses with 32 bit image base offset relative references to the
         toAddress
        @throws CancelledException if the user cancels via the monitor.
        """
        ...

    @staticmethod
    def findString(__a0: unicode, __a1: ghidra.program.model.listing.Program, __a2: List[object], __a3: ghidra.program.model.address.AddressSetView, __a4: ghidra.util.task.TaskMonitor) -> List[object]: ...

    @overload
    @staticmethod
    def getAddressSet(program: ghidra.program.model.listing.Program) -> ghidra.program.model.address.AddressSetView:
        """
        Gets the address set for the specified program.
        @param program the program whose address set we want.
        @return the address set
        """
        ...

    @overload
    @staticmethod
    def getAddressSet(program: ghidra.program.model.listing.Program, blocksWithBytes: bool) -> ghidra.program.model.address.AddressSet:
        """
        Gets a new address set indicating all addresses of the indicated
         memory type in the specified program.
        @param program the program whose address set we want.
        @param blocksWithBytes if true, include memory blocks that have their own bytes.
        @return the memory's address set of the indicated type.
        """
        ...

    def getClass(self) -> java.lang.Class: ...

    @staticmethod
    def getDirectAddressBytes(program: ghidra.program.model.listing.Program, toAddress: ghidra.program.model.address.Address) -> List[int]:
        """
        Get a representation of an address as it would appear in bytes in memory.
        @param program program
        @param toAddress target address
        @return byte representation of toAddress
        """
        ...

    @staticmethod
    def getImageBaseOffsets32Bytes(program: ghidra.program.model.listing.Program, alignment: int, toAddress: ghidra.program.model.address.Address) -> List[int]: ...

    @staticmethod
    def getMemBlocks(program: ghidra.program.model.listing.Program, withBytes: bool) -> List[ghidra.program.model.mem.MemoryBlock]:
        """
        Gets the program memory blocks of the indicated type for the
         specified program.
        @param program the program whose memory blocks we want.
        @param withBytes if true include blocks that have their own bytes. If false, include only
         blocks that don't have their own bytes (this includes bit and byte mapped blocks)
        @return an array of program memory blocks
        """
        ...

    @staticmethod
    def getMemoryBlocksStartingWithName(program: ghidra.program.model.listing.Program, set: ghidra.program.model.address.AddressSetView, name: unicode, monitor: ghidra.util.task.TaskMonitor) -> List[ghidra.program.model.mem.MemoryBlock]:
        """
        Gets a list of memory blocks whose name starts with the indicated name. Only memory
         blocks that are initialized  and part of the indicated address set will be returned.
        @param program the program for obtaining the memory blocks
        @param set the address set to use to limit the blocks returned
        @param name the text which the memory block's name must start with.
        @param monitor a status monitor that allows the operation to be cancelled
        @return the list of memory blocks
        @throws CancelledException if the user cancels
        """
        ...

    @staticmethod
    def getOverlayAddresses(program: ghidra.program.model.listing.Program) -> ghidra.program.model.address.AddressSet:
        """
        Gets an address set with the overlay addresses that are in the specified program.
        @param program the program
        @return the overlay addresses within the specified program.
        """
        ...

    @staticmethod
    def getShiftedDirectAddressBytes(program: ghidra.program.model.listing.Program, toAddress: ghidra.program.model.address.Address) -> List[int]:
        """
        returns shifted address bytes if they are different than un-shifted
        @param program program
        @param toAddress target address
        @return shifted bytes, null if same as un-shifted
        """
        ...

    def hashCode(self) -> int: ...

    @overload
    @staticmethod
    def loadDirectReferenceList(program: ghidra.program.model.listing.Program, alignment: int, toAddress: ghidra.program.model.address.Address, toAddressSet: ghidra.program.model.address.AddressSetView, accumulator: ghidra.util.datastruct.Accumulator, monitor: ghidra.util.task.TaskMonitor) -> None:
        """
        Checks a programs memory for direct references to the addresses indicated in the toAddressSet.
         Direct references are only found at addresses that match the indicated alignment. Each
         direct reference is added to the directReferenceList as a from/to address pair.
        @param program the program whose memory is to be checked.
        @param alignment direct references are to only be found at the indicated alignment in memory.
        @param toAddress address that we are interested in finding references to.
        @param toAddressSet address set indicating the addresses that we are interested in
         		  finding directly referred to in memory.
         		  Null if only interested in finding references to the toAddress.
        @param accumulator the datastructure to be populated with possible direct references
        @param monitor a task monitor for progress or to allow cancelling.
        @throws CancelledException if the user cancels via the monitor.
        """
        ...

    @overload
    @staticmethod
    def loadDirectReferenceList(__a0: ghidra.program.model.listing.Program, __a1: int, __a2: ghidra.program.model.address.Address, __a3: ghidra.program.model.address.AddressSetView, __a4: List[object], __a5: ghidra.util.task.TaskMonitor) -> None: ...

    @staticmethod
    def locateString(__a0: unicode, __a1: utility.function.TerminatingConsumer, __a2: ghidra.program.model.listing.Program, __a3: List[object], __a4: ghidra.program.model.address.AddressSetView, __a5: ghidra.util.task.TaskMonitor) -> None: ...

    def notify(self) -> None: ...

    def notifyAll(self) -> None: ...

    def toString(self) -> unicode: ...

    @overload
    def wait(self) -> None: ...

    @overload
    def wait(self, __a0: long) -> None: ...

    @overload
    def wait(self, __a0: long, __a1: int) -> None: ...
