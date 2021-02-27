import java.lang


class Apple8900Constants(object):
    AES_IV_ZERO_BYTES: List[int] = array('b', [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0])
    AES_KEY_BYTES: List[int] = array('b', [24, -124, 88, -90, -47, 80, 52, -33, -29, -122, -14, 59, 97, -44, 55, 116])
    AES_KEY_STRING: unicode = u'188458A6D15034DFE386F23B61D43774'
    FORMAT_ENCRYPTED: int = 3
    FORMAT_PLAIN: int = 4
    MAGIC: unicode = u'8900'
    MAGIC_BYTES: List[int] = array('b', [56, 57, 48, 48])
    MAGIC_LENGTH: int = 4



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
