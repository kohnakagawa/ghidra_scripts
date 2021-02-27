from typing import List
import ghidra.program.model.data
import java.lang


class DataOrganization(object):
    NO_MAXIMUM_ALIGNMENT: int = 0







    def clearSizeAlignmentMap(self) -> None:
        """
        Remove all entries from the size alignment map
        """
        ...

    def equals(self, __a0: object) -> bool: ...

    def getAbsoluteMaxAlignment(self) -> int:
        """
        Gets the maximum alignment value that is allowed by this data organization. When getting
         an alignment for any data type it will not exceed this value. If NO_MAXIMUM_ALIGNMENT
         is returned, the data organization isn't specifically limited.
        @return the absolute maximum alignment or NO_MAXIMUM_ALIGNMENT
        """
        ...

    def getAlignment(self, dataType: ghidra.program.model.data.DataType, dtSize: int) -> int:
        """
        Determines the alignment value for the indicated data type. (i.e. how the data type gets
         aligned within other data types.)  NOTE: the alignment of bitfields is dependent upon packing
         rules which must be considered at the composite level.
        @param dataType the data type
        @param dtSize the data type's size or component size
        @return the alignment
        """
        ...

    def getAlignmentOffset(self, minimumOffset: int, dataType: ghidra.program.model.data.DataType, dtSize: int) -> int:
        """
        Determines the offset where the specified data type should be placed to be properly aligned.
        @param minimumOffset the minimum allowable offset where the data type can be placed.
        @param dataType the data type
        @param dtSize the data type's size
        @return the aligned offset for the data type
        """
        ...

    def getBitFieldPacking(self) -> ghidra.program.model.data.BitFieldPacking:
        """
        Get the composite bitfield packing information associated with this data organization.
        @return composite bitfield packing information
        """
        ...

    def getCharSize(self) -> int:
        """
        @return the size of a char (char) primitive data type in bytes.
        """
        ...

    def getClass(self) -> java.lang.Class: ...

    def getDefaultAlignment(self) -> int:
        """
        Gets the default alignment to be used for any data type that isn't a
         structure, union, array, pointer, type definition, and whose size isn't in the
         size/alignment map.
        @return the default alignment to be used if no other alignment can be
         determined for a data type.
        """
        ...

    def getDefaultPointerAlignment(self) -> int:
        """
        Gets the default alignment to be used for a pointer that doesn't have size.
        @return the default alignment for a pointer
        """
        ...

    def getDoubleSize(self) -> int:
        """
        @return the size of a double primitive data type in bytes.
        """
        ...

    def getFloatSize(self) -> int:
        """
        @return the size of a float primitive data type in bytes.
        """
        ...

    def getForcedAlignment(self, dataType: ghidra.program.model.data.DataType) -> int: ...

    def getIntegerCTypeApproximation(self, size: int, signed: bool) -> unicode:
        """
        Returns the best fitting integer C-type whose size is less-than-or-equal
         to the specified size.  "long long" will be returned for any size larger
         than "long long";
        @param size integer size
        @param signed if false the unsigned modifier will be prepended.
        @return the best fitting
        """
        ...

    def getIntegerSize(self) -> int:
        """
        @return the size of a int primitive data type in bytes.
        """
        ...

    def getLongDoubleSize(self) -> int:
        """
        @return the size of a long double primitive data type in bytes.
        """
        ...

    def getLongLongSize(self) -> int:
        """
        @return the size of a long long primitive data type in bytes.
        """
        ...

    def getLongSize(self) -> int:
        """
        @return the size of a long primitive data type in bytes.
        """
        ...

    def getMachineAlignment(self) -> int:
        """
        Gets the maximum useful alignment for the target machine
        @return the machine alignment
        """
        ...

    def getPointerShift(self) -> int:
        """
        Shift amount affects interpretation of in-memory pointer values only
         and will also be reflected within instruction pcode.  A value of zero indicates
         that shifted-pointers are not supported.
        @return the left shift amount for shifted-pointers.
        """
        ...

    def getPointerSize(self) -> int:
        """
        @return the size of a pointer data type in bytes.
        """
        ...

    def getShortSize(self) -> int:
        """
        @return the size of a short primitive data type in bytes.
        """
        ...

    def getSizeAlignment(self, size: int) -> int:
        """
        Gets the alignment that is defined for a data type of the indicated size if one is defined.
        @param size the size of the data type
        @return the alignment of the data type.
        @throws NoValueException if there isn't an alignment defined for the indicated size.
        """
        ...

    def getSizeAlignmentCount(self) -> int:
        """
        Gets the number of sizes that have an alignment specified.
        @return the number of sizes with an alignment mapped to them.
        """
        ...

    def getSizes(self) -> List[int]:
        """
        Gets the sizes that have an alignment specified.
        @return the sizes with alignments mapped to them.
        """
        ...

    def getWideCharSize(self) -> int:
        """
        @return the size of a wide-char (wchar_t) primitive data type in bytes.
        """
        ...

    def hashCode(self) -> int: ...

    def isBigEndian(self) -> bool:
        """
        @return true if data stored big-endian byte order
        """
        ...

    def isForcingAlignment(self, dataType: ghidra.program.model.data.DataType) -> bool: ...

    def isSignedChar(self) -> bool:
        """
        @return true if the "char" type is signed
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
    def absoluteMaxAlignment(self) -> int: ...

    @property
    def bigEndian(self) -> bool: ...

    @property
    def bitFieldPacking(self) -> ghidra.program.model.data.BitFieldPacking: ...

    @property
    def charSize(self) -> int: ...

    @property
    def defaultAlignment(self) -> int: ...

    @property
    def defaultPointerAlignment(self) -> int: ...

    @property
    def doubleSize(self) -> int: ...

    @property
    def floatSize(self) -> int: ...

    @property
    def integerSize(self) -> int: ...

    @property
    def longDoubleSize(self) -> int: ...

    @property
    def longLongSize(self) -> int: ...

    @property
    def longSize(self) -> int: ...

    @property
    def machineAlignment(self) -> int: ...

    @property
    def pointerShift(self) -> int: ...

    @property
    def pointerSize(self) -> int: ...

    @property
    def shortSize(self) -> int: ...

    @property
    def signedChar(self) -> bool: ...

    @property
    def sizeAlignmentCount(self) -> int: ...

    @property
    def sizes(self) -> List[int]: ...

    @property
    def wideCharSize(self) -> int: ...
