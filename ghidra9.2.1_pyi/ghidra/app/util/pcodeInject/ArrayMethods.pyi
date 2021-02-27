from typing import List
import ghidra.app.util.pcodeInject
import ghidra.javaclass.format.constantpool
import ghidra.program.model.data
import java.lang


class ArrayMethods(object):








    def equals(self, __a0: object) -> bool: ...

    @staticmethod
    def getArrayBaseType(__a0: int, __a1: ghidra.program.model.data.DataTypeManager) -> ghidra.program.model.data.DataType: ...

    def getClass(self) -> java.lang.Class: ...

    @staticmethod
    def getPcodeForMultiANewArray(__a0: ghidra.app.util.pcodeInject.PcodeOpEmitter, __a1: int, __a2: List[ghidra.javaclass.format.constantpool.AbstractConstantPoolInfoJava], __a3: int) -> None: ...

    @staticmethod
    def getPrimitiveArrayToken(__a0: int) -> unicode: ...

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
