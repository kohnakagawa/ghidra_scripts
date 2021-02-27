import java.lang


class DmgConstants(object):
    DMG_MAGIC_BYTES_v1: List[int] = array('b', [99, 100, 115, 97, 101, 110, 99, 114])
    DMG_MAGIC_BYTES_v2: List[int] = array('b', [101, 110, 99, 114, 99, 100, 115, 97])
    DMG_MAGIC_LENGTH: int = 8



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
