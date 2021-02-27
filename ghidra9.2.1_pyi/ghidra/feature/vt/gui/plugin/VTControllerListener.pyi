import ghidra.feature.vt.api.main
import ghidra.feature.vt.gui.util
import ghidra.framework.model
import ghidra.framework.options
import java.lang


class VTControllerListener(object):








    def disposed(self) -> None: ...

    def equals(self, __a0: object) -> bool: ...

    def getClass(self) -> java.lang.Class: ...

    def hashCode(self) -> int: ...

    def markupItemSelected(self, __a0: ghidra.feature.vt.api.main.VTMarkupItem) -> None: ...

    def matchSelected(self, __a0: ghidra.feature.vt.gui.util.MatchInfo) -> None: ...

    def notify(self) -> None: ...

    def notifyAll(self) -> None: ...

    def optionsChanged(self, __a0: ghidra.framework.options.Options) -> None: ...

    def sessionChanged(self, __a0: ghidra.feature.vt.api.main.VTSession) -> None: ...

    def sessionUpdated(self, __a0: ghidra.framework.model.DomainObjectChangedEvent) -> None: ...

    def toString(self) -> unicode: ...

    @overload
    def wait(self) -> None: ...

    @overload
    def wait(self, __a0: long) -> None: ...

    @overload
    def wait(self, __a0: long, __a1: int) -> None: ...
