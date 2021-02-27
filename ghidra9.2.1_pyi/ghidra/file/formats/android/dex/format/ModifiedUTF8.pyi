from typing import List
import java.io
import java.lang


class ModifiedUTF8(object):




    def __init__(self): ...



    @staticmethod
    def decode(__a0: java.io.InputStream, __a1: List[int]) -> unicode: ...

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
