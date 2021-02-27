import ghidra.program.model.address
import ghidra.program.model.listing
import ghidra.program.util
import java.lang
import javax.swing.text


class ProgramDiffDetails(object):
    """
    ProgramDiffDetails is used to determine the detailed differences between
     two programs at a particular address. The differences are determined for
     the extent of the code units from each program at a particular address.
    """

    BLUE: java.awt.Color
    DARK_CYAN: java.awt.Color
    GRAY: java.awt.Color
    GREEN: java.awt.Color
    MAROON: java.awt.Color
    OLIVE: java.awt.Color
    ORANGE: java.awt.Color
    PINK: java.awt.Color
    PURPLE: java.awt.Color
    RED: java.awt.Color
    YELLOW: java.awt.Color



    def __init__(self, p1: ghidra.program.model.listing.Program, p2: ghidra.program.model.listing.Program):
        """
        Constructor for ProgramDiffDetails.
        @param p1 the original program
        @param p2 the program to diff against.
        """
        ...



    def equals(self, __a0: object) -> bool: ...

    def getAllDetails(self, p1DiffAddress: ghidra.program.model.address.Address, doc: javax.swing.text.StyledDocument, prefixString: unicode) -> None:
        """
        Determine the detailed differences between the two programs at the
         indicated address. The differences are determined for the extent of the
         code units in the two programs at the indicated address.
        @param p1DiffAddress the address that difference details are needed for.
         This address should be derived from program1.
        @param doc the document where the details of differences between the two
         programs should be written.
        @param prefixString Line of text to display at beginning of the difference details information.
        """
        ...

    def getClass(self) -> java.lang.Class: ...

    def getDetails(self, p1DiffAddress: ghidra.program.model.address.Address, filter: ghidra.program.util.ProgramDiffFilter, doc: javax.swing.text.StyledDocument, prefixString: unicode) -> None:
        """
        Determine the detailed differences between the two programs at the
         indicated address. The differences are determined for the extent of the
         code units in the two programs at the indicated address.
        @param p1DiffAddress the address that difference details are needed for.
         This address should be derived from program1.
        @param filter the program diff filter that indicates the diff details to show.
        @param doc the document where the details of differences between the two
         programs should be written.
        @param prefixString Line of text to display at beginning of the difference details information.
        """
        ...

    def getDetailsAddressSet(self, p1Address: ghidra.program.model.address.Address) -> ghidra.program.model.address.AddressSetView:
        """
        Gets the address set where detailed differences will be determined for details at the
         indicated address. An address set is returned since the indicated address may be in different
         sized code units in each of the two programs.
        @param p1Address the current address where details are desired.
         This address may be from program1 or program2.
        @return the program1 address set for code units containing that address within the programs being diffed.
        """
        ...

    @overload
    def getDiffDetails(self, p1DiffAddress: ghidra.program.model.address.Address) -> unicode:
        """
        Gets a string indicating the types of differences for the code units at the indicated
         address. The string contains information from each program where there are differences.
         It containing multiple lines separated by newline characters)
        @param p1DiffAddress the address that difference details are needed for.
         This address should be derived from program1.
        @return a string indicating the differences.
        """
        ...

    @overload
    def getDiffDetails(self, p1DiffAddress: ghidra.program.model.address.Address, filter: ghidra.program.util.ProgramDiffFilter) -> unicode:
        """
        Gets a string indicating the types of differences for the code units at the indicated
         address. The string contains information from each program where there are differences.
         It containing multiple lines separated by newline characters)
        @param p1DiffAddress the address that difference details are needed for.
         This address should be derived from program1.
        @param filter the program diff filter that indicates the diff details to show.
        @return a string indicating the differences.
        """
        ...

    @overload
    @staticmethod
    def getDiffDetails(p1: ghidra.program.model.listing.Program, p2: ghidra.program.model.listing.Program, p1DiffAddress: ghidra.program.model.address.Address) -> unicode:
        """
        Gets a string indicating the types of differences for the code units at the indicated
         address. The string contains information from each program where there are differences.
         It containing multiple lines separated by newline characters)
        @param p1 the original program
        @param p2 the program to diff against.
        @param p1DiffAddress the address that difference details are needed for.
         This address should be derived from program1.
        @return a string indicating the differences.
        """
        ...

    @overload
    @staticmethod
    def getDiffDetails(p1: ghidra.program.model.listing.Program, p2: ghidra.program.model.listing.Program, p1DiffAddress: ghidra.program.model.address.Address, filter: ghidra.program.util.ProgramDiffFilter) -> unicode:
        """
        Gets a string indicating the types of differences for the code units at the indicated
         address. The string contains information from each program where there are differences.
         It containing multiple lines separated by newline characters)
        @param p1 the original program
        @param p2 the program to diff against.
        @param p1DiffAddress the address that difference details are needed for.
         This address should be derived from program1.
        @param filter the program diff filter that indicates the diff details to show.
        @return a string indicating the differences.
        """
        ...

    def hashCode(self) -> int: ...

    def notify(self) -> None: ...

    def notifyAll(self) -> None: ...

    def toString(self) -> unicode: ...

    @overload
    def wait(self) -> None: ...

    @overload
    def wait(self, __a0: long) -> None: ...

    @overload
    def wait(self, __a0: long, __a1: int) -> None: ...
