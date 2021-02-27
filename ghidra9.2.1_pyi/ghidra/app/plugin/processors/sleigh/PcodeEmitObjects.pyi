from typing import List
import ghidra.app.plugin.processors.sleigh
import ghidra.app.plugin.processors.sleigh.template
import ghidra.program.model.address
import ghidra.program.model.pcode
import java.lang


class PcodeEmitObjects(ghidra.app.plugin.processors.sleigh.PcodeEmit):




    @overload
    def __init__(self, walk: ghidra.app.plugin.processors.sleigh.ParserWalker):
        """
        Pcode emitter constructor for producing PcodeOp objects for unimplemented, snippets or empty responses
         when {@link #getFallOffset()} will not be used.
        @param walk state of the ParserContext from which to generate p-code
        """
        ...

    @overload
    def __init__(self, walk: ghidra.app.plugin.processors.sleigh.ParserWalker, fallOffset: int):
        """
        Pcode emitter constructor for producing PcodeOp objects for unimplemented, snippets or empty responses.
        @param walk state of the ParserContext from which to generate p-code
        @param fallOffset default fall-through offset (i.e., the full length
         of instruction including delay-sloted instructions)
        """
        ...

    @overload
    def __init__(self, walk: ghidra.app.plugin.processors.sleigh.ParserWalker, ictx: ghidra.program.model.lang.InstructionContext, fallOffset: int, override: ghidra.program.model.pcode.PcodeOverride, uniqueFactory: ghidra.program.model.address.UniqueAddressFactory):
        """
        @param walk state of the ParserContext from which to generate p-code
        @param ictx is the InstructionContext used to resolve delayslot and crossbuild directives
        @param fallOffset default instruction fall offset (i.e., instruction length including delay slotted instructions)
        @param override required if pcode overrides are to be utilized
        @param uniqueFactory required when override specified or if overlay normalization is required
        """
        ...



    def build(self, construct: ghidra.app.plugin.processors.sleigh.template.ConstructTpl, secnum: int) -> None: ...

    def equals(self, __a0: object) -> bool: ...

    def getClass(self) -> java.lang.Class: ...

    def getFallOffset(self) -> int: ...

    def getPcodeOp(self) -> List[ghidra.program.model.pcode.PcodeOp]: ...

    def getStartAddress(self) -> ghidra.program.model.address.Address: ...

    def getWalker(self) -> ghidra.app.plugin.processors.sleigh.ParserWalker: ...

    def hashCode(self) -> int: ...

    def notify(self) -> None: ...

    def notifyAll(self) -> None: ...

    def resolveRelatives(self) -> None: ...

    def toString(self) -> unicode: ...

    @overload
    def wait(self) -> None: ...

    @overload
    def wait(self, __a0: long) -> None: ...

    @overload
    def wait(self, __a0: long, __a1: int) -> None: ...

    @property
    def pcodeOp(self) -> List[ghidra.program.model.pcode.PcodeOp]: ...
