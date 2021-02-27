import java.lang


class VisualGraphActionContext(object):
    """
    Action context for VisualGraphs
    """









    def equals(self, __a0: object) -> bool: ...

    def getClass(self) -> java.lang.Class: ...

    def hashCode(self) -> int: ...

    def notify(self) -> None: ...

    def notifyAll(self) -> None: ...

    def shouldShowSatelliteActions(self) -> bool:
        """
        Returns true actions that manipulate the satellite viewer should be enabled for this context
        @return true actions that manipulate the satellite viewer should be enabled for this context
        """
        ...

    def toString(self) -> unicode: ...

    @overload
    def wait(self) -> None: ...

    @overload
    def wait(self, __a0: long) -> None: ...

    @overload
    def wait(self, __a0: long, __a1: int) -> None: ...
