import ghidra.program.model.address
import ghidra.util.table.field
import java.lang


class AddressBasedLocation(object, java.lang.Comparable):
    """
    AddressBasedLocation provides the ability to render and compare
     addresses (e.g., location table column). This may be necessary when working a
     mixture of address types (e.g., memory, stack, register, variable, external)
     with the need to render in a meaningful way. Generally, only memory addresses
     are meaningful to a user when rendered as a simple address (e.g.,
     ram:00123456). While most address types are handled, VARIABLE addresses will
     only render as "VARIABLE". As such, this implementation should be
     extended if VARIABLE addresses will be encountered.
    """





    @overload
    def __init__(self):
        """
        Construct a null location which generally corresponds to a unknown/bad
         address
        """
        ...

    @overload
    def __init__(self, program: ghidra.program.model.listing.Program, address: ghidra.program.model.address.Address):
        """
        Construction a location. The memory block name will never be included in
         string representation.
        @param program program to which address belongs
        @param address address object (VARIABLE addresses should be avoided)
        """
        ...

    @overload
    def __init__(self, program: ghidra.program.model.listing.Program, reference: ghidra.program.model.symbol.Reference, showBlockName: ghidra.program.model.listing.CodeUnitFormatOptions.ShowBlockName):
        """
        Construct a location which corresponds to a reference TO address. String
         representation includes support for Offset References and allows control
         over inclusion of memory block name with memory addresses.
        @param program program to which address belongs
        @param reference program reference (e.g., memory, stack, register, external)
        @param showBlockName ShowBlockName option for controlling inclusion of memory block
         name with address rendering
        """
        ...



    @overload
    def compareTo(self, otherLocation: ghidra.util.table.field.AddressBasedLocation) -> int: ...

    @overload
    def compareTo(self, __a0: object) -> int: ...

    def equals(self, obj: object) -> bool: ...

    def getAddress(self) -> ghidra.program.model.address.Address: ...

    def getClass(self) -> java.lang.Class: ...

    def hashCode(self) -> int: ...

    def isMemoryLocation(self) -> bool:
        """
        @return true if location corresponds to memory address
        """
        ...

    def isOffsetAddress(self) -> bool:
        """
        Determine if location corresponds to a shifted memory reference
         destination
        @return true if location corresponds to a shifted memory reference destination
        """
        ...

    def isReferenceDestination(self) -> bool:
        """
        Determine if location corresponds to a reference destination
        @return true if location corresponds to a reference destination
        """
        ...

    def isShiftedAddress(self) -> bool:
        """
        Determine if location corresponds to a shifted memory reference destination
        @return true if location corresponds to a shifted memory reference destination
        """
        ...

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
    def address(self) -> ghidra.program.model.address.Address: ...

    @property
    def memoryLocation(self) -> bool: ...

    @property
    def offsetAddress(self) -> bool: ...

    @property
    def referenceDestination(self) -> bool: ...

    @property
    def shiftedAddress(self) -> bool: ...
