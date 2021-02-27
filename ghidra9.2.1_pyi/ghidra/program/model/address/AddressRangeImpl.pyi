from typing import Iterator
import ghidra.program.model.address
import java.io
import java.lang
import java.util
import java.util.function


class AddressRangeImpl(object, ghidra.program.model.address.AddressRange, java.io.Serializable):
    """
    Implementation of an AddressRange.  An AddressRange is a contiguous
     inclusive set of addresses from some minimum to a maximum address.  Once created
     it is immutable.
    """





    @overload
    def __init__(self, range: ghidra.program.model.address.AddressRange):
        """
        Construct a new AddressRangeImpl from the given range.
        @param range the address range to copy.
        """
        ...

    @overload
    def __init__(self, start: ghidra.program.model.address.Address, length: long):
        """
        Construct an AddressRange with the given start address and length.
        @param start start address in the range
        @param length the length of the range.
        @exception AddressOverflowException if the length would wrap.
        """
        ...

    @overload
    def __init__(self, start: ghidra.program.model.address.Address, end: ghidra.program.model.address.Address):
        """
        Construct an AddressRange with the given start and end address.
         If the start address is before the end address,
           they are swapped to be in order.
        @param start start address in the range
        @param end end address in the range
        @exception IllegalArgumentException thrown if the minimum and
         maximum addresses are not comparable.
        """
        ...

    def __iter__(self): ...

    @overload
    def compareTo(self, addr: ghidra.program.model.address.Address) -> int:
        """
        @see ghidra.program.model.address.AddressRange#compareTo(ghidra.program.model.address.Address)
        """
        ...

    @overload
    def compareTo(self, o: ghidra.program.model.address.AddressRange) -> int: ...

    @overload
    def compareTo(self, __a0: object) -> int: ...

    def contains(self, addr: ghidra.program.model.address.Address) -> bool:
        """
        @see ghidra.program.model.address.AddressRange#contains(ghidra.program.model.address.Address)
        """
        ...

    def equals(self, obj: object) -> bool:
        """
        @see java.lang.Object#equals(java.lang.Object)
        """
        ...

    def forEach(self, __a0: java.util.function.Consumer) -> None: ...

    def getAddressSpace(self) -> ghidra.program.model.address.AddressSpace: ...

    def getBigLength(self) -> long: ...

    def getClass(self) -> java.lang.Class: ...

    def getLength(self) -> long:
        """
        @see ghidra.program.model.address.AddressRange#getLength()
        """
        ...

    def getMaxAddress(self) -> ghidra.program.model.address.Address:
        """
        @see ghidra.program.model.address.AddressRange#getMaxAddress()
        """
        ...

    def getMinAddress(self) -> ghidra.program.model.address.Address:
        """
        @see ghidra.program.model.address.AddressRange#getMinAddress()
        """
        ...

    def hashCode(self) -> int: ...

    def intersect(self, range: ghidra.program.model.address.AddressRange) -> ghidra.program.model.address.AddressRange:
        """
        @see ghidra.program.model.address.AddressRange#intersect(ghidra.program.model.address.AddressRange)
        """
        ...

    def intersectRange(self, start: ghidra.program.model.address.Address, end: ghidra.program.model.address.Address) -> ghidra.program.model.address.AddressRange:
        """
        @see ghidra.program.model.address.AddressRange#intersectRange(ghidra.program.model.address.Address, ghidra.program.model.address.Address)
        """
        ...

    @overload
    def intersects(self, range: ghidra.program.model.address.AddressRange) -> bool:
        """
        @see ghidra.program.model.address.AddressRange#intersects(ghidra.program.model.address.AddressRange)
        """
        ...

    @overload
    def intersects(self, start: ghidra.program.model.address.Address, end: ghidra.program.model.address.Address) -> bool:
        """
        @see ghidra.program.model.address.AddressRange#intersects(ghidra.program.model.address.Address, ghidra.program.model.address.Address)
        """
        ...

    def iterator(self) -> Iterator[ghidra.program.model.address.Address]: ...

    def notify(self) -> None: ...

    def notifyAll(self) -> None: ...

    def spliterator(self) -> java.util.Spliterator: ...

    def toString(self) -> unicode:
        """
        @see java.lang.Object#toString()
        """
        ...

    @overload
    def wait(self) -> None: ...

    @overload
    def wait(self, __a0: long) -> None: ...

    @overload
    def wait(self, __a0: long, __a1: int) -> None: ...

    @property
    def addressSpace(self) -> ghidra.program.model.address.AddressSpace: ...

    @property
    def bigLength(self) -> long: ...

    @property
    def length(self) -> long: ...

    @property
    def maxAddress(self) -> ghidra.program.model.address.Address: ...

    @property
    def minAddress(self) -> ghidra.program.model.address.Address: ...
