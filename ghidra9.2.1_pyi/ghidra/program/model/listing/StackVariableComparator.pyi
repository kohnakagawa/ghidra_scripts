import ghidra.program.model.listing
import java.lang
import java.util
import java.util.function


class StackVariableComparator(object, java.util.Comparator):
    """
    Compares stack variable offsets; has a static factory method to get
     a StackVariableComparator.
    """





    def __init__(self): ...



    def compare(self, obj1: object, obj2: object) -> int:
        """
        Compares a stack variable offsets. One or both objects must be
         a StackVariable.
        @param obj1 a StackVariable or Integer
        @param obj2 a StackVariable or Integer
         <P>
        @return a negative integer, zero, or a positive integer
          if the first argument is less than, equal to, or greater than the second.
        """
        ...

    @overload
    @staticmethod
    def comparing(__a0: java.util.function.Function) -> java.util.Comparator: ...

    @overload
    @staticmethod
    def comparing(__a0: java.util.function.Function, __a1: java.util.Comparator) -> java.util.Comparator: ...

    @staticmethod
    def comparingDouble(__a0: java.util.function.ToDoubleFunction) -> java.util.Comparator: ...

    @staticmethod
    def comparingInt(__a0: java.util.function.ToIntFunction) -> java.util.Comparator: ...

    @staticmethod
    def comparingLong(__a0: java.util.function.ToLongFunction) -> java.util.Comparator: ...

    def equals(self, __a0: object) -> bool: ...

    @staticmethod
    def get() -> ghidra.program.model.listing.StackVariableComparator:
        """
        Returns a shared instance of a StackVariableComparator.
        """
        ...

    def getClass(self) -> java.lang.Class: ...

    def hashCode(self) -> int: ...

    @staticmethod
    def naturalOrder() -> java.util.Comparator: ...

    def notify(self) -> None: ...

    def notifyAll(self) -> None: ...

    @staticmethod
    def nullsFirst(__a0: java.util.Comparator) -> java.util.Comparator: ...

    @staticmethod
    def nullsLast(__a0: java.util.Comparator) -> java.util.Comparator: ...

    @staticmethod
    def reverseOrder() -> java.util.Comparator: ...

    def reversed(self) -> java.util.Comparator: ...

    @overload
    def thenComparing(self, __a0: java.util.Comparator) -> java.util.Comparator: ...

    @overload
    def thenComparing(self, __a0: java.util.function.Function) -> java.util.Comparator: ...

    @overload
    def thenComparing(self, __a0: java.util.function.Function, __a1: java.util.Comparator) -> java.util.Comparator: ...

    def thenComparingDouble(self, __a0: java.util.function.ToDoubleFunction) -> java.util.Comparator: ...

    def thenComparingInt(self, __a0: java.util.function.ToIntFunction) -> java.util.Comparator: ...

    def thenComparingLong(self, __a0: java.util.function.ToLongFunction) -> java.util.Comparator: ...

    def toString(self) -> unicode: ...

    @overload
    def wait(self) -> None: ...

    @overload
    def wait(self, __a0: long) -> None: ...

    @overload
    def wait(self, __a0: long, __a1: int) -> None: ...
