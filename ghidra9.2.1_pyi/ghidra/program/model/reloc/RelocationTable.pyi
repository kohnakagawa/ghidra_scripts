from typing import Iterator
from typing import List
import ghidra.program.model.address
import ghidra.program.model.reloc
import java.lang


class RelocationTable(object):
    """
    An interface for storing the relocations defined in a program.
    """

    RELOCATABLE_PROP_NAME: unicode = u'Relocatable'







    def add(self, addr: ghidra.program.model.address.Address, type: int, values: List[long], bytes: List[int], symbolName: unicode) -> ghidra.program.model.reloc.Relocation:
        """
        Creates and adds a new relocation with the specified
         address, type, and value.
        @param addr the address where the relocation is required
        @param type the type of relocation to perform
        @param values the values needed when performing the relocation
        @param bytes original instruction bytes affected by relocation
        @param symbolName the name of the symbol being relocated; may be null
        @return the newly added relocation object
        """
        ...

    def equals(self, __a0: object) -> bool: ...

    def getClass(self) -> java.lang.Class: ...

    def getRelocation(self, addr: ghidra.program.model.address.Address) -> ghidra.program.model.reloc.Relocation:
        """
        Returns the relocation with the specified address.
        @param addr the address where the relocation is defined
        @return the relocation with the specified address
        """
        ...

    def getRelocationAfter(self, addr: ghidra.program.model.address.Address) -> ghidra.program.model.reloc.Relocation:
        """
        Returns the next relocation point which follows the specified address.
        @param addr starting point
        @return next relocation after addr
        """
        ...

    @overload
    def getRelocations(self) -> Iterator[ghidra.program.model.reloc.Relocation]:
        """
        Returns an iterator over all relocation points (in ascending address order) located
         within the program.
        @return relocation iterator
        """
        ...

    @overload
    def getRelocations(self, set: ghidra.program.model.address.AddressSetView) -> Iterator[ghidra.program.model.reloc.Relocation]:
        """
        Returns an iterator over all the relocation points (in ascending address order) located
         within the specified address set.
        @param set address set
        @return relocation iterator
        """
        ...

    def getSize(self) -> int:
        """
        Returns the number of relocation in this table.
        @return the number of relocation in this table
        """
        ...

    def hashCode(self) -> int: ...

    def isRelocatable(self) -> bool:
        """
        Returns true if this relocation table contains relocations for a relocatable binary.
         Some binaries may contain relocations, but not actually be relocatable. For example, ELF executables.
        @return true if this relocation table contains relocations for a relocatable binary
        """
        ...

    def notify(self) -> None: ...

    def notifyAll(self) -> None: ...

    def remove(self, reloc: ghidra.program.model.reloc.Relocation) -> None:
        """
        Removes the relocation object.
        @param reloc the relocation object to remove
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
    def relocatable(self) -> bool: ...

    @property
    def relocations(self) -> java.util.Iterator: ...

    @property
    def size(self) -> int: ...
