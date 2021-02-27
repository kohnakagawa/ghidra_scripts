import java.lang


class DecompiledFunction(object):
    """
    A class to hold pieces of a decompiled function.
    """





    def __init__(self, signature: unicode, c: unicode):
        """
        Constructs a new decompiled function.
        @param signature the function signature or prototype (eg, "int foo(double d)")
        @param c the complete C code of the function.
        """
        ...



    def equals(self, __a0: object) -> bool: ...

    def getC(self) -> unicode:
        """
        Returns the complete C code of the function.
        @return the complete C code of the function
        """
        ...

    def getClass(self) -> java.lang.Class: ...

    def getSignature(self) -> unicode:
        """
        Returns the function signature or prototype (eg, "int foo(double d)").
        @return the function signature or prototype (eg, "int foo(double d)")
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
    def c(self) -> unicode: ...

    @property
    def signature(self) -> unicode: ...
