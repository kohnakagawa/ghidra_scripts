from typing import List
import ghidra.app.util.bin.format.pe.debug
import java.lang


class OMFModule(object):
    """

     typedef struct OMFModule {
         unsigned short  ovlNumber;      // overlay number
         unsigned short  iLib;           // library that the module was linked from
         unsigned short  cSeg;           // count of number of segments in module
         char            Style[2];       // debugging style "CV"
         OMFSegDesc      SegInfo[1];     // describes segments in module
         char            Name[];         // length prefixed module name padded to long word boundary
     } OMFModule;

    """





    def __init__(self):
        """
        DO NOT USE THIS CONSTRUCTOR, USE create*(GenericFactory ...) FACTORY METHODS INSTEAD.
        """
        ...



    def equals(self, __a0: object) -> bool: ...

    def getClass(self) -> java.lang.Class: ...

    def getILib(self) -> int: ...

    def getName(self) -> unicode: ...

    def getOMFSegDescs(self) -> List[ghidra.app.util.bin.format.pe.debug.OMFSegDesc]:
        """
        Returns the OMF segment descriptions in this OMF module.
        @return the OMF segment descriptions in this OMF module
        """
        ...

    def getOvlNumber(self) -> int: ...

    def getStyle(self) -> int: ...

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
    def ILib(self) -> int: ...

    @property
    def OMFSegDescs(self) -> List[ghidra.app.util.bin.format.pe.debug.OMFSegDesc]: ...

    @property
    def name(self) -> unicode: ...

    @property
    def ovlNumber(self) -> int: ...

    @property
    def style(self) -> int: ...
