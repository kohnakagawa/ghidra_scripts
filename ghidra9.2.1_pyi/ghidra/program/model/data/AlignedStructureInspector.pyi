from typing import List
import ghidra.program.model.data
import ghidra.program.model.data.AlignedStructurePacker
import java.lang


class AlignedStructureInspector(ghidra.program.model.data.AlignedStructurePacker):
    """
    AlignedStructureInspector provides a simple instance of a structure
     member container used to perform alignment operations without forcing modification
     of the actual structure.  A wrapper is not used for the flexible array component
     which will not be modified by packer.
    """









    def equals(self, __a0: object) -> bool: ...

    def getClass(self) -> java.lang.Class: ...

    def hashCode(self) -> int: ...

    def notify(self) -> None: ...

    def notifyAll(self) -> None: ...

    @overload
    @staticmethod
    def packComponents(structure: ghidra.program.model.data.Structure) -> ghidra.program.model.data.AlignedStructurePacker.StructurePackResult:
        """
        Perform structure component packing in a read-only fashion primarily
         for the purpose of computing external alignment for existing structures.
        @param structure
        @return aligned packing result
        """
        ...

    @overload
    @staticmethod
    def packComponents(__a0: ghidra.program.model.data.Structure, __a1: List[object]) -> ghidra.program.model.data.AlignedStructurePacker.StructurePackResult: ...

    def toString(self) -> unicode: ...

    @overload
    def wait(self) -> None: ...

    @overload
    def wait(self, __a0: long) -> None: ...

    @overload
    def wait(self, __a0: long, __a1: int) -> None: ...
