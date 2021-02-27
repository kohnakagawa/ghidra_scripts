import ghidra.app.util.bin
import ghidra.app.util.bin.format.objectiveC
import ghidra.program.model.data
import java.lang


class ObjectiveC1_Protocol(object, ghidra.app.util.bin.StructConverter):
    ASCII: ghidra.program.model.data.DataType = char
    BYTE: ghidra.program.model.data.DataType = byte
    DWORD: ghidra.program.model.data.DataType = dword
    IBO32: ghidra.program.model.data.DataType = ImageBaseOffset32
    NAME: unicode = u'objc_protocol'
    POINTER: ghidra.program.model.data.DataType = pointer
    QWORD: ghidra.program.model.data.DataType = qword
    SIZEOF: int = 20
    STRING: ghidra.program.model.data.DataType = string
    UTF16: ghidra.program.model.data.DataType = unicode
    UTF8: ghidra.program.model.data.DataType = string-utf8
    VOID: ghidra.program.model.data.DataType = void
    WORD: ghidra.program.model.data.DataType = word



    def __init__(self, state: ghidra.app.util.bin.format.objectiveC.ObjectiveC1_State, reader: ghidra.app.util.bin.BinaryReader): ...



    def applyTo(self) -> None: ...

    def equals(self, __a0: object) -> bool: ...

    def getClass(self) -> java.lang.Class: ...

    def getClassMethods(self) -> ghidra.app.util.bin.format.objectiveC.ObjectiveC1_ProtocolMethodList: ...

    def getInstanceMethods(self) -> ghidra.app.util.bin.format.objectiveC.ObjectiveC1_ProtocolMethodList: ...

    def getIsa(self) -> int: ...

    def getName(self) -> unicode: ...

    def getProtocolList(self) -> ghidra.app.util.bin.format.objectiveC.ObjectiveC1_ProtocolList: ...

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
    def classMethods(self) -> ghidra.app.util.bin.format.objectiveC.ObjectiveC1_ProtocolMethodList: ...

    @property
    def instanceMethods(self) -> ghidra.app.util.bin.format.objectiveC.ObjectiveC1_ProtocolMethodList: ...

    @property
    def isa(self) -> int: ...

    @property
    def name(self) -> unicode: ...

    @property
    def protocolList(self) -> ghidra.app.util.bin.format.objectiveC.ObjectiveC1_ProtocolList: ...
