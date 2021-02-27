from typing import List
import ghidra.program.model.lang.ConstantPool
import ghidra.program.model.pcode
import java.lang


class ConstantPool(object):
    """
    Class for manipulating "deferred" constant systems like the java virtual machine constant pool
    """

    ARRAY_LENGTH: int = 5
    CHECK_CAST: int = 7
    CLASS_REFERENCE: int = 2
    INSTANCE_OF: int = 6
    POINTER_FIELD: int = 4
    POINTER_METHOD: int = 3
    PRIMITIVE: int = 0
    STRING_LITERAL: int = 1




    class Record(object):
        byteData: List[int]
        isConstructor: bool
        tag: int
        token: unicode
        type: ghidra.program.model.data.DataType
        value: long



        def __init__(self): ...



        def build(self, __a0: long, __a1: ghidra.program.model.pcode.PcodeDataTypeManager) -> java.lang.StringBuilder: ...

        def equals(self, __a0: object) -> bool: ...

        def getClass(self) -> java.lang.Class: ...

        def hashCode(self) -> int: ...

        def notify(self) -> None: ...

        def notifyAll(self) -> None: ...

        def setUTF8Data(self, __a0: unicode) -> None: ...

        def toString(self) -> unicode: ...

        @overload
        def wait(self) -> None: ...

        @overload
        def wait(self, __a0: long) -> None: ...

        @overload
        def wait(self, __a0: long, __a1: int) -> None: ...

        @property
        def UTF8Data(self) -> None: ...  # No getter available.

        @UTF8Data.setter
        def UTF8Data(self, value: unicode) -> None: ...

    def __init__(self): ...



    def equals(self, __a0: object) -> bool: ...

    def getClass(self) -> java.lang.Class: ...

    def getRecord(self, ref: List[long]) -> ghidra.program.model.lang.ConstantPool.Record: ...

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
