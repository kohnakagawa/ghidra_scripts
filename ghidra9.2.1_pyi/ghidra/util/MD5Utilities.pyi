from typing import List
import java.io
import java.lang


class MD5Utilities(object):
    SALTED_HASH_LENGTH: int = 36
    SALT_LENGTH: int = 4
    UNSALTED_HASH_LENGTH: int = 32



    def __init__(self): ...



    def equals(self, __a0: object) -> bool: ...

    def getClass(self) -> java.lang.Class: ...

    @overload
    @staticmethod
    def getMD5Hash(msg: List[int]) -> List[int]:
        """
        Generate MD5 hash in a hex character representation
        @param msg message text
        @return hex hash value in text format
        """
        ...

    @overload
    @staticmethod
    def getMD5Hash(file: java.io.File) -> unicode:
        """
        Generate MD5 message digest hash for specified file contents.
        @param file file to be read
        @return message digest hash
        @throws IOException if opening or reading file produces an error
        """
        ...

    @overload
    @staticmethod
    def getMD5Hash(in_: java.io.InputStream) -> unicode:
        """
        Generate MD5 message digest hash for specified input stream.
         Stream will be read until EOF is reached.
        @param in input stream
        @return message digest hash
        @throws IOException if reading input stream produces an error
        """
        ...

    @overload
    @staticmethod
    def getMD5Hash(__a0: List[object]) -> unicode: ...

    @overload
    @staticmethod
    def getSaltedMD5Hash(msg: List[int]) -> List[int]:
        """
        Generate salted MD5 hash for specified message using random salt.
         First 4-characters of returned hash correspond to the salt data.
        @param msg message text
        @return salted hash using randomly generated salt which is
         returned as a prefix to the hash
        """
        ...

    @overload
    @staticmethod
    def getSaltedMD5Hash(salt: List[int], msg: List[int]) -> List[int]:
        """
        Generate salted MD5 hash for specified message.  Supplied salt is
         returned as prefix to returned hash.
        @param salt digest salt (use empty string for no salt)
        @param msg message text
        @return salted hash using specified salt which is
         returned as a prefix to the hash
        """
        ...

    def hashCode(self) -> int: ...

    @staticmethod
    def hexDump(data: List[int]) -> List[int]:
        """
        Convert binary data to a sequence of hex characters.
        @param data binary data
        @return hex character representation of data
        """
        ...

    def notify(self) -> None: ...

    def notifyAll(self) -> None: ...

    def toString(self) -> unicode: ...

    @overload
    def wait(self) -> None: ...

    @overload
    def wait(self, __a0: long) -> None: ...

    @overload
    def wait(self, __a0: long, __a1: int) -> None: ...
