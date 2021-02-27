import docking
import java.lang


class PluginToolMacAboutHandler(object):
    """
    A plugin-level about handler that serves as the callback from the Dock's 'About' popup action.
    """





    def __init__(self): ...



    def equals(self, __a0: object) -> bool: ...

    def getClass(self) -> java.lang.Class: ...

    def hashCode(self) -> int: ...

    @staticmethod
    def install(winMgr: docking.DockingWindowManager) -> None:
        """
        Applies an about handler which will show our custom about dialog.
        @param winMgr The docking window manager to use to install the about dialog.
        """
        ...

    def notify(self) -> None: ...

    def notifyAll(self) -> None: ...

    def toString(self) -> unicode: ...

    @overload
    def wait(self) -> None: ...

    @overload
    def wait(self, __a0: long) -> None: ...

    @overload
    def wait(self, __a0: long, __a1: int) -> None: ...
