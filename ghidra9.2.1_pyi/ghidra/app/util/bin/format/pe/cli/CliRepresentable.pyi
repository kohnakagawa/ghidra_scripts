import ghidra.app.util.bin.format.pe.cli.streams
import java.lang


class CliRepresentable(object):
    """
    Describes the methods necessary to get a long and short representation, with or without an metadata stream.
     This is used in the token analyzer to cut down on duplication across modules.
    """









    def equals(self, __a0: object) -> bool: ...

    def getClass(self) -> java.lang.Class: ...

    @overload
    def getRepresentation(self) -> unicode: ...

    @overload
    def getRepresentation(self, stream: ghidra.app.util.bin.format.pe.cli.streams.CliStreamMetadata) -> unicode: ...

    @overload
    def getShortRepresentation(self) -> unicode: ...

    @overload
    def getShortRepresentation(self, stream: ghidra.app.util.bin.format.pe.cli.streams.CliStreamMetadata) -> unicode: ...

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

    @property
    def representation(self) -> unicode: ...

    @property
    def shortRepresentation(self) -> unicode: ...
