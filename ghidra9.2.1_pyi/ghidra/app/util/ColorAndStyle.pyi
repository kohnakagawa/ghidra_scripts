import java.awt
import java.lang


class ColorAndStyle(object):
    """
    A container class to hold a color and a style value.
    """









    def equals(self, __a0: object) -> bool: ...

    def getClass(self) -> java.lang.Class: ...

    def getColor(self) -> java.awt.Color: ...

    def getStyle(self) -> int: ...

    def hashCode(self) -> int: ...

    def isBold(self) -> bool: ...

    def isItalic(self) -> bool: ...

    def notify(self) -> None: ...

    def notifyAll(self) -> None: ...

    def toHtml(self, text: unicode) -> unicode:
        """
        Wraps the given text with HTML markup for each attribute and color defined by this
         class.  The returned result will <b>not</b> be prepended with <code>&lt;HTML&gt;</code>.
        @param text the text to wrap
        @return the wrapped text
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
    def bold(self) -> bool: ...

    @property
    def color(self) -> java.awt.Color: ...

    @property
    def italic(self) -> bool: ...

    @property
    def style(self) -> int: ...
