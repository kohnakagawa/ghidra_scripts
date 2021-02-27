import java.lang


class DwarfSectionNames(object):




    def __init__(self, program: ghidra.program.model.listing.Program):
        """
        Creates a new Dwarf Section Names for the specific program.
        @param program the program containing dwarf debug information.
        @throws IllegalArgumentException if the program's format is not handled.
        """
        ...



    def SECTION_NAME_ABBREV(self) -> unicode:
        """
        Holds tag, attribute names, and attribute forms encodings
        """
        ...

    def SECTION_NAME_ARANGES(self) -> unicode:
        """
        A mapping between memory address and compilation
        """
        ...

    def SECTION_NAME_FRAME(self) -> unicode:
        """
        Holds information about call frame activations
        """
        ...

    def SECTION_NAME_INFO(self) -> unicode:
        """
        Debugging information entries for DWARF v2
        """
        ...

    def SECTION_NAME_LINE(self) -> unicode:
        """
        Line Number Program
        """
        ...

    def SECTION_NAME_LOC(self) -> unicode:
        """
        Location lists are used in place of location expressions whenever the object whose location is
         being described can change location during its lifetime. Location lists are contained in a separate
         object file section called .debug_loc. A location list is indicated by a location attribute
         whose value is represented as a constant offset from the beginning of the .debug_loc section
         to the first byte of the list for the object in question.
        """
        ...

    def SECTION_NAME_MACINFO(self) -> unicode:
        """
        A lookup table for global objects and functions
        """
        ...

    def SECTION_NAME_PUBNAMES(self) -> unicode:
        """
        A lookup table for global objects and functions
        """
        ...

    def SECTION_NAME_PUBTYPES(self) -> unicode:
        """
        A lookup table for global types
        """
        ...

    def SECTION_NAME_RANGES(self) -> unicode:
        """
        Address ranges referenced by DIEs
        """
        ...

    def SECTION_NAME_STR(self) -> unicode:
        """
        String table used by .debug_info
        """
        ...

    def equals(self, __a0: object) -> bool: ...

    def getClass(self) -> java.lang.Class: ...

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
