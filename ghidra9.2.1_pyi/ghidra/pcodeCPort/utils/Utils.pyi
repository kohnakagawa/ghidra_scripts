from typing import List
import ghidra.pcodeCPort.utils
import ghidra.sleigh.grammar
import java.lang


class Utils(object):
    endl: unicode = u'\n'



    def __init__(self): ...



    @staticmethod
    def ashiftRight(__a0: long, __a1: long) -> long: ...

    @staticmethod
    def byte_swap(__a0: long, __a1: int) -> long: ...

    @staticmethod
    def bytesToInt(__a0: List[int], __a1: bool) -> int: ...

    @staticmethod
    def bytesToLong(__a0: List[int]) -> long: ...

    @staticmethod
    def calc_mask(__a0: int) -> long: ...

    @staticmethod
    def calc_maskword(__a0: ghidra.sleigh.grammar.Location, __a1: int, __a2: int, __a3: ghidra.pcodeCPort.utils.MutableInt, __a4: ghidra.pcodeCPort.utils.MutableInt, __a5: ghidra.pcodeCPort.utils.MutableInt) -> None: ...

    @staticmethod
    def coveringmask(__a0: long) -> long: ...

    def equals(self, __a0: object) -> bool: ...

    def getClass(self) -> java.lang.Class: ...

    def hashCode(self) -> int: ...

    @staticmethod
    def isascii(__a0: int) -> bool: ...

    @staticmethod
    def isprint(__a0: int) -> bool: ...

    @staticmethod
    def leastsigbit_set(__a0: long) -> int: ...

    @staticmethod
    def lshiftRight(__a0: long, __a1: long) -> long: ...

    @staticmethod
    def main(__a0: List[unicode]) -> None: ...

    @staticmethod
    def mostsigbit_set(__a0: long) -> int: ...

    def notify(self) -> None: ...

    def notifyAll(self) -> None: ...

    @staticmethod
    def paddedHexString(__a0: long, __a1: int) -> unicode: ...

    @staticmethod
    def pcode_left(__a0: long, __a1: int) -> long: ...

    @staticmethod
    def pcode_right(__a0: long, __a1: int) -> long: ...

    @staticmethod
    def shiftLeft(__a0: long, __a1: long) -> long: ...

    @staticmethod
    def sign_extend(__a0: long, __a1: int, __a2: int) -> long: ...

    @staticmethod
    def signbit_negative(__a0: long, __a1: int) -> bool: ...

    def toString(self) -> unicode: ...

    @staticmethod
    def toUnsignedIntHex(__a0: int) -> unicode: ...

    @staticmethod
    def uintb_negate(__a0: long, __a1: int) -> long: ...

    @overload
    @staticmethod
    def unsignedCompare(__a0: long, __a1: long) -> int: ...

    @overload
    @staticmethod
    def unsignedCompare(__a0: int, __a1: int) -> int: ...

    @staticmethod
    def unsignedDivide(__a0: int, __a1: int) -> int: ...

    @staticmethod
    def unsignedInt(__a0: int) -> long: ...

    @staticmethod
    def unsignedModulo(__a0: int, __a1: int) -> int: ...

    @overload
    def wait(self) -> None: ...

    @overload
    def wait(self, __a0: long) -> None: ...

    @overload
    def wait(self, __a0: long, __a1: int) -> None: ...

    @staticmethod
    def zzz_sign_extend(__a0: long, __a1: int) -> long: ...

    @staticmethod
    def zzz_zero_extend(__a0: long, __a1: int) -> long: ...
