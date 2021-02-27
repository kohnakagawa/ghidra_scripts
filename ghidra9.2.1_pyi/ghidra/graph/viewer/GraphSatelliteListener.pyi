import java.lang


class GraphSatelliteListener(object):
    """
    A listener to get notified of changes to the SatelliteGraphViewer
    """









    def equals(self, __a0: object) -> bool: ...

    def getClass(self) -> java.lang.Class: ...

    def hashCode(self) -> int: ...

    def notify(self) -> None: ...

    def notifyAll(self) -> None: ...

    def satelliteVisibilityChanged(self, docked: bool, visible: bool) -> None:
        """
        Called when the visibility and/or docked state of the watched satellite changes
        @param docked true if the satellite is now docked
        @param visible true if the satellite is now visible
        """
        ...

    def toString(self) -> unicode: ...

    @overload
    def wait(self) -> None: ...

    @overload
    def wait(self, __a0: long) -> None: ...

    @overload
    def wait(self, __a0: long, __a1: int) -> None: ...
