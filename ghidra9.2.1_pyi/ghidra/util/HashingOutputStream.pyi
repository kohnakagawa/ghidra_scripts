from typing import List
import java.io
import java.lang


class HashingOutputStream(java.io.OutputStream):
    """
    A filtering OutputStream that calculates the hash of the bytes being
     written.

     Call #getDigest() to retrieve the hash value bytes.
    """





    def __init__(self, out: java.io.OutputStream, hashAlgo: unicode):
        """
        @param out - OutputStream to wrap
        @param hashAlgo - see {@link MessageDigest#getInstance(String)}, ie. "MD5".
        @throws NoSuchAlgorithmException
        """
        ...



    def close(self) -> None: ...

    def equals(self, __a0: object) -> bool: ...

    def flush(self) -> None: ...

    def getClass(self) -> java.lang.Class: ...

    def getDigest(self) -> List[int]: ...

    def hashCode(self) -> int: ...

    def notify(self) -> None: ...

    def notifyAll(self) -> None: ...

    @staticmethod
    def nullOutputStream() -> java.io.OutputStream: ...

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
    def digest(self) -> List[int]: ...
