import java.lang


class ConstantPoolTagsJava(object):
    CONSTANT_Class: int = 7
    CONSTANT_Double: int = 6
    CONSTANT_Dynamic: int = 17
    CONSTANT_Fieldref: int = 9
    CONSTANT_Float: int = 4
    CONSTANT_Integer: int = 3
    CONSTANT_InterfaceMethodref: int = 11
    CONSTANT_InvokeDynamic: int = 18
    CONSTANT_Long: int = 5
    CONSTANT_MethodHandle: int = 15
    CONSTANT_MethodType: int = 16
    CONSTANT_Methodref: int = 10
    CONSTANT_Module: int = 19
    CONSTANT_NameAndType: int = 12
    CONSTANT_Package: int = 20
    CONSTANT_String: int = 8
    CONSTANT_Utf8: int = 1



    def __init__(self): ...



    def equals(self, __a0: object) -> bool: ...

    def getClass(self) -> java.lang.Class: ...

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
