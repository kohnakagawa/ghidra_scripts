from typing import List
import java.lang
import javax.swing.plaf


class DockingWindowsLookAndFeelUtils(object):
    """
    A utility class to manage LookAndFeel (LaF) settings.
    """

    LAST_LOOK_AND_FEEL_KEY: unicode = u'LastLookAndFeel'
    METAL_LOOK_AND_FEEL: unicode = u'Metal'
    USE_INVERTED_COLORS_KEY: unicode = u'LookAndFeel.UseInvertedColors'







    def equals(self, __a0: object) -> bool: ...

    def getClass(self) -> java.lang.Class: ...

    @staticmethod
    def getInstalledLookAndFeelName() -> unicode:
        """
        Returns the currently installed LaF.
        @return the currently installed LaF.
        """
        ...

    @staticmethod
    def getLookAndFeelNames() -> List[unicode]:
        """
        Returns all installed LaFs.  This will vary by OS.
        @return all installed LaFs.
        """
        ...

    @staticmethod
    def getUseInvertedColorsPreference() -> bool:
        """
        Returns the {@link Preferences} value for whether to use inverted colors when paiting.
        @return the {@link Preferences} value for whether to use inverted colors when paiting.
        """
        ...

    def hashCode(self) -> int: ...

    @staticmethod
    def isUsingAquaUI(UI: javax.swing.plaf.ComponentUI) -> bool:
        """
        Returns true if the given UI object is using the Aqua Look and Feel.
        @param UI the UI to examine.
        @return true if the UI is using Aqua
        """
        ...

    @staticmethod
    def isUsingNimbusUI() -> bool:
        """
        Returns true if 'Nimbus' is the current Look and Feel
        @return true if 'Nimbus' is the current Look and Feel
        """
        ...

    @staticmethod
    def loadFromPreferences() -> None:
        """
        Loads settings from {@link Preferences}.
        """
        ...

    def notify(self) -> None: ...

    def notifyAll(self) -> None: ...

    @staticmethod
    def setLookAndFeel(lookAndFeelName: unicode) -> None:
        """
        Set the look and feel (LAF) indicated by the string passed in as a parameter.
         The string value can be either the class name of the LAF, as returned by
         <code>LookAndFeelInfo.getClassName()</code> or the name as returned by
         <code>LookAndFeelInfo.getName()</code>.
         <p>
         Note: to be effective, this call needs to be made before any components have been created
         and shown.
        @param lookAndFeelName the string indicating which look and feel is desired (see above)
        """
        ...

    @staticmethod
    def setUseInvertedColors(useInvertedColors: bool) -> None: ...

    def toString(self) -> unicode: ...

    @overload
    def wait(self) -> None: ...

    @overload
    def wait(self, __a0: long) -> None: ...

    @overload
    def wait(self, __a0: long, __a1: int) -> None: ...
