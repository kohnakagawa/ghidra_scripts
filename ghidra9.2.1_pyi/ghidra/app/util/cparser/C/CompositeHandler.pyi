import ghidra.app.util.cparser.C
import ghidra.program.model.data
import java.lang


class CompositeHandler(object):
    """
    Used by the CParser to handle fields added to structures(composites).
     Currently only bitfields are handled specially.

     NOTE: when bitfield handling is added directly to structures, this class may
     no longer be necessary.
    """





    def __init__(self, parent: ghidra.program.model.data.Composite): ...



    def add(self, dec: ghidra.app.util.cparser.C.Declaration) -> None: ...

    def equals(self, __a0: object) -> bool: ...

    def getClass(self) -> java.lang.Class: ...

    def getComposite(self) -> ghidra.program.model.data.Composite: ...

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
    def composite(self) -> ghidra.program.model.data.Composite: ...
