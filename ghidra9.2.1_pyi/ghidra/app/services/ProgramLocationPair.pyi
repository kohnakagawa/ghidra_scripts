import ghidra.program.model.listing
import ghidra.program.util
import java.lang


class ProgramLocationPair(object):
    """
    A simple object that contains a ProgramLocation and its associated Program
    """





    def __init__(self, program: ghidra.program.model.listing.Program, location: ghidra.program.util.ProgramLocation): ...



    def equals(self, __a0: object) -> bool: ...

    def getClass(self) -> java.lang.Class: ...

    def getProgram(self) -> ghidra.program.model.listing.Program: ...

    def getProgramLocation(self) -> ghidra.program.util.ProgramLocation: ...

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
    def program(self) -> ghidra.program.model.listing.Program: ...

    @property
    def programLocation(self) -> ghidra.program.util.ProgramLocation: ...
