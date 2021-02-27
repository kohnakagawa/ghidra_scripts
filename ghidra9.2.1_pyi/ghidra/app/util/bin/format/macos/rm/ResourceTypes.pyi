import java.lang


class ResourceTypes(object):
    TYPE_CFRG: int = 1667658343
    TYPE_ICON: int = 1229147683
    TYPE_STR_POUND: int = 1398034979
    TYPE_STR_SPACE: int = 1398034976







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
