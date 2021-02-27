from typing import List
import java.lang


class MathUtilities(object):








    @staticmethod
    def clamp(value: int, min: int, max: int) -> int:
        """
        Ensures that the given value is within the given range.
        @param value the value to check
        @param min the minimum value allowed
        @param max the maximum value allowed
        @return the clamped value
        """
        ...

    def equals(self, __a0: object) -> bool: ...

    def getClass(self) -> java.lang.Class: ...

    def hashCode(self) -> int: ...

    @staticmethod
    def main(args: List[unicode]) -> None: ...

    def notify(self) -> None: ...

    def notifyAll(self) -> None: ...

    def toString(self) -> unicode: ...

    @staticmethod
    def unsignedDivide(numerator: long, denominator: long) -> long:
        """
        Perform unsigned division. Provides proper handling of all 64-bit unsigned values.
        @param numerator unsigned numerator
        @param denominator positive divisor
        @return result of unsigned division
        @throws IllegalArgumentException if negative denominator is specified
        """
        ...

    @overload
    @staticmethod
    def unsignedMax(a: long, b: long) -> long:
        """
        Compute the maximum, treating the inputs as unsigned
        @param a the first value to consider
        @param b the second value to consider
        @return the maximum
        """
        ...

    @overload
    @staticmethod
    def unsignedMax(a: int, b: long) -> long:
        """
        Compute the maximum, treating the inputs as unsigned

         <p>
         This method is overloaded to prevent accidental signed-extension on one of the inputs. This
         method will correctly zero-extend the {@code int} parameter before performing any comparison.
        @param a the first value to consider
        @param b the second value to consider
        @return the maximum
        """
        ...

    @overload
    @staticmethod
    def unsignedMax(a: long, b: int) -> long:
        """
        Compute the maximum, treating the inputs as unsigned

         <p>
         This method is overloaded to prevent accidental signed-extension on one of the inputs. This
         method will correctly zero-extend the {@code int} parameter before performing any comparison.
        @param a the first value to consider
        @param b the second value to consider
        @return the maximum
        """
        ...

    @overload
    @staticmethod
    def unsignedMax(a: int, b: int) -> int:
        """
        Compute the maximum, treating the inputs as unsigned
        @param a the first value to consider
        @param b the second value to consider
        @return the maximum
        """
        ...

    @overload
    @staticmethod
    def unsignedMin(a: long, b: long) -> long:
        """
        Compute the minimum, treating the inputs as unsigned
        @param a the first value to consider
        @param b the second value to consider
        @return the minimum
        """
        ...

    @overload
    @staticmethod
    def unsignedMin(a: int, b: long) -> int:
        """
        Compute the minimum, treating the inputs as unsigned

         <p>
         This method is overloaded to prevent accidental signed-extension on one of the inputs. This
         method will correctly zero-extend the {@code int} parameter before performing any comparison.
         Also note the return type is {@code int}, since b would never be selected if it overflows an
         {@code int}.
        @param a the first value to consider
        @param b the second value to consider
        @return the minimum
        """
        ...

    @overload
    @staticmethod
    def unsignedMin(a: long, b: int) -> int:
        """
        Compute the minimum, treating the inputs as unsigned

         <p>
         This method is overloaded to prevent accidental signed-extension on one of the inputs. This
         method will correctly zero-extend the {@code int} parameter before performing any comparison.
         Also note the return type is {@code int}, since b would never be selected if it overflows an
         {@code int}.
        @param a the first value to consider
        @param b the second value to consider
        @return the minimum
        """
        ...

    @overload
    @staticmethod
    def unsignedMin(a: int, b: int) -> int:
        """
        Compute the minimum, treating the inputs as unsigned
        @param a the first value to consider
        @param b the second value to consider
        @return the minimum
        """
        ...

    @staticmethod
    def unsignedModulo(numerator: long, denominator: long) -> long:
        """
        Perform unsigned modulo. Provides proper handling of all 64-bit unsigned values.
        @param numerator unsigned numerator
        @param denominator positive divisor
        @return result of unsigned modulo (i.e., remainder)
        @throws IllegalArgumentException if negative denominator is specified
        """
        ...

    @overload
    def wait(self) -> None: ...

    @overload
    def wait(self, __a0: long) -> None: ...

    @overload
    def wait(self, __a0: long, __a1: int) -> None: ...
