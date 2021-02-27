import java.lang


class GnuConstants(object):
    """
    GNU Constants.
    """

    VER_NDX_ELIMINATE: int = -255
    VER_NDX_GLOBAL: int = 1
    VER_NDX_LOCAL: int = 0
    VER_NDX_LORESERVE: int = -256







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
