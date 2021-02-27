from typing import List
import docking.framework
import ghidra.util
import java.awt
import java.lang
import javax.swing


class SettableApplicationInformationDisplayFactory(docking.framework.ApplicationInformationDisplayFactory):




    def __init__(self): ...



    @staticmethod
    def createAboutComponent() -> javax.swing.JComponent: ...

    @staticmethod
    def createAboutTitle() -> unicode: ...

    @staticmethod
    def createHelpLocation() -> ghidra.util.HelpLocation: ...

    @staticmethod
    def createSplashScreenComponent() -> javax.swing.JComponent: ...

    @staticmethod
    def createSplashScreenTitle() -> unicode: ...

    def doGetHomeIcon(self) -> javax.swing.ImageIcon: ...

    def equals(self, __a0: object) -> bool: ...

    def getClass(self) -> java.lang.Class: ...

    @staticmethod
    def getHomeCallback() -> java.lang.Runnable: ...

    @staticmethod
    def getHomeIcon() -> javax.swing.ImageIcon: ...

    @staticmethod
    def getLargestWindowIcon() -> java.awt.Image: ...

    @staticmethod
    def getWindowIcons() -> List[java.awt.Image]: ...

    def hashCode(self) -> int: ...

    def notify(self) -> None: ...

    def notifyAll(self) -> None: ...

    def setHomeCallback(self, callback: java.lang.Runnable) -> None: ...

    def setHomeIcon(self, icon: javax.swing.ImageIcon) -> None: ...

    def setSplashIcon128(self, splashIcon: javax.swing.ImageIcon) -> None: ...

    def setWindowsIcons(self, __a0: List[object]) -> None: ...

    def toString(self) -> unicode: ...

    @overload
    def wait(self) -> None: ...

    @overload
    def wait(self, __a0: long) -> None: ...

    @overload
    def wait(self, __a0: long, __a1: int) -> None: ...

    @property
    def homeCallback(self) -> None: ...  # No getter available.

    @homeCallback.setter
    def homeCallback(self, value: java.lang.Runnable) -> None: ...

    @property
    def homeIcon(self) -> None: ...  # No getter available.

    @homeIcon.setter
    def homeIcon(self, value: javax.swing.ImageIcon) -> None: ...

    @property
    def splashIcon128(self) -> None: ...  # No getter available.

    @splashIcon128.setter
    def splashIcon128(self, value: javax.swing.ImageIcon) -> None: ...

    @property
    def windowsIcons(self) -> None: ...  # No getter available.

    @windowsIcons.setter
    def windowsIcons(self, value: List[object]) -> None: ...
