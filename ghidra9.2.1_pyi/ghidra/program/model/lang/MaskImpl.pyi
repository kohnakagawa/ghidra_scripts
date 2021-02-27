from typing import List
import ghidra.program.model.lang
import ghidra.program.model.mem
import java.io
import java.lang


class MaskImpl(object, ghidra.program.model.lang.Mask, java.io.Serializable):
    """
    Implements the Mask interface as a byte array.
    """





    def __init__(self, msk: List[int]):
        """
        Construct a mask from a byte array.
        @param msk the bits that make up the mask.
        """
        ...



    @overload
    def applyMask(self, buffer: ghidra.program.model.mem.MemBuffer) -> List[int]:
        """
        @see ghidra.program.model.lang.Mask#applyMask(ghidra.program.model.mem.MemBuffer)
        """
        ...

    @overload
    def applyMask(self, cde: List[int], result: List[int]) -> List[int]:
        """
        @see ghidra.program.model.lang.Mask#applyMask(byte[], byte[])
        """
        ...

    @overload
    def applyMask(self, cde: List[int], cdeOffset: int, results: List[int], resultsOffset: int) -> None: ...

    def complementMask(self, msk: List[int], results: List[int]) -> List[int]:
        """
        @see ghidra.program.model.lang.Mask#complementMask(byte[], byte[])
        """
        ...

    def equalMaskedValue(self, cde: List[int], target: List[int]) -> bool:
        """
        @see ghidra.program.model.lang.Mask#equalMaskedValue(byte[], byte[])
        """
        ...

    @overload
    def equals(self, otherMask: List[int]) -> bool:
        """
        @see ghidra.program.model.lang.Mask#equals(byte[])
        """
        ...

    @overload
    def equals(self, obj: object) -> bool:
        """
        @see java.lang.Object#equals(java.lang.Object)
        """
        ...

    def getBytes(self) -> List[int]:
        """
        @see ghidra.program.model.lang.Mask#getBytes()
        """
        ...

    def getClass(self) -> java.lang.Class: ...

    def hashCode(self) -> int: ...

    def notify(self) -> None: ...

    def notifyAll(self) -> None: ...

    def subMask(self, msk: List[int]) -> bool:
        """
        @see ghidra.program.model.lang.Mask#subMask(byte[])
        """
        ...

    def toString(self) -> unicode:
        """
        @see java.lang.Object#toString()
        """
        ...

    @overload
    def wait(self) -> None: ...

    @overload
    def wait(self, __a0: long) -> None: ...

    @overload
    def wait(self, __a0: long, __a1: int) -> None: ...

    @property
    def bytes(self) -> List[int]: ...
