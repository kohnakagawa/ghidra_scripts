from typing import List
import java.lang


class StringRenderBuilder(object):
    """
    Helper class used to build up a formatted (for human consumption) string representation returned
     by Unicode and String data types.

     Call #toString() to retrieve the formatted string.

     Example (quotes are part of result):
    """

    DOUBLE_QUOTE: int = '"'
    SINGLE_QUOTE: int = "'"



    @overload
    def __init__(self, charSize: int): ...

    @overload
    def __init__(self, charSize: int, quoteChar: int): ...



    def addByteSeq(self, bytes: List[int]) -> None:
        """
        Add byte values, shown as numeric hex values.
         <p>
         {@literal { 0, 1, 2 } -> 00,01,02}
        @param bytes to convert to hex and append.  If null, append "???"
        """
        ...

    def addCodePointChar(self, codePoint: int) -> None:
        """
        Add a single character.  It will be shown in a quoted text region.
        @param codePoint Character to add
        """
        ...

    def addCodePointValue(self, codePoint: int) -> None:
        """
        Add a single character that needs to be shown as a numeric hex value.
        @param codePoint Character to add
        """
        ...

    def addEscapedChar(self, ch: int) -> None:
        """
        Append the specified char after an escaping backslash "\", ie
         {@literal "x" -> "\x";}
        @param ch
        """
        ...

    def addEscapedCodePoint(self, codePoint: int) -> None:
        """
        Add an unicode codepoint as its escaped hex value, with a escape character
         prefix of 'x', 'u' or 'U' depending on the magnitude of the codePoint value.
         <p>
         {@literal codePoint 15 -> '\' 'x' "0F"}<br>
         {@literal codePoint 65535 -> '\' 'u' "FFFF"}<br>
         {@literal codePoint 65536 -> '\' 'U' "10000"}<br>
        @param codePoint int value
        """
        ...

    def addString(self, str: unicode) -> None:
        """
        Append the characters in the specified string. The added characters will
         be shown in a quoted text region.
        @param str String to add
        """
        ...

    def equals(self, __a0: object) -> bool: ...

    def getClass(self) -> java.lang.Class: ...

    def hashCode(self) -> int: ...

    def notify(self) -> None: ...

    def notifyAll(self) -> None: ...

    def startsWithQuotedText(self) -> bool:
        """
        Returns true if the current formatted string starts with a quoted text section,
         instead of a byte value section.  Useful to indicate if
         the string could have a prefix applied to it (ie. u8"text")
         <p>
        @return boolean true if this string will start with a quoted text section
        """
        ...

    def toString(self) -> unicode:
        """
        Example (quotes are part of result): {@code "Test\tstring",01,02,"Second\npart",00}
         <p>
        @return Formatted string
        """
        ...

    @overload
    def wait(self) -> None: ...

    @overload
    def wait(self, __a0: long) -> None: ...

    @overload
    def wait(self, __a0: long, __a1: int) -> None: ...
