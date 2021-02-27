import java.lang


class AccessFlags(object):
    ACC_ABSTRACT: int = 1024
    ACC_ANNOTATION: int = 8192
    ACC_BRIDGE: int = 64
    ACC_CONSTRUCTOR: int = 65536
    ACC_DECLARED_SYNCHRONIZED: int = 131072
    ACC_ENUM: int = 16384
    ACC_FINAL: int = 16
    ACC_INTERFACE: int = 512
    ACC_NATIVE: int = 256
    ACC_PRIVATE: int = 2
    ACC_PROTECTED: int = 4
    ACC_PUBLIC: int = 1
    ACC_STATIC: int = 8
    ACC_STRICT: int = 2048
    ACC_SYNCHRONIZED: int = 32
    ACC_SYNTHETIC: int = 4096
    ACC_TRANSIENT: int = 128
    ACC_VARARGS: int = 128
    ACC_VOLATILE: int = 64



    def __init__(self): ...



    def equals(self, __a0: object) -> bool: ...

    def getClass(self) -> java.lang.Class: ...

    def hashCode(self) -> int: ...

    def notify(self) -> None: ...

    def notifyAll(self) -> None: ...

    @overload
    def toString(self) -> unicode: ...

    @overload
    @staticmethod
    def toString(__a0: int) -> unicode: ...

    @overload
    def wait(self) -> None: ...

    @overload
    def wait(self, __a0: long) -> None: ...

    @overload
    def wait(self, __a0: long, __a1: int) -> None: ...
