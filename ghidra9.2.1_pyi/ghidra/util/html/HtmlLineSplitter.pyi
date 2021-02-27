from typing import List
import java.lang


class HtmlLineSplitter(object):
    """
    Splits into lines a given String that is meant to be rendered as HTML.

     Really, this class exists simply to remove hundreds of lines of code from
     HTMLUtilities, which is what this code supports.  The methods in here could easily
     be in StringUtils, but to keep dependencies low on code that has such a specific use,
     it lives here, with a name that implies you shouldn't use it unless you are working with
     HTML.
    """

    MAX_WORD_LENGTH: int = 10



    def __init__(self): ...



    def equals(self, __a0: object) -> bool: ...

    def getClass(self) -> java.lang.Class: ...

    def hashCode(self) -> int: ...

    def notify(self) -> None: ...

    def notifyAll(self) -> None: ...

    @overload
    @staticmethod
    def split(text: unicode, maxLineLength: int) -> List[unicode]:
        """
        Splits the given line into multiple lines based upon the given max length.  This method
         will first split on each newline and then wrap each of the lines returned from that split.

         <P>The wrapping routine will attempt to wrap at word boundaries.

         <P>This method does not retain leading whitespace.
        @param text the text to wrap
        @param maxLineLength the max desired length of each output line; 0 or less signals not
                to wrap the line based upon length
        @return the new lines
        @see #wrap(String, int, WhitespaceHandler)
        @see #split(String, int, boolean)
        """
        ...

    @overload
    @staticmethod
    def split(text: unicode, maxLineLength: int, retainSpacing: bool) -> List[unicode]:
        """
        Splits the given line into multiple lines based upon the given max length.  This method
         will first split on each newline and then wrap each of the lines returned from that split.

         <P>The wrapping routine will attempt to wrap at word boundaries.
        @param text the text to wrap
        @param maxLineLength the max desired length of each output line; 0 or less signals not
                to wrap the line based upon length
        @param retainSpacing true signals to keep whitespace on line breaks; false discards
                leading whitespace
        @return the new lines
        @see #wrap(String, int, WhitespaceHandler)
        """
        ...

    def toString(self) -> unicode: ...

    @overload
    def wait(self) -> None: ...

    @overload
    def wait(self, __a0: long) -> None: ...

    @overload
    def wait(self, __a0: long, __a1: int) -> None: ...
