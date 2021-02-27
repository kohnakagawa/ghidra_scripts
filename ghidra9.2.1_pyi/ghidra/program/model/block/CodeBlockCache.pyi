from typing import List
import ghidra.program.model.address
import java.lang


class CodeBlockCache(ghidra.program.model.address.AddressObjectMap):
    """
    Provides a subroutine cache implementation.


     Created: February 28, 2002
    """





    def __init__(self): ...



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
