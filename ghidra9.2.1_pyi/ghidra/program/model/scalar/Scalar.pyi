from typing import List
import ghidra.program.model.scalar
import java.lang


class Scalar(object, java.lang.Comparable):
    """

     The Scalar defines a immutable fixed bit signed integer.
     Bit operations on a Scalar expect Scalar to act as a number in the
     two's complement format. Scalar was designed to be used as an
     offset (difference between two Addresses), an arithmetic operand,
     and also potentially for simulating registers.



     If an operation varies depending on whether the Scalar is
     treated as signed or unsigned, there are usally two version such as
     multiply and unsignedMultiply.  Please note that this means that
     the Comparable interface treats the number as signed.

    """





    @overload
    def __init__(self, bitLength: int, value: long):
        """
        Constructor a new signed scalar object.
        @param bitLength number of bits
        @param value value of the scalar
        """
        ...

    @overload
    def __init__(self, bitLength: int, value: long, signed: bool):
        """
        Constructor
        @param bitLength number of bits
        @param value value of the scalar
        @param signed true for a signed value, false for an unsigned value.
        """
        ...



    def add(self, n: long) -> ghidra.program.model.scalar.Scalar:
        """
        <p>Adds the integer n to <code>this</code>.
         Computes (<code>this = this + n</code>).
        @param n the value to add to this scalars value to produce a new scalar.
        """
        ...

    def bitLength(self) -> int:
        """
        <p>The size of this Scalar in bits.  This is constant for a
         Scalar.  It is not dependent on the particular value of the scalar.
         For example, a 16-bit Scalar should always return 16 regardless of the
         actual value held.</p>
        @return the width of this Scalar.
        """
        ...

    def byteArrayValue(self) -> List[int]:
        """
        <p>Returns a byte array representing this Scalar.  The size of
         the byte array is the number of bytes required to hold the
         number of bits returned by <CODE>bitLength()</CODE>.</p>
        @return a big-endian byte array containing the bits in this Scalar.
        """
        ...

    def clearBit(self, n: int) -> ghidra.program.model.scalar.Scalar:
        """
        <p>The bit number n in this Scalar is set to zero.  Computes
         (this = this &amp; ~(1&lt;&lt;n)).  Bits are numbered 0..bitlength()-1
         with 0 being the least significant bit.</p>
        @param n the bit to clear in this scalar.
        @throws IndexOutOfBoundsException if n &gt;= bitLength().
        """
        ...

    @overload
    def compareTo(self, other: ghidra.program.model.scalar.Scalar) -> int:
        """
        @see java.lang.Comparable#compareTo(java.lang.Object)
        """
        ...

    @overload
    def compareTo(self, __a0: object) -> int: ...

    def equals(self, obj: object) -> bool:
        """
        @see java.lang.Object#equals(java.lang.Object)
        """
        ...

    def flipBit(self, n: int) -> ghidra.program.model.scalar.Scalar:
        """
        <p>The bit number n in this Scalar is flipped.  Computes
         (this = this ^ (1&lt;&lt;n)).  Bits are numbered 0..bitlength()-1
         with 0 being the least significant bit.</p>
        @param n the bit to flip.
        @throws IndexOutOfBoundsException if n &gt;= bitLength().
        """
        ...

    def getBigInteger(self) -> long:
        """
        Returns the BigInteger representation of the value.
        """
        ...

    def getClass(self) -> java.lang.Class: ...

    def getSignedValue(self) -> long:
        """
        Get the value as signed.
        """
        ...

    def getUnsignedValue(self) -> long:
        """
        Get the value as unsigned.
        """
        ...

    def getValue(self) -> long:
        """
        Returns the value as a signed value if it was created signed, otherwise the value is
         returned as an unsigned value
        """
        ...

    def hashCode(self) -> int: ...

    def isSigned(self) -> bool:
        """
        Returns true if scalar was created as a signed value
        """
        ...

    def newScalar(self, newValue: long) -> ghidra.program.model.scalar.Scalar:
        """
        <p>Creates a new Scalar of the same size as this scalar but with the
         given value
        @param newValue the Scalar value which will be used to initialize
          the new Scalar.
        @return the new Scalar.
        """
        ...

    def notify(self) -> None: ...

    def notifyAll(self) -> None: ...

    def setBit(self, n: int) -> ghidra.program.model.scalar.Scalar:
        """
        <p>The bit number n in this Scalar is set to one.  Computes
         (this = this | (1&lt;&lt;n)).  Bits are numbered 0..bitlength()-1
         with 0 being the least significant bit.</p>
        @param n the bit to set.
        @throws IndexOutOfBoundsException if n &gt;= bitLength().
        """
        ...

    def shiftLeft(self, n: int) -> ghidra.program.model.scalar.Scalar:
        """
        <p>Sets <code>this = this &lt;&lt; n</code>.</p>
        @param n the number of bits to shift left.
        @throws ArithmeticException if n &lt; 0.
        """
        ...

    def shiftRight(self, n: int) -> ghidra.program.model.scalar.Scalar:
        """
        <p>Sets <code>this = this &gt;&gt; n</code> using 0 as the fill bit.</p>
        @param n the number of bits to shift right.
        @throws ArithmeticException if n &lt; 0.
        """
        ...

    def shiftRightSign(self, n: int) -> ghidra.program.model.scalar.Scalar:
        """
        <p>Sets <code>this = this &gt;&gt; n</code> replicating the sign bit.</p>
        @param n the number of bits to arithmetically shift.
        @throws ArithmeticException if n &lt; 0.
        """
        ...

    def subtract(self, n: long) -> ghidra.program.model.scalar.Scalar:
        """
        <p>Sets <code>this = this - n</code>.</p>
        @param n the value to subtract from this scalar to produce a new scalar.
        """
        ...

    def testBit(self, n: int) -> bool:
        """
        <p>Returns true if and only if the designated bit is set to one.
         Computes ((this &amp; (1&lt;&lt;n)) != 0).  Bits are numbered
         0..bitlength()-1 with 0 being the least significant bit.</p>
        @param n the bit to test.
        @return true if and only if the designated bit is set to one.
        @throws IndexOutOfBoundsException if n &gt;= bitLength().
        """
        ...

    @overload
    def toString(self) -> unicode:
        """
        @see java.lang.Object#toString()
        """
        ...

    @overload
    def toString(self, radix: int, zeroPadded: bool, showSign: bool, pre: unicode, post: unicode) -> unicode:
        """
        <p>Get a String representing this Scalar using the
         format defined by radix.</p>
        @param radix an integer base to use in representing the number
          (only 2, 8, 10, 16 are valid).  If 10 is specified, all
          remaining parameters are ignored.
        @param zeroPadded a boolean which if true will have the
          number left padded with 0 to the width necessary to hold
          the maximum value.
        @param showSign if true the '-' sign will be prepended for negative values, else
         value will be treated as an unsigned value and output without a sign.
        @param pre a String to append after the sign (if signed) but before
          the digits.
        @param post a String to append after the digits.
        @return a String representation of this scalar.
        @throws IllegalArgumentException If radix is not valid.
        """
        ...

    @overload
    def wait(self) -> None: ...

    @overload
    def wait(self, __a0: long) -> None: ...

    @overload
    def wait(self, __a0: long, __a1: int) -> None: ...

    @property
    def bigInteger(self) -> long: ...

    @property
    def bit(self) -> None: ...  # No getter available.

    @bit.setter
    def bit(self, value: int) -> None: ...

    @property
    def signed(self) -> bool: ...

    @property
    def signedValue(self) -> long: ...

    @property
    def unsignedValue(self) -> long: ...

    @property
    def value(self) -> long: ...
