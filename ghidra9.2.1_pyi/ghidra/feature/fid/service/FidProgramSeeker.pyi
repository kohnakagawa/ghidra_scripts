from typing import List
import ghidra.feature.fid.service
import ghidra.program.model.listing
import ghidra.util.task
import java.lang
import java.util


class FidProgramSeeker(object):
    MAX_NUM_PARENTS_FOR_SCORE: int



    def __init__(self, __a0: ghidra.feature.fid.db.FidQueryService, __a1: ghidra.program.model.listing.Program, __a2: ghidra.feature.fid.hash.FidHasher, __a3: int, __a4: int, __a5: float): ...



    def equals(self, __a0: object) -> bool: ...

    @staticmethod
    def getChildren(__a0: ghidra.program.model.listing.Function, __a1: bool) -> java.util.ArrayList: ...

    def getClass(self) -> java.lang.Class: ...

    @staticmethod
    def getParents(__a0: ghidra.program.model.listing.Function, __a1: bool) -> java.util.ArrayList: ...

    def hashCode(self) -> int: ...

    def notify(self) -> None: ...

    def notifyAll(self) -> None: ...

    def search(self, __a0: ghidra.util.task.TaskMonitor) -> List[object]: ...

    def searchFunction(self, __a0: ghidra.program.model.listing.Function, __a1: ghidra.util.task.TaskMonitor) -> ghidra.feature.fid.service.FidSearchResult: ...

    def toString(self) -> unicode: ...

    @overload
    def wait(self) -> None: ...

    @overload
    def wait(self, __a0: long) -> None: ...

    @overload
    def wait(self, __a0: long, __a1: int) -> None: ...
