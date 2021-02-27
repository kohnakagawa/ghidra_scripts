from typing import List
import ghidra.app.util.viewer.listingpanel
import ghidra.program.model.address
import ghidra.program.model.listing
import ghidra.program.util
import java.lang


class ListingDiff(object):
    """
    Determines where instructions couldn't be matched and where they differ between sets of
     addresses as provided by a ListingAddressCorrelation. Initially this will be byte
     differences and instruction operand differences for any instructions that were determined
     to be matched.
     Important: This class is not intended to be used for an entire program. Instead it is
     for comparing smaller portions such as functions. If the correlation handed to this class
     associates two large address sets, then the address sets, such as byte differences, that are
     created by this class could potentially consume large amounts of memory.
    """





    def __init__(self):
        """
        Creates a ListingDiff to determine where instructions couldn't be matched and where they
         differ between sets of addresses as provided by a ListingAddressCorrelation.
        """
        ...



    def addListingDiffChangeListener(self, listener: ghidra.app.util.viewer.listingpanel.ListingDiffChangeListener) -> None:
        """
        Adds the indicated listener to those that get notified when the ListingDiff's set of
         differences and unmatched addresses changes.
        @param listener the listener to be notified
        """
        ...

    def doesEntireOperandSetDiffer(self, codeUnit1: ghidra.program.model.listing.CodeUnit, codeUnit2: ghidra.program.model.listing.CodeUnit) -> bool:
        """
        Determines if the entire set of operands should indicate that it differs.
         If the code units aren't the same type then the entire set of operands is considered different.
         Also if the number of operands differs then as far as we're concerned the entire set differs.
        @param codeUnit1 the first code unit
        @param codeUnit2 the second code unit
        @return true if we should indicate that all operands differ.
        """
        ...

    def equals(self, __a0: object) -> bool: ...

    def getClass(self) -> java.lang.Class: ...

    def getListing1ByteDiffs(self) -> ghidra.program.model.address.AddressSetView:
        """
        Gets the addresses in the first listing where byte differences were found based on the
         current difference settings.
        @return the addresses with byte differences in the first listing.
        """
        ...

    def getListing1CodeUnitDiffs(self) -> ghidra.program.model.address.AddressSetView:
        """
        Gets the addresses in the first listing where code unit (mnemonic and/or operand) differences
         were found based on the current difference settings.
        @return the addresses with code unit differences in the first listing.
        """
        ...

    def getListing1Diffs(self) -> ghidra.program.model.address.AddressSetView:
        """
        Gets the addresses in the first listing where differences were found based on the current
         difference settings.
        @return the addresses with differences in the first listing.
        """
        ...

    def getListing1UnmatchedCode(self) -> ghidra.program.model.address.AddressSetView:
        """
        Gets the addresses in the first listing where matching code couldn't be determined in the
         second listing.
        @return the addresses of the unmatched code in the first listing.
        """
        ...

    def getListing2ByteDiffs(self) -> ghidra.program.model.address.AddressSetView:
        """
        Gets the addresses in the second listing where byte differences were found based on the
         current difference settings.
        @return the addresses with byte differences in the second listing.
        """
        ...

    def getListing2CodeUnitDiffs(self) -> ghidra.program.model.address.AddressSetView:
        """
        Gets the addresses in the second listing where code unit (mnemonic and/or operand) differences
         were found based on the current difference settings.
        @return the addresses with code unit differences in the second listing.
        """
        ...

    def getListing2Diffs(self) -> ghidra.program.model.address.AddressSetView:
        """
        Gets the addresses in the second listing where differences were found based on the current
         difference settings.
        @return the addresses with differences in the second listing.
        """
        ...

    def getListing2UnmatchedCode(self) -> ghidra.program.model.address.AddressSetView:
        """
        Gets the addresses in the second listing where matching code couldn't be determined in the
         first listing.
        @return the addresses of the unmatched code in the second listing.
        """
        ...

    def getMatchingAddress(self, address: ghidra.program.model.address.Address, isListing1: bool) -> ghidra.program.model.address.Address:
        """
        Gets the matching address from the other listing for the specified address from one
         of the two listings whose differences this class determines.
        @param address the address whose matching address this determines.
        @param isListing1 true indicates the address is from the first listing. false indicates
         it is from the second listing.
        @return the matching address or null
        """
        ...

    def getMatchingCodeUnit(self, codeUnit: ghidra.program.model.listing.CodeUnit, isListing1: bool) -> ghidra.program.model.listing.CodeUnit:
        """
        Gets the matching code unit from the other listing for the specified code unit from one
         of the two listings whose differences this class determines.
        @param codeUnit the code unit whose match this determines.
        @param isListing1 true indicates the code unit is from the first listing. false indicates
         it is from the second listing.
        @return the matching code unit or null
        """
        ...

    def getOperandsThatDiffer(self, codeUnit1: ghidra.program.model.listing.CodeUnit, codeUnit2: ghidra.program.model.listing.CodeUnit) -> List[int]:
        """
        Gets an array containing the operand indices where the two indicated code units differ.
         These differences are determined based on whether constants and registers are
         being ignored.
        @param codeUnit1 the first code unit
        @param codeUnit2 the second code unit
        @return an array of operand indices where the operands differ between the two code units
         based on the current settings that indicate what differences can be ignored.
        """
        ...

    def hasCorrelation(self) -> bool:
        """
        Determines if this ListingDiff currently has an address correlation to use.
        @return true if it has an address correlation currently.
        """
        ...

    def hashCode(self) -> int: ...

    def isIgnoringByteDiffs(self) -> bool:
        """
        Gets the setting indicating if byte differences are currently being ignored.
        @return true if byte differences are being ignored.
        """
        ...

    def isIgnoringConstants(self) -> bool:
        """
        Gets the setting indicating if values of operand constants that differ are currently
         being ignored when determining code unit differences.
        @return true if code unit differences are ignoring differences in values of operand
         constants.
        """
        ...

    def isIgnoringRegisters(self) -> bool:
        """
        Gets the setting indicating if operand registers that differ other than in size
         are currently being ignored when determining code unit differences.
        @return true if code unit differences are ignoring operand register differences other
         than in size.
        """
        ...

    def notify(self) -> None: ...

    def notifyAll(self) -> None: ...

    def printFunctionComparisonDiffs(self) -> None:
        """
        Outputs an information message, primarily for debugging, that indicates where code was
         unmatched with the other listing and where various differences, such as bytes and
         code units, were found.
        """
        ...

    def removeListingDiffChangeListener(self, listener: ghidra.app.util.viewer.listingpanel.ListingDiffChangeListener) -> None:
        """
        Removes the indicated listener from those that get notified when the ListingDiff's set of
         differences and unmatched addresses changes.
        @param listener the listener to be removed
        """
        ...

    def setCorrelation(self, correlation: ghidra.program.util.ListingAddressCorrelation) -> None:
        """
        Sets the address correlation that is used to determine matching addresses between the two
         listings. Differences can then be determined where a matching address is found.
         <br>Important: This class is not intended to be used for an entire program. Instead it is
         for comparing smaller portions such as functions. If the correlation handed to this class
         associates two large address sets, then the address sets, such as byte differences, that are
         created by this class could potentially consume large amounts of memory.
        @param correlation the address correlation. Otherwise, null to clear the correlation.
        @throws MemoryAccessException if memory can't be read.
        """
        ...

    def setIgnoreByteDiffs(self, ignore: bool) -> None:
        """
        Changes the setting indicating whether or not byte differences should be ignored.
        @param ignore true indicates to ignore byte differences
        """
        ...

    def setIgnoreConstants(self, ignore: bool) -> None:
        """
        Changes the setting indicating if values of operand constants that differ should be
         ignored when determining code unit differences.
        @param ignore true means code unit differences should ignore differences in values of
         operand constants.
        """
        ...

    def setIgnoreRegisters(self, ignore: bool) -> None:
        """
        Changes the setting indicating if operand registers that differ other than in size
         should be ignored when determining code unit differences.
        @param ignore true means code unit differences should ignore operand register differences
         other than in size.
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
    def correlation(self) -> None: ...  # No getter available.

    @correlation.setter
    def correlation(self, value: ghidra.program.util.ListingAddressCorrelation) -> None: ...

    @property
    def ignoreByteDiffs(self) -> None: ...  # No getter available.

    @ignoreByteDiffs.setter
    def ignoreByteDiffs(self, value: bool) -> None: ...

    @property
    def ignoreConstants(self) -> None: ...  # No getter available.

    @ignoreConstants.setter
    def ignoreConstants(self, value: bool) -> None: ...

    @property
    def ignoreRegisters(self) -> None: ...  # No getter available.

    @ignoreRegisters.setter
    def ignoreRegisters(self, value: bool) -> None: ...

    @property
    def ignoringByteDiffs(self) -> bool: ...

    @property
    def ignoringConstants(self) -> bool: ...

    @property
    def ignoringRegisters(self) -> bool: ...

    @property
    def listing1ByteDiffs(self) -> ghidra.program.model.address.AddressSetView: ...

    @property
    def listing1CodeUnitDiffs(self) -> ghidra.program.model.address.AddressSetView: ...

    @property
    def listing1Diffs(self) -> ghidra.program.model.address.AddressSetView: ...

    @property
    def listing1UnmatchedCode(self) -> ghidra.program.model.address.AddressSetView: ...

    @property
    def listing2ByteDiffs(self) -> ghidra.program.model.address.AddressSetView: ...

    @property
    def listing2CodeUnitDiffs(self) -> ghidra.program.model.address.AddressSetView: ...

    @property
    def listing2Diffs(self) -> ghidra.program.model.address.AddressSetView: ...

    @property
    def listing2UnmatchedCode(self) -> ghidra.program.model.address.AddressSetView: ...
