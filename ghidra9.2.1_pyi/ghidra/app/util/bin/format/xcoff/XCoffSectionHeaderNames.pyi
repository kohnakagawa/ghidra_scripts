import java.lang


class XCoffSectionHeaderNames(object):
    """
    Names of "special" sections.
    """

    _BSS: unicode = u'.bss'
    _DATA: unicode = u'.data'
    _DEBUG: unicode = u'.debug'
    _EXCEPT: unicode = u'.except'
    _INFO: unicode = u'.info'
    _LOADER: unicode = u'.loader'
    _OVRFLO: unicode = u'.ovrflo'
    _PAD: unicode = u'.pad'
    _TEXT: unicode = u'.text'
    _TYPCHK: unicode = u'.typchk'



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
