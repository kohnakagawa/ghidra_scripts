import ghidra.program.model.address
import java.lang


class SynchronizedAddressSetCollection(object, ghidra.program.model.address.AddressSetCollection):
    """
    Implementation of AddressSetCollection used by ProgramChangeSet.  It contains the
     actual instances of the addressSets used by the ProgramChangeSet and protects access
     to them by synchronizing on the ProgramChangeSet.

     Because these objects use the actual addressSets within the programChangeSet for
     efficiency reasons, any changes to those
     underlying sets will be reflected in the set of addresses represented by this collection.
     But since it is synchronized, you will always get a stable set during any given call and
     the AddressSetCollection interface is careful not to include iterator or other methods
     that can't tolerate a underlying change.  This object is really only intended for use by
     the GUI change bars and if it changes, it only results in possibly seeing the changes bars
     a bit earlier than otherwise.
    """





    def __init__(self, sync: object, addressSetViews: List[ghidra.program.model.address.AddressSetView]): ...



    def contains(self, address: ghidra.program.model.address.Address) -> bool: ...

    def equals(self, __a0: object) -> bool: ...

    def findFirstAddressInCommon(self, set: ghidra.program.model.address.AddressSetView) -> ghidra.program.model.address.Address: ...

    def getClass(self) -> java.lang.Class: ...

    def getCombinedAddressSet(self) -> ghidra.program.model.address.AddressSet: ...

    def getMaxAddress(self) -> ghidra.program.model.address.Address: ...

    def getMinAddress(self) -> ghidra.program.model.address.Address: ...

    def hasFewerRangesThan(self, rangeThreshold: int) -> bool: ...

    def hashCode(self) -> int: ...

    @overload
    def intersects(self, addrSet: ghidra.program.model.address.AddressSetView) -> bool: ...

    @overload
    def intersects(self, start: ghidra.program.model.address.Address, end: ghidra.program.model.address.Address) -> bool: ...

    def isEmpty(self) -> bool: ...

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
    def combinedAddressSet(self) -> ghidra.program.model.address.AddressSet: ...

    @property
    def empty(self) -> bool: ...

    @property
    def maxAddress(self) -> ghidra.program.model.address.Address: ...

    @property
    def minAddress(self) -> ghidra.program.model.address.Address: ...
