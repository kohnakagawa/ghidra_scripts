import ghidra.app.plugin.assembler.sleigh.expr
import java.lang


class MaskedLong(object, java.lang.Comparable):
    """
    A -bit value where each bit is , , or  (undefined)
    """

    ONES: ghidra.app.plugin.assembler.sleigh.expr.MaskedLong = FF:FF:FF:FF:FF:FF:FF:FF
    UNKS: ghidra.app.plugin.assembler.sleigh.expr.MaskedLong = X
    ZERO: ghidra.app.plugin.assembler.sleigh.expr.MaskedLong = 00:00:00:00:00:00:00:00







    def add(self, that: ghidra.app.plugin.assembler.sleigh.expr.MaskedLong) -> ghidra.app.plugin.assembler.sleigh.expr.MaskedLong:
        """
        Compute the arithmetic sum of this and another masked long
        @param that the other masked long.
        @return the result.
        """
        ...

    @overload
    def agrees(self, that: long) -> bool:
        """
        Checks if this and a long agree

         The masked long agrees with the given long iff the masked long's defined bit positions agree
         with the corresponding bit positions in the given long. Where there are undefined bits, no
         check is applied. In the case that the masked long is fully-defined, this is the same as an
         equality check on the value.
        @param that the long
        @return true if this and that agree.
        """
        ...

    @overload
    def agrees(self, that: ghidra.app.plugin.assembler.sleigh.expr.MaskedLong) -> bool:
        """
        Checks if this and another masked long agree

         Two masked longs agree iff their corresponding defined bit positions are equal. Where either
         or both positions are undefined, no check is applied. In the case that both masked longs are
         fully-defined, this is the same as an equality check on the values.
        @param that the other masked long.
        @return true if this and that agree.
        """
        ...

    @overload
    def agrees(self, that: object) -> bool:
        """
        Check if this and another object agree
        @param that a {@link MaskedLong} or {@link Long} to check.
        @see #agrees(MaskedLong)
        @see #agrees(long)
        @return true if this and that agree.
        """
        ...

    def and(self, that: ghidra.app.plugin.assembler.sleigh.expr.MaskedLong) -> ghidra.app.plugin.assembler.sleigh.expr.MaskedLong:
        """
        Compute the bitwise AND of this and another masked long

         To handle unknown bits, the result is derived from the following truth table:

         <pre>{@literal
           0 x 1 <= A (this)
         0 0 0 0
         x 0 x x
         1 0 x 1
         ^
         B (that)
         }</pre>
        @param that the other masked long ({@code B}).
        @return the result.
        """
        ...

    def byteSwap(self, n: int) -> ghidra.app.plugin.assembler.sleigh.expr.MaskedLong:
        """
        Reverse the least significant {@code n} bytes

         This interprets the bits as an {@code n}-byte value and changes the endianness. Any bits
         outside of the interpretation are truncated, i.e., become unknown.
        @param n the size, in bytes, of the interpreted value.
        @return the result.
        """
        ...

    def combine(self, that: ghidra.app.plugin.assembler.sleigh.expr.MaskedLong) -> ghidra.app.plugin.assembler.sleigh.expr.MaskedLong:
        """
        Combine this and another masked long into one, by taking defined bits from either

         If this masked long agrees with the other, then the two are combined. For each bit position
         in the result, the defined bit from either corresponding position is taken. If neither is
         defined, then the position is undefined in the result. If both are defined, they must agree.
        @param that the other masked long
        @return the combined masked long
        @throws SolverException if this and the other masked long disagree
        """
        ...

    @overload
    def compareTo(self, that: ghidra.app.plugin.assembler.sleigh.expr.MaskedLong) -> int:
        """
        "Compare" two masked longs

         This is not meant to reflect a numerical comparison. Rather, this is just to impose an
         ordering for the sake of storing these in sorted collections.
        """
        ...

    @overload
    def compareTo(self, __a0: object) -> int: ...

    def divideSigned(self, that: ghidra.app.plugin.assembler.sleigh.expr.MaskedLong) -> ghidra.app.plugin.assembler.sleigh.expr.MaskedLong: ...

    def divideUnsigned(self, that: ghidra.app.plugin.assembler.sleigh.expr.MaskedLong) -> ghidra.app.plugin.assembler.sleigh.expr.MaskedLong:
        """
        Compute the unsigned arithmetic quotient: this masked long divided by another
        @param that the other masked long.
        @return the result.
        """
        ...

    def equals(self, other: object) -> bool:
        """
        Check for equality

         This will only return true if the other object is a masked long, even if this one is
         fully-defined, and the value is equal to a given long (or {@link Long}). The other masked
         long must have the same mask and value to be considered equal. For other sorts of "equality"
         checks, see {@link #agrees(Object)} and friends.
        """
        ...

    def fillMask(self) -> ghidra.app.plugin.assembler.sleigh.expr.MaskedLong:
        """
        Set all undefined bits to 0
        @return the result
        """
        ...

    @staticmethod
    def fromLong(val: long) -> ghidra.app.plugin.assembler.sleigh.expr.MaskedLong:
        """
        Create a fully-defined value from the bits of a long
        @param val the value to take
        @return the constructed masked long
        """
        ...

    @staticmethod
    def fromMaskAndValue(msk: long, val: long) -> ghidra.app.plugin.assembler.sleigh.expr.MaskedLong:
        """
        Create a masked value from a mask and a long

         Any positions in {@code msk} set to 0 create an {@code x} in the corresponding position of
         the result. Otherwise, the position takes the corresponding bit from {@code val}.
        @param msk the mask
        @param val the value
        @return the constructed masked long
        """
        ...

    def getClass(self) -> java.lang.Class: ...

    def getMask(self) -> long:
        """
        Get the mask as a long

         Positions with a defined bit are {@code 1}; positions with an undefined bit are {@code 0}.
        @return the mask as a long
        """
        ...

    def hashCode(self) -> int: ...

    def invAnd(self, that: ghidra.app.plugin.assembler.sleigh.expr.MaskedLong) -> ghidra.app.plugin.assembler.sleigh.expr.MaskedLong:
        """
        Solves the expression {@code A & B = C, for B, given C and A}
         <p>
         To handle unknown bits, the solution is derived from the following truth table, where
         {@code *} indicates no solution:

         <pre>{@literal
           0 x 1 <= A (that)
         0 x x 0
         x x x x
         1 * 1 1
         ^
         B (this)
         }</pre>
        @param that the other masked long ({@code B}).
        @return the result.
        @throws SolverException if no solution exists.
        """
        ...

    def invMultiplyUnsigned(self, that: ghidra.app.plugin.assembler.sleigh.expr.MaskedLong) -> ghidra.app.plugin.assembler.sleigh.expr.MaskedLong:
        """
        Compute the arithmetic quotient as a solution to unsigned multiplication

         This is slightly different than {@link #divideUnsigned(MaskedLong)} in its treatment of
         unknowns.
        @param that the known factor
        @return a solution to that*x == this, if possible
        @throws SolverException
        """
        ...

    def invOr(self, that: ghidra.app.plugin.assembler.sleigh.expr.MaskedLong) -> ghidra.app.plugin.assembler.sleigh.expr.MaskedLong:
        """
        Solves the expression A | B = C, for B, given C and A

         To handle unknown bits, the solution is derived from the following truth table, where
         {@code *} indicates no solution:

         <pre>{@literal
           0 x 1 <= A (that)
         0 0 0 *
         x x x x
         1 1 x x
         ^
         B (this)
         }</pre>
        @param that the other masked long ({@code B}).
        @return the result.
        @throws SolverException if not solution exists.
        """
        ...

    @overload
    def invShiftLeft(self, n: long) -> ghidra.app.plugin.assembler.sleigh.expr.MaskedLong:
        """
        Invert a left shift of {@code n} positions, that is shift right

         This is different from a normal shift right, in that it inserts unknowns at the left. The
         normal right shift inserts zeros or sign bits. Additionally, if any ones would fall off the
         right, the inversion is undefined.
        @param n the number of positions
        @return the result
        @throws SolverException if the inversion is undefined
        """
        ...

    @overload
    def invShiftLeft(self, n: ghidra.app.plugin.assembler.sleigh.expr.MaskedLong) -> ghidra.app.plugin.assembler.sleigh.expr.MaskedLong:
        """
        Invert a left shift of {@code n} positions, that is shift right

         This is different from a normal shift right, in that it inserts unknowns at the left. The
         normal right shift inserts zeros or sign bits. Additionally, if any ones would fall off the
         right, the inversion is undefined.
        @param n the number of positions
        @return the result
        @throws SolverException if the inversion is undefined
        """
        ...

    @overload
    def invShiftRight(self, n: long) -> ghidra.app.plugin.assembler.sleigh.expr.MaskedLong:
        """
        Invert an arithmetic right shift of {@code n} positions, that is shift left

         This is different from a normal shift left, in that it inserts unknowns at the right. The
         normal left shift inserts zeros. Additionally, all bits that fall off the left must match the
         resulting sign bit, or else the inversion is undefined.
        @param n the number of positions
        @return the result
        @throws SolverException if the inversion is undefined
        """
        ...

    @overload
    def invShiftRight(self, n: ghidra.app.plugin.assembler.sleigh.expr.MaskedLong) -> ghidra.app.plugin.assembler.sleigh.expr.MaskedLong:
        """
        Invert an arithmetic right shift of {@code n} positions, that is shift left

         This is different from a normal shift left, in that it inserts unknowns at the right. The
         normal left shift inserts zeros. Additionally, all bits that fall off the left must match the
         resulting sign bit, or else the inversion is undefined.
        @param n the number of positions
        @return the result
        @throws SolverException if the inversion is undefined
        """
        ...

    @overload
    def invShiftRightLogical(self, n: long) -> ghidra.app.plugin.assembler.sleigh.expr.MaskedLong:
        """
        Invert a logical right shift of {@code n} positions, that is shift left

         This is different from a normal shift left, in that it inserts unknowns at the right. The
         normal left shift inserts zeros. Additionally, if any ones would fall off the left, the
         inversion is undefined.
        @param n the number of positions
        @return the result
        @throws SolverException if the inversion is undefined
        """
        ...

    @overload
    def invShiftRightLogical(self, n: ghidra.app.plugin.assembler.sleigh.expr.MaskedLong) -> ghidra.app.plugin.assembler.sleigh.expr.MaskedLong:
        """
        Invert a logical right shift of {@code n} positions, that is shift left

         This is different from a normal shift left, in that it inserts unknowns at the right. The
         normal left shift inserts zeros. Additionally, if any ones would fall off the left, the
         inversion is undefined.
        @param n the number of positions
        @return the result
        @throws SolverException if the inversion is undefined
        """
        ...

    def isFullyDefined(self) -> bool:
        """
        True iff there are no undefined bits
        @return true if fully-defined, false otherwise
        """
        ...

    def isFullyUndefined(self) -> bool:
        """
        True iff there are no defined bits
        @return true if full-undefined, false otherwise
        """
        ...

    def isInRange(self, max: long, signed: bool) -> bool:
        """
        Check if the masked value falls within a given range

         The range is defined by a maximum and a signedness. The maximum must be one less than a
         positive power of 2. In other words, it defines a maximum number of bits, including the sign
         bit if applicable.

         The defined bits of this masked long are then checked to fall in the given range. The
         effective value is derived by sign/zero extending the value according to its mask. In
         general, if any {@code 1} bits exist outside of the given max, the value is rejected, unless
         that {@code 1} is purely a result of signedness.
        @param max the maximum value, taken as an unsigned long.
        @param signed true to interpret the masked value as signed.
        @return true if the masked value "fits" into the given range.
        """
        ...

    def longValue(self) -> long:
        """
        Obtain the value as a long, where all undefined bits are treated as {@code 0}
        @return the value as a long
        """
        ...

    def mask(self, mask: long) -> ghidra.app.plugin.assembler.sleigh.expr.MaskedLong:
        """
        Apply an additional mask to this masked long

         Any {@code 0} bit in {@code msk} will result in an undefined bit in the result. {@code 1}
         bits result in a copy of the corresponding bit in the result.
        @param mask the mask to apply
        @return the result.
        """
        ...

    def multiply(self, that: ghidra.app.plugin.assembler.sleigh.expr.MaskedLong) -> ghidra.app.plugin.assembler.sleigh.expr.MaskedLong:
        """
        Compute the arithmetic product of this and another masked long
        @param that the other masked long.
        @return the result.
        """
        ...

    def negate(self) -> ghidra.app.plugin.assembler.sleigh.expr.MaskedLong:
        """
        Negate the value
        @return the result.
        """
        ...

    def not(self) -> ghidra.app.plugin.assembler.sleigh.expr.MaskedLong:
        """
        Compute the bitwise NOT

         To handle unknown bits, the result is derived from the following truth table:

         <pre>{@literal
         0 x 1 <= A (this)
         1 x 0
         }</pre>
        @return the result.
        """
        ...

    def notify(self) -> None: ...

    def notifyAll(self) -> None: ...

    def or(self, that: ghidra.app.plugin.assembler.sleigh.expr.MaskedLong) -> ghidra.app.plugin.assembler.sleigh.expr.MaskedLong:
        """
        Compute the bitwise OR of this and another masked long

         To handle unknown bits, the result is derived from the following truth table:

         <pre>{@literal
           0 x 1 <= A (this)
         0 0 x 1
         x x x 1
         1 1 1 1
         ^
         B (that)
         }</pre>
        @param that the other masked long ({@code B}).
        @return the result.
        """
        ...

    @overload
    def shiftCircular(self, n: long, size: int, dir: int) -> ghidra.app.plugin.assembler.sleigh.expr.MaskedLong:
        """
        Shift {@code size} bits @{code n) positions circularly in a given direction

         The shifted bits are the least significant {@code size} bits. The remaining bits are
         unaffected.
        @param n the number of positions
        @param size the number of bits (least significant) to include in the shift
        @param dir the direction to shift (0 for left, 1 for right)
        @return the result
        """
        ...

    @overload
    def shiftCircular(self, n: ghidra.app.plugin.assembler.sleigh.expr.MaskedLong, size: int, dir: int) -> ghidra.app.plugin.assembler.sleigh.expr.MaskedLong:
        """
        Shift {@code size} bits @{code n) positions circularly in a given direction

         The shifted bits are the least significant {@code size} bits. The remaining bits are
         unaffected.
        @param n the number of positions
        @param size the number of bits (least significant) to include in the shift
        @param dir the direction to shift (0 for left, 1 for right)
        @return the result
        """
        ...

    @overload
    def shiftLeft(self, n: long) -> ghidra.app.plugin.assembler.sleigh.expr.MaskedLong:
        """
        Shift the bits @{code n} positions left

         This implements both a signed and unsigned shift.
        @param n the number of positions.
        @return the result.
        """
        ...

    @overload
    def shiftLeft(self, n: ghidra.app.plugin.assembler.sleigh.expr.MaskedLong) -> ghidra.app.plugin.assembler.sleigh.expr.MaskedLong:
        """
        Shift the bits {@code n} positions left

         This implements both a signed and unsigned shift.
        @param n the number of positions.
        @return the result.
        """
        ...

    @overload
    def shiftRight(self, n: long) -> ghidra.app.plugin.assembler.sleigh.expr.MaskedLong:
        """
        Shift the bits arithmetically {@code n} positions right

         This implements a signed shift.
        @param n the number of positions.
        @return the result.
        """
        ...

    @overload
    def shiftRight(self, n: ghidra.app.plugin.assembler.sleigh.expr.MaskedLong) -> ghidra.app.plugin.assembler.sleigh.expr.MaskedLong:
        """
        Shift the bits arithmetically {@code n} positions right

         This implements a signed shift.
        @param n the number of positions.
        @return the result.
        """
        ...

    @overload
    def shiftRightLogical(self, n: long) -> ghidra.app.plugin.assembler.sleigh.expr.MaskedLong:
        """
        Shift the bits logically {@code n} positions right

         This implements an unsigned shift.
        @param n the number of positions.
        @return the result.
        """
        ...

    @overload
    def shiftRightLogical(self, n: ghidra.app.plugin.assembler.sleigh.expr.MaskedLong) -> ghidra.app.plugin.assembler.sleigh.expr.MaskedLong:
        """
        Shift the bits logically {@code n} positions right

         This implements an unsigned shift.
        @param n the number of positions.
        @return the result.
        """
        ...

    def shiftRightPositional(self, n: long) -> ghidra.app.plugin.assembler.sleigh.expr.MaskedLong:
        """
        Shift the bits positionally {@code n} positions right

         This fills the left with unknown bits
        @param n
        @return
        """
        ...

    @overload
    def signExtend(self) -> ghidra.app.plugin.assembler.sleigh.expr.MaskedLong:
        """
        Sign extend the masked value, according to its mask, to a full long

         The leftmost defined bit is taken as the sign bit, and extended to the left.
        @return the sign-extended masked long
        """
        ...

    @overload
    def signExtend(self, n: int) -> ghidra.app.plugin.assembler.sleigh.expr.MaskedLong:
        """
        Sign extend the masked value as if of the given size in bits, to a full long
        @param n the number of bits to take (right-to-left)
        @return the sign-extended masked long
        """
        ...

    def subtract(self, that: ghidra.app.plugin.assembler.sleigh.expr.MaskedLong) -> ghidra.app.plugin.assembler.sleigh.expr.MaskedLong:
        """
        Compute the arithmetic difference: this masked long minus another
        @param that the other masked long.
        @return the result.
        """
        ...

    def toString(self) -> unicode: ...

    def unknownExtend(self, n: int) -> ghidra.app.plugin.assembler.sleigh.expr.MaskedLong:
        """
        Mask out all but the lowest {@code n} bits of the value
        @param n the number of bits to take (right-to-left)
        @return the unknown-extended masked long
        """
        ...

    @overload
    def wait(self) -> None: ...

    @overload
    def wait(self, __a0: long) -> None: ...

    @overload
    def wait(self, __a0: long, __a1: int) -> None: ...

    def xor(self, that: ghidra.app.plugin.assembler.sleigh.expr.MaskedLong) -> ghidra.app.plugin.assembler.sleigh.expr.MaskedLong:
        """
        Compute the bitwise XOR of this and another masked long

         To handle unknown bits, the result is derived from the following truth table:

         <pre>{@literal
           0 x 1 <= A (this)
         0 0 x 1
         x x x x
         1 1 x 0
         ^
         B (that)
         }</pre>
        @param that the other masked long ({@code B}).
        @return the result.
        """
        ...

    @overload
    def zeroExtend(self) -> ghidra.app.plugin.assembler.sleigh.expr.MaskedLong:
        """
        Zero extend the masked value, according to its mask, to a full long

         All bits to the left of the leftmost defined bit are set to 0.
        @return the zero-extended masked long
        """
        ...

    @overload
    def zeroExtend(self, n: int) -> ghidra.app.plugin.assembler.sleigh.expr.MaskedLong:
        """
        Zero extend the masked value as if of the given size in bits, to a full long
        @param n the number of bits to take (right-to-left)
        @return the zero-extended masked long
        """
        ...

    @property
    def fullyDefined(self) -> bool: ...

    @property
    def fullyUndefined(self) -> bool: ...
