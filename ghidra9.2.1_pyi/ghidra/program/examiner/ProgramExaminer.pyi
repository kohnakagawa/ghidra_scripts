from typing import List
import java.lang


class ProgramExaminer(object):
    """
    Wrapper for Ghidra code to find images (and maybe other artifacts later) in a program

     NOTE: This is intended for end-user use and has no direct references within Ghidra.
     Typical use of the class entails generating a ghidra.jar (see BuildGhidraJarScript.java)
     and referencing this class from end-user code.
    """





    @overload
    def __init__(self, bytes: List[int]):
        """
        Constructs a new ProgramExaminer.
        @param bytes the bytes of the potential program to be examined.
        @throws GhidraException if any exception occurs while processing the bytes.
        """
        ...

    @overload
    def __init__(self, file: java.io.File):
        """
        Constructs a new ProgramExaminer.
        @param file file object containing the bytes to be examined.
        @throws GhidraException if any exception occurs while processing the bytes.
        """
        ...



    def dispose(self) -> None:
        """
        Releases file/database resources.
        """
        ...

    def equals(self, __a0: object) -> bool: ...

    def getClass(self) -> java.lang.Class: ...

    def getImages(self) -> List[int]:
        """
        Returns a list of byte[] containing image data.  The bytes will be either a png, a gif, or
         a bitmap
        """
        ...

    def getType(self) -> unicode:
        """
        Returns a string indication the program format. i.e. PE, elf, raw
        """
        ...

    def hashCode(self) -> int: ...

    @staticmethod
    def initializeGhidra() -> None: ...

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
    def images(self) -> List[object]: ...

    @property
    def type(self) -> unicode: ...
