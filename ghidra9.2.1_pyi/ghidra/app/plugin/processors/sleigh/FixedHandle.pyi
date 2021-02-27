import ghidra.program.model.pcode
import java.lang


class FixedHandle(object):
    """
    The resulting data for a HandleTemplate after all the
     placeholders have been resolved through context
    """

    fixable: bool
    offset_offset: long
    offset_size: int
    offset_space: ghidra.program.model.address.AddressSpace
    size: int
    space: ghidra.program.model.address.AddressSpace
    temp_offset: long
    temp_space: ghidra.program.model.address.AddressSpace



    def __init__(self): ...



    def equals(self, obj: object) -> bool: ...

    def getClass(self) -> java.lang.Class: ...

    def getDynamicOffset(self) -> ghidra.program.model.pcode.Varnode: ...

    def getDynamicTemp(self) -> ghidra.program.model.pcode.Varnode: ...

    def getStaticVarnode(self) -> ghidra.program.model.pcode.Varnode: ...

    def hashCode(self) -> int: ...

    def isDynamic(self) -> bool: ...

    def isInvalid(self) -> bool: ...

    def notify(self) -> None: ...

    def notifyAll(self) -> None: ...

    def setInvalid(self) -> None: ...

    def toString(self) -> unicode: ...

    @overload
    def wait(self) -> None: ...

    @overload
    def wait(self, __a0: long) -> None: ...

    @overload
    def wait(self, __a0: long, __a1: int) -> None: ...

    @property
    def dynamic(self) -> bool: ...

    @property
    def dynamicOffset(self) -> ghidra.program.model.pcode.Varnode: ...

    @property
    def dynamicTemp(self) -> ghidra.program.model.pcode.Varnode: ...

    @property
    def invalid(self) -> bool: ...

    @property
    def staticVarnode(self) -> ghidra.program.model.pcode.Varnode: ...
