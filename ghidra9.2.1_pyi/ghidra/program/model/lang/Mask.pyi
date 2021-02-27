from typing import List
import ghidra.program.model.mem
import java.lang


class Mask(object):
    """
    The Mask class is used to perform some basic bit tests on an
     array of bits.
    """









    @overload
    def applyMask(self, buffer: ghidra.program.model.mem.MemBuffer) -> List[int]:
        """
        Apply the mask to a memory buffer.
        @param buffer the memory buffer that contains the values to be masked
        @return the resulting masked byte array.
        @exception MemoryAccessException thrown if mask exceeds the available data
         within buffer
        """
        ...

    @overload
    def applyMask(self, cde: List[int], results: List[int]) -> List[int]:
        """
        Apply the mask to a byte array.
        @param cde the array that contains the values to be masked
        @param results the array to contain the results.
        @return the resulting byte array.
        @exception IncompatibleMaskException thrown if byte
         arrays are not of the correct size
        """
        ...

    @overload
    def applyMask(self, cde: List[int], cdeOffset: int, results: List[int], resultsOffset: int) -> None:
        """
        Apply the mask to a byte array.
        @param cde the array that contains the values to be masked
        @param cdeOffset the offset into the array that contains the values to be masked
        @param results the array to contain the results.
        @param resultsOffset the offset into the array that contains the results
        @exception IncompatibleMaskException thrown if byte
         arrays are not of the correct size
        """
        ...

    def complementMask(self, msk: List[int], results: List[int]) -> List[int]:
        """
        applies the complement of the mask to the given byte array.
        @param msk the bytes to apply the inverted mask.
        @param results the array for storing the results.
        @return the results array.
        @exception IncompatibleMaskException thrown if byte
         arrays are not of the correct size
        """
        ...

    def equalMaskedValue(self, cde: List[int], target: List[int]) -> bool:
        """
        Tests if the results of apply the mask to the given array matches a
           target array.
        @param cde the source bytes.
        @param target the result bytes to be tested.
        @return true if the target array is equal to the source array with
           the mask applied.
        @exception IncompatibleMaskException thrown if byte
         arrays are not of the correct size
        """
        ...

    @overload
    def equals(self, mask: List[int]) -> bool:
        """
        Check if the mask represented by the byte array is equal to this one.
        @param mask mask represented as byte array
        @return true if the masks are the same, false otherwise
        """
        ...

    @overload
    def equals(self, obj: object) -> bool:
        """
        Test if the given object is equal to this object. Two masks are
           equal if they have exactly the same values in thier byte arrays.
        @param obj the object to be tested for equals
        @return true if the object is equal to this mask, false otherwise.
        """
        ...

    def getBytes(self) -> List[int]:
        """
        Returns the bytes that make up this mask.
        """
        ...

    def getClass(self) -> java.lang.Class: ...

    def hashCode(self) -> int: ...

    def notify(self) -> None: ...

    def notifyAll(self) -> None: ...

    def subMask(self, msk: List[int]) -> bool:
        """
        Tests if the given mask matches the this mask for the first n
           bytes, where n is the size of the given mask.
        @param msk the bytes to be tested to see if they match the first
           bytes of this mask.
        @return true if the bytes match up to the length of the passed in
           byte array.
        @exception IncompatibleMaskException thrown if byte
         arrays are not of the correct size
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
    def bytes(self) -> List[int]: ...
