import ghidra.util.bytesearch
import ghidra.xml
import java.lang


class AlignRule(object, ghidra.util.bytesearch.PostRule):
    """
    ByteSearch post search rule when a pattern is found. Used when a pattern must have a certain
     alignment at an offset from the location the pattern matches.

     The pattern can be constructed or restored from XML of the form,
     where alignOffset=mark, alignmask=bits


    """





    @overload
    def __init__(self): ...

    @overload
    def __init__(self, alignOffset: int, alignmask: int):
        """
        ByteSearch post search rule when a pattern is found. Used when a pattern must have a certain
         alignment at an offset from the location the pattern matches. The alignment is
         specified by the alignmask bits that must be zero.

           Normally alignOffset is 0, since most patterns will match at the address that must be aligned
           To align a match, use the following

          align to  2 = alignmask 0x1 - lower bit must be zero
          align to  4 = alignmask 0x3 - lower two bits must be zero
          align to  8 = alignmask 0x7 - lower three bits must be zero
          align to 16 = alignmask 0xF - lower four bits must be zero
          ....
          Other strange alignments could be specified, but most likely the above suffice.
        @param alignOffset - bytes offset from pattern to check for alignment
        @param alignmask - the mask where a 1 bit must be zero
        """
        ...



    def apply(self, pat: ghidra.util.bytesearch.Pattern, matchoffset: long) -> bool: ...

    def equals(self, __a0: object) -> bool: ...

    def getAlignMask(self) -> int: ...

    def getClass(self) -> java.lang.Class: ...

    def hashCode(self) -> int: ...

    def notify(self) -> None: ...

    def notifyAll(self) -> None: ...

    def restoreXml(self, parser: ghidra.xml.XmlPullParser) -> None: ...

    def toString(self) -> unicode: ...

    @overload
    def wait(self) -> None: ...

    @overload
    def wait(self, __a0: long) -> None: ...

    @overload
    def wait(self, __a0: long, __a1: int) -> None: ...

    @property
    def alignMask(self) -> int: ...
