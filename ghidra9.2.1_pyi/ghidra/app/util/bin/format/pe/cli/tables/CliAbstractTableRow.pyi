import ghidra.app.util.bin.format.pe.cli
import ghidra.app.util.bin.format.pe.cli.streams
import java.lang


class CliAbstractTableRow(object, ghidra.app.util.bin.format.pe.cli.CliRepresentable):
    """
    Generic Metadata table row.  Subclasses should provided implementations for the actual
     table rows.
    """





    def __init__(self): ...



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
