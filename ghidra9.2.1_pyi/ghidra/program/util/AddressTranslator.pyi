import ghidra.program.model.address
import ghidra.program.model.listing
import java.lang


class AddressTranslator(object):








    def equals(self, __a0: object) -> bool: ...

    def getAddress(self, sourceAddress: ghidra.program.model.address.Address) -> ghidra.program.model.address.Address:
        """
        Converts the given source address to the returned destination address.
         This interface is intended to translate an address from the source program to an
         address in the destination program.
        @param sourceAddress the source address to be converted.
        @return the destination address that is equivalent in some way to the source address.
         How the address is equivalent depends upon the particular translator.
         throws AddressTranslationException if the address can't be translated to an equivalent
         address in the other program.
        """
        ...

    def getAddressRange(self, sourceAddressRange: ghidra.program.model.address.AddressRange) -> ghidra.program.model.address.AddressRange:
        """
        Converts the given source address range to the returned destination address range.
         This interface is intended to translate an address range from the source program to an
         address range in the destination program.
         <br>This method should be implemented if isOneForOneTranslator() returns true.
        @param sourceAddressRange the source address range to be converted.
        @return the destination address range that is equivalent in some way to the source address range.
         How the address range is equivalent depends upon the particular translator.
         throws AddressTranslationException if the address set can't be translated to an equivalent
         address range in the other program.
        """
        ...

    def getAddressSet(self, sourceAddressSet: ghidra.program.model.address.AddressSetView) -> ghidra.program.model.address.AddressSet:
        """
        Converts the given source address set to the returned destination address set.
         This interface is intended to translate an address set from the source program to an
         address set in the destination program.
         <br>This method should be implemented if isOneForOneTranslator() returns true.
        @param sourceAddressSet the source address set to be converted.
        @return the destination address set that is equivalent in some way to the source address set.
         How the address set is equivalent depends upon the particular translator.
         throws AddressTranslationException if the address set can't be translated to an equivalent
         address set in the other program.
        """
        ...

    def getClass(self) -> java.lang.Class: ...

    def getDestinationProgram(self) -> ghidra.program.model.listing.Program:
        """
        Gets the destination program for addresses that have been translated.
        @return program1.
        """
        ...

    def getSourceProgram(self) -> ghidra.program.model.listing.Program:
        """
        Gets the source program for obtaining the addresses that need to be translated.
        @return program2.
        """
        ...

    def hashCode(self) -> int: ...

    def isOneForOneTranslator(self) -> bool:
        """
        This method should return true if it can translate an address set from the source program
         to an address set for the destination program and there is a one to one correspondence
         between the two programs addresses.
         In other words two addresses that make up the start and end of an address range
         would be at the same distance and relative location from each other as the equivalent two
         individual translated addresses are from each other.
         Otherwise this should return false.
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
    def destinationProgram(self) -> ghidra.program.model.listing.Program: ...

    @property
    def oneForOneTranslator(self) -> bool: ...

    @property
    def sourceProgram(self) -> ghidra.program.model.listing.Program: ...
