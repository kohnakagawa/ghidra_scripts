from typing import List
import ghidra.util
import java.io
import java.lang


class DataConverter(java.io.Serializable, object):
    """
    Stateless helper classes with static singleton instances that contain methods to convert
     Java numeric types to and from their raw form in a byte array.

    """









    def equals(self, __a0: object) -> bool: ...

    @overload
    def getBigInteger(self, b: List[int], size: int, signed: bool) -> long:
        """
        Get the value from the given byte array using the specified size.
        @param b array containing bytes
        @param size number of bytes to use from array at offset 0
        @param signed boolean flag indicating the value is signed
        @return {@link BigInteger} with value
        @throws IndexOutOfBoundsException if byte array size is
         less than size
        """
        ...

    @overload
    def getBigInteger(self, b: List[int], offset: int, size: int, signed: bool) -> long:
        """
        Get the value from the given byte array using the specified size.
        @param b array containing bytes
        @param size number of bytes to use from array
        @param offset offset into byte array for getting the long
        @param signed boolean flag indicating the value is signed
        @return {@link BigInteger} with value
        @throws IndexOutOfBoundsException if byte array size is
         less than offset+size
        """
        ...

    @overload
    def getBytes(self, value: long) -> List[int]:
        """
        Converts the long value to an array of bytes.
        @param value long value to be converted
        @return array of bytes
        """
        ...

    @overload
    def getBytes(self, value: int) -> List[int]:
        """
        Converts the short value to an array of bytes.
        @param value short value to be converted
        @return array of bytes
        """
        ...

    @overload
    def getBytes(self, value: int) -> List[int]:
        """
        Converts the short value to an array of bytes.
        @param value short value to be converted
        @return array of bytes
        """
        ...

    @overload
    def getBytes(self, value: long, size: int) -> List[int]:
        """
        Converts the value to an array of bytes.
        @param value value to be converted
        @param size value size in bytes
        @return array of bytes
        """
        ...

    @overload
    def getBytes(self, value: long, b: List[int]) -> None:
        """
        Converts the given value to bytes.
         <p>
         See {@link #putLong(byte[], long)}
        @param value value to convert to bytes
        @param b byte array to store bytes
        @throws IndexOutOfBoundsException if b.length is not at least
         8.
        """
        ...

    @overload
    def getBytes(self, value: int, b: List[int]) -> None:
        """
        Converts the given value to bytes.
         See {@link #putShort(byte[], short)}
        @param value value to convert to bytes
        @param b byte array to store bytes
        @throws IndexOutOfBoundsException if b.length is not at least
         2.
        """
        ...

    @overload
    def getBytes(self, value: int, b: List[int]) -> None:
        """
        Converts the given value to bytes.
         See {@link #putShort(byte[], short)}
        @param value value to convert to bytes
        @param b byte array to store bytes
        @throws IndexOutOfBoundsException if b.length is not at least
         2.
        """
        ...

    @overload
    def getBytes(self, value: long, b: List[int], offset: int) -> None:
        """
        Converts the given value to bytes.
         <p>
         See {@link #putLong(byte[], long)}
        @param value value to convert to bytes
        @param b byte array to store bytes
        @param offset offset into byte array to put the bytes
        @throws IndexOutOfBoundsException if (offset+8)&gt;b.length
        """
        ...

    @overload
    def getBytes(self, value: int, b: List[int], offset: int) -> None:
        """
        Converts the given value to bytes.
         <p>
         See {@link #putShort(byte[], int, short)}
        @param value value to convert to bytes
        @param b byte array to store bytes
        @param offset offset into byte array to put the bytes
        @throws IndexOutOfBoundsException if (offset+2)&gt;b.length
        """
        ...

    @overload
    def getBytes(self, value: int, b: List[int], offset: int) -> None:
        """
        Converts the given value to bytes.
         <p>
         See {@link #putShort(byte[], int, short)}
        @param value value to convert to bytes
        @param b byte array to store bytes
        @param offset offset into byte array to put the bytes
        @throws IndexOutOfBoundsException if (offset+2)&gt;b.length
        """
        ...

    @overload
    def getBytes(self, value: long, size: int, b: List[int], offset: int) -> None:
        """
        Converts the given value to bytes using the number of least significant bytes
         specified by size.
         <p>
         See {@link #putValue(long, int, byte[], int)}
        @param value value to convert to bytes
        @param size number of least significant bytes of value to be written to the byte array
        @param b byte array to store bytes
        @param offset offset into byte array to put the bytes
        @throws IndexOutOfBoundsException if (offset+size)&gt;b.length
        """
        ...

    @overload
    def getBytes(self, value: long, size: int, b: List[int], offset: int) -> None:
        """
        Converts the given value to bytes using the number of least significant bytes
         specified by size.
         <p>
         See {@link #putValue(long, int, byte[], int)}
        @param value value to convert to bytes
        @param size number of least significant bytes of value to be written to the byte array
        @param b byte array to store bytes
        @param offset offset into byte array to put the bytes
        @throws IndexOutOfBoundsException if (offset+size)&gt;b.length
        """
        ...

    def getClass(self) -> java.lang.Class: ...

    @staticmethod
    def getInstance(isBigEndian: bool) -> ghidra.util.DataConverter:
        """
        Returns the correct DataConverter static instance for the requested endian-ness.
        @param isBigEndian boolean flag, true means big endian
        @return static DataConverter instance
        """
        ...

    @overload
    def getInt(self, b: List[int]) -> int:
        """
        Get the int value from the given byte array.
        @param b array containing bytes
        @return signed int value from the beginning of the specified array
        @throws IndexOutOfBoundsException if byte array size is less than 4
        """
        ...

    @overload
    def getInt(self, b: List[int], offset: int) -> int:
        """
        Get the int value from the given byte array.
        @param b array containing bytes
        @param offset offset into byte array for getting the int
        @return signed int value
        @throws IndexOutOfBoundsException if byte array size is less than offset+4
        """
        ...

    @overload
    def getLong(self, b: List[int]) -> long:
        """
        Get the long value from the given byte array.
        @param b array containing bytes
        @return signed long value from the beginning of the specified array
        @throws IndexOutOfBoundsException if byte array size is less than 8
        """
        ...

    @overload
    def getLong(self, b: List[int], offset: int) -> long:
        """
        Get the long value from the given byte array.
        @param b array containing bytes
        @param offset offset into byte array for getting the long
        @return signed long value
        @throws IndexOutOfBoundsException if byte array size is less than offset+8
        """
        ...

    @overload
    def getShort(self, b: List[int]) -> int:
        """
        Get the short value from the given byte array.
        @param b array containing bytes
        @return signed short value from the beginning of the specified array
        @throws IndexOutOfBoundsException if byte array size is less than 2.
        """
        ...

    @overload
    def getShort(self, b: List[int], offset: int) -> int:
        """
        Get the short value from the given byte array.
        @param b array containing bytes
        @param offset offset into byte array for getting the short
        @return signed short value
        @throws IndexOutOfBoundsException if byte array size is less than offset+2
        """
        ...

    @overload
    def getSignedValue(self, b: List[int], size: int) -> long:
        """
        Get the <b>signed</b> value from the given byte array using the specified
         integer size, returned as a long.
         <p>
         Values with a size less than sizeof(long) will have their sign bit
         extended.
        @param b array containing bytes
        @param size number of bytes (1 - 8) to use from array at offset 0
        @return signed value from the beginning of the specified array
        @throws IndexOutOfBoundsException if byte array size is less than specified size
        """
        ...

    @overload
    def getSignedValue(self, b: List[int], offset: int, size: int) -> long:
        """
        Get the <b>signed</b> value from the given byte array using the specified
         integer size, returned as a long.
         <p>
         Values with a size less than sizeof(long) will have their sign bit
         extended.
        @param b array containing bytes
        @param size number of bytes (1 - 8) to use from array
        @param offset offset into byte array for getting the long
        @return signed value
        @throws IndexOutOfBoundsException if byte array size is
         less than offset+size or size is greater than 8 (sizeof long)
        """
        ...

    @overload
    def getValue(self, b: List[int], size: int) -> long:
        """
        Get the <b>unsigned</b> value from the given byte array using the specified
         integer size, returned as a long.
         <p>
         Values with a size less than sizeof(long) will <b>not</b> have their sign bit
         extended and therefore will appear as an 'unsigned' value.
         <p>
         Casting the 'unsigned' long value to the correctly sized smaller
         java primitive will cause the value to appear as a signed value.
         <p>
         Values of size 8 (ie. longs) will be signed.
        @param b array containing bytes
        @param size number of bytes (1 - 8) to use from array at offset 0
        @return unsigned value from the beginning of the specified array
        @throws IndexOutOfBoundsException if byte array size is less than specified size
        """
        ...

    @overload
    def getValue(self, b: List[int], offset: int, size: int) -> long:
        """
        Get the <b>unsigned</b> value from the given byte array using the specified
         integer size, returned as a long.
         <p>
         Values with a size less than sizeof(long) will <b>not</b> have their sign bit
         extended and therefore will appear as an 'unsigned' value.
         <p>
         Casting the 'unsigned' long value to the correctly sized smaller
         java primitive will cause the value to appear as a signed value.
         <p>
         Values of size 8 (ie. longs) will be signed.
        @param b array containing bytes
        @param size number of bytes (1 - 8) to use from array
        @param offset offset into byte array for getting the long
        @return unsigned value
        @throws IndexOutOfBoundsException if byte array size is
         less than offset+size or size is greater than 8 (sizeof long)
        """
        ...

    def hashCode(self) -> int: ...

    def isBigEndian(self) -> bool:
        """
        Returns the endianess of this DataConverter instance.
        @return boolean flag, true means big-endian
        """
        ...

    def notify(self) -> None: ...

    def notifyAll(self) -> None: ...

    @overload
    def putBigInteger(self, b: List[int], size: int, value: long) -> None:
        """
        Writes a value of specified size into the byte array at the given offset.
         <p>
         See {@link #getBytes(BigInteger, int, byte[], int)}
        @param b array to contain the bytes at offset 0
        @param size number of bytes to be written
        @param value BigInteger value to convert
        @throws IndexOutOfBoundsException if byte array is less than specified size
        """
        ...

    @overload
    def putBigInteger(self, b: List[int], offset: int, size: int, value: long) -> None:
        """
        Writes a value of specified size into the byte array at the given offset
         <p>
         See {@link #getBytes(BigInteger, int, byte[], int)}
        @param b array to contain the bytes
        @param offset the offset into the byte array to store the value
        @param size number of bytes to be written
        @param value BigInteger value to convert
        @throws IndexOutOfBoundsException if (offset+size)&gt;b.length
        """
        ...

    @overload
    def putInt(self, b: List[int], value: int) -> None:
        """
        Writes a int value into a byte array.
         <p>
         See {@link #getBytes(int, byte[])}
        @param b array to contain the bytes
        @param value the int value
        @throws IndexOutOfBoundsException if byte array is too small to hold the value
        """
        ...

    @overload
    def putInt(self, b: List[int], offset: int, value: int) -> None:
        """
        Writes a int value into the byte array at the given offset.
         <p>
         See {@link #getBytes(int, byte[], int)}
        @param b array to contain the bytes
        @param offset the offset into the byte array to store the value
        @param value the int value
        @throws IndexOutOfBoundsException if offset is too large or byte array
         is too small to hold the value
        """
        ...

    @overload
    def putLong(self, b: List[int], value: long) -> None:
        """
        Writes a long value into a byte array.
         <p>
         See {@link #getBytes(long, byte[])}
        @param b array to contain the bytes
        @param value the long value
        @throws IndexOutOfBoundsException if byte array is too small to hold the value
        """
        ...

    @overload
    def putLong(self, b: List[int], offset: int, value: long) -> None:
        """
        Writes a long value into the byte array at the given offset
         <p>
         See {@link #getBytes(long, byte[], int)}
        @param b array to contain the bytes
        @param offset the offset into the byte array to store the value
        @param value the long value
        @throws IndexOutOfBoundsException if offset is too large or byte array
         is too small to hold the value
        """
        ...

    @overload
    def putShort(self, b: List[int], value: int) -> None:
        """
        Writes a short value into a byte array.
        @param b array to contain the bytes
        @param value the short value
        @throws IndexOutOfBoundsException if byte array is too small to hold the value
        """
        ...

    @overload
    def putShort(self, b: List[int], offset: int, value: int) -> None:
        """
        Writes a short value into the byte array at the given offset
        @param b array to contain the bytes
        @param offset the offset into the byte array to store the value
        @param value the short value
        @throws IndexOutOfBoundsException if offset is too large or byte array
         is too small to hold the value
        """
        ...

    def putValue(self, value: long, size: int, b: List[int], offset: int) -> None:
        """
        Converts the given value to bytes using the number of least significant bytes
         specified by size.
         <p>
        @param value value to convert to bytes
        @param size number of least significant bytes of value to be written to the byte array
        @param b byte array to store bytes
        @param offset offset into byte array to put the bytes
        @throws IndexOutOfBoundsException if (offset+size)&gt;b.length
        """
        ...

    @staticmethod
    def swapBytes(val: long, size: int) -> long:
        """
        Swap the least-significant bytes (based upon size)
        @param val value whose bytes are to be swapped
        @param size number of least significant bytes to be swapped
        @return value with bytes swapped (any high-order bytes beyond size will be 0)
        """
        ...

    def toString(self) -> unicode: ...

    @overload
    def wait(self) -> None: ...

    @overload
    def wait(self, __a0: long) -> None: ...

    @overload
    def wait(self, __a0: long, __a1: int) -> None: ...

    @property
    def bigEndian(self) -> bool: ...
