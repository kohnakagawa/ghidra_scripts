from typing import List
import ghidra.util.task
import java.lang
import java.util


class Algorithms(object):
    """
    Algorithms is a class containing static methods that implement
     general algorithms based on objects returned from a data model.
    """





    def __init__(self): ...



    @staticmethod
    def binarySearchWithDuplicates(__a0: List[object], __a1: object, __a2: java.util.Comparator) -> int: ...

    @staticmethod
    def bubbleSort(data: List[object], low: int, high: int, comparator: java.util.Comparator) -> None: ...

    def equals(self, __a0: object) -> bool: ...

    def getClass(self) -> java.lang.Class: ...

    def hashCode(self) -> int: ...

    @staticmethod
    def mergeSort(data: List[object], c: java.util.Comparator, monitor: ghidra.util.task.TaskMonitor) -> None: ...

    def notify(self) -> None: ...

    def notifyAll(self) -> None: ...

    def toString(self) -> unicode: ...

    @overload
    def wait(self) -> None: ...

    @overload
    def wait(self, __a0: long) -> None: ...

    @overload
    def wait(self, __a0: long, __a1: int) -> None: ...
