import ghidra.app.plugin.prototype.dataArchiveUtilities
import ghidra.program.model.data
import java.lang
import java.util


class ComplexName(object):




    def __init__(self, __a0: unicode): ...



    def equals(self, __a0: object) -> bool: ...

    def genUIData(self, __a0: ghidra.program.model.data.DataTypeManager, __a1: java.util.Hashtable, __a2: ghidra.app.plugin.prototype.dataArchiveUtilities.ComplexName, __a3: int) -> ghidra.program.model.data.DataType: ...

    def getCategoryPath(self) -> ghidra.program.model.data.CategoryPath: ...

    def getClass(self) -> java.lang.Class: ...

    @overload
    def getDataType(self, __a0: ghidra.program.model.data.FileDataTypeManager, __a1: java.util.Hashtable) -> ghidra.program.model.data.DataType: ...

    @overload
    def getDataType(self, __a0: ghidra.program.model.data.DataTypeManager, __a1: java.util.Hashtable, __a2: bool) -> ghidra.program.model.data.DataType: ...

    def getName(self) -> unicode: ...

    def getNamespace(self) -> unicode: ...

    def hashCode(self) -> int: ...

    def isArray(self) -> bool: ...

    def isPointer(self) -> bool: ...

    def notify(self) -> None: ...

    def notifyAll(self) -> None: ...

    def toString(self) -> unicode: ...

    def usesNamespace(self) -> bool: ...

    @overload
    def wait(self) -> None: ...

    @overload
    def wait(self, __a0: long) -> None: ...

    @overload
    def wait(self, __a0: long, __a1: int) -> None: ...

    @property
    def array(self) -> bool: ...

    @property
    def categoryPath(self) -> ghidra.program.model.data.CategoryPath: ...

    @property
    def name(self) -> unicode: ...

    @property
    def namespace(self) -> unicode: ...

    @property
    def pointer(self) -> bool: ...