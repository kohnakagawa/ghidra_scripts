import ghidra.util.datastruct
import java.lang
import java.util


class RedBlackEntry(object, java.util.Map.Entry):








    @overload
    @staticmethod
    def comparingByKey() -> java.util.Comparator: ...

    @overload
    @staticmethod
    def comparingByKey(__a0: java.util.Comparator) -> java.util.Comparator: ...

    @overload
    @staticmethod
    def comparingByValue() -> java.util.Comparator: ...

    @overload
    @staticmethod
    def comparingByValue(__a0: java.util.Comparator) -> java.util.Comparator: ...

    def equals(self, __a0: object) -> bool: ...

    def getClass(self) -> java.lang.Class: ...

    def getKey(self) -> K: ...

    def getPredecessor(self) -> ghidra.util.datastruct.RedBlackEntry: ...

    def getSuccessor(self) -> ghidra.util.datastruct.RedBlackEntry: ...

    def getValue(self) -> V: ...

    def hashCode(self) -> int: ...

    def isDisposed(self) -> bool: ...

    def notify(self) -> None: ...

    def notifyAll(self) -> None: ...

    def setValue(self, __a0: object) -> object: ...

    def toString(self) -> unicode: ...

    @overload
    def wait(self) -> None: ...

    @overload
    def wait(self, __a0: long) -> None: ...

    @overload
    def wait(self, __a0: long, __a1: int) -> None: ...

    @property
    def disposed(self) -> bool: ...

    @property
    def key(self) -> object: ...

    @property
    def predecessor(self) -> ghidra.util.datastruct.RedBlackEntry: ...

    @property
    def successor(self) -> ghidra.util.datastruct.RedBlackEntry: ...

    @property
    def value(self) -> object: ...

    @value.setter
    def value(self, value: object) -> None: ...
