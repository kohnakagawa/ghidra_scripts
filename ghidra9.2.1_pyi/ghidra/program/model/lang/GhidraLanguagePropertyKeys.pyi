import java.lang


class GhidraLanguagePropertyKeys(object):
    ADDRESSES_DO_NOT_APPEAR_DIRECTLY_IN_CODE: unicode = u'addressesDoNotAppearDirectlyInCode'
    ALLOW_OFFCUT_REFERENCES_TO_FUNCTION_STARTS: unicode = u'allowOffcutReferencesToFunctionStarts'
    CUSTOM_DISASSEMBLER_CLASS: unicode = u'customDisassemblerClass'
    EMULATE_INSTRUCTION_STATE_MODIFIER_CLASS: unicode = u'emulateInstructionStateModifierClass'
    ENABLE_NO_RETURN_ANALYSIS: unicode = u'enableNoReturnAnalysis'
    ENABLE_SHARED_RETURN_ANALYSIS: unicode = u'enableSharedReturnAnalysis'
    IS_TMS320_FAMILY: unicode = u'isTMS320Family'
    MINIMUM_DATA_IMAGE_BASE: unicode = u'minimumDataImageBase'
    PARALLEL_INSTRUCTION_HELPER_CLASS: unicode = u'parallelInstructionHelperClass'
    PCODE_INJECT_LIBRARY_CLASS: unicode = u'pcodeInjectLibraryClass'
    RESET_CONTEXT_ON_UPGRADE: unicode = u'resetContextOnUpgrade'
    USE_NEW_FUNCTION_STACK_ANALYSIS: unicode = u'useNewFunctionStackAnalysis'
    USE_OPERAND_REFERENCE_ANALYZER_SWITCH_TABLES: unicode = u'useOperandReferenceAnalyzerSwitchTables'







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
