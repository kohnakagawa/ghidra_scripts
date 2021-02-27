from typing import List
import ghidra.program.model.data
import java.lang


class AlignedStructurePacker(object):
    """
    AlignedStructurePacker provides support for performing aligned packing
     of Structure components.

     NOTE: We currently have no way of conveying or supporting explicit bitfield component pragmas
     supported by some compilers (e.g., bit_field_size, bit_field_align, bit_packing).
    """






    class StructurePackResult(object):
        alignment: int
        componentsChanged: bool
        numComponents: int
        structureLength: int







        def equals(self, __a0: object) -> bool: ...

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







    def equals(self, __a0: object) -> bool: ...

    def getClass(self) -> java.lang.Class: ...

    def hashCode(self) -> int: ...

    def notify(self) -> None: ...

    def notifyAll(self) -> None: ...

    @staticmethod
    def packComponents(__a0: ghidra.program.model.data.Structure, __a1: List[object]) -> ghidra.program.model.data.AlignedStructurePacker.StructurePackResult: ...

    def toString(self) -> unicode: ...

    @overload
    def wait(self) -> None: ...

    @overload
    def wait(self, __a0: long) -> None: ...

    @overload
    def wait(self, __a0: long, __a1: int) -> None: ...
