from typing import List
import ghidra.app.util.bin.format.pe.debug
import java.lang


class OMFSrcModuleFile(object):
    """
    A class to represent the Object Module Format (OMF) Source Module File data structure.

     This class describes the code segments that receive code from a source file.

     short cSeg 		- Number of segments that receive code from the source file.

     short pad 		- pad field to maintain alignment

     int [] baseSrcLn - array of offsets for the line or address mapping for each segment that receives code from the source file.

     int [] starts 	- starting addresses within the segment of the first byte of code from the module.

     int [] ends 		- ending addresses of the code from the module.

     byte cbName 		- count or number of bytes in source file name.

     String name 		- name of source file.

    """





    def __init__(self):
        """
        DO NOT USE THIS CONSTRUCTOR, USE create*(GenericFactory ...) FACTORY METHODS INSTEAD.
        """
        ...



    def equals(self, __a0: object) -> bool: ...

    def getBaseSrcLn(self) -> List[int]:
        """
        Returns an array of offsets for the line or address mapping for each segment
         that receives code from the source file.
        @return an array of offsets for the line or address mapping for each segment
        """
        ...

    def getClass(self) -> java.lang.Class: ...

    def getEnds(self) -> List[int]:
        """
        Returns the ending addresses of the code from the module.
        @return the ending addresses of the code from the module
        """
        ...

    def getName(self) -> unicode:
        """
        Returns the name of source file.
        @return the name of source file
        """
        ...

    def getOMFSrcModuleLines(self) -> List[ghidra.app.util.bin.format.pe.debug.OMFSrcModuleLine]:
        """
        Returns an array of the source module lines.
        @return an array of the source module lines
        """
        ...

    def getPad(self) -> int:
        """
        Returns the pad field to maintain alignment.
        @return the pad field to maintain alignment
        """
        ...

    def getSegmentCount(self) -> int:
        """
        Returns the number of segments that receive code from the source file.
        @return the number of segments that receive code from the source file
        """
        ...

    def getStarts(self) -> List[int]:
        """
        Returns the starting addresses within the segment of the first byte of code from the module.
        @return the starting addresses within the segment of the first byte of code from the module
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
    def OMFSrcModuleLines(self) -> List[ghidra.app.util.bin.format.pe.debug.OMFSrcModuleLine]: ...

    @property
    def baseSrcLn(self) -> List[int]: ...

    @property
    def ends(self) -> List[int]: ...

    @property
    def name(self) -> unicode: ...

    @property
    def pad(self) -> int: ...

    @property
    def segmentCount(self) -> int: ...

    @property
    def starts(self) -> List[int]: ...
