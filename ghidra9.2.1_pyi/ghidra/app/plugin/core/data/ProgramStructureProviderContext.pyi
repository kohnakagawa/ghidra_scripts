from typing import List
import ghidra.program.model.data
import ghidra.program.model.lang
import java.lang


class ProgramStructureProviderContext(object, ghidra.program.model.lang.DataTypeProviderContext):




    @overload
    def __init__(self, program: ghidra.program.model.listing.Program, loc: ghidra.program.util.ProgramLocation): ...

    @overload
    def __init__(self, program: ghidra.program.model.listing.Program, addr: ghidra.program.model.address.Address, struct: ghidra.program.model.data.Structure, myOffset: int): ...



    def equals(self, __a0: object) -> bool: ...

    def getClass(self) -> java.lang.Class: ...

    def getDataTypeComponent(self, offset: int) -> ghidra.program.model.data.DataTypeComponent: ...

    def getDataTypeComponents(self, start: int, end: int) -> List[ghidra.program.model.data.DataTypeComponent]:
        """
        Get an array of CodePrototypes that begin at or after start up to end.
           Prototypes that exist before start are not returned
           Prototypes that exist before end, but terminate after end ARE returned
           The prototypes must be contiguous from start to end
        @param start start offset
        @param end end offset
        @return array of CodePrototypes that exist between start and end.
        """
        ...

    def getUniqueName(self, baseName: unicode) -> unicode: ...

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
