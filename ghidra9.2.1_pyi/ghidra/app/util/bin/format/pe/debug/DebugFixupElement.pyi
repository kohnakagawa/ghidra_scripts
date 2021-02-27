import java.lang


class DebugFixupElement(object):
    """
    A possible implementation of the FIXUP debug directory elements.
     It may be inaccurate and/or incomplete.
    """





    def __init__(self):
        """
        DO NOT USE THIS CONSTRUCTOR, USE create*(GenericFactory ...) FACTORY METHODS INSTEAD.
        """
        ...



    def equals(self, __a0: object) -> bool: ...

    def getAddress1(self) -> int:
        """
        Returns the first address of this FIXUP element.
        @return the first address of this FIXUP element
        """
        ...

    def getAddress2(self) -> int:
        """
        Returns the second address of this FIXUP element.
        @return the second address of this FIXUP element
        """
        ...

    def getClass(self) -> java.lang.Class: ...

    def getType(self) -> int:
        """
        Returns the FIXUP element type.
        @return the FIXUP element type
        """
        ...

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
    def address1(self) -> int: ...

    @property
    def address2(self) -> int: ...

    @property
    def type(self) -> int: ...
