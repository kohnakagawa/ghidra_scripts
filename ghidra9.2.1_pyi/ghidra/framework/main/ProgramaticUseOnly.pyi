import java.lang


class ProgramaticUseOnly(object):
    """
    Marker interface for plugins that only get constructed programatically for specific purposes.
     Plugins that implement this interface should never be added via the config GUIs.
    """









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
