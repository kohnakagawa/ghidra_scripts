from typing import List
import ghidra.app.util.bin.format.pe.debug
import java.lang


class OMFSrcModule(object):
    """
    A class to represent the Object Module Format (OMF) Source Module data structure.

     short cFile 		  - Number of source files contributing code to segments

     short cSeg		  - Number of code segments receiving code from module

     int [] baseSrcFile -  An array of base offsets

     int [] starts 	  - start offset within the segment of the first byte of code from the module

     int [] ends        - ending address of code from the module

     short [] segs      - Array of segment indicies that receive code from the module
    """





    def __init__(self):
        """
        DO NOT USE THIS CONSTRUCTOR, USE create*(GenericFactory ...) FACTORY METHODS INSTEAD.
        """
        ...



    def equals(self, __a0: object) -> bool: ...

    def getBaseSrcFile(self) -> List[int]:
        """
        Returns an array of base offsets.
        @return an array of base offsets
        """
        ...

    def getClass(self) -> java.lang.Class: ...

    def getEnds(self) -> List[int]:
        """
        Returns an array of ending addresses of code from the module.
        @return an array of ending addresses of code from the module
        """
        ...

    def getFileCount(self) -> int:
        """
        Returns the number of source files contributing code to segments.
        @return the number of source files contributing code to segments
        """
        ...

    def getOMFSrcModuleFiles(self) -> List[ghidra.app.util.bin.format.pe.debug.OMFSrcModuleFile]:
        """
        Returns the array of source files.
        @return the array of source files
        """
        ...

    def getSegmentCount(self) -> int:
        """
        Returns the number of code segments receiving code from module.
        @return the number of code segments receiving code from module
        """
        ...

    def getSegments(self) -> List[int]:
        """
        Returns an array of segment indicies that receive code from the module.
        @return an array of segment indicies that receive code from the module
        """
        ...

    def getStarts(self) -> List[int]:
        """
        Returns an array of start offsets within the segment of the first byte of code from the module.
        @return an array of start offsets within the segment of the first byte of code from the module
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
    def OMFSrcModuleFiles(self) -> List[ghidra.app.util.bin.format.pe.debug.OMFSrcModuleFile]: ...

    @property
    def baseSrcFile(self) -> List[int]: ...

    @property
    def ends(self) -> List[int]: ...

    @property
    def fileCount(self) -> int: ...

    @property
    def segmentCount(self) -> int: ...

    @property
    def segments(self) -> List[int]: ...

    @property
    def starts(self) -> List[int]: ...
