import ghidra.program.model.lang
import java.lang


class DWARFRegisterMappings(object):
    """
    Immutable mapping information between DWARF and Ghidra.

     Use DWARFRegisterMappingsManager to get an instance for a Program's specific
     language.

     The data held in this class is read from DWARF register mapping information contained
     in xml files referenced from the language *.ldefs file in an
     external_name tool="DWARF.register.mapping.file" name="register_mapping_filename_here"/

     The format is:

     dwarf
       register_mappings
           !-- Simple single mapping: --
           !-- NN == dwarf register number --
           !-- RegName == Ghidra register name string --
           !-- register_mapping dwarf="NN" ghidra="RegName" / --

           !-- Example: --
         register_mapping dwarf="0" ghidra="r0" /

           !-- Single mapping specifying stack pointer: --
           !-- NN == dwarf register number --
           !-- RegName == Ghidra register name string --
           !-- register_mapping dwarf="NN" ghidra="RegName" stackpointer="true"/ --

           !-- Example: --
         register_mapping dwarf="4" ghidra="ESP" stackpointer="true"/

           !-- Multiple mapping: --
           !-- NN == dwarf register number --
           !-- XX == number of times to repeat --
           !-- RegNameYY == Ghidra register name string with a mandatory integer suffix --
           !-- register_mapping dwarf="NN" ghidra="RegNameYY" auto_count="XX"/ --

           !-- Example, creates mapping from 0..12 to r0..r12: --
         register_mapping dwarf="0" ghidra="r0" auto_count="12"/

           !-- Example, creates mapping from 17..32 to XMM0..XMM15: --
         register_mapping dwarf="17" ghidra="XMM0" auto_count="16"/

       /register_mappings

         !-- Call Frame CFA Value: --
       call_frame_cfa value="NN"/

         !-- Use Formal Parameter Storage toggle: --
       use_formal_parameter_storage/
     /dwarf

    """

    DUMMY: ghidra.app.util.bin.format.dwarf4.next.DWARFRegisterMappings = DWARFRegisterMappings [dwarfRegisterMap={}, callFrameCFA=0, stackPointerIndex=-1, useFormalParameterStorage=false]



    def __init__(self, regmap: java.util.Map, callFrameCFA: long, stackPointerIndex: int, useFPS: bool): ...



    def equals(self, __a0: object) -> bool: ...

    def getCallFrameCFA(self) -> long: ...

    def getClass(self) -> java.lang.Class: ...

    def getDWARFStackPointerRegNum(self) -> int: ...

    def getGhidraReg(self, dwarfRegNum: int) -> ghidra.program.model.lang.Register: ...

    def hashCode(self) -> int: ...

    def isUseFormalParameterStorage(self) -> bool: ...

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
    def DWARFStackPointerRegNum(self) -> int: ...

    @property
    def callFrameCFA(self) -> long: ...

    @property
    def useFormalParameterStorage(self) -> bool: ...
