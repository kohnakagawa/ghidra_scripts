from typing import List
import ghidra.javaclass.format.constantpool
import ghidra.program.model.lang
import java.lang


class ConstantPoolJava(ghidra.program.model.lang.ConstantPool):
    CPOOL_ANEWARRAY: unicode = u'0'
    CPOOL_ARRAYLENGTH: unicode = u'17'
    CPOOL_CHECKCAST: unicode = u'1'
    CPOOL_GETFIELD: unicode = u'2'
    CPOOL_GETSTATIC: unicode = u'3'
    CPOOL_INSTANCEOF: unicode = u'6'
    CPOOL_INVOKEDYNAMIC: unicode = u'7'
    CPOOL_INVOKEINTERFACE: unicode = u'8'
    CPOOL_INVOKESPECIAL: unicode = u'9'
    CPOOL_INVOKESTATIC: unicode = u'10'
    CPOOL_INVOKEVIRTUAL: unicode = u'11'
    CPOOL_LDC: unicode = u'4'
    CPOOL_LDC2_W: unicode = u'5'
    CPOOL_MULTIANEWARRAY: unicode = u'12'
    CPOOL_NEW: unicode = u'13'
    CPOOL_NEWARRAY: unicode = u'14'
    CPOOL_OP: unicode = u'cpool'
    CPOOL_PUTFIELD: unicode = u'16'
    CPOOL_PUTSTATIC: unicode = u'15'



    def __init__(self, __a0: ghidra.program.model.listing.Program): ...



    def equals(self, __a0: object) -> bool: ...

    def getClass(self) -> java.lang.Class: ...

    def getConstantPool(self) -> List[ghidra.javaclass.format.constantpool.AbstractConstantPoolInfoJava]: ...

    def getRecord(self, __a0: List[long]) -> ghidra.program.model.lang.ConstantPool.Record: ...

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
    def constantPool(self) -> List[ghidra.javaclass.format.constantpool.AbstractConstantPoolInfoJava]: ...
