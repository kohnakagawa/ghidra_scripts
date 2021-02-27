import ghidra.program.model.address
import ghidra.program.util.string
import ghidra.util.task
import java.lang


class StringSearcher(ghidra.program.util.string.AbstractStringSearcher):




    @overload
    def __init__(self, program: ghidra.program.model.listing.Program, minimumStringSize: int, alignment: int, allCharSizes: bool, requireNullTermination: bool): ...

    @overload
    def __init__(self, program: ghidra.program.model.listing.Program, charSet: ghidra.util.ascii.CharSetRecognizer, minimumStringSize: int, alignment: int, allCharSizes: bool, requireNullTermination: bool): ...



    def equals(self, __a0: object) -> bool: ...

    def getAlignment(self) -> int: ...

    def getClass(self) -> java.lang.Class: ...

    def hashCode(self) -> int: ...

    def notify(self) -> None: ...

    def notifyAll(self) -> None: ...

    def search(self, addressSet: ghidra.program.model.address.AddressSetView, callback: ghidra.program.util.string.FoundStringCallback, searchLoadedMemoryBlocksOnly: bool, monitor: ghidra.util.task.TaskMonitor) -> ghidra.program.model.address.AddressSetView:
        """
        Searches the given addressSet for strings.
         <p>
         Note: The address set searched will be modified before searching in the following ways:
         <ul>
         <li> if the given set is null, it will be re-initialized to encompass all of program memory</li>
         <li> the set will be further culled to only include loaded memory blocks, if specified</li>
         </ul>
         <p>
        @param addressSet the address set to search over; if null, will initialized to all memory
        @param callback the callback invoked when a string is found
        @param searchLoadedMemoryBlocksOnly if true, will exclude unloaded memory blocks from the search
        @param monitor the user monitor
        @return the updated address set used for the search
        """
        ...

    def toString(self) -> unicode: ...

    def updateAddressesToSearch(self, addressSet: ghidra.program.model.address.AddressSetView, useLoadedBlocksOnly: bool) -> ghidra.program.model.address.AddressSetView:
        """
        Returns a new address set that is the intersection of the given set with the
         desired memory block addresses (loaded or unloaded).
         <p>
         Note: This desired set of memory blocks is known by inspecting the
         {@link StringTableOptions#useLoadedBlocksOnly()} attribute set by the user.
        @param addressSet the address set to update
        @param useLoadedBlocksOnly if true, only return addresses in loaded memory blocks
        @return new the new address set
        """
        ...

    @overload
    def wait(self) -> None: ...

    @overload
    def wait(self, __a0: long) -> None: ...

    @overload
    def wait(self, __a0: long, __a1: int) -> None: ...
