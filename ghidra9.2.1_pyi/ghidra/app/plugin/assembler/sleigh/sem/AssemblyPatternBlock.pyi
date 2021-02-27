from typing import List
import ghidra.app.plugin.assembler.sleigh.expr
import ghidra.app.plugin.assembler.sleigh.sem
import ghidra.app.plugin.processors.sleigh
import ghidra.app.plugin.processors.sleigh.expression
import ghidra.app.plugin.processors.sleigh.pattern
import ghidra.program.model.lang
import java.lang


class AssemblyPatternBlock(object, java.lang.Comparable):
    """
    The analog of PatternBlock, designed for use by the assembler

     It is suitable for the assembler because it is represented byte-by-byte, and it offers a number
     of useful conversions and operations.

     TODO A lot of this could probably be factored into the PatternBlock class, but it was
     best to experiment in another class altogether to avoid breaking things.
    """









    def combine(self, that: ghidra.app.plugin.assembler.sleigh.sem.AssemblyPatternBlock) -> ghidra.app.plugin.assembler.sleigh.sem.AssemblyPatternBlock:
        """
        Combine this pattern block with another given block

         Two blocks can be combined in their corresponding defined bits agree. When blocks are
         combined, their bytes are aligned according to their shifts, and the defined bits are taken
         from either block. If neither block defines a bit (i.e., the mask bit at that position is
         {@code 0} for both input blocks, then the output has an undefined bit in the corresponding
         position. If both blocks define the bit, but they have opposite values, then the result is
         an error.
        @param that the other block
        @return the new combined block, or null if the blocks disagree for any bit
        """
        ...

    @overload
    def compareTo(self, that: ghidra.app.plugin.assembler.sleigh.sem.AssemblyPatternBlock) -> int: ...

    @overload
    def compareTo(self, __a0: object) -> int: ...

    def copy(self) -> ghidra.app.plugin.assembler.sleigh.sem.AssemblyPatternBlock:
        """
        Duplicate this pattern block
        @return the duplicate
        """
        ...

    def countPossibleVals(self) -> int: ...

    def equals(self, obj: object) -> bool: ...

    def fillMask(self) -> ghidra.app.plugin.assembler.sleigh.sem.AssemblyPatternBlock:
        """
        Fill all unknown bits with {@code 0} bits
        @return the result
        """
        ...

    @staticmethod
    def fromBytes(offset: int, vals: List[int]) -> ghidra.app.plugin.assembler.sleigh.sem.AssemblyPatternBlock:
        """
        Get a pattern block with the given (fully-included) values at the given offset
        @param offset the offset (0-up, left-to-right)
        @param vals the values
        @return a pattern block (having a full mask)
        """
        ...

    @staticmethod
    def fromContextField(cf: ghidra.app.plugin.processors.sleigh.expression.ContextField, val: ghidra.app.plugin.assembler.sleigh.expr.MaskedLong) -> ghidra.app.plugin.assembler.sleigh.sem.AssemblyPatternBlock:
        """
        Encode the given masked long into a pattern block as specified by a given context field
        @param cf the context field specifying the location of the value to encode
        @param val the value to encode
        @return the pattern block with the encoded value
        """
        ...

    @staticmethod
    def fromLength(length: int) -> ghidra.app.plugin.assembler.sleigh.sem.AssemblyPatternBlock:
        """
        Allocate a fully-undefined pattern block of the given length
        @param length the length in bytes
        @return the block of all unknown bits
        """
        ...

    @staticmethod
    def fromLong(value: long) -> ghidra.app.plugin.assembler.sleigh.sem.AssemblyPatternBlock:
        """
        Convert the given long to a pattern block (having offset 0 and a full mask)
         NOTE: The result will be 8 bytes in length
        @param value the value to convert
        @return the pattern block containing the big-endian representation of the value
        """
        ...

    @staticmethod
    def fromMaskedLong(ml: ghidra.app.plugin.assembler.sleigh.expr.MaskedLong) -> ghidra.app.plugin.assembler.sleigh.sem.AssemblyPatternBlock:
        """
        Convert the given masked long to a pattern block (having offset 0)
         NOTE: The result will be 8 bytes in length
        @param ml the masked long, whose values and mask to convert
        @return the pattern block containing the big-endian representation of the value
        """
        ...

    @staticmethod
    def fromPattern(pat: ghidra.app.plugin.processors.sleigh.pattern.DisjointPattern, minLen: int, context: bool) -> ghidra.app.plugin.assembler.sleigh.sem.AssemblyPatternBlock:
        """
        Convert a block from a disjoint pattern into an assembly pattern block
        @param pat the pattern to convert
        @param context true to select the context block, false to select the instruction block
        @return the converted pattern block
        """
        ...

    @staticmethod
    def fromRegisterValue(rv: ghidra.program.model.lang.RegisterValue) -> ghidra.app.plugin.assembler.sleigh.sem.AssemblyPatternBlock:
        """
        Convert a register value into a pattern block
        @param rv the register value
        @return the pattern block

         This is used primarily to compute default context register values, and pass them into an
         assembler.
        """
        ...

    @staticmethod
    def fromString(str: unicode) -> ghidra.app.plugin.assembler.sleigh.sem.AssemblyPatternBlock:
        """
        Convert a string representation to a pattern block
        @see NumericUtilities#convertHexStringToMaskedValue(AtomicLong, AtomicLong, String, int, int, String)
        @param str the string to convert
        @return the resulting pattern block
        """
        ...

    @staticmethod
    def fromTokenField(tf: ghidra.app.plugin.processors.sleigh.expression.TokenField, val: ghidra.app.plugin.assembler.sleigh.expr.MaskedLong) -> ghidra.app.plugin.assembler.sleigh.sem.AssemblyPatternBlock:
        """
        Encode the given masked long into a pattern block as specified by a given token field
        @param tf the token field specifying the location of the value to encode
        @param val the value to encode
        @return the pattern block with the encoded value
        """
        ...

    def getClass(self) -> java.lang.Class: ...

    def getMask(self) -> List[int]:
        """
        Get the mask array
        @return the array
        """
        ...

    def getOffset(self) -> int:
        """
        Get the number of undefined bytes preceding the mask and values arrays
        @return the offset
        """
        ...

    def getSpecificity(self) -> int:
        """
        Counts the total number of known bits in the pattern

         At a slightly lower level, counts the number of 1-bits in the mask.
        @return the count
        """
        ...

    def getVals(self) -> List[int]:
        """
        Get the values array
        @return the array
        """
        ...

    def hashCode(self) -> int: ...

    def isFullMask(self) -> bool:
        """
        Check if there are any unknown bits
        @return true if no unknown bits are present, false otherwise
        """
        ...

    def isZero(self) -> bool:
        """
        Check if all bits are {@code 0} bits
        @return true if all are {@code 0}, false otherwise
        """
        ...

    def length(self) -> int:
        """
        Get the length (plus the offset) of this pattern block
        @return the total length
        """
        ...

    def maskOut(self, cop: ghidra.app.plugin.processors.sleigh.ContextOp) -> ghidra.app.plugin.assembler.sleigh.sem.AssemblyPatternBlock:
        """
        Set all bits read by a given context operation to unknown
        @param cop the context operation
        @return the result

         This is used during resolution to remove a context requirement passed upward by a child.
         When a parent constructor writes the required value to the context register, that
         requirement need not be passed further upward, since the write satisfies the requirement.
        """
        ...

    @staticmethod
    def nop() -> ghidra.app.plugin.assembler.sleigh.sem.AssemblyPatternBlock:
        """
        Get an empty pattern block
        @return the pattern block
        """
        ...

    def notify(self) -> None: ...

    def notifyAll(self) -> None: ...

    def possibleVals(self) -> List[java.lang.Iterable]:
        """
        Get an iterable over all the possible fillings of the value, given a partial mask

         This is meant to be used idiomatically, as in an enhanced for loop:

         <pre>
         {@code
         for (byte[] val : pattern.possibleVals()) {
             System.out.println(format(val));
         }
         }
         </pre>

         NOTE: A single byte array is instantiated with the call to {@link Iterable#iterator()}. Each
         call to {@link Iterator#next()} modifies the one byte array and returns it. As such, if you
         intend to preserve the value in the array for later use, you <em>must</em> make a copy.
        @return the iterable.
        """
        ...

    def readBytes(self, start: int, len: int) -> ghidra.app.plugin.assembler.sleigh.expr.MaskedLong:
        """
        Decode {@code} len bytes (values and mask) in big-endian format, beginning at {@code start}
        @param start the first byte to decode
        @param len the number of bytes to decode
        @return the decoded masked long
        """
        ...

    def readContextOp(self, cop: ghidra.app.plugin.processors.sleigh.ContextOp) -> ghidra.app.plugin.assembler.sleigh.expr.MaskedLong:
        """
        Read the input of a context operation from this pattern block
        @param cop the context operation
        @return the decoded input, as a masked value
        """
        ...

    def readMaskBytes(self, start: int, len: int) -> long:
        """
        Decode {@code} len mask bytes in big-endian format, beginning at {@code start}
        @param start the first byte to decode
        @param len the number of bytes to decode
        @return the decoded long
        """
        ...

    def readValBytes(self, start: int, len: int) -> long:
        """
        Decode {@code} len value bytes in big-endian format, beginning at {@code start}
        @param start the first byte to decode
        @param len the number of bytes to decode
        @return the decoded long
        """
        ...

    def shift(self, amt: int) -> ghidra.app.plugin.assembler.sleigh.sem.AssemblyPatternBlock:
        """
        Shift, i.e., increase the offset of, this pattern block
        @param amt the amount to shift right
        @return the shifted pattern block
        """
        ...

    def toBigInteger(self, n: int) -> long:
        """
        Decode the values array into a {@link BigInteger} of length {@code n} bytes

         The array is either truncated or zero-extended <em>on the right</em> to match the requested
         number of bytes, then decoded in big-endian format as an unsigned value.
        @param n the number of bytes (left-to-right) to decode
        @return the decoded big integer
        """
        ...

    def toString(self) -> unicode: ...

    def truncate(self, amt: int) -> ghidra.app.plugin.assembler.sleigh.sem.AssemblyPatternBlock:
        """
        Truncate (unshift) this pattern block by removing bytes from the left
        @param amt the amount to truncate or shift left
        @return the truncated pattern block
        """
        ...

    @overload
    def wait(self) -> None: ...

    @overload
    def wait(self, __a0: long) -> None: ...

    @overload
    def wait(self, __a0: long, __a1: int) -> None: ...

    def writeContextOp(self, cop: ghidra.app.plugin.processors.sleigh.ContextOp, val: ghidra.app.plugin.assembler.sleigh.expr.MaskedLong) -> ghidra.app.plugin.assembler.sleigh.sem.AssemblyPatternBlock:
        """
        Encode the given value into a copy of this pattern block as specified by a context operation

         NOTE: this method is given as a special operation, instead of a conversion factory method,
         because this is a write operation, not a combine operation. As such, the bits (including
         undefined bits) replace the bits in the existing pattern block. Were this a conversion
         method, we would lose the distinction between unknown bits being written, and bits whose
         values are simply not included in the write.
        @param cop the context operation specifying the location of the value to encode
        @param val the value to encode
        @return the new copy with the encoded value
        """
        ...

    @property
    def fullMask(self) -> bool: ...

    @property
    def mask(self) -> List[int]: ...

    @property
    def offset(self) -> int: ...

    @property
    def specificity(self) -> int: ...

    @property
    def vals(self) -> List[int]: ...

    @property
    def zero(self) -> bool: ...
