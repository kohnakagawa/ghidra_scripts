import ghidra.feature.fid.db
import ghidra.feature.fid.hash
import java.lang


class FidDBUtils(object):




    def __init__(self): ...



    def equals(self, __a0: object) -> bool: ...

    @overload
    @staticmethod
    def generateInferiorFullHashSmash(__a0: ghidra.feature.fid.db.FunctionRecord, __a1: ghidra.feature.fid.db.FunctionRecord) -> long: ...

    @overload
    @staticmethod
    def generateInferiorFullHashSmash(__a0: ghidra.feature.fid.hash.FidHashQuad, __a1: ghidra.feature.fid.db.FunctionRecord) -> long: ...

    @overload
    @staticmethod
    def generateSuperiorFullHashSmash(__a0: ghidra.feature.fid.db.FunctionRecord, __a1: ghidra.feature.fid.db.FunctionRecord) -> long: ...

    @overload
    @staticmethod
    def generateSuperiorFullHashSmash(__a0: ghidra.feature.fid.db.FunctionRecord, __a1: ghidra.feature.fid.hash.FidHashQuad) -> long: ...

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
