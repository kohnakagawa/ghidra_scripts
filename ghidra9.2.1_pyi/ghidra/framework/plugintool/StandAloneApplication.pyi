from typing import List
import ghidra.framework.model
import ghidra.framework.plugintool
import java.lang
import javax.swing


class StandAloneApplication(object, ghidra.framework.plugintool.GenericStandAloneApplication):




    @overload
    def __init__(self, propertiesFilename: unicode):
        """
        Creates a new application using the given properties filename. The
         filename is expected reside in the current working directory.

         <p>
         <b>The given properties file is expected to have the
         {@link ApplicationProperties#APPLICATION_NAME_PROPERTY} and
         {@link ApplicationProperties#APPLICATION_VERSION_PROPERTY} properties
         set.</b>
        @param propertiesFilename the name of the properties file.
        """
        ...

    @overload
    def __init__(self, name: unicode, version: unicode): ...



    def equals(self, __a0: object) -> bool: ...

    def exit(self) -> None: ...

    def getClass(self) -> java.lang.Class: ...

    def getToolServices(self) -> ghidra.framework.model.ToolServices: ...

    def hashCode(self) -> int: ...

    def notify(self) -> None: ...

    def notifyAll(self) -> None: ...

    def setHomeCallback(self, callback: java.lang.Runnable) -> None: ...

    def setHomeIcon(self, icon: javax.swing.ImageIcon) -> None: ...

    def setWindowsIcons(self, __a0: List[object]) -> None: ...

    def showSpashScreen(self, splashIcon: javax.swing.ImageIcon) -> None: ...

    def start(self) -> None: ...

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
    def toolServices(self) -> ghidra.framework.model.ToolServices: ...

    @property
    def windowsIcons(self) -> None: ...  # No getter available.

    @windowsIcons.setter
    def windowsIcons(self, value: List[object]) -> None: ...
