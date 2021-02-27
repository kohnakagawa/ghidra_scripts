import java.lang


class FileCacheEntry(object):
    """
    Simple class that contains a File and its MD5 string.
    """

    file: java.io.File
    md5: unicode



    def __init__(self, file: java.io.File, md5: unicode): ...



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
