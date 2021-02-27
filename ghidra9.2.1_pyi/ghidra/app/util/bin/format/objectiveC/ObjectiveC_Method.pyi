import ghidra.app.util.bin
import ghidra.app.util.bin.format.objectiveC
import ghidra.program.model.data
import ghidra.program.model.symbol
import java.lang


class ObjectiveC_Method(object, ghidra.app.util.bin.StructConverter):
    ASCII: ghidra.program.model.data.DataType = char
    BYTE: ghidra.program.model.data.DataType = byte
    DWORD: ghidra.program.model.data.DataType = dword
    IBO32: ghidra.program.model.data.DataType = ImageBaseOffset32
    POINTER: ghidra.program.model.data.DataType = pointer
    QWORD: ghidra.program.model.data.DataType = qword
    STRING: ghidra.program.model.data.DataType = string
    UTF16: ghidra.program.model.data.DataType = unicode
    UTF8: ghidra.program.model.data.DataType = string-utf8
    VOID: ghidra.program.model.data.DataType = void
    WORD: ghidra.program.model.data.DataType = word







    def applyTo(self, namespace: ghidra.program.model.symbol.Namespace) -> None: ...

    def equals(self, __a0: object) -> bool: ...

    def getClass(self) -> java.lang.Class: ...

    def getImplementation(self) -> long: ...

    def getIndex(self) -> long: ...

    def getMethodType(self) -> ghidra.app.util.bin.format.objectiveC.ObjectiveC_MethodType: ...

    def getName(self) -> unicode: ...

    def getTypes(self) -> unicode: ...

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
    def implementation(self) -> long: ...

    @property
    def index(self) -> long: ...

    @property
    def methodType(self) -> ghidra.app.util.bin.format.objectiveC.ObjectiveC_MethodType: ...

    @property
    def name(self) -> unicode: ...

    @property
    def types(self) -> unicode: ...
