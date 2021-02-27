from typing import List
import ghidra.app.util.html.diff
import java.lang


class DataTypeDiffBuilder(object):








    @staticmethod
    def diffBody(left: ghidra.app.util.html.diff.DataTypeDiffInput, right: ghidra.app.util.html.diff.DataTypeDiffInput) -> ghidra.app.util.html.diff.DataTypeDiff: ...

    @staticmethod
    def diffHeader(left: ghidra.app.util.html.diff.DataTypeDiffInput, right: ghidra.app.util.html.diff.DataTypeDiffInput) -> ghidra.app.util.html.diff.DataTypeDiff: ...

    @staticmethod
    def diffLines(left: ghidra.app.util.html.diff.DataTypeDiffInput, right: ghidra.app.util.html.diff.DataTypeDiffInput) -> ghidra.app.util.html.diff.DataTypeDiff: ...

    def equals(self, __a0: object) -> bool: ...

    def getClass(self) -> java.lang.Class: ...

    def hashCode(self) -> int: ...

    @staticmethod
    def highlightDifferences(__a0: List[object], __a1: List[object]) -> None: ...

    def notify(self) -> None: ...

    def notifyAll(self) -> None: ...

    @staticmethod
    def padLines(leftLines: ghidra.app.util.html.diff.DiffLines, rightLines: ghidra.app.util.html.diff.DiffLines) -> None: ...

    def toString(self) -> unicode: ...

    @overload
    def wait(self) -> None: ...

    @overload
    def wait(self, __a0: long) -> None: ...

    @overload
    def wait(self, __a0: long, __a1: int) -> None: ...
