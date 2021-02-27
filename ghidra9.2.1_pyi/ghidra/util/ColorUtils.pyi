import java.awt
import java.lang


class ColorUtils(object):
    HUE_BLUE: float = 0.6666666865348816
    HUE_GREEN: float = 0.3333333432674408
    HUE_LIME: float = 0.25
    HUE_ORANGE: float = 0.0833333358168602
    HUE_PINE: float = 0.4166666567325592
    HUE_PINK: float = 0.9166666865348816
    HUE_PURPLE: float = 0.8333333134651184
    HUE_RED: float = 0.0
    HUE_ROYAL: float = 0.75
    HUE_SAPPHIRE: float = 0.5833333134651184
    HUE_TURQUISE: float = 0.5
    HUE_YELLOW: float = 0.1666666716337204



    def __init__(self): ...



    @staticmethod
    def blend(c1: java.awt.Color, c2: java.awt.Color, ratio: float) -> java.awt.Color:
        """
        Takes the first color, blending into it the second color, using the given ratio.  A
         lower ratio (say .1f) signals to use very little of the first color; a larger ratio
         signals to use more of the first color.
        @param c1 the first color
        @param c2 the second color
        @param ratio the amount of the first color to include in the final output
        @return the new color
        """
        ...

    @staticmethod
    def contrastForegroundColor(color: java.awt.Color) -> java.awt.Color:
        """
        A method to produce a color (either black or white) that contrasts with the given color.
         This is useful for finding a readable foreground color for a given background.
        @param color the color for which to find a contrast.
        @return the contrasting color.
        """
        ...

    @overload
    @staticmethod
    def deriveBackground(background: java.awt.Color, hue: float) -> java.awt.Color: ...

    @overload
    @staticmethod
    def deriveBackground(src: java.awt.Color, hue: float, sfact: float, bfact: float) -> java.awt.Color: ...

    @overload
    @staticmethod
    def deriveForeground(bg: java.awt.Color, hue: float) -> java.awt.Color: ...

    @overload
    @staticmethod
    def deriveForeground(bg: java.awt.Color, hue: float, brt: float) -> java.awt.Color: ...

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
