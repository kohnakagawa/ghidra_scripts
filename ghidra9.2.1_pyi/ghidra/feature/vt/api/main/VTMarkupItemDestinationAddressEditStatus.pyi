from typing import List
import ghidra.feature.vt.api.main
import java.lang


class VTMarkupItemDestinationAddressEditStatus(java.lang.Enum):
    EDITABLE: ghidra.feature.vt.api.main.VTMarkupItemDestinationAddressEditStatus = EDITABLE: This item's destination address is editable.
    UNEDITABLE_DATA_ADDRESS: ghidra.feature.vt.api.main.VTMarkupItemDestinationAddressEditStatus = UNEDITABLE_DATA_ADDRESS: This item's destination address is based on the address of data and can't be edited.
    UNEDITABLE_FUNCTION_ENTRY_POINT: ghidra.feature.vt.api.main.VTMarkupItemDestinationAddressEditStatus = UNEDITABLE_FUNCTION_ENTRY_POINT: This item's destination address is based on the function's entry point and can't be edited.
    UNEDITABLE_UNAPPLIABLE_ASSOCIATION_STATUS: ghidra.feature.vt.api.main.VTMarkupItemDestinationAddressEditStatus = UNEDITABLE_UNAPPLIABLE_ASSOCIATION_STATUS: This markup item's Match status prevents its destination address from being edited.
    UNEDITABLE_UNAPPLIABLE_MARKUP_STATUS: ghidra.feature.vt.api.main.VTMarkupItemDestinationAddressEditStatus = UNEDITABLE_UNAPPLIABLE_MARKUP_STATUS: This markup item's status prevents its destination address from being edited.







    @overload
    def compareTo(self, __a0: java.lang.Enum) -> int: ...

    @overload
    def compareTo(self, __a0: object) -> int: ...

    def equals(self, __a0: object) -> bool: ...

    def getClass(self) -> java.lang.Class: ...

    def getDeclaringClass(self) -> java.lang.Class: ...

    def getDescription(self) -> unicode: ...

    def hashCode(self) -> int: ...

    def name(self) -> unicode: ...

    def notify(self) -> None: ...

    def notifyAll(self) -> None: ...

    def ordinal(self) -> int: ...

    def toString(self) -> unicode: ...

    @overload
    @staticmethod
    def valueOf(__a0: unicode) -> ghidra.feature.vt.api.main.VTMarkupItemDestinationAddressEditStatus: ...

    @overload
    @staticmethod
    def valueOf(__a0: java.lang.Class, __a1: unicode) -> java.lang.Enum: ...

    @staticmethod
    def values() -> List[ghidra.feature.vt.api.main.VTMarkupItemDestinationAddressEditStatus]: ...

    @overload
    def wait(self) -> None: ...

    @overload
    def wait(self, __a0: long) -> None: ...

    @overload
    def wait(self, __a0: long, __a1: int) -> None: ...

    @property
    def description(self) -> unicode: ...
