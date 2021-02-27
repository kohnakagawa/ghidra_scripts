import java.lang


class KeyedObject(object):
    """
    The KeyedObject class is used as a base class for objects which have keys.
      Some specific examples of KeyedObject are Vertex and Edge.
    """









    def equals(self, __a0: object) -> bool: ...

    def getClass(self) -> java.lang.Class: ...

    def hashCode(self) -> int: ...

    def key(self) -> long:
        """
        Returns the key for this KeyedObject.
        """
        ...

    def notify(self) -> None: ...

    def notifyAll(self) -> None: ...

    def toString(self) -> unicode: ...

    @overload
    def wait(self) -> None: ...

    @overload
    def wait(self, __a0: long) -> None: ...

    @overload
    def wait(self, __a0: long, __a1: int) -> None: ...
