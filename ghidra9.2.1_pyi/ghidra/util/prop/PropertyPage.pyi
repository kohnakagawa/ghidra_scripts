import java.io
import java.lang


class PropertyPage(object, java.io.Serializable):
    """
    Manages property values of type int, String, Object, and
     "void"  for a page of possible addresses. Void serves as a marker
     for whether an address has a property. The derived class for each type holds
     the actual value of the property, and overrides the
     appropriate add() and get() methods.
    """









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
