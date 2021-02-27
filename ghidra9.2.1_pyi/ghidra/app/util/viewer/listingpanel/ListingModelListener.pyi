import java.lang


class ListingModelListener(object):








    def dataChanged(self, updateImmediately: bool) -> None:
        """
        Called when the data at an index or range of indexes changes.
        @param updateImmediately true to immediately update the listing upon change.
        """
        ...

    def equals(self, __a0: object) -> bool: ...

    def getClass(self) -> java.lang.Class: ...

    def hashCode(self) -> int: ...

    def modelSizeChanged(self) -> None:
        """
        Called whenever the number of indexes changed
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
