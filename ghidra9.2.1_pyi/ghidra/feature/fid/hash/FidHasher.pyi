import ghidra.feature.fid.hash
import ghidra.program.model.listing
import java.lang


class FidHasher(object):








    def equals(self, __a0: object) -> bool: ...

    def getClass(self) -> java.lang.Class: ...

    def hash(self, __a0: ghidra.program.model.listing.Function) -> ghidra.feature.fid.hash.FidHashQuad: ...

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
