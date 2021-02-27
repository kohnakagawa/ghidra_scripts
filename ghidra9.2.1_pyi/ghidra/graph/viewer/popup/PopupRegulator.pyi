import java.lang


class PopupRegulator(object):
    """
    A class to control popups for graph clients, bypassing Java's default tool tip mechanism
    """





    def __init__(self, popupSupplier: ghidra.graph.viewer.popup.PopupSource): ...



    def equals(self, __a0: object) -> bool: ...

    def getClass(self) -> java.lang.Class: ...

    def hashCode(self) -> int: ...

    def isPopupShowing(self) -> bool:
        """
        Returns true if this class's popup is showing
        @return true if this class's popup is showing
        """
        ...

    def notify(self) -> None: ...

    def notifyAll(self) -> None: ...

    def setPopupDelay(self, delayMs: int) -> None:
        """
        Sets the time between mouse movements to wait before showing this class's popup
        @param delayMs the delay
        """
        ...

    def setPopupsVisible(self, visible: bool) -> None:
        """
        Sets the enablement of this class's popup
        @param visible true to have popups enabled
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
    def popupDelay(self) -> None: ...  # No getter available.

    @popupDelay.setter
    def popupDelay(self, value: int) -> None: ...

    @property
    def popupShowing(self) -> bool: ...

    @property
    def popupsVisible(self) -> None: ...  # No getter available.

    @popupsVisible.setter
    def popupsVisible(self, value: bool) -> None: ...
