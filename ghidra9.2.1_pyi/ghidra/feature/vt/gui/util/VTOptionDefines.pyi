import java.lang


class VTOptionDefines(object):
    ACCEPT_MATCH_OPTIONS_NAME: unicode = u'Accept Match Options'
    APPLY_DATA_NAME_ON_ACCEPT: unicode = u'Accept Match Options.Automatically Apply Data Label on Accept'
    APPLY_FUNCTION_NAME_ON_ACCEPT: unicode = u'Accept Match Options.Automatically Apply Function Name on Accept'
    APPLY_MARKUP_OPTIONS_NAME: unicode = u'Apply Markup Options'
    AUTO_CREATE_IMPLIED_MATCH: unicode = u'Accept Match Options.Auto Create Implied Matches'
    CALLING_CONVENTION: unicode = u'Apply Markup Options.Function Calling Convention'
    CALL_FIXUP: unicode = u'Apply Markup Options.Function Call Fixup'
    DATA_MATCH_DATA_TYPE: unicode = u'Apply Markup Options.Data Match Data Type'
    DEFAULT_OPTION_FOR_CALLING_CONVENTION: ghidra.feature.vt.gui.util.VTMatchApplyChoices.CallingConventionChoices
    DEFAULT_OPTION_FOR_CALL_FIXUP: ghidra.feature.vt.gui.util.VTMatchApplyChoices.ReplaceChoices
    DEFAULT_OPTION_FOR_DATA_MATCH_DATA_TYPE: ghidra.feature.vt.gui.util.VTMatchApplyChoices.ReplaceDataChoices
    DEFAULT_OPTION_FOR_EOL_COMMENTS: ghidra.feature.vt.gui.util.VTMatchApplyChoices.CommentChoices
    DEFAULT_OPTION_FOR_FUNCTION_NAME: ghidra.feature.vt.gui.util.VTMatchApplyChoices.FunctionNameChoices
    DEFAULT_OPTION_FOR_FUNCTION_RETURN_TYPE: ghidra.feature.vt.gui.util.VTMatchApplyChoices.ParameterDataTypeChoices
    DEFAULT_OPTION_FOR_FUNCTION_SIGNATURE: ghidra.feature.vt.gui.util.VTMatchApplyChoices.FunctionSignatureChoices
    DEFAULT_OPTION_FOR_HIGHEST_NAME_PRIORITY: ghidra.feature.vt.gui.util.VTMatchApplyChoices.HighestSourcePriorityChoices
    DEFAULT_OPTION_FOR_IGNORE_EXCLUDED_MARKUP_ITEMS: bool
    DEFAULT_OPTION_FOR_IGNORE_INCOMPLETE_MARKUP_ITEMS: bool
    DEFAULT_OPTION_FOR_INLINE: ghidra.feature.vt.gui.util.VTMatchApplyChoices.ReplaceChoices
    DEFAULT_OPTION_FOR_LABELS: ghidra.feature.vt.gui.util.VTMatchApplyChoices.LabelChoices
    DEFAULT_OPTION_FOR_NO_RETURN: ghidra.feature.vt.gui.util.VTMatchApplyChoices.ReplaceChoices
    DEFAULT_OPTION_FOR_PARAMETER_COMMENTS: ghidra.feature.vt.gui.util.VTMatchApplyChoices.CommentChoices
    DEFAULT_OPTION_FOR_PARAMETER_DATA_TYPES: ghidra.feature.vt.gui.util.VTMatchApplyChoices.ParameterDataTypeChoices
    DEFAULT_OPTION_FOR_PARAMETER_NAMES: ghidra.feature.vt.gui.util.VTMatchApplyChoices.SourcePriorityChoices
    DEFAULT_OPTION_FOR_PARAMETER_NAMES_REPLACE_IF_SAME_PRIORITY: bool
    DEFAULT_OPTION_FOR_PLATE_COMMENTS: ghidra.feature.vt.gui.util.VTMatchApplyChoices.CommentChoices
    DEFAULT_OPTION_FOR_POST_COMMENTS: ghidra.feature.vt.gui.util.VTMatchApplyChoices.CommentChoices
    DEFAULT_OPTION_FOR_PRE_COMMENTS: ghidra.feature.vt.gui.util.VTMatchApplyChoices.CommentChoices
    DEFAULT_OPTION_FOR_REPEATABLE_COMMENTS: ghidra.feature.vt.gui.util.VTMatchApplyChoices.CommentChoices
    DEFAULT_OPTION_FOR_VAR_ARGS: ghidra.feature.vt.gui.util.VTMatchApplyChoices.ReplaceChoices
    DISPLAY_APPLY_MARKUP_OPTIONS: unicode = u'Apply Markup Options.Display Apply Markup Options'
    END_OF_LINE_COMMENT: unicode = u'Apply Markup Options.End of Line Comment'
    FUNCTION_NAME: unicode = u'Apply Markup Options.Function Name'
    FUNCTION_RETURN_TYPE: unicode = u'Apply Markup Options.Function Return Type'
    FUNCTION_SIGNATURE: unicode = u'Apply Markup Options.Function Signature'
    HIGHEST_NAME_PRIORITY: unicode = u'Apply Markup Options.Function Parameter Names Highest Name Priority'
    IGNORE_EXCLUDED_MARKUP_ITEMS: unicode = u'Apply Markup Options.Set Excluded Markup Items To Ignored'
    IGNORE_INCOMPLETE_MARKUP_ITEMS: unicode = u'Apply Markup Options.Set Incomplete Markup Items To Ignored'
    INLINE: unicode = u'Apply Markup Options.Function Inline'
    LABELS: unicode = u'Apply Markup Options.Labels'
    NO_RETURN: unicode = u'Apply Markup Options.Function No Return'
    PARAMETER_COMMENTS: unicode = u'Apply Markup Options.Function Parameter Comments'
    PARAMETER_DATA_TYPES: unicode = u'Apply Markup Options.Function Parameter Data Types'
    PARAMETER_NAMES: unicode = u'Apply Markup Options.Function Parameter Names'
    PARAMETER_NAMES_REPLACE_IF_SAME_PRIORITY: unicode = u'Apply Markup Options.Function Parameter Names Replace If Same Priority'
    PLATE_COMMENT: unicode = u'Apply Markup Options.Plate Comment'
    POST_COMMENT: unicode = u'Apply Markup Options.Post Comment'
    PRE_COMMENT: unicode = u'Apply Markup Options.Pre Comment'
    REPEATABLE_COMMENT: unicode = u'Apply Markup Options.Repeatable Comment'
    VAR_ARGS: unicode = u'Apply Markup Options.Function Var Args'



    def __init__(self): ...



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
