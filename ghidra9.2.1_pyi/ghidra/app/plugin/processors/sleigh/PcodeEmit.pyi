import ghidra.app.plugin.processors.sleigh
import ghidra.app.plugin.processors.sleigh.template
import ghidra.program.model.address
import java.lang


class PcodeEmit(object):
    """
    Class for converting ConstructTpl into a pcode ops given
     a particular InstructionContext
    """





    def __init__(self, walk: ghidra.app.plugin.processors.sleigh.ParserWalker, ictx: ghidra.program.model.lang.InstructionContext, fallOffset: int, override: ghidra.program.model.pcode.PcodeOverride, uniqueFactory: ghidra.program.model.address.UniqueAddressFactory):
        """
        Pcode emitter constructor
        @param walk is the ParserWalker state for the tree that needs to be walked to generate pcode
        @param ictx is the InstructionContext interface to resolve requests for context
        @param fallOffset default instruction fall offset (i.e., instruction length including delay slotted instructions)
        @param override required if pcode overrides are to be utilized
        @param uniqueFactory required when override specified or if overlay normalization is required
        """
        ...



    def build(self, construct: ghidra.app.plugin.processors.sleigh.template.ConstructTpl, secnum: int) -> None: ...

    def equals(self, __a0: object) -> bool: ...

    def getClass(self) -> java.lang.Class: ...

    def getFallOffset(self) -> int: ...

    def getStartAddress(self) -> ghidra.program.model.address.Address: ...

    def getWalker(self) -> ghidra.app.plugin.processors.sleigh.ParserWalker: ...

    def hashCode(self) -> int: ...

    def notify(self) -> None: ...

    def notifyAll(self) -> None: ...

    def resolveRelatives(self) -> None:
        """
        Now that we have seen all label templates and references
         convert the collected references into full relative
         addresses
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
    def fallOffset(self) -> int: ...

    @property
    def startAddress(self) -> ghidra.program.model.address.Address: ...

    @property
    def walker(self) -> ghidra.app.plugin.processors.sleigh.ParserWalker: ...
