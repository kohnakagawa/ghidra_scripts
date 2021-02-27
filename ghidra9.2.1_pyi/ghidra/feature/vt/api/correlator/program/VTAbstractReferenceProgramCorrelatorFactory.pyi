import ghidra.feature.vt.api.main
import ghidra.feature.vt.api.util
import ghidra.framework.plugintool
import ghidra.program.model.address
import ghidra.program.model.listing
import java.lang


class VTAbstractReferenceProgramCorrelatorFactory(ghidra.feature.vt.api.util.VTAbstractProgramCorrelatorFactory):
    CONFIDENCE_THRESHOLD: unicode = u'Confidence threshold (info content)'
    CONFIDENCE_THRESHOLD_DEFAULT: float = 1.0
    CONFIDENCE_THRESHOLD_DESC: unicode = u'Minimum bit threshold should be > 0.0'
    MEMORY_MODEL: unicode = u'Memory model'
    MEMORY_MODEL_DEFAULT: generic.lsh.LSHMemoryModel = Large (faster)
    MEMORY_MODEL_DESC: unicode = u'Larger memory model results in faster runtime.'
    REFINE_RESULTS: unicode = u'Refine Results'
    REFINE_RESULTS_DEFAULT: bool = True
    REFINE_RESULTS_DESC: unicode = u'Remove results that have conflicting scores.'
    SIMILARITY_THRESHOLD: unicode = u'Minimum similarity threshold (score)'
    SIMILARITY_THRESHOLD_DEFAULT: float = 0.5
    SIMILARITY_THRESHOLD_DESC: unicode = u'Similarity should be between 0 and 1'
    correlatorName: unicode



    def __init__(self): ...



    def createCorrelator(self, __a0: ghidra.framework.plugintool.ServiceProvider, __a1: ghidra.program.model.listing.Program, __a2: ghidra.program.model.address.AddressSetView, __a3: ghidra.program.model.listing.Program, __a4: ghidra.program.model.address.AddressSetView, __a5: ghidra.feature.vt.api.util.VTOptions) -> ghidra.feature.vt.api.main.VTProgramCorrelator: ...

    def createDefaultOptions(self) -> ghidra.feature.vt.api.util.VTOptions: ...

    def equals(self, __a0: object) -> bool: ...

    def getAddressRestrictionPreference(self) -> ghidra.feature.vt.api.main.VTProgramCorrelatorAddressRestrictionPreference: ...

    def getClass(self) -> java.lang.Class: ...

    def getDescription(self) -> unicode: ...

    def getName(self) -> unicode: ...

    def getPriority(self) -> int: ...

    def hashCode(self) -> int: ...

    def notify(self) -> None: ...

    def notifyAll(self) -> None: ...

    def setName(self, __a0: unicode) -> None: ...

    def toString(self) -> unicode: ...

    @overload
    def wait(self) -> None: ...

    @overload
    def wait(self, __a0: long) -> None: ...

    @overload
    def wait(self, __a0: long, __a1: int) -> None: ...

    @property
    def description(self) -> unicode: ...

    @property
    def name(self) -> unicode: ...

    @name.setter
    def name(self, value: unicode) -> None: ...

    @property
    def priority(self) -> int: ...
