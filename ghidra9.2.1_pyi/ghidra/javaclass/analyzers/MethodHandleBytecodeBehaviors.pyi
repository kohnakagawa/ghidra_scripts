import java.lang


class MethodHandleBytecodeBehaviors(object):
    REF_getField: int = 1
    REF_getStatic: int = 2
    REF_invokeInterface: int = 9
    REF_invokeSpecial: int = 7
    REF_invokeStatic: int = 6
    REF_invokeVirtual: int = 5
    REF_newInvokeSpecial: int = 8
    REF_putField: int = 3
    REF_putStatic: int = 4



    def __init__(self): ...



    def equals(self, __a0: object) -> bool: ...

    def getClass(self) -> java.lang.Class: ...

    @staticmethod
    def getName(__a0: int) -> unicode: ...

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
