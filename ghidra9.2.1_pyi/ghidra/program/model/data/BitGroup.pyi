import ghidra.program.model.data
import java.lang
import java.util


class BitGroup(object):
    """
    Class used to organize long values into sets of values with overlapping bits.
     For example, if you had values 1,2,3, 8, 12, you could partition them into two bit groups.
     The values 1,2,3, would be in one bit group because they all either use the "1" or "2" bit
     (If there was on "3", then 1 and 2 could be in separate groups). Also the values "8" and "12"
     are in the same group since they share the "8" bit.
    """









    def equals(self, __a0: object) -> bool: ...

    def getClass(self) -> java.lang.Class: ...

    def getMask(self) -> long:
        """
        Returns the mask that represents all the bits that are used by the values in this
         BitGroup.
        @return the mask that represents all the bits that are used by the values in this
         BitGroup.
        """
        ...

    def getValues(self) -> java.util.Set:
        """
        Gets the set of values that make up this BitGroup.
        @return the set of values that make up this BitGroup.
        """
        ...

    def hashCode(self) -> int: ...

    def intersects(self, bitGroup: ghidra.program.model.data.BitGroup) -> bool:
        """
        Tests if this bit group has any overlapping bits with the given bit group.
        @param bitGroup the BitGroup to test for overlap.
        @return true if the groups have any bits in common.
        """
        ...

    def merge(self, bitGroup: ghidra.program.model.data.BitGroup) -> None:
        """
        Merges the given BitGroup into the group.  All of its values will be added to this
         group's values and the masks will be or'ed together.
        @param bitGroup the BitGroup to merge into this one.
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

    @property
    def mask(self) -> long: ...

    @property
    def values(self) -> java.util.Set: ...
