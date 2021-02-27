import ghidra.javaclass.format.constantpool
import ghidra.program.model.data
import java.lang


class AbstractConstantPoolReferenceInfo(ghidra.javaclass.format.constantpool.AbstractConstantPoolInfoJava):








    def equals(self, __a0: object) -> bool: ...

    def getClass(self) -> java.lang.Class: ...

    def getClassIndex(self) -> int: ...

    def getNameAndTypeIndex(self) -> int: ...

    def getOffset(self) -> long: ...

    def getTag(self) -> int: ...

    def hashCode(self) -> int: ...

    def notify(self) -> None: ...

    def notifyAll(self) -> None: ...

    def toDataType(self) -> ghidra.program.model.data.DataType: ...

    def toString(self) -> unicode: ...

    @overload
    def wait(self) -> None: ...

    @overload
    def wait(self, __a0: long) -> None: ...

    @overload
    def wait(self, __a0: long, __a1: int) -> None: ...

    @property
    def classIndex(self) -> int: ...

    @property
    def nameAndTypeIndex(self) -> int: ...
