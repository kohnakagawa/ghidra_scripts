import java.lang


class MutableLong(object):




    @overload
    def __init__(self): ...

    @overload
    def __init__(self, __a0: long): ...



    def add(self, __a0: long) -> None: ...

    def equals(self, __a0: object) -> bool: ...

    def get(self) -> long: ...

    def getClass(self) -> java.lang.Class: ...

    def hashCode(self) -> int: ...

    def increment(self) -> None: ...

    def notify(self) -> None: ...

    def notifyAll(self) -> None: ...

    def set(self, __a0: long) -> None: ...

    def toString(self) -> unicode: ...

    @overload
    def wait(self) -> None: ...

    @overload
    def wait(self, __a0: long) -> None: ...

    @overload
    def wait(self, __a0: long, __a1: int) -> None: ...
