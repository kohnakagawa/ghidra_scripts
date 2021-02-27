from typing import Iterator
import ghidra.program.model.data
import java.lang
import java.util.Map


class NoisyStructureBuilder(object):
    """
    Build a structure from a "noisy" source of field information.
     Feed it field records, either via addDataType(), when we
     have more definitive info about the size of the field, or via addReference()
     when we have a pointer reference to the field with possibly less info about the field size.

     As records come in, overlaps and conflicts in specific field data-types are resolved.
     In a conflict, less specific data-types are replaced.
     After all information is collected a final Structure can be built by iterating over
     the final field entries.
    """





    def __init__(self): ...



    def addDataType(self, offset: long, dt: ghidra.program.model.data.DataType) -> None:
        """
        Add data-type information about a specific field
        @param offset of the field within the structure
        @param dt is the data-type of field if known (null otherwise)
        """
        ...

    def addReference(self, offset: long, dt: ghidra.program.model.data.DataType) -> None:
        """
        Adds information for a field given a pointer reference.
         The data-type information is not used unless it is a pointer.
        @param offset is the offset of the field within the structure
        @param dt is the data-type of the pointer to the field (or null)
        """
        ...

    def equals(self, __a0: object) -> bool: ...

    def getClass(self) -> java.lang.Class: ...

    def getSize(self) -> long:
        """
        @return the size of the structure in bytes (given current information)
        """
        ...

    def hashCode(self) -> int: ...

    def iterator(self) -> Iterator[java.util.Map.Entry]:
        """
        @return an iterator to the current field entries
        """
        ...

    def notify(self) -> None: ...

    def notifyAll(self) -> None: ...

    def populateOriginalStructure(self, dt: ghidra.program.model.data.Structure) -> None:
        """
        Populate this builder with fields from a preexisting Structure.
         The builder presumes it is rebuilding this Structure so it can check for
         pathological containment issues.
        @param dt is the preexisting Structure
        """
        ...

    def setMinimumSize(self, size: long) -> None:
        """
        We may have partial information about the size of the structure.  This method feeds it to the
         builder as a minimum size for the structure.
        @param size is the minimum size in bytes
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
    def minimumSize(self) -> None: ...  # No getter available.

    @minimumSize.setter
    def minimumSize(self, value: long) -> None: ...

    @property
    def size(self) -> long: ...
