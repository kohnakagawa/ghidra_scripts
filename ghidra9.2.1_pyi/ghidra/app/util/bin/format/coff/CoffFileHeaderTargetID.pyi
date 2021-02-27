import java.lang


class CoffFileHeaderTargetID(object):
    TIC27X_TARGET_ID: int = 157
    TIC2xx_TARGET_ID: int = 146
    TIC54X_TARGET_ID: int = 152
    TIC55X_TARGET_ID: int = 156
    TIC5X_TARGET_ID: int = 146
    TIC64X_TARGET_ID: int = 153
    TIC80_TARGET_ID: int = 149



    def __init__(self): ...



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
