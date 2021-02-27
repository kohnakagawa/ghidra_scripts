from typing import List
import ghidra.app.util.pcodeInject
import ghidra.javaclass.format.constantpool
import java.lang


class ReferenceMethods(object):








    def equals(self, __a0: object) -> bool: ...

    def getClass(self) -> java.lang.Class: ...

    @staticmethod
    def getPcodeForGetField(__a0: ghidra.app.util.pcodeInject.PcodeOpEmitter, __a1: int, __a2: List[ghidra.javaclass.format.constantpool.AbstractConstantPoolInfoJava]) -> None: ...

    @staticmethod
    def getPcodeForGetStatic(__a0: ghidra.app.util.pcodeInject.PcodeOpEmitter, __a1: int, __a2: List[ghidra.javaclass.format.constantpool.AbstractConstantPoolInfoJava]) -> None: ...

    @staticmethod
    def getPcodeForPutField(__a0: ghidra.app.util.pcodeInject.PcodeOpEmitter, __a1: int, __a2: List[ghidra.javaclass.format.constantpool.AbstractConstantPoolInfoJava]) -> None: ...

    @staticmethod
    def getPcodeForPutStatic(__a0: ghidra.app.util.pcodeInject.PcodeOpEmitter, __a1: int, __a2: List[ghidra.javaclass.format.constantpool.AbstractConstantPoolInfoJava]) -> None: ...

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
