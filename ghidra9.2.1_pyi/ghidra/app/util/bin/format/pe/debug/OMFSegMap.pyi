from typing import List
import ghidra.app.util.bin.format.pe.debug
import java.lang


class OMFSegMap(object):
    """

     typedef struct OMFSegMap {
         unsigned short  cSeg;        // total number of segment descriptors
         unsigned short  cSegLog;     // number of logical segment descriptors
         OMFSegMapDesc   rgDesc[0];   // array of segment descriptors
     };

    """





    def __init__(self):
        """
        DO NOT USE THIS CONSTRUCTOR, USE create*(GenericFactory ...) FACTORY METHODS INSTEAD.
        """
        ...



    def equals(self, __a0: object) -> bool: ...

    def getClass(self) -> java.lang.Class: ...

    def getLogicalSegmentDescriptorCount(self) -> int:
        """
        Returns the number of logical segment descriptors.
        @return the number of logical segment descriptors
        """
        ...

    def getSegmentDescriptor(self) -> List[ghidra.app.util.bin.format.pe.debug.OMFSegMapDesc]:
        """
        Returns the array of segment descriptors.
        @return the array of segment descriptors
        """
        ...

    def getSegmentDescriptorCount(self) -> int:
        """
        Returns the total number of segment descriptors.
        @return the total number of segment descriptors
        """
        ...

    def hashCode(self) -> int: ...

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
    def logicalSegmentDescriptorCount(self) -> int: ...

    @property
    def segmentDescriptor(self) -> List[ghidra.app.util.bin.format.pe.debug.OMFSegMapDesc]: ...

    @property
    def segmentDescriptorCount(self) -> int: ...
