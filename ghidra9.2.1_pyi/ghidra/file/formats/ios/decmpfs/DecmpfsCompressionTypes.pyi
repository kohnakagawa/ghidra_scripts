import java.lang


class DecmpfsCompressionTypes(object):
    CMP_MAX: int = 255
    CMP_Type1: int = 1
    CMP_Type10: int = 10
    CMP_Type3: int = 3
    CMP_Type4: int = 4



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
