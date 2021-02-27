from typing import List
import ghidra.app.util.pcodeInject
import ghidra.javaclass.format.constantpool
import java.lang


class InvokeMethods(object):








    def equals(self, __a0: object) -> bool: ...

    def getClass(self) -> java.lang.Class: ...

    @staticmethod
    def getPcodeForInvoke(__a0: ghidra.app.util.pcodeInject.PcodeOpEmitter, __a1: int, __a2: List[ghidra.javaclass.format.constantpool.AbstractConstantPoolInfoJava], __a3: ghidra.app.util.pcodeInject.JavaInvocationType) -> None: ...

    @staticmethod
    def getPcodeForInvokeDynamic(__a0: ghidra.app.util.pcodeInject.PcodeOpEmitter, __a1: int, __a2: List[ghidra.javaclass.format.constantpool.AbstractConstantPoolInfoJava]) -> None: ...

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
