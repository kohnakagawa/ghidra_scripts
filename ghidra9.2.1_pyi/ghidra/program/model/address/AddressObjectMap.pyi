from typing import List
import ghidra.program.model.address
import java.lang


class AddressObjectMap(object):
    """
    AddressObjectMap maintains a mapping between addresses in the program
     and Objects that have been discovered.

     AddressObjectMap uses an ObjectPropertySet to track which addresses belong to
     which Objects. If a range [addr1,addr2] is assigned to a Object
     with id ID then -ID will be placed as the property value at
     addr1 and ID will be placed at addr2.
     In other words AddressObjectMap marks the beginning of a range belonging to an
     Object with its id (a positive number) and the end with its
     id (a negative number). A single address "range" will just have one entry
     which will contain -objID.

     It is important to realize that the current implementation of this cache,
     an address can only belong in one Object.  This could have bad effects
     for BlockModels where code can exist in more than one Object.  If this
     is to be used in that case, one must not just clear an area before adding in
     a range of addresses.  You would need to check if there is anything already
     defined and store a new index in those places that would represent a multi-block
     location.

     An AddressObjectMap instance should only be used to map to addresses contained within
     a single program.  The map should be discard if any changes
     are made to that programs address map (e.g., removing or renaming overlay spaces).
    """





    def __init__(self):
        """
        Creates a new <CODE>AddressObjectMap</CODE> object.
        """
        ...



    @overload
    def addObject(self, obj: object, set: ghidra.program.model.address.AddressSetView) -> None:
        """
        Associates the given object with the given set of addresses
        @param obj the object to associate
        @param set the set of address to be associated with the object.
        """
        ...

    @overload
    def addObject(self, obj: object, startAddr: ghidra.program.model.address.Address, endAddr: ghidra.program.model.address.Address) -> None:
        """
        Associates the given object with the given range of addresses
        @param obj the object to associate
        @param startAddr the first address in the range
        @param endAddr the last address in the range
        """
        ...

    def equals(self, __a0: object) -> bool: ...

    def getClass(self) -> java.lang.Class: ...

    def getObjects(self, addr: ghidra.program.model.address.Address) -> List[object]:
        """
        Get the objs associated with the given address.
        @param addr the address at which to get objects.
        @return an array of objects at the given address.
        """
        ...

    def hashCode(self) -> int: ...

    def notify(self) -> None: ...

    def notifyAll(self) -> None: ...

    @overload
    def removeObject(self, obj: object, set: ghidra.program.model.address.AddressSetView) -> None:
        """
        Removes any association with the object and the addresses in the given address set.
        @param obj the object to remove
        @param set the set of address from which to remove the object.
        """
        ...

    @overload
    def removeObject(self, obj: object, startAddr: ghidra.program.model.address.Address, endAddr: ghidra.program.model.address.Address) -> None:
        """
        Removes any association with the given object and the given range of addresses.
        @param obj the object to remove from associations in the given range.
        @param startAddr the first address in the range.
        @param endAddr the last address in the range.
        """
        ...

    def toString(self) -> unicode: ...

    @overload
    def wait(self) -> None: ...

    @overload
    def wait(self, __a0: long) -> None: ...

    @overload
    def wait(self, __a0: long, __a1: int) -> None: ...
