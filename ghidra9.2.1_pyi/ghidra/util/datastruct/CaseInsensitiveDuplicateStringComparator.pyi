import java.lang
import java.util
import java.util.function


class CaseInsensitiveDuplicateStringComparator(object, java.util.Comparator):
    """
    Comparator for sorting Strings in a case insensitive way except that case insensitive duplicates
     are then sub-sorted by reverse case so that lower case is before upper case.

     Example:   the strings "abc", "bob", "Bob", "zzz" would always sort as shown.  In a normal case
     insensitive sort, the "bob" and "Bob" order would be arbitrary.
    """





    def __init__(self): ...



    @overload
    def compare(self, name1: unicode, name2: unicode) -> int: ...

    @overload
    def compare(self, __a0: object, __a1: object) -> int: ...

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
