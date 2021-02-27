from typing import List
import ghidra.app.util.pcodeInject
import ghidra.javaclass.format.constantpool
import ghidra.program.model.data
import java.lang


class DescriptorDecoder(object):
    BASE_TYPE_ANNOTATION: int = 64
    BASE_TYPE_ARRAY: int = 91
    BASE_TYPE_BOOLEAN: int = 90
    BASE_TYPE_BYTE: int = 66
    BASE_TYPE_CHAR: int = 67
    BASE_TYPE_CLASS: int = 99
    BASE_TYPE_DOUBLE: int = 68
    BASE_TYPE_ENUM: int = 101
    BASE_TYPE_FLOAT: int = 70
    BASE_TYPE_INT: int = 73
    BASE_TYPE_LONG: int = 74
    BASE_TYPE_REFERENCE: int = 76
    BASE_TYPE_SHORT: int = 83
    BASE_TYPE_STRING: int = 115
    BASE_TYPE_VOID: int = 86







    def equals(self, __a0: object) -> bool: ...

    def getClass(self) -> java.lang.Class: ...

    @staticmethod
    def getComputationalCategoryOfDescriptor(__a0: unicode) -> ghidra.app.util.pcodeInject.JavaComputationalCategory: ...

    @staticmethod
    def getDataTypeList(__a0: unicode, __a1: ghidra.program.model.data.DataTypeManager) -> List[object]: ...

    @staticmethod
    def getDataTypeOfDescriptor(__a0: unicode, __a1: ghidra.program.model.data.DataTypeManager) -> ghidra.program.model.data.DataType: ...

    @staticmethod
    def getDescriptorForInvoke(__a0: int, __a1: List[ghidra.javaclass.format.constantpool.AbstractConstantPoolInfoJava], __a2: ghidra.app.util.pcodeInject.JavaInvocationType) -> unicode: ...

    @staticmethod
    def getParameterCategories(__a0: unicode) -> List[object]: ...

    @staticmethod
    def getParameterString(__a0: unicode) -> unicode: ...

    @staticmethod
    def getPointerType(__a0: unicode, __a1: ghidra.program.model.data.DataTypeManager) -> ghidra.program.model.data.DataType: ...

    @staticmethod
    def getReferenceTypeOfDescriptor(__a0: unicode, __a1: ghidra.program.model.data.DataTypeManager, __a2: bool) -> ghidra.program.model.data.DataType: ...

    @staticmethod
    def getReturnCategoryOfMethodDescriptor(__a0: unicode) -> ghidra.app.util.pcodeInject.JavaComputationalCategory: ...

    @staticmethod
    def getReturnTypeOfMethodDescriptor(__a0: unicode, __a1: ghidra.program.model.data.DataTypeManager) -> ghidra.program.model.data.DataType: ...

    @staticmethod
    def getStackPurge(__a0: unicode) -> int: ...

    @staticmethod
    def getTypeNameFromDescriptor(__a0: unicode, __a1: bool, __a2: bool) -> unicode: ...

    @staticmethod
    def getTypeNameList(__a0: unicode, __a1: bool, __a2: bool) -> List[object]: ...

    def hashCode(self) -> int: ...

    def notify(self) -> None: ...

    def notifyAll(self) -> None: ...

    @staticmethod
    def resolveClassForString(__a0: unicode, __a1: ghidra.program.model.data.DataTypeManager, __a2: ghidra.program.model.data.DataType) -> ghidra.program.model.data.DataType: ...

    def toString(self) -> unicode: ...

    @overload
    def wait(self) -> None: ...

    @overload
    def wait(self, __a0: long) -> None: ...

    @overload
    def wait(self, __a0: long, __a1: int) -> None: ...
