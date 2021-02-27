from typing import List
import ghidra.program.model.lang
import ghidra.program.model.pcode
import java.lang


class VarnodeTranslator(object):




    @overload
    def __init__(self, lang: ghidra.program.model.lang.Language): ...

    @overload
    def __init__(self, program: ghidra.program.model.listing.Program): ...



    def equals(self, __a0: object) -> bool: ...

    def getClass(self) -> java.lang.Class: ...

    def getRegister(self, node: ghidra.program.model.pcode.Varnode) -> ghidra.program.model.lang.Register:
        """
        Translate the Varnode into a register if possible
        @param node varnode to translate
        @return Register or null if node is not a register
        """
        ...

    def getRegisters(self) -> List[ghidra.program.model.lang.Register]:
        """
        Get all defined registers for the program this translator was created
         with.
        @return all defined registers as unmodifiable list
        """
        ...

    def getVarnode(self, register: ghidra.program.model.lang.Register) -> ghidra.program.model.pcode.Varnode:
        """
        Get a varnode that maps to the given register
        @param register register to translate into a varnode
        @return varnode that reprents the register
        """
        ...

    def hashCode(self) -> int: ...

    def notify(self) -> None: ...

    def notifyAll(self) -> None: ...

    def supportsPcode(self) -> bool:
        """
        @return true if this program's language supports pcode
        """
        ...

    def toString(self) -> unicode: ...

    @overload
    def wait(self) -> None: ...

    @overload
    def wait(self, __a0: long) -> None: ...

    @overload
    def wait(self, __a0: long, __a1: int) -> None: ...

    @property
    def registers(self) -> List[object]: ...
