from typing import List
import java.io
import java.lang


class HashUtilities(object):
    MD5_ALGORITHM: unicode
    MD5_SALTED_HASH_LENGTH: int = 36
    MD5_UNSALTED_HASH_LENGTH: int = 32
    SALT_LENGTH: int = 4
    SHA256_ALGORITHM: unicode
    SHA256_SALTED_HASH_LENGTH: int = 68
    SHA256_UNSALTED_HASH_LENGTH: int = 64



    def __init__(self): ...



    def equals(self, __a0: object) -> bool: ...

    def getClass(self) -> java.lang.Class: ...

    @overload
    @staticmethod
    def getHash(algorithm: unicode, msg: List[int]) -> List[int]:
        """
        Generate hash in a hex character representation
        @param algorithm message digest algorithm
        @param msg message text
        @return hex hash value in text format
        @throws IllegalArgumentException if specified algorithm is not supported
        @see MessageDigest for supported algorithms
        """
        ...

    @overload
    @staticmethod
    def getHash(algorithm: unicode, file: java.io.File) -> unicode:
        """
        Generate message digest hash for specified file contents.
        @param algorithm message digest algorithm
        @param file file to be read
        @return message digest hash
        @throws IOException if opening or reading file produces an error
        @throws IllegalArgumentException if specified algorithm is not supported
        @see MessageDigest for supported hash algorithms
        """
        ...

    @overload
    @staticmethod
    def getHash(algorithm: unicode, in_: java.io.InputStream) -> unicode:
        """
        Generate message digest hash for specified input stream.  Stream will be read
         until EOF is reached.
        @param algorithm message digest algorithm
        @param in input stream
        @return message digest hash
        @throws IOException if reading input stream produces an error
        @throws IllegalArgumentException if specified algorithm is not supported
        @see MessageDigest for supported hash algorithms
        """
        ...

    @overload
    @staticmethod
    def getHash(__a0: unicode, __a1: List[object]) -> unicode: ...

    @overload
    @staticmethod
    def getSaltedHash(algorithm: unicode, msg: List[int]) -> List[int]:
        """
        Generate salted hash for specified message using random salt.
         First 4-characters of returned hash correspond to the salt data.
        @param algorithm message digest algorithm
        @param msg message text
        @return salted hash using randomly generated salt which is
         returned as a prefix to the hash
        @throws IllegalArgumentException if specified algorithm is not supported
        @see MessageDigest for supported hash algorithms
        """
        ...

    @overload
    @staticmethod
    def getSaltedHash(algorithm: unicode, salt: List[int], msg: List[int]) -> List[int]:
        """
        Generate salted hash for specified message.  Supplied salt is
         returned as prefix to returned hash.
        @param algorithm message digest algorithm
        @param salt digest salt (use empty string for no salt)
        @param msg message text
        @return salted hash using specified salt which is
         returned as a prefix to the hash
        @throws IllegalArgumentException if specified algorithm is not supported
        @see MessageDigest for supported hash algorithms
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
