from typing import List
import ghidra.app.util.bin.format.pe.debug
import java.lang


class DebugFixup(object):
    """
    A possible implementation of the FIXUP debug directory.
     It may be inaccurate and/or incomplete.
    """





    def __init__(self):
        """
        DO NOT USE THIS CONSTRUCTOR, USE create*(GenericFactory ...) FACTORY METHODS INSTEAD.
        """
        ...



    def equals(self, __a0: object) -> bool: ...

    def getClass(self) -> java.lang.Class: ...

    def getDebugFixupElements(self) -> List[ghidra.app.util.bin.format.pe.debug.DebugFixupElement]:
        """
        Returns the array of FIXUP elements associated with this fixup debug directory.
        @return the array of FIXUP elements associated with this fixup debug directory
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
    def debugFixupElements(self) -> List[ghidra.app.util.bin.format.pe.debug.DebugFixupElement]: ...
