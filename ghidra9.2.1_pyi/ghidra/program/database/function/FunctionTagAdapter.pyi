import java.lang


class FunctionTagAdapter(object):
    """
    This represents a table that stores all possible function tags available for use.
     The table consists of two columns: one for the tag name, and one indicating
     whether this tag is modifiable.

     Non-modifiable tags cannot be deleted or edited by any user. These are typically
     tags that have been pre-loaded via some external mechanism and need to be
     preserved as originally defined.
    """





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
