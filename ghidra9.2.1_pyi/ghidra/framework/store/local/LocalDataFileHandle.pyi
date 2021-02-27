from typing import List
import ghidra.framework.store
import java.lang


class LocalDataFileHandle(object, ghidra.framework.store.DataFileHandle):
    """
    LocalDataFileHandle provides random access to
     a local File.
    """





    def __init__(self, file: java.io.File, readOnly: bool):
        """
        Construct and open a local DataFileHandle.
        @param file file to be opened
        @param readOnly if true resulting handle may only be read.
        @throws FileNotFoundException if file was not found
        @throws IOException if an IO Error occurs
        """
        ...



    def close(self) -> None: ...

    def equals(self, __a0: object) -> bool: ...

    def getClass(self) -> java.lang.Class: ...

    def hashCode(self) -> int: ...

    def isReadOnly(self) -> bool: ...

    def length(self) -> long: ...

    def notify(self) -> None: ...

    def notifyAll(self) -> None: ...

    @overload
    def read(self, b: List[int]) -> None: ...

    @overload
    def read(self, b: List[int], off: int, len: int) -> None: ...

    def seek(self, pos: long) -> None: ...

    def setLength(self, newLength: long) -> None: ...

    def skipBytes(self, n: int) -> int: ...

    def toString(self) -> unicode: ...

    @overload
    def wait(self) -> None: ...

    @overload
    def wait(self, __a0: long) -> None: ...

    @overload
    def wait(self, __a0: long, __a1: int) -> None: ...

    @overload
    def write(self, b: int) -> None: ...

    @overload
    def write(self, b: List[int]) -> None: ...

    @overload
    def write(self, b: List[int], off: int, len: int) -> None: ...

    @property
    def readOnly(self) -> bool: ...
