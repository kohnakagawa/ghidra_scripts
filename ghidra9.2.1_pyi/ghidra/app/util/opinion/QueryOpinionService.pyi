from typing import List
import ghidra.app.util.opinion
import java.lang
import java.util


class QueryOpinionService(object):




    def __init__(self): ...



    def equals(self, __a0: object) -> bool: ...

    def getClass(self) -> java.lang.Class: ...

    @staticmethod
    def getQueryResultWithSecondaryMasking(secondaryKey: unicode, byPrimary: java.util.Map) -> java.util.Set: ...

    def hashCode(self) -> int: ...

    def notify(self) -> None: ...

    def notifyAll(self) -> None: ...

    @staticmethod
    def query(loaderName: unicode, primaryKey: unicode, secondaryKey: unicode) -> List[ghidra.app.util.opinion.QueryResult]: ...

    def toString(self) -> unicode: ...

    @overload
    def wait(self) -> None: ...

    @overload
    def wait(self, __a0: long) -> None: ...

    @overload
    def wait(self, __a0: long, __a1: int) -> None: ...
