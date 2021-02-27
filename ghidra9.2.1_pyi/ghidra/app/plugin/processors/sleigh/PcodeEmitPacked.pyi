import ghidra.app.plugin.processors.sleigh
import ghidra.app.plugin.processors.sleigh.template
import ghidra.program.model.address
import ghidra.program.model.lang
import java.lang


class PcodeEmitPacked(ghidra.app.plugin.processors.sleigh.PcodeEmit):
    addrsz_tag: int = 37
    end_tag: int = 96
    inst_tag: int = 33
    op_tag: int = 34
    spaceid_tag: int = 36
    unimpl_tag: int = 32
    void_tag: int = 35




    class LabelRef(object):
        labelIndex: int
        labelSize: int
        opIndex: int
        streampos: int



        def __init__(self, __a0: ghidra.app.plugin.processors.sleigh.PcodeEmitPacked, __a1: int, __a2: int, __a3: int, __a4: int): ...



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



    @overload
    def __init__(self):
        """
        Pcode emitter constructor for producing a packed binary representation
         for unimplemented or empty responses.
        """
        ...

    @overload
    def __init__(self, walk: ghidra.app.plugin.processors.sleigh.ParserWalker, ictx: ghidra.program.model.lang.InstructionContext, fallOffset: int, override: ghidra.program.model.pcode.PcodeOverride, uniqueFactory: ghidra.program.model.address.UniqueAddressFactory):
        """
        Pcode emitter constructor for producing a packed binary representation.
        @param walk parser walker
        @param ictx instruction contexts
        @param fallOffset default instruction fall offset (i.e., instruction length including delay slotted instructions)
        @param override required if pcode overrides are to be utilized
        @param uniqueFactory required when override specified or if overlay normalization is required
        """
        ...



    def build(self, construct: ghidra.app.plugin.processors.sleigh.template.ConstructTpl, secnum: int) -> None: ...

    def dumpOffset(self, val: long) -> None:
        """
        Encode and dump an integer value to the packed byte stream
        @param val is the integer to write
        """
        ...

    def equals(self, __a0: object) -> bool: ...

    def getClass(self) -> java.lang.Class: ...

    def getFallOffset(self) -> int: ...

    def getPackedBytes(self) -> ghidra.program.model.lang.PackedBytes: ...

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

    def write(self, val: int) -> None: ...

    @property
    def packedBytes(self) -> ghidra.program.model.lang.PackedBytes: ...
