from typing import List
import ghidra.feature.vt.gui.util
import java.lang


class VTMatchApplyChoices(object):





    class ParameterDataTypeChoices(java.lang.Enum):
        EXCLUDE: ghidra.feature.vt.gui.util.VTMatchApplyChoices.ParameterDataTypeChoices = Do Not Apply
        REPLACE: ghidra.feature.vt.gui.util.VTMatchApplyChoices.ParameterDataTypeChoices = Replace
        REPLACE_UNDEFINED_DATA_TYPES_ONLY: ghidra.feature.vt.gui.util.VTMatchApplyChoices.ParameterDataTypeChoices = Replace Undefined Data Types Only







        @overload
        def compareTo(self, __a0: java.lang.Enum) -> int: ...

        @overload
        def compareTo(self, __a0: object) -> int: ...

        def equals(self, __a0: object) -> bool: ...

        def getClass(self) -> java.lang.Class: ...

        def getDeclaringClass(self) -> java.lang.Class: ...

        def hashCode(self) -> int: ...

        def name(self) -> unicode: ...

        def notify(self) -> None: ...

        def notifyAll(self) -> None: ...

        def ordinal(self) -> int: ...

        def toString(self) -> unicode: ...

        @overload
        @staticmethod
        def valueOf(__a0: unicode) -> ghidra.feature.vt.gui.util.VTMatchApplyChoices.ParameterDataTypeChoices: ...

        @overload
        @staticmethod
        def valueOf(__a0: java.lang.Class, __a1: unicode) -> java.lang.Enum: ...

        @staticmethod
        def values() -> List[ghidra.feature.vt.gui.util.VTMatchApplyChoices.ParameterDataTypeChoices]: ...

        @overload
        def wait(self) -> None: ...

        @overload
        def wait(self, __a0: long) -> None: ...

        @overload
        def wait(self, __a0: long, __a1: int) -> None: ...






    class HighestSourcePriorityChoices(java.lang.Enum):
        IMPORT_PRIORITY_HIGHEST: ghidra.feature.vt.gui.util.VTMatchApplyChoices.HighestSourcePriorityChoices = Import
        USER_PRIORITY_HIGHEST: ghidra.feature.vt.gui.util.VTMatchApplyChoices.HighestSourcePriorityChoices = User







        @overload
        def compareTo(self, __a0: java.lang.Enum) -> int: ...

        @overload
        def compareTo(self, __a0: object) -> int: ...

        def equals(self, __a0: object) -> bool: ...

        def getClass(self) -> java.lang.Class: ...

        def getDeclaringClass(self) -> java.lang.Class: ...

        def hashCode(self) -> int: ...

        def name(self) -> unicode: ...

        def notify(self) -> None: ...

        def notifyAll(self) -> None: ...

        def ordinal(self) -> int: ...

        def toString(self) -> unicode: ...

        @overload
        @staticmethod
        def valueOf(__a0: unicode) -> ghidra.feature.vt.gui.util.VTMatchApplyChoices.HighestSourcePriorityChoices: ...

        @overload
        @staticmethod
        def valueOf(__a0: java.lang.Class, __a1: unicode) -> java.lang.Enum: ...

        @staticmethod
        def values() -> List[ghidra.feature.vt.gui.util.VTMatchApplyChoices.HighestSourcePriorityChoices]: ...

        @overload
        def wait(self) -> None: ...

        @overload
        def wait(self, __a0: long) -> None: ...

        @overload
        def wait(self, __a0: long, __a1: int) -> None: ...






    class FunctionAttributeChoices(java.lang.Enum):
        EXCLUDE: ghidra.feature.vt.gui.util.VTMatchApplyChoices.FunctionAttributeChoices = Do Not Apply
        REPLACE: ghidra.feature.vt.gui.util.VTMatchApplyChoices.FunctionAttributeChoices = Replace
        WHEN_TAKING_SIGNATURE: ghidra.feature.vt.gui.util.VTMatchApplyChoices.FunctionAttributeChoices = Replace When Replacing Signature







        @overload
        def compareTo(self, __a0: java.lang.Enum) -> int: ...

        @overload
        def compareTo(self, __a0: object) -> int: ...

        def equals(self, __a0: object) -> bool: ...

        def getClass(self) -> java.lang.Class: ...

        def getDeclaringClass(self) -> java.lang.Class: ...

        def hashCode(self) -> int: ...

        def name(self) -> unicode: ...

        def notify(self) -> None: ...

        def notifyAll(self) -> None: ...

        def ordinal(self) -> int: ...

        def toString(self) -> unicode: ...

        @overload
        @staticmethod
        def valueOf(__a0: unicode) -> ghidra.feature.vt.gui.util.VTMatchApplyChoices.FunctionAttributeChoices: ...

        @overload
        @staticmethod
        def valueOf(__a0: java.lang.Class, __a1: unicode) -> java.lang.Enum: ...

        @staticmethod
        def values() -> List[ghidra.feature.vt.gui.util.VTMatchApplyChoices.FunctionAttributeChoices]: ...

        @overload
        def wait(self) -> None: ...

        @overload
        def wait(self, __a0: long) -> None: ...

        @overload
        def wait(self, __a0: long, __a1: int) -> None: ...






    class CallingConventionChoices(java.lang.Enum):
        EXCLUDE: ghidra.feature.vt.gui.util.VTMatchApplyChoices.CallingConventionChoices = Do Not Apply
        NAME_MATCH: ghidra.feature.vt.gui.util.VTMatchApplyChoices.CallingConventionChoices = Replace If Has Named Convention
        SAME_LANGUAGE: ghidra.feature.vt.gui.util.VTMatchApplyChoices.CallingConventionChoices = Replace If Same Language







        @overload
        def compareTo(self, __a0: java.lang.Enum) -> int: ...

        @overload
        def compareTo(self, __a0: object) -> int: ...

        def equals(self, __a0: object) -> bool: ...

        def getClass(self) -> java.lang.Class: ...

        def getDeclaringClass(self) -> java.lang.Class: ...

        def hashCode(self) -> int: ...

        def name(self) -> unicode: ...

        def notify(self) -> None: ...

        def notifyAll(self) -> None: ...

        def ordinal(self) -> int: ...

        def toString(self) -> unicode: ...

        @overload
        @staticmethod
        def valueOf(__a0: unicode) -> ghidra.feature.vt.gui.util.VTMatchApplyChoices.CallingConventionChoices: ...

        @overload
        @staticmethod
        def valueOf(__a0: java.lang.Class, __a1: unicode) -> java.lang.Enum: ...

        @staticmethod
        def values() -> List[ghidra.feature.vt.gui.util.VTMatchApplyChoices.CallingConventionChoices]: ...

        @overload
        def wait(self) -> None: ...

        @overload
        def wait(self, __a0: long) -> None: ...

        @overload
        def wait(self, __a0: long, __a1: int) -> None: ...






    class ReplaceChoices(java.lang.Enum):
        EXCLUDE: ghidra.feature.vt.gui.util.VTMatchApplyChoices.ReplaceChoices = Do Not Apply
        REPLACE: ghidra.feature.vt.gui.util.VTMatchApplyChoices.ReplaceChoices = Replace







        @overload
        def compareTo(self, __a0: java.lang.Enum) -> int: ...

        @overload
        def compareTo(self, __a0: object) -> int: ...

        def equals(self, __a0: object) -> bool: ...

        def getClass(self) -> java.lang.Class: ...

        def getDeclaringClass(self) -> java.lang.Class: ...

        def hashCode(self) -> int: ...

        def name(self) -> unicode: ...

        def notify(self) -> None: ...

        def notifyAll(self) -> None: ...

        def ordinal(self) -> int: ...

        def toString(self) -> unicode: ...

        @overload
        @staticmethod
        def valueOf(__a0: unicode) -> ghidra.feature.vt.gui.util.VTMatchApplyChoices.ReplaceChoices: ...

        @overload
        @staticmethod
        def valueOf(__a0: java.lang.Class, __a1: unicode) -> java.lang.Enum: ...

        @staticmethod
        def values() -> List[ghidra.feature.vt.gui.util.VTMatchApplyChoices.ReplaceChoices]: ...

        @overload
        def wait(self) -> None: ...

        @overload
        def wait(self, __a0: long) -> None: ...

        @overload
        def wait(self, __a0: long, __a1: int) -> None: ...






    class FunctionSignatureChoices(java.lang.Enum):
        EXCLUDE: ghidra.feature.vt.gui.util.VTMatchApplyChoices.FunctionSignatureChoices = Do Not Apply
        REPLACE: ghidra.feature.vt.gui.util.VTMatchApplyChoices.FunctionSignatureChoices = Replace
        WHEN_SAME_PARAMETER_COUNT: ghidra.feature.vt.gui.util.VTMatchApplyChoices.FunctionSignatureChoices = Replace When Same Parameter Count







        @overload
        def compareTo(self, __a0: java.lang.Enum) -> int: ...

        @overload
        def compareTo(self, __a0: object) -> int: ...

        def equals(self, __a0: object) -> bool: ...

        def getClass(self) -> java.lang.Class: ...

        def getDeclaringClass(self) -> java.lang.Class: ...

        def hashCode(self) -> int: ...

        def name(self) -> unicode: ...

        def notify(self) -> None: ...

        def notifyAll(self) -> None: ...

        def ordinal(self) -> int: ...

        def toString(self) -> unicode: ...

        @overload
        @staticmethod
        def valueOf(__a0: unicode) -> ghidra.feature.vt.gui.util.VTMatchApplyChoices.FunctionSignatureChoices: ...

        @overload
        @staticmethod
        def valueOf(__a0: java.lang.Class, __a1: unicode) -> java.lang.Enum: ...

        @staticmethod
        def values() -> List[ghidra.feature.vt.gui.util.VTMatchApplyChoices.FunctionSignatureChoices]: ...

        @overload
        def wait(self) -> None: ...

        @overload
        def wait(self, __a0: long) -> None: ...

        @overload
        def wait(self, __a0: long, __a1: int) -> None: ...






    class ReplaceDefaultChoices(java.lang.Enum):
        EXCLUDE: ghidra.feature.vt.gui.util.VTMatchApplyChoices.ReplaceDefaultChoices = Do Not Apply
        REPLACE_ALWAYS: ghidra.feature.vt.gui.util.VTMatchApplyChoices.ReplaceDefaultChoices = Replace Always
        REPLACE_DEFAULT_ONLY: ghidra.feature.vt.gui.util.VTMatchApplyChoices.ReplaceDefaultChoices = Replace Default Only







        @overload
        def compareTo(self, __a0: java.lang.Enum) -> int: ...

        @overload
        def compareTo(self, __a0: object) -> int: ...

        def equals(self, __a0: object) -> bool: ...

        def getClass(self) -> java.lang.Class: ...

        def getDeclaringClass(self) -> java.lang.Class: ...

        def hashCode(self) -> int: ...

        def name(self) -> unicode: ...

        def notify(self) -> None: ...

        def notifyAll(self) -> None: ...

        def ordinal(self) -> int: ...

        def toString(self) -> unicode: ...

        @overload
        @staticmethod
        def valueOf(__a0: unicode) -> ghidra.feature.vt.gui.util.VTMatchApplyChoices.ReplaceDefaultChoices: ...

        @overload
        @staticmethod
        def valueOf(__a0: java.lang.Class, __a1: unicode) -> java.lang.Enum: ...

        @staticmethod
        def values() -> List[ghidra.feature.vt.gui.util.VTMatchApplyChoices.ReplaceDefaultChoices]: ...

        @overload
        def wait(self) -> None: ...

        @overload
        def wait(self, __a0: long) -> None: ...

        @overload
        def wait(self, __a0: long, __a1: int) -> None: ...






    class SourcePriorityChoices(java.lang.Enum):
        EXCLUDE: ghidra.feature.vt.gui.util.VTMatchApplyChoices.SourcePriorityChoices = Do Not Apply
        PRIORITY_REPLACE: ghidra.feature.vt.gui.util.VTMatchApplyChoices.SourcePriorityChoices = Priority Replace
        REPLACE: ghidra.feature.vt.gui.util.VTMatchApplyChoices.SourcePriorityChoices = Replace
        REPLACE_DEFAULTS_ONLY: ghidra.feature.vt.gui.util.VTMatchApplyChoices.SourcePriorityChoices = Replace Default Only







        @overload
        def compareTo(self, __a0: java.lang.Enum) -> int: ...

        @overload
        def compareTo(self, __a0: object) -> int: ...

        def equals(self, __a0: object) -> bool: ...

        def getClass(self) -> java.lang.Class: ...

        def getDeclaringClass(self) -> java.lang.Class: ...

        def hashCode(self) -> int: ...

        def name(self) -> unicode: ...

        def notify(self) -> None: ...

        def notifyAll(self) -> None: ...

        def ordinal(self) -> int: ...

        def toString(self) -> unicode: ...

        @overload
        @staticmethod
        def valueOf(__a0: unicode) -> ghidra.feature.vt.gui.util.VTMatchApplyChoices.SourcePriorityChoices: ...

        @overload
        @staticmethod
        def valueOf(__a0: java.lang.Class, __a1: unicode) -> java.lang.Enum: ...

        @staticmethod
        def values() -> List[ghidra.feature.vt.gui.util.VTMatchApplyChoices.SourcePriorityChoices]: ...

        @overload
        def wait(self) -> None: ...

        @overload
        def wait(self, __a0: long) -> None: ...

        @overload
        def wait(self, __a0: long, __a1: int) -> None: ...






    class ReplaceDataChoices(java.lang.Enum):
        EXCLUDE: ghidra.feature.vt.gui.util.VTMatchApplyChoices.ReplaceDataChoices = Do Not Apply
        REPLACE_ALL_DATA: ghidra.feature.vt.gui.util.VTMatchApplyChoices.ReplaceDataChoices = Replace All Data
        REPLACE_FIRST_DATA_ONLY: ghidra.feature.vt.gui.util.VTMatchApplyChoices.ReplaceDataChoices = Replace First Data Only
        REPLACE_UNDEFINED_DATA_ONLY: ghidra.feature.vt.gui.util.VTMatchApplyChoices.ReplaceDataChoices = Replace Undefined Data Only







        @overload
        def compareTo(self, __a0: java.lang.Enum) -> int: ...

        @overload
        def compareTo(self, __a0: object) -> int: ...

        def equals(self, __a0: object) -> bool: ...

        def getClass(self) -> java.lang.Class: ...

        def getDeclaringClass(self) -> java.lang.Class: ...

        def hashCode(self) -> int: ...

        def name(self) -> unicode: ...

        def notify(self) -> None: ...

        def notifyAll(self) -> None: ...

        def ordinal(self) -> int: ...

        def toString(self) -> unicode: ...

        @overload
        @staticmethod
        def valueOf(__a0: unicode) -> ghidra.feature.vt.gui.util.VTMatchApplyChoices.ReplaceDataChoices: ...

        @overload
        @staticmethod
        def valueOf(__a0: java.lang.Class, __a1: unicode) -> java.lang.Enum: ...

        @staticmethod
        def values() -> List[ghidra.feature.vt.gui.util.VTMatchApplyChoices.ReplaceDataChoices]: ...

        @overload
        def wait(self) -> None: ...

        @overload
        def wait(self, __a0: long) -> None: ...

        @overload
        def wait(self, __a0: long, __a1: int) -> None: ...






    class ParameterSourceChoices(java.lang.Enum):
        ENTIRE_PARAMETER_SIGNATURE_MARKUP: ghidra.feature.vt.gui.util.VTMatchApplyChoices.ParameterSourceChoices = Use Entire Parameters Signature
        INDIVIDUAL_PARAMETER_MARKUP: ghidra.feature.vt.gui.util.VTMatchApplyChoices.ParameterSourceChoices = Use Individual Parameter Items







        @overload
        def compareTo(self, __a0: java.lang.Enum) -> int: ...

        @overload
        def compareTo(self, __a0: object) -> int: ...

        def equals(self, __a0: object) -> bool: ...

        def getClass(self) -> java.lang.Class: ...

        def getDeclaringClass(self) -> java.lang.Class: ...

        def hashCode(self) -> int: ...

        def name(self) -> unicode: ...

        def notify(self) -> None: ...

        def notifyAll(self) -> None: ...

        def ordinal(self) -> int: ...

        def toString(self) -> unicode: ...

        @overload
        @staticmethod
        def valueOf(__a0: unicode) -> ghidra.feature.vt.gui.util.VTMatchApplyChoices.ParameterSourceChoices: ...

        @overload
        @staticmethod
        def valueOf(__a0: java.lang.Class, __a1: unicode) -> java.lang.Enum: ...

        @staticmethod
        def values() -> List[ghidra.feature.vt.gui.util.VTMatchApplyChoices.ParameterSourceChoices]: ...

        @overload
        def wait(self) -> None: ...

        @overload
        def wait(self, __a0: long) -> None: ...

        @overload
        def wait(self, __a0: long, __a1: int) -> None: ...






    class LabelChoices(java.lang.Enum):
        ADD: ghidra.feature.vt.gui.util.VTMatchApplyChoices.LabelChoices = Add
        ADD_AS_PRIMARY: ghidra.feature.vt.gui.util.VTMatchApplyChoices.LabelChoices = Add As Primary
        EXCLUDE: ghidra.feature.vt.gui.util.VTMatchApplyChoices.LabelChoices = Do Not Apply
        REPLACE_ALL: ghidra.feature.vt.gui.util.VTMatchApplyChoices.LabelChoices = Replace All
        REPLACE_DEFAULT_ONLY: ghidra.feature.vt.gui.util.VTMatchApplyChoices.LabelChoices = Replace Default Only







        @overload
        def compareTo(self, __a0: java.lang.Enum) -> int: ...

        @overload
        def compareTo(self, __a0: object) -> int: ...

        def equals(self, __a0: object) -> bool: ...

        def getClass(self) -> java.lang.Class: ...

        def getDeclaringClass(self) -> java.lang.Class: ...

        def hashCode(self) -> int: ...

        def name(self) -> unicode: ...

        def notify(self) -> None: ...

        def notifyAll(self) -> None: ...

        def ordinal(self) -> int: ...

        def toString(self) -> unicode: ...

        @overload
        @staticmethod
        def valueOf(__a0: unicode) -> ghidra.feature.vt.gui.util.VTMatchApplyChoices.LabelChoices: ...

        @overload
        @staticmethod
        def valueOf(__a0: java.lang.Class, __a1: unicode) -> java.lang.Enum: ...

        @staticmethod
        def values() -> List[ghidra.feature.vt.gui.util.VTMatchApplyChoices.LabelChoices]: ...

        @overload
        def wait(self) -> None: ...

        @overload
        def wait(self, __a0: long) -> None: ...

        @overload
        def wait(self, __a0: long, __a1: int) -> None: ...






    class FunctionNameChoices(java.lang.Enum):
        ADD: ghidra.feature.vt.gui.util.VTMatchApplyChoices.FunctionNameChoices = Add
        ADD_AS_PRIMARY: ghidra.feature.vt.gui.util.VTMatchApplyChoices.FunctionNameChoices = Add As Primary
        EXCLUDE: ghidra.feature.vt.gui.util.VTMatchApplyChoices.FunctionNameChoices = Do Not Apply
        REPLACE_ALWAYS: ghidra.feature.vt.gui.util.VTMatchApplyChoices.FunctionNameChoices = Replace Always
        REPLACE_DEFAULT_ONLY: ghidra.feature.vt.gui.util.VTMatchApplyChoices.FunctionNameChoices = Replace Default Only







        @overload
        def compareTo(self, __a0: java.lang.Enum) -> int: ...

        @overload
        def compareTo(self, __a0: object) -> int: ...

        def equals(self, __a0: object) -> bool: ...

        def getClass(self) -> java.lang.Class: ...

        def getDeclaringClass(self) -> java.lang.Class: ...

        def hashCode(self) -> int: ...

        def name(self) -> unicode: ...

        def notify(self) -> None: ...

        def notifyAll(self) -> None: ...

        def ordinal(self) -> int: ...

        def toString(self) -> unicode: ...

        @overload
        @staticmethod
        def valueOf(__a0: unicode) -> ghidra.feature.vt.gui.util.VTMatchApplyChoices.FunctionNameChoices: ...

        @overload
        @staticmethod
        def valueOf(__a0: java.lang.Class, __a1: unicode) -> java.lang.Enum: ...

        @staticmethod
        def values() -> List[ghidra.feature.vt.gui.util.VTMatchApplyChoices.FunctionNameChoices]: ...

        @overload
        def wait(self) -> None: ...

        @overload
        def wait(self, __a0: long) -> None: ...

        @overload
        def wait(self, __a0: long, __a1: int) -> None: ...






    class CommentChoices(java.lang.Enum):
        APPEND_TO_EXISTING: ghidra.feature.vt.gui.util.VTMatchApplyChoices.CommentChoices = Add To Existing
        EXCLUDE: ghidra.feature.vt.gui.util.VTMatchApplyChoices.CommentChoices = Do Not Apply
        OVERWRITE_EXISTING: ghidra.feature.vt.gui.util.VTMatchApplyChoices.CommentChoices = Replace Existing







        @overload
        def compareTo(self, __a0: java.lang.Enum) -> int: ...

        @overload
        def compareTo(self, __a0: object) -> int: ...

        def equals(self, __a0: object) -> bool: ...

        def getClass(self) -> java.lang.Class: ...

        def getDeclaringClass(self) -> java.lang.Class: ...

        def hashCode(self) -> int: ...

        def name(self) -> unicode: ...

        def notify(self) -> None: ...

        def notifyAll(self) -> None: ...

        def ordinal(self) -> int: ...

        def toString(self) -> unicode: ...

        @overload
        @staticmethod
        def valueOf(__a0: unicode) -> ghidra.feature.vt.gui.util.VTMatchApplyChoices.CommentChoices: ...

        @overload
        @staticmethod
        def valueOf(__a0: java.lang.Class, __a1: unicode) -> java.lang.Enum: ...

        @staticmethod
        def values() -> List[ghidra.feature.vt.gui.util.VTMatchApplyChoices.CommentChoices]: ...

        @overload
        def wait(self) -> None: ...

        @overload
        def wait(self, __a0: long) -> None: ...

        @overload
        def wait(self, __a0: long, __a1: int) -> None: ...



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
