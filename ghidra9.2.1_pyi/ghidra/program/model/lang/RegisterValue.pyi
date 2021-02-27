from typing import List
import ghidra.program.model.lang
import java.lang


class RegisterValue(object):
    """
    Class for representing register values that keep track of which bits are actually set.
     Values are stored as big-endian: MSB of mask is stored at bytes index 0,
     MSB of value is stored at (bytes.length/2).

     Bytes storage example for 4-byte register:
        Index:  0   1   2   3   4   5   6   7
              |MSB|   |   |LSB|MSB|   |   |LSB|
              | ----MASK----- | ----VALUE---- |
    """





    @overload
    def __init__(self, register: ghidra.program.model.lang.Register):
        """
        Creates a new RegisterValue for a register that has no value (all mask bits are 0);
        @param register the register associated with this value.
        """
        ...

    @overload
    def __init__(self, register: ghidra.program.model.lang.Register, bytes: List[int]):
        """
        Constructs a new RegisterValue object for the given register and the mask/value byte array
        @param register the register associated with this value.  The register specifies which bits
         int the total mask/value arrays are used for this register which may be a sub-register of
         some larger register.  The byte[] always is sized for the largest Register that contains
         the given register.
        @param bytes the mask/value array - the first n/2 bytes are the mask and the last n/2 bytes
         are the value bits.
        """
        ...

    @overload
    def __init__(self, register: ghidra.program.model.lang.Register, value: long):
        """
        Constructs a new RegisterValue object for the given register and value.
        @param value the value to set. All mask bits for the given register are set to "valid" (on).
        """
        ...

    @overload
    def __init__(self, register: ghidra.program.model.lang.Register, value: long, mask: long):
        """
        Constructs a new RegisterValue using a specified value and mask
        @param register
        @param value value corresponding to specified register
        @param mask value mask identifying which value bits are valid
        """
        ...



    @overload
    def assign(self, subRegister: ghidra.program.model.lang.Register, value: ghidra.program.model.lang.RegisterValue) -> ghidra.program.model.lang.RegisterValue:
        """
        Assign the value to a portion of this register value
        @param subRegister identifies a piece of this register value to be assigned
        @param value new value
        @return new register value after assignment
        """
        ...

    @overload
    def assign(self, subRegister: ghidra.program.model.lang.Register, value: long) -> ghidra.program.model.lang.RegisterValue:
        """
        Assign the value to a portion of this register value
        @param subRegister identifies a piece of this register value to be assigned
        @param value new value
        @return new register value after assignment
        """
        ...

    def clearBitValues(self, mask: List[int]) -> ghidra.program.model.lang.RegisterValue:
        """
        Clears the value bits corresponding to the "ON" bits in the given mask.
        @param mask the byte array containing the mask bits to clear.
        @return a new MaskedBytes object containg the original value bits and mask bits cleared
         where the passed in mask bits were "on".
        """
        ...

    def combineValues(self, otherValue: ghidra.program.model.lang.RegisterValue) -> ghidra.program.model.lang.RegisterValue:
        """
        Creates a new RegisterValue.
         The resulting value is a combination of this RegisterValue and the given RegisterValue,
         where the given RegisterValue's value bits take precedence over this RegisterValue's value.

         Each value bit is determined as follows:
         If the mask bit in <code>otherValue</code> is "ON", then <code>otherValue</code>'s value bit is used. Otherwise,
         <code>this</code> value bit used.

         The mask bits are OR'd together to form the new mask bits.
        @param otherValue the currently stored mask and value bytes.  The base register must match the base register
         of this register value.
        @return a new RegisterValue object containing the original value bits where the new array
         mask bits are "OFF" and the new value bits where the new array mask bits are "ON".
         If the registers differ the resulting register value will be relative to the base register.
        """
        ...

    def equals(self, obj: object) -> bool:
        """
        @see java.lang.Object#equals(java.lang.Object)
        """
        ...

    def getBaseRegisterValue(self) -> ghidra.program.model.lang.RegisterValue:
        """
        Returns this register value in terms of the base register
        """
        ...

    def getBaseValueMask(self) -> List[int]:
        """
        Returns the value mask that indicates which bits relative to the base register have a
         valid value.
        """
        ...

    def getClass(self) -> java.lang.Class: ...

    def getRegister(self) -> ghidra.program.model.lang.Register:
        """
        Returns the register used in this register value object.
        @return the register used in this register value object
        """
        ...

    def getRegisterValue(self, newRegister: ghidra.program.model.lang.Register) -> ghidra.program.model.lang.RegisterValue: ...

    def getSignedValue(self) -> long:
        """
        Returns the signed value for this register if all the appropriate mask bits are "ON". Otherwise,
         null is return.
        @return the signed value for this register if all the appropriate mask bits are "ON". Otherwise,
         returns null.
        """
        ...

    def getSignedValueIgnoreMask(self) -> long:
        """
        Returns the signed value for this register regardless of the mask bits.  Bits that have "OFF" mask
         bits will have the value of 0.
        @return the signed value for this register regardless of the mask bits.  Bits that have "OFF" mask
         bits will have the value of 0.
        """
        ...

    def getUnsignedValue(self) -> long:
        """
        Returns the unsigned value for this register if all the appropriate mask bits are "ON". Otherwise,
         null is return.
        @return the value for this register if all the appropriate mask bits are "ON". Otherwise,
         returns null.
        """
        ...

    def getUnsignedValueIgnoreMask(self) -> long:
        """
        Returns the unsigned value for this register regardless of the mask bits.  Bits that have "OFF" mask
         bits will have the value of 0.
        @return the unsigned value for this register regardless of the mask bits.  Bits that have "OFF" mask
         bits will have the value of 0.
        """
        ...

    def getValueMask(self) -> long:
        """
        Returns a value mask which is sized based upon the register
        """
        ...

    def hasAnyValue(self) -> bool: ...

    def hasValue(self) -> bool:
        """
        Tests if this RegisterValue contains valid value bits for the entire register.  In otherwords
         getSignedValue() or getUnsignedValue will not return null.
        @return true if all mask bits for the associated register are "ON".
        """
        ...

    def hashCode(self) -> int: ...

    def notify(self) -> None: ...

    def notifyAll(self) -> None: ...

    def toBytes(self) -> List[int]:
        """
        Returns the mask/value bytes for this register value.
        @return the mask/value bytes for this register value.
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
    def baseRegisterValue(self) -> ghidra.program.model.lang.RegisterValue: ...

    @property
    def baseValueMask(self) -> List[int]: ...

    @property
    def register(self) -> ghidra.program.model.lang.Register: ...

    @property
    def signedValue(self) -> long: ...

    @property
    def signedValueIgnoreMask(self) -> long: ...

    @property
    def unsignedValue(self) -> long: ...

    @property
    def unsignedValueIgnoreMask(self) -> long: ...

    @property
    def valueMask(self) -> long: ...
