from typing import Iterator
from typing import List
import ghidra.util
import java.lang
import java.util.concurrent.atomic
import java.util.stream


class NumericUtilities(object):
    MAX_SIGNED_LONG: long = 0x7fffffffffffffffL
    MAX_UNSIGNED_INT32_AS_LONG: long = 0xffffffffL
    MAX_UNSIGNED_LONG: long = 0xffffffffffffffffL







    @staticmethod
    def bigIntegerToUnsignedLong(value: long) -> long: ...

    @overload
    @staticmethod
    def convertBytesToString(bytes: List[int]) -> unicode:
        """
        Convert a byte array into a hexadecimal string.
        @param bytes byte array
        @return hex string representation
        """
        ...

    @overload
    @staticmethod
    def convertBytesToString(bytes: List[int], delimeter: unicode) -> unicode:
        """
        Convert a byte array into a hexadecimal string.
        @param bytes byte array
        @param delimeter the text between byte strings
        @return hex string representation
        """
        ...

    @overload
    @staticmethod
    def convertBytesToString(bytes: java.lang.Iterable, delimiter: unicode) -> unicode:
        """
        Convert a bytes into a hexadecimal string.
        @param bytes an iterable of bytes
        @param delimiter the text between byte strings; null is allowed
        @return hex string representation
        """
        ...

    @overload
    @staticmethod
    def convertBytesToString(bytes: Iterator[int], delimiter: unicode) -> unicode:
        """
        Convert a bytes into a hexadecimal string.
        @param bytes an iterator of bytes
        @param delimiter the text between byte strings; null is allowed
        @return hex string representation
        """
        ...

    @overload
    @staticmethod
    def convertBytesToString(bytes: java.util.stream.Stream, delimiter: unicode) -> unicode:
        """
        Convert a bytes into a hexadecimal string.
        @param bytes an stream of bytes
        @param delimiter the text between byte strings; null is allowed
        @return hex string representation
        """
        ...

    @overload
    @staticmethod
    def convertBytesToString(bytes: List[int], start: int, len: int, delimeter: unicode) -> unicode:
        """
        Convert a byte array into a hexadecimal string.
        @param bytes byte array
        @param start start index
        @param len number of bytes to convert
        @param delimeter the text between byte strings
        @return hex string representation
        """
        ...

    @staticmethod
    def convertHexStringToMaskedValue(msk: java.util.concurrent.atomic.AtomicLong, val: java.util.concurrent.atomic.AtomicLong, hex: unicode, n: int, spaceevery: int, spacer: unicode) -> None:
        """
        The reverse of {@link #convertMaskedValueToHexString(long, long, int, boolean, int, String)}
        @param msk an object to receive the resulting mask
        @param val an object to receive the resulting value
        @param hex the input string to parse
        @param n the number of nibbles to parse (they are stored right aligned in the result)
        @param spaceevery how many nibbles are expected between spacers
        @param spacer the spacer
        @see #convertMaskedValueToHexString(long, long, int, boolean, int, String)
        @see #convertMaskToHexString(long, int, boolean, int, String)
        """
        ...

    @staticmethod
    def convertMaskToHexString(msk: long, n: int, truncate: bool, spaceevery: int, spacer: unicode) -> unicode:
        """
        Convert a mask to a hexadecimal-ish string.

         Converts the mask in a similar way to
         {@link #convertMaskedValueToHexString(long, long, int, boolean, int, String)}.
         Philosophically, it is hexadecimal, but the only valid digits are 0 and F. Any
         partially-included nibble will be broken down into bracketed bits. Displaying masks in this
         way is convenient when shown proximal to related masked values.
        @param msk the mask
        @param n the number of nibbles, starting at the right
        @param truncate true if leading Xs may be truncated
        @param spaceevery how many nibbles in spaced groups, 0 for no spaces
        @param spacer the group separator, if applicable
        @return the string representation
        @see #convertMaskedValueToHexString(long, long, int, boolean, int, String)
        @see #convertHexStringToMaskedValue(AtomicLong, AtomicLong, String, int, int, String)
        """
        ...

    @staticmethod
    def convertMaskedValueToHexString(msk: long, val: long, n: int, truncate: bool, spaceevery: int, spacer: unicode) -> unicode:
        """
        Convert a masked value into a hexadecimal-ish string.

         Converts the data to hexadecimal, placing an X where a nibble is unknown. Where a nibble is
         partially defined, it is displayed as four bits in brackets []. Bits are displayed as x, or
         the defined value.

         For example, consider the mask 00001111:01011100, and the value 00001001:00011000. This will
         display as {@code X8:[x0x1][10xx]}. To see the correlation, consider the table:
         <table>
         <caption></caption>
         <tr>
         <th>Display</th>
         <th>{@code X}</th>
         <th>{@code 8}</th>
         <th>{@code :}</th>
         <th>{@code [x0x1]}</th>
         <th>{@code [10xx]}</th>
         </tr>
         <tr>
         <th>Mask</th>
         <td>{@code 0000}</td>
         <td>{@code 1111}</td>
         <td>{@code :}</td>
         <td>{@code 0101}</td>
         <td>{@code 1100}</td>
         </tr>
         <tr>
         <th>Value</th>
         <td>{@code 0000}</td>
         <td>{@code 1000}</td>
         <td>{@code :}</td>
         <td>{@code 0001}</td>
         <td>{@code 1000}</td>
         </tr>
         </table>
        @param msk the mask
        @param val the value
        @param n the number of nibbles, starting at the right. The example uses 4.
        @param truncate true if leading Xs may be truncated. The example uses {@code false}.
        @param spaceevery how many nibbles in spaced groups, 0 for no spaces. The example uses 2.
        @param spacer the group separator, if applicable. The example uses {@code ':'}.
        @return the string representation
        @see #convertMaskToHexString(long, int, boolean, int, String)
        @see #convertHexStringToMaskedValue(AtomicLong, AtomicLong, String, int, int, String)
        """
        ...

    @staticmethod
    def convertStringToBytes(hexString: unicode) -> List[int]:
        """
        Parse hexadecimal digits into a byte array.
        @param hexString hexadecimal digits
        @return numeric value as a byte array, or null if string contains invalid hex characters.
        """
        ...

    def equals(self, __a0: object) -> bool: ...

    @overload
    @staticmethod
    def formatNumber(number: long, radix: int) -> unicode:
        """
        Render <code>number</code> in different bases using the default signedness mode.
         <p>
         This invokes {@linkplain #formatNumber(long, int, SignednessFormatMode)} with a
         <code>mode</code> parameter of <code>{@linkplain SignednessFormatMode#DEFAULT}</code>.
        @param number The number to represent
        @param radix the base in which <code>number</code> is represented
        @return formatted string of the number parameter in provided radix base
        @see #formatNumber(long, int, SignednessFormatMode)
        """
        ...

    @overload
    @staticmethod
    def formatNumber(number: long, radix: int, mode: ghidra.util.SignednessFormatMode) -> unicode:
        """
        Provide renderings of <code>number</code> in different bases:
         <ul>
         <li><code>0</code> - renders <code>number</code> as an escaped character sequence</li>
         <li><code>2</code> - renders <code>number</code> as a <code>base-2</code> integer</li>
         <li><code>8</code> - renders <code>number</code> as a <code>base-8</code> integer</li>
         <li><code>10</code> - renders <code>number</code> as a <code>base-10</code> integer</li>
         <li><code>16</code> (default) - renders <code>number</code> as a <code>base-16</code>
         integer</li>
         </ul>
         <table>
         <caption></caption>
         <tr>
         <th>Number</th>
         <th>Radix</th>
         <th>DEFAULT Mode Alias</th>
         <th style="text-align:center"><i>UNSIGNED</i> Mode Value</th>
         <th><i>SIGNED</i> Mode Value</th>
         </tr>
         <tr>
         <td>&nbsp;</td>
         <td></td>
         <td><i></i></td>
         <td></td>
         <td></td>
         </tr>
         <tr style="text-align:right;font-family: monospace">
         <td>100</td>
         <td>2</td>
         <td><i>UNSIGNED</i></td>
         <td>1100100b</td>
         <td>1100100b</td>
         </tr>
         <tr style="text-align:right;font-family: monospace">
         <td>100</td>
         <td>8</td>
         <td><i>UNSIGNED</i></td>
         <td>144o</td>
         <td>144o</td>
         </tr>
         <tr style="text-align:right;font-family: monospace">
         <td>100</td>
         <td>10</td>
         <td><i>SIGNED</i></td>
         <td>100</td>
         <td>100</td>
         </tr>
         <tr style="text-align:right;font-family: monospace">
         <td>100</td>
         <td>16</td>
         <td><i>UNSIGNED</i></td>
         <td>64h</td>
         <td>64h</td>
         </tr>
         <tr>
         <td>&nbsp;</td>
         <td></td>
         <td><i></i></td>
         <td></td>
         <td></td>
         </tr>
         <tr style="text-align:right;font-family: monospace">
         <td>-1</td>
         <td>2</td>
         <td><i>UNSIGNED</i></td>
         <td>1111111111111111111111111111111111111111111111111111111111111111b</td>
         <td>-1b</td>
         </tr>
         <tr style="text-align:right;font-family: monospace">
         <td>-1</td>
         <td>8</td>
         <td><i>UNSIGNED</i></td>
         <td>1777777777777777777777o</td>
         <td>-1o</td>
         </tr>
         <tr style="text-align:right;font-family: monospace">
         <td>-1</td>
         <td>10</td>
         <td><i>SIGNED</i></td>
         <td>18446744073709551615</td>
         <td>-1</td>
         </tr>
         <tr style="text-align:right;font-family: monospace">
         <td>-1</td>
         <td>16</td>
         <td><i>UNSIGNED</i></td>
         <td>ffffffffffffffffh</td>
         <td>-1h</td>
         </tr>
         <tr>
         <td>&nbsp;</td>
         <td></td>
         <td><i></i></td>
         <td></td>
         <td></td>
         </tr>
         <tr style="text-align:right;font-family: monospace">
         <td>-100</td>
         <td>2</td>
         <td><i>UNSIGNED</i></td>
         <td>1111111111111111111111111111111111111111111111111111111110011100b</td>
         <td>-1100100b</td>
         </tr>
         <tr style="text-align:right;font-family: monospace">
         <td>-100</td>
         <td>8</td>
         <td><i>UNSIGNED</i></td>
         <td>1777777777777777777634o</td>
         <td>-144o</td>
         </tr>
         <tr style="text-align:right;font-family: monospace">
         <td>-100</td>
         <td>10</td>
         <td><i>SIGNED</i></td>
         <td>18446744073709551516</td>
         <td>-100</td>
         </tr>
         <tr style="text-align:right;font-family: monospace">
         <td>-100</td>
         <td>16</td>
         <td><i>UNSIGNED</i></td>
         <td>ffffffffffffff9ch</td>
         <td>-64h</td>
         </tr>
         </table>
        @param number The number to represent
        @param radix The base in which <code>number</code> is represented
        @param mode Specifies how the number is formatted with respect to its signed-ness
        @return number string in the given base
        """
        ...

    def getClass(self) -> java.lang.Class: ...

    @staticmethod
    def getUnsignedAlignedValue(unsignedValue: long, alignment: long) -> long:
        """
        Get an unsigned aligned value corresponding to the specified unsigned value which will be
         greater than or equal the specified value.
        @param unsignedValue value to be aligned
        @param alignment alignment
        @return aligned value
        """
        ...

    def hashCode(self) -> int: ...

    @overload
    @staticmethod
    def isFloatingPointType(numClass: java.lang.Class) -> bool:
        """
        Determine if the provided Number class is a floating-point type.
        @param numClass Class of an object
        @return true if the class parameter is a floating-point type, false otherwise
        """
        ...

    @overload
    @staticmethod
    def isFloatingPointType(number: java.lang.Number) -> bool:
        """
        Determine if the provided Number is a floating-point type -- Float or Double.
        @param number the object to check for for floating-point-type
        @return true if the provided number is a floating-point-type, false otherwise
        """
        ...

    @overload
    @staticmethod
    def isIntegerType(numClass: java.lang.Class) -> bool:
        """
        Determine if the provided Number class is an integer type.
        @param numClass Class of an object
        @return true if the class parameter is a integer type, false otherwise
        """
        ...

    @overload
    @staticmethod
    def isIntegerType(number: java.lang.Number) -> bool:
        """
        Determine if the provided Number is an integer type -- Byte, Short, Integer, or Long.
        @param number the object to check for for integer-type
        @return true if the provided number is an integer-type, false otherwise
        """
        ...

    def notify(self) -> None: ...

    def notifyAll(self) -> None: ...

    @staticmethod
    def parseHexBigInteger(numStr: unicode) -> long: ...

    @staticmethod
    def parseHexLong(numStr: unicode) -> long: ...

    @staticmethod
    def parseLong(numStr: unicode) -> long:
        """
        parses the given string as a numeric value, detecting whether or not it begins with a Hex
         prefix, and if not, parses as a long int value.
        """
        ...

    @staticmethod
    def parseNumber(numStr: unicode) -> long:
        """
        parses the given string as a numeric value, detecting whether or not it begins with a Hex
         prefix, and if not, parses as a long int value.
        """
        ...

    @staticmethod
    def parseOctLong(numStr: unicode) -> long:
        """
        parses the given string as a numeric value, detecting whether or not it begins with a Hex
         prefix, and if not, parses as a long int value.
        """
        ...

    @overload
    @staticmethod
    def toHexString(value: long) -> unicode:
        """
        returns the value of the specified long as hexadecimal, prefixing with the HEX_PREFIX_x
         string.
        @param value the long value to convert
        """
        ...

    @overload
    @staticmethod
    def toHexString(value: long, size: int) -> unicode:
        """
        returns the value of the specified long as hexadecimal, prefixing with the HEX_PREFIX_x
         string.
        @param value the long value to convert
        @param size number of bytes to be represented
        """
        ...

    @staticmethod
    def toSignedHexString(value: long) -> unicode:
        """
        returns the value of the specified long as signed hexadecimal, prefixing with the
         HEX_PREFIX_x string.
        @param value the long value to convert
        """
        ...

    @overload
    def toString(self) -> unicode: ...

    @overload
    @staticmethod
    def toString(b: int) -> unicode:
        """
        Convert the given byte into a two character String, padding with a leading 0 if needed.
        @param b the byte
        @return the byte string
        """
        ...

    @staticmethod
    def unsignedLongToBigInteger(value: long) -> long:
        """
        Converts a <strong>unsigned</strong> long value, which is currently stored in a
         java <strong>signed</strong> long, into a {@link BigInteger}.
         <p>
         In other words, the full 64 bits of the primitive java <strong>signed</strong>
         long is being used to store an <strong>unsigned</strong> value.  This
         method converts this into a positive BigInteger value.
        @param value java <strong>unsigned</strong> long value stuffed into a
         java <strong>signed</strong> long
        @return new {@link BigInteger} with the positive value of the unsigned long value
        """
        ...

    @overload
    def wait(self) -> None: ...

    @overload
    def wait(self, __a0: long) -> None: ...

    @overload
    def wait(self, __a0: long, __a1: int) -> None: ...
