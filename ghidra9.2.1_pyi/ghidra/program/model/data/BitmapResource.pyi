from typing import List
import ghidra.program.model.data
import ghidra.program.model.mem
import java.lang


class BitmapResource(object):




    def __init__(self, buf: ghidra.program.model.mem.MemBuffer):
        """
        @throws IOException
        """
        ...



    def equals(self, __a0: object) -> bool: ...

    def getBitCount(self) -> int: ...

    def getClass(self) -> java.lang.Class: ...

    def getClrImportant(self) -> int: ...

    def getClrUsed(self) -> int: ...

    def getColorMap(self, buf: ghidra.program.model.mem.MemBuffer) -> List[int]: ...

    def getColorMapLength(self) -> int:
        """
        @return int
        """
        ...

    def getCompression(self) -> int: ...

    def getDataImage(self, buf: ghidra.program.model.mem.MemBuffer) -> ghidra.program.model.data.DataImage:
        """
        @return DataImage
        """
        ...

    def getHeight(self) -> int: ...

    def getImageDataSize(self) -> int:
        """
        Returns the uncompressed image data size.  The default implementation will
         return the image data size specified by the header if non-zero, otherwize
         a computed data length will be returned based upon getHeight(), getWidth() and
         getBitCount().
        @return image data size
        """
        ...

    def getMaskLength(self) -> int:
        """
        @return int size of mask section in bytes
        """
        ...

    def getPixelData(self, buf: ghidra.program.model.mem.MemBuffer) -> List[int]: ...

    def getPlanes(self) -> int: ...

    def getRGBData(self, buf: ghidra.program.model.mem.MemBuffer) -> List[int]: ...

    def getRawSizeImage(self) -> int:
        """
        Get the raw image data size as contained within this resource.  If compressed,
         this will be smaller than the value returned by {@link #getImageDataSize()} which reflects
         the uncompressed size.
        @return raw image data size
        """
        ...

    def getSize(self) -> int: ...

    def getWidth(self) -> int: ...

    def getXPelsPerMeter(self) -> int: ...

    def getYPelsPerMeter(self) -> int: ...

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
    def XPelsPerMeter(self) -> int: ...

    @property
    def YPelsPerMeter(self) -> int: ...

    @property
    def bitCount(self) -> int: ...

    @property
    def clrImportant(self) -> int: ...

    @property
    def clrUsed(self) -> int: ...

    @property
    def colorMapLength(self) -> int: ...

    @property
    def compression(self) -> int: ...

    @property
    def height(self) -> int: ...

    @property
    def imageDataSize(self) -> int: ...

    @property
    def maskLength(self) -> int: ...

    @property
    def planes(self) -> int: ...

    @property
    def rawSizeImage(self) -> int: ...

    @property
    def size(self) -> int: ...

    @property
    def width(self) -> int: ...
