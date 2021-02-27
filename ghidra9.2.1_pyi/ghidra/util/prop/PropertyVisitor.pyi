import ghidra.util
import java.lang


class PropertyVisitor(object):
    """
    PropertyVisitor is an interface for use with user defined
     properties when you know the name of the property but not its
     type.
    """









    def equals(self, __a0: object) -> bool: ...

    def getClass(self) -> java.lang.Class: ...

    def hashCode(self) -> int: ...

    def notify(self) -> None: ...

    def notifyAll(self) -> None: ...

    def toString(self) -> unicode: ...

    @overload
    def visit(self) -> None:
        """
        Handle the case of a void property type.
        """
        ...

    @overload
    def visit(self, value: int) -> None:
        """
        Handle the case of an int property type.
        """
        ...

    @overload
    def visit(self, value: unicode) -> None:
        """
        Handle the case of a String property type.
        """
        ...

    @overload
    def visit(self, value: ghidra.util.Saveable) -> None:
        """
        Handle the case of a Saveable property type
        """
        ...

    @overload
    def visit(self, value: object) -> None:
        """
        Handle the case of an Object property type.
        """
        ...

    @overload
    def wait(self) -> None: ...

    @overload
    def wait(self, __a0: long) -> None: ...

    @overload
    def wait(self, __a0: long, __a1: int) -> None: ...
