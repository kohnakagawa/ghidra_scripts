import docking.widgets.fieldpanel.listener
import java.lang


class AddressBasedIndexMapper(object, docking.widgets.fieldpanel.listener.IndexMapper):
    """
    Implementation of IndexMapper that uses an old and new AddressIndexMap to map indexes
      when the AddressIndexMap changes.
    """

    IDENTITY_MAPPER: docking.widgets.fieldpanel.listener.IndexMapper = docking.widgets.fieldpanel.listener.IndexMapper$1@4e239a1d



    def __init__(self, from_: ghidra.app.util.viewer.util.AddressIndexMap, to: ghidra.app.util.viewer.util.AddressIndexMap): ...



    def equals(self, __a0: object) -> bool: ...

    def getClass(self) -> java.lang.Class: ...

    def hashCode(self) -> int: ...

    def map(self, value: long) -> long: ...

    def notify(self) -> None: ...

    def notifyAll(self) -> None: ...

    def toString(self) -> unicode: ...

    @overload
    def wait(self) -> None: ...

    @overload
    def wait(self, __a0: long) -> None: ...

    @overload
    def wait(self, __a0: long, __a1: int) -> None: ...
