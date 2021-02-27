from typing import List
import ghidra.app.plugin.processors.sleigh
import ghidra.program.model.lang
import ghidra.program.model.lang.InjectPayload
import ghidra.program.model.listing
import ghidra.program.model.pcode
import java.lang


class InjectPayload(object):
    """
    InjectPayload encapsulates a semantic (p-code) override which can be injected
     into analyses that work with p-code (Decompiler, SymbolicPropagator)
     The payload typically replaces either a subroutine call or a userop
    """

    CALLFIXUP_TYPE: int = 1
    CALLMECHANISM_TYPE: int = 3
    CALLOTHERFIXUP_TYPE: int = 2
    EXECUTABLEPCODE_TYPE: int = 4




    class InjectParameter(object):




        def __init__(self, __a0: unicode, __a1: int): ...



        def equals(self, __a0: object) -> bool: ...

        def getClass(self) -> java.lang.Class: ...

        def getIndex(self) -> int: ...

        def getName(self) -> unicode: ...

        def getSize(self) -> int: ...

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
        def index(self) -> int: ...

        @property
        def name(self) -> unicode: ...

        @property
        def size(self) -> int: ...





    def equals(self, __a0: object) -> bool: ...

    def getClass(self) -> java.lang.Class: ...

    def getInput(self) -> List[ghidra.program.model.lang.InjectPayload.InjectParameter]:
        """
        @return array of any input parameters for this inject
        """
        ...

    def getName(self) -> unicode:
        """
        @return formal name for this injection
        """
        ...

    def getOutput(self) -> List[ghidra.program.model.lang.InjectPayload.InjectParameter]:
        """
        @return array of any output parameters for this inject
        """
        ...

    def getParamShift(self) -> int:
        """
        @return number of parameters from the original call which should be truncated
        """
        ...

    def getPcode(self, program: ghidra.program.model.listing.Program, con: ghidra.program.model.lang.InjectContext) -> List[ghidra.program.model.pcode.PcodeOp]:
        """
        A convenience function wrapping the inject method, to produce the final set
         of PcodeOp objects in an array
        @param program is the Program for which injection is happening
        @param con is the context for injection
        @return the array of PcodeOps
        """
        ...

    def getSource(self) -> unicode:
        """
        @return a String describing the source of this payload
        """
        ...

    def getType(self) -> int:
        """
        @return the type of this injection:  CALLFIXUP_TYPE, CALLMECHANISM_TYPE, etc.
        """
        ...

    def hashCode(self) -> int: ...

    def inject(self, context: ghidra.program.model.lang.InjectContext, emit: ghidra.app.plugin.processors.sleigh.PcodeEmit) -> None:
        """
        Given a context, send the p-code payload to the emitter
        @param context is the context for injection
        @param emit is the object accumulating the final p-code
        """
        ...

    def isFallThru(self) -> bool:
        """
        @return true if the injected p-code falls thru
        """
        ...

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
    def fallThru(self) -> bool: ...

    @property
    def input(self) -> List[ghidra.program.model.lang.InjectPayload.InjectParameter]: ...

    @property
    def name(self) -> unicode: ...

    @property
    def output(self) -> List[ghidra.program.model.lang.InjectPayload.InjectParameter]: ...

    @property
    def paramShift(self) -> int: ...

    @property
    def source(self) -> unicode: ...

    @property
    def type(self) -> int: ...
