from typing import List
import ghidra.app.util.recognizer
import java.lang


class PpmdRecognizer(object, ghidra.app.util.recognizer.Recognizer):




    def __init__(self): ...



    def equals(self, __a0: object) -> bool: ...

    def getClass(self) -> java.lang.Class: ...

    def getPriority(self) -> int: ...

    def hashCode(self) -> int: ...

    def notify(self) -> None: ...

    def notifyAll(self) -> None: ...

    def numberOfBytesRequired(self) -> int: ...

    def recognize(self, __a0: List[int]) -> unicode: ...

    def toString(self) -> unicode: ...

    @overload
    def wait(self) -> None: ...

    @overload
    def wait(self, __a0: long) -> None: ...

    @overload
    def wait(self, __a0: long, __a1: int) -> None: ...

    @property
    def priority(self) -> int: ...
