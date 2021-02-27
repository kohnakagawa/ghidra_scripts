import ghidra.app.plugin.processors.sleigh
import ghidra.program.model.address
import ghidra.xml
import java.lang


class ConstTpl(object):
    """
    A placeholder for what will resolve to a field of a Varnode
     (an AddressSpace or integer offset or integer size)
     given a particular InstructionContext
    """

    HANDLE: int = 1
    J_CURSPACE: int = 4
    J_CURSPACE_SIZE: int = 5
    J_FLOWDEST: int = 10
    J_FLOWDEST_SIZE: int = 11
    J_FLOWREF: int = 8
    J_FLOWREF_SIZE: int = 9
    J_NEXT: int = 3
    J_RELATIVE: int = 7
    J_START: int = 2
    REAL: int = 0
    SPACEID: int = 6
    V_OFFSET: int = 1
    V_OFFSET_PLUS: int = 3
    V_SIZE: int = 2
    V_SPACE: int = 0
    calc_mask: List[long] = array('l', [0L, 255L, 65535L, 16777215L, 4294967295L, 1099511627775L, 281474976710655L, 72057594037927935L, -1L])



    @overload
    def __init__(self, tp: int): ...

    @overload
    def __init__(self, op2: ghidra.app.plugin.processors.sleigh.template.ConstTpl): ...

    @overload
    def __init__(self, spc: ghidra.program.model.address.AddressSpace): ...

    @overload
    def __init__(self, tp: int, val: long): ...

    @overload
    def __init__(self, tp: int, ht: int, vf: int): ...



    def equals(self, __a0: object) -> bool: ...

    def fillinOffset(self, hand: ghidra.app.plugin.processors.sleigh.FixedHandle, walker: ghidra.app.plugin.processors.sleigh.ParserWalker) -> None:
        """
        Fillin the offset portion of a FixedHandle based on this
         const. If the offset value is dynamic, fill in the handle
         appropriately.  We don't just fill in the temporary
         variable offset, like "fix". Assume that hand.space is
         already filled in
        @param hand handle to fillin
        @param walker current parser walker
        """
        ...

    def fillinSpace(self, hand: ghidra.app.plugin.processors.sleigh.FixedHandle, walker: ghidra.app.plugin.processors.sleigh.ParserWalker) -> None:
        """
        Fill in the space portion of a FixedHandle, based
         on this const.
        @param hand handle to fillin
        @param walker current parser walker
        """
        ...

    def fix(self, walker: ghidra.app.plugin.processors.sleigh.ParserWalker) -> long: ...

    def fixSpace(self, walker: ghidra.app.plugin.processors.sleigh.ParserWalker) -> ghidra.program.model.address.AddressSpace: ...

    def getClass(self) -> java.lang.Class: ...

    def getHandleIndex(self) -> int: ...

    def getReal(self) -> long: ...

    def getSpaceId(self) -> ghidra.program.model.address.AddressSpace: ...

    def getType(self) -> int: ...

    def hashCode(self) -> int: ...

    def isConstSpace(self) -> bool: ...

    def isUniqueSpace(self) -> bool: ...

    def notify(self) -> None: ...

    def notifyAll(self) -> None: ...

    def restoreXml(self, parser: ghidra.xml.XmlPullParser, factory: ghidra.program.model.address.AddressFactory) -> None: ...

    def toString(self) -> unicode: ...

    @overload
    def wait(self) -> None: ...

    @overload
    def wait(self, __a0: long) -> None: ...

    @overload
    def wait(self, __a0: long, __a1: int) -> None: ...

    @property
    def constSpace(self) -> bool: ...

    @property
    def handleIndex(self) -> int: ...

    @property
    def real(self) -> long: ...

    @property
    def spaceId(self) -> ghidra.program.model.address.AddressSpace: ...

    @property
    def type(self) -> int: ...

    @property
    def uniqueSpace(self) -> bool: ...
