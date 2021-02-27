from typing import List
import ghidra.program.model.address
import ghidra.program.model.listing
import ghidra.util.task
import java.lang


class MatchData(object):








    def equals(self, __a0: object) -> bool: ...

    def getClass(self) -> java.lang.Class: ...

    def hashCode(self) -> int: ...

    @staticmethod
    def matchData(__a0: ghidra.program.model.listing.Program, __a1: ghidra.program.model.address.AddressSetView, __a2: ghidra.program.model.listing.Program, __a3: ghidra.program.model.address.AddressSetView, __a4: int, __a5: int, __a6: int, __a7: bool, __a8: bool, __a9: bool, __a10: ghidra.util.task.TaskMonitor) -> List[object]: ...

    def notify(self) -> None: ...

    def notifyAll(self) -> None: ...

    def toString(self) -> unicode: ...

    @overload
    def wait(self) -> None: ...

    @overload
    def wait(self, __a0: long) -> None: ...

    @overload
    def wait(self, __a0: long, __a1: int) -> None: ...
