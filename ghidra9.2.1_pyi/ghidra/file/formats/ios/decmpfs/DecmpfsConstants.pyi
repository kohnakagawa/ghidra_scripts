import java.lang


class DecmpfsConstants(object):
    DECMPFS_MAGIC: unicode = u'fpmc'
    DECMPFS_MAGIC_BYTES: List[int] = array('b', [102, 112, 109, 99])
    MAX_DECMPFS_XATTR_SIZE: int = 3802



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
