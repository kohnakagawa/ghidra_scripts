import ghidra.program.model.address
import java.lang


class ConflictUtility(object):
    """
    ConflictUtility provides some constants and static methods
     used by the Listing Merge portion of the multi-user merge.
     For now, the VariousChoicesPanel and VerticalChoicesPanel use HTML in
     JLabels to display color etc. This is because they also show radiobuttons
     and checkboxes.
    """

    ADDRESS_COLOR: unicode
    BLUE: unicode
    DARK_CYAN: unicode
    EMPHASIZE_COLOR: unicode
    GRAY: unicode
    GREEN: unicode
    MAROON: unicode
    NO_VALUE: unicode
    NUMBER_COLOR: unicode
    OFFSET_COLOR: unicode
    OLIVE: unicode
    ORANGE: unicode
    PINK: unicode
    PURPLE: unicode
    YELLOW: unicode



    def __init__(self): ...



    @staticmethod
    def addAddress(buf: java.lang.StringBuffer, addr: ghidra.program.model.address.Address) -> None:
        """
        Adds a color program address to the indicated string buffer.
        @param buf the string buffer
        @param addr the program address
        """
        ...

    @staticmethod
    def addCount(buf: java.lang.StringBuffer, value: int) -> None:
        """
        Adds a color number to the indicated string  buffer.
        @param buf the string buffer
        @param value the integer number
        """
        ...

    @overload
    @staticmethod
    def colorString(rgbColor: unicode, value: int) -> unicode:
        """
        This creates a colored number by converting the number to a string and
         wrapping it with an HTML font tag that has a color attribute.
        @param rgbColor (eg. "#8c0000")
        @param value the integer number
        @return the tagged string.
        """
        ...

    @overload
    @staticmethod
    def colorString(rgbColor: unicode, text: unicode) -> unicode:
        """
        This creates color text by wrapping a text string with an HTML font tag
         that has a color attribute.
        @param rgbColor (eg. "#8c0000")
        @param text the text to be colored
        @return the tagged string.
        """
        ...

    def equals(self, __a0: object) -> bool: ...

    @staticmethod
    def getAddressConflictCount(addressNum: int, totalAddresses: int, isRange: bool) -> unicode:
        """
        Creates a standard address set conflict count message. This indicates
         which address or address range with conflicts you are resolving of some
         total number of addresses or address ranges with conflicts.
        @param addressNum the current conflicting address number.
        @param totalAddresses the total number of conflicting addresses.
        @param isRange true if the current conflict is for an address range.
        @return the message string containing HTML tags.
        """
        ...

    @overload
    @staticmethod
    def getAddressString(address: ghidra.program.model.address.Address) -> unicode:
        """
        Creates a string containing HTML tags to represent the address in color.
        @param address the program address.
        @return the message string containing HTML tags.
        """
        ...

    @overload
    @staticmethod
    def getAddressString(address: ghidra.program.model.address.Address, showAddressSpace: bool) -> unicode:
        """
        Creates a string containing HTML tags to represent the address in color.
        @param address the program address.
        @param showAddressSpace true indicates the address string should show the address space.
        @return the message string containing HTML tags.
        """
        ...

    def getClass(self) -> java.lang.Class: ...

    @overload
    @staticmethod
    def getConflictCount(conflictNum: int, totalConflicts: int) -> unicode:
        """
        Creates a standard conflict count message. This indicates which conflict
         you are resolving of some total number of conflicts.
        @param conflictNum the current conflict number.
        @param totalConflicts the total number of conflicts
        @return the message string containing HTML tags.
        """
        ...

    @overload
    @staticmethod
    def getConflictCount(conflictNum: int, totalConflicts: int, addr: ghidra.program.model.address.Address) -> unicode:
        """
        Creates a standard conflict count message for an address. This indicates which conflict
         you are resolving of some total number of conflicts at a given address.
        @param conflictNum the current conflict number.
        @param totalConflicts the total number of conflicts
        @param addr the address for the indicated conflicts.
        @return the message string containing HTML tags.
        """
        ...

    @overload
    @staticmethod
    def getConflictCount(conflictNum: int, totalConflicts: int, range: ghidra.program.model.address.AddressRange) -> unicode:
        """
        Creates a standard conflict count message for an address range. This indicates which conflict
         you are resolving of some total number of conflicts for a given address range.
        @param conflictNum the current conflict number.
        @param totalConflicts the total number of conflicts
        @param range the address range for the indicated conflicts.
        @return the message string containing HTML tags.
        """
        ...

    @staticmethod
    def getEmphasizeString(text: unicode) -> unicode:
        """
        Creates a string containing HTML tags to represent the text in color for emphasis.
        @param text the text to be emphasized.
        @return the message string containing HTML tags.
        """
        ...

    @staticmethod
    def getHashString(hash: long) -> unicode:
        """
        Creates a string containing HTML tags to represent the hash value in
         color as an unsigned hexadecimal value.
        @param hash the hash to be displayed in hexadecimal
        @return the message string containing HTML tags.
        """
        ...

    @staticmethod
    def getNumberString(count: int) -> unicode:
        """
        Creates a string containing HTML tags to represent the integer number in color.
        @param count the integer number
        @return the message string containing HTML tags.
        """
        ...

    @staticmethod
    def getOffsetString(offset: int) -> unicode:
        """
        Creates a string containing HTML tags to represent the offset value in
         color as a hexadecimal value.
        @param offset the offset to be displayed in hexadecimal
        @return the message string containing HTML tags.
        """
        ...

    @staticmethod
    def getTruncatedHTMLString(originalString: unicode, truncLength: int) -> unicode:
        """
        Surrounds the originalString with HTML tags. It truncates the string at
         truncLength number of characters and adds "..." if it is longer than truncLength.
         It also replaces newline characters with HTML break tags.
         <br>
         Warning: The originalString should not contain special HTML tags. If it does,
         they may get truncated in the middle of a tag.
        @param originalString
        @param truncLength truncate at this length
        @return the truncated message string containing HTML tags.
        """
        ...

    def hashCode(self) -> int: ...

    def notify(self) -> None: ...

    def notifyAll(self) -> None: ...

    @staticmethod
    def spaces(num: int) -> unicode:
        """
        Creates a string for the number of spaces indicated that can be used in HTML.
         This string can be used to preserve spacing.
        @param num the number of spaces
        @return the string representing that many spaces in HTML.
        """
        ...

    def toString(self) -> unicode: ...

    @overload
    def wait(self) -> None: ...

    @overload
    def wait(self, __a0: long) -> None: ...

    @overload
    def wait(self, __a0: long, __a1: int) -> None: ...

    @staticmethod
    def wrapAsHTML(text: unicode) -> unicode:
        """
        Puts HTML and BODY tags around the string.
        """
        ...
