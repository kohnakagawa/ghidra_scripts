from typing import List
import java.lang


class GUID(object):
    """
    GUIDs identify objects such as interfaces, manager entry-point vectors (EPVs),
     and class objects. A GUID is a 128-bit value consisting of one group
     of 8 hexadecimal digits, followed by three groups of 4 hexadecimal
     digits each, followed by one group of 12 hexadecimal digits. The
     following example shows the groupings of hexadecimal digits in a GUID.

     6B29FC40-CA47-1067-B31D-00DD010662DA


     typedef struct _GUID {
     		DWORD Data1;
     		WORD Data2;
     		WORD Data3;
     		BYTE Data4[8];
     } GUID;

     Data1 - Specifies the first 8 hexadecimal digits of the GUID.
     Data2 - Specifies the first group of 4 hexadecimal digits.
     Data3 - Specifies the second group of 4 hexadecimal digits.
     Data4 - Array of 8 bytes.
             The first 2 bytes contain the third group of 4 hexadecimal digits.
             The remaining 6 bytes contain the final 12 hexadecimal digits.
    """

    SIZEOF: int = 16



    @overload
    def __init__(self, guidString: unicode):
        """
        Creates a GUID object using the GUID string form.
        @param guidString - "6B29FC40-CA47-1067-B31D-00DD010662DA"
        @throws IllegalArgumentException if string does not represent a valid GUID
        """
        ...

    @overload
    def __init__(self, reader: ghidra.app.util.bin.BinaryReader):
        """
        Reads a GUID from the given binary reader.
        @param reader the binary reader to read the GUID
        @throws IOException if an I/O error occurs while reading the GUID
        """
        ...

    @overload
    def __init__(self, buf: ghidra.program.model.mem.MemBuffer):
        """
        Reads a GUID from the given memory buffer.
        @param buf the memory buffer to read the GUID
        @throws MemoryAccessException if an error occurs while reading the GUID
        """
        ...

    @overload
    def __init__(self, data1: int, data2: int, data3: int, data4: List[int]):
        """
        Constructs a GUID using the constitute pieces.
        """
        ...



    def equals(self, obj: object) -> bool: ...

    def getClass(self) -> java.lang.Class: ...

    def getData1(self) -> int:
        """
        Specifies the first 8 hexadecimal digits of the GUID.
        @return
        """
        ...

    def getData2(self) -> int:
        """
        Specifies the first group of 4 hexadecimal digits.
        @return
        """
        ...

    def getData3(self) -> int:
        """
        Specifies the second group of 4 hexadecimal digits.
        @return
        """
        ...

    def getData4(self) -> List[int]:
        """
        Array of 8 bytes.
         The first 2 bytes contain the third group of 4 hexadecimal digits.
         The remaining 6 bytes contain the final 12 hexadecimal digits.
        @return
        """
        ...

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

    @property
    def data1(self) -> int: ...

    @property
    def data2(self) -> int: ...

    @property
    def data3(self) -> int: ...

    @property
    def data4(self) -> List[int]: ...
