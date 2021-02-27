from typing import List
import ghidra.app.util.bin
import java.lang


class LEB128(object):




    def __init__(self): ...



    @overload
    @staticmethod
    def decode(bytes: List[int], isSigned: bool) -> long:
        """
        Decodes a LEB128 number using a byte array and stores it in a long.
         This function cannot read numbers larger than Long.MAX_VALUE.
        @param bytes the bytes representing the LEB128 number
        @param isSigned true if the value is signed
        @throws IOException
        """
        ...

    @overload
    @staticmethod
    def decode(reader: ghidra.app.util.bin.BinaryReader, isSigned: bool) -> long:
        """
        Decodes a LEB128 number using a binary reader and stores it in a long.
         <p>
         Large unsigned integers that use 64 bits will be returned in java's native
         'long' type, which is signed.  It is up to the caller to treat the value as unsigned.
         <p>
         Large integers that use more than 64 bits will cause an IOException to be thrown.
         <p>
        @param reader the binary reader
        @param isSigned true if the value is signed
        @throws IOException if an I/O error occurs
        """
        ...

    @overload
    @staticmethod
    def decode(bytes: List[int], offset: int, isSigned: bool) -> long:
        """
        Decodes a LEB128 number using an offset into a byte array and stores it in a long.
         This function cannot read numbers larger than Long.MAX_VALUE.
        @param bytes the bytes representing the LEB128 number
        @param offset offset into the byte array
        @param isSigned true if the value is signed
        @throws IOException
        """
        ...

    @staticmethod
    def decode32s(reader: ghidra.app.util.bin.BinaryReader) -> int:
        """
        Decode a LEB128 signed number and return it as a java 32 bit int.
         <p>
         If the value of the number can not fit in the int type, an {@link IOException} will
         be thrown.
        @param reader
        @return
        @throws IOException
        """
        ...

    @staticmethod
    def decode32u(reader: ghidra.app.util.bin.BinaryReader) -> int:
        """
        Decode a LEB128 unsigned number and return it as a java 32 bit int.
         <p>
         If the value of the number can not fit in the positive range of the int type,
         an {@link IOException} will be thrown.
        @param reader
        @return
        @throws IOException
        """
        ...

    def equals(self, __a0: object) -> bool: ...

    def getClass(self) -> java.lang.Class: ...

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
