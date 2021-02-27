import ghidra.feature.vt.api.main
import java.lang


class DisplayableMarkupItemAction(object):
    ADD_ACTION: ghidra.feature.vt.gui.actions.DisplayableMarkupItemAction = ghidra.feature.vt.gui.actions.DisplayableMarkupItemAction@d4cfbd0
    EXCLUDE_ACTION: ghidra.feature.vt.gui.actions.DisplayableMarkupItemAction = ghidra.feature.vt.gui.actions.DisplayableMarkupItemAction@7d0e7de8
    REPLACE_ACTION: ghidra.feature.vt.gui.actions.DisplayableMarkupItemAction = ghidra.feature.vt.gui.actions.DisplayableMarkupItemAction@37c610d6







    def equals(self, __a0: object) -> bool: ...

    def getAction(self) -> ghidra.feature.vt.api.main.VTMarkupItemApplyActionType: ...

    def getClass(self) -> java.lang.Class: ...

    def getDisplayString(self) -> unicode: ...

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
    def action(self) -> ghidra.feature.vt.api.main.VTMarkupItemApplyActionType: ...

    @property
    def displayString(self) -> unicode: ...
