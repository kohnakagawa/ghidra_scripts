import java.lang


class OMFDirEntry(object):
    """

     typedef struct OMFDirEntry {
         unsigned short  SubSection;     // subsection type (sst...)
         unsigned short  iMod;           // module index
         long            lfo;            // large file offset of subsection
         unsigned long   cb;             // number of bytes in subsection
     };

    """





    def __init__(self):
        """
        DO NOT USE THIS CONSTRUCTOR, USE create*(GenericFactory ...) FACTORY METHODS INSTEAD.
        """
        ...



    def equals(self, __a0: object) -> bool: ...

    def getClass(self) -> java.lang.Class: ...

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
