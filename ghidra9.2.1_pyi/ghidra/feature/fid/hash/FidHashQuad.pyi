import java.lang


class FidHashQuad(object):








    def equals(self, __a0: object) -> bool: ...

    def getClass(self) -> java.lang.Class: ...

    def getCodeUnitSize(self) -> int: ...

    def getFullHash(self) -> long: ...

    def getSpecificHash(self) -> long: ...

    def getSpecificHashAdditionalSize(self) -> int: ...

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

    @property
    def codeUnitSize(self) -> int: ...

    @property
    def fullHash(self) -> long: ...

    @property
    def specificHash(self) -> long: ...

    @property
    def specificHashAdditionalSize(self) -> int: ...
