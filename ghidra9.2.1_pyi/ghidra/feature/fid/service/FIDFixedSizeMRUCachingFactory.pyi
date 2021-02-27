import generic.cache
import ghidra.feature.fid.hash
import ghidra.program.model.listing
import java.lang


class FIDFixedSizeMRUCachingFactory(object, generic.cache.Factory):




    def __init__(self, __a0: generic.cache.Factory, __a1: int): ...



    def equals(self, __a0: object) -> bool: ...

    @overload
    def get(self, __a0: ghidra.program.model.listing.Function) -> ghidra.feature.fid.hash.FidHashQuad: ...

    @overload
    def get(self, __a0: object) -> object: ...

    def getClass(self) -> java.lang.Class: ...

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
