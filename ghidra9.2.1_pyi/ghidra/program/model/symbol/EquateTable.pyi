from typing import Iterator
from typing import List
import ghidra.program.model.address
import ghidra.program.model.symbol
import ghidra.util.task
import java.lang


class EquateTable(object):
    """
    EquateTable manages all equates for program. An equate defines a relationship
       between a scalar value and a string whereby the scalar may be represented by
       the string. All equates are defined by the user and remain until explicitly
       removed by the user.
    """









    def createEquate(self, name: unicode, value: long) -> ghidra.program.model.symbol.Equate:
        """
        Creates a new equate
        @param name the name to associate with the given value.
        @param value the value to associate with the given name.
        @return the equate
        @exception DuplicateNameException thrown if name is already in use
           as an equate.
        @throws InvalidInputException if name contains blank characters,
         is zero length, or is null
        """
        ...

    def deleteAddressRange(self, start: ghidra.program.model.address.Address, end: ghidra.program.model.address.Address, monitor: ghidra.util.task.TaskMonitor) -> None:
        """
        Removes all equates defined in the given range.
        @param start start of the range
        @param end end of the range
        @param monitor task monitor to cancel the remove operation
        @throws CancelledException if the operation was cancelled.
        """
        ...

    def equals(self, __a0: object) -> bool: ...

    def getClass(self) -> java.lang.Class: ...

    @overload
    def getEquate(self, name: unicode) -> ghidra.program.model.symbol.Equate:
        """
        Returns the equate with the given name, null if no such equate exists
        @param name the of the equate to be retrieved
        @return the equate
        """
        ...

    @overload
    def getEquate(self, reference: ghidra.program.model.address.Address, opndPosition: int, value: long) -> ghidra.program.model.symbol.Equate:
        """
        Returns the first equate found that is associated with the given
         value at the given reference address and operand position;
        @param reference address where the equate is used.
        @param opndPosition the operand index of the operand where the equate is used.
        @param value the value where the equate is used.
        @return the equate or null if there is no such equate.
        """
        ...

    @overload
    def getEquateAddresses(self) -> ghidra.program.model.address.AddressIterator:
        """
        Returns an address iterator over all the addresses where
         equates have been set.
        @return the iterator
        """
        ...

    @overload
    def getEquateAddresses(self, start: ghidra.program.model.address.Address) -> ghidra.program.model.address.AddressIterator:
        """
        Return an address iterator over each address with an
         equate reference starting at the start address.
        @param start start address
        @return an AddressIterator over addresses with defined equate references
        """
        ...

    @overload
    def getEquateAddresses(self, asv: ghidra.program.model.address.AddressSetView) -> ghidra.program.model.address.AddressIterator:
        """
        Return an address iterator over each address with an
         equate reference that is in the specified address set.
        @param asv the address set
        @return AddressIterator over addresses with defined equate references
        """
        ...

    @overload
    def getEquates(self) -> Iterator[ghidra.program.model.symbol.Equate]:
        """
        Returns an iterator over all equates.
        @return the iterator
        """
        ...

    @overload
    def getEquates(self, value: long) -> List[ghidra.program.model.symbol.Equate]:
        """
        Returns all equates defined for value.
        @param value the value to get all equates for.
        @return the equates
        """
        ...

    @overload
    def getEquates(self, reference: ghidra.program.model.address.Address) -> List[ghidra.program.model.symbol.Equate]:
        """
        Returns the equates (one for each scalar and opIndex) at the given reference address.
         For an instruction a given operand can have multiple scalars.
        @param reference address where the equate is used.
        @return the list of equates or empty list if there is no such equate.
        """
        ...

    @overload
    def getEquates(self, reference: ghidra.program.model.address.Address, opndPosition: int) -> List[ghidra.program.model.symbol.Equate]:
        """
        Returns the equates (one for each scalar) at the given reference address
         and operand position; For an instruction a given operand can have multiple scalars.
        @param reference address where the equate is used.
        @param opndPosition the operand index of the operand where the equate is used.
        @return the list of equates or empty list if there is no such equate.
        """
        ...

    def hashCode(self) -> int: ...

    def notify(self) -> None: ...

    def notifyAll(self) -> None: ...

    def removeEquate(self, name: unicode) -> bool:
        """
        Removes the equate from the program.
        @param name the name of the equate to remove.
        @return true if the equate existed, false otherwise.
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
    def equateAddresses(self) -> ghidra.program.model.address.AddressIterator: ...

    @property
    def equates(self) -> java.util.Iterator: ...
