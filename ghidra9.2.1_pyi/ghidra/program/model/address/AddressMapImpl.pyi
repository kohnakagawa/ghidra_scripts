from typing import List
import ghidra.program.model.address
import java.lang


class AddressMapImpl(object):
    """
    AddressMapImpl provides a stand-alone AddressMap.
     An AddressMapImpl instance should only be used to decode keys which it has generated.
     If this map is used for a specific program instance, the map should be discard if any changes
     are made to that programs address map (e.g., removing or renaming overlay spaces).
    """





    @overload
    def __init__(self):
        """
        Creates a new AddressMapImpl with a mapID of 0.
        """
        ...

    @overload
    def __init__(self, mapID: int, addrFactory: ghidra.program.model.address.AddressFactory):
        """
        Creates a new AddressMapImpl with the specified mapID
        @param mapID the 8-bit value is placed in the upper 8 bits of every address encoding.
        """
        ...



    def decodeAddress(self, value: long) -> ghidra.program.model.address.Address:
        """
        @see ghidra.program.database.map.AddressMap#decodeAddress(long)
        """
        ...

    def equals(self, __a0: object) -> bool: ...

    def findKeyRange(self, __a0: List[object], __a1: ghidra.program.model.address.Address) -> int: ...

    def getClass(self) -> java.lang.Class: ...

    def getKey(self, addr: ghidra.program.model.address.Address) -> long:
        """
        Generate a unique key for the specified addr.  Only addresses from a single address space or
         single program should be passed to this method. Only limited checking is not performed in order to
         improve performance.
        @param addr address
        @see ghidra.program.database.map.AddressMap#getKey(Address, boolean)
        """
        ...

    @overload
    def getKeyRanges(self, set: ghidra.program.model.address.AddressSetView) -> List[ghidra.program.model.address.KeyRange]:
        """
        @see ghidra.program.database.map.AddressMap#getKeyRanges(AddressSetView, boolean)
        """
        ...

    @overload
    def getKeyRanges(self, start: ghidra.program.model.address.Address, end: ghidra.program.model.address.Address) -> List[ghidra.program.model.address.KeyRange]:
        """
        @see ghidra.program.database.map.AddressMap#getKeyRanges(Address, Address, boolean)
        """
        ...

    def hashCode(self) -> int: ...

    def notify(self) -> None: ...

    def notifyAll(self) -> None: ...

    def reconcile(self) -> None:
        """
        Reconcile address space changes using associated address factory.
         This method should be invoked following an undo/redo (if the
         associated address factory may have changed) or removal of an
         overlay memory block.
        """
        ...

    def toString(self) -> unicode: ...

    @overload
    def wait(self) -> None: ...

    @overload
    def wait(self, __a0: long) -> None: ...

    @overload
    def wait(self, __a0: long, __a1: int) -> None: ...
