import ghidra.app.plugin.core.osgi
import java.lang
import java.util


class BundleHostListener(object):








    def bundleActivationChange(self, __a0: ghidra.app.plugin.core.osgi.GhidraBundle, __a1: bool) -> None: ...

    def bundleAdded(self, __a0: ghidra.app.plugin.core.osgi.GhidraBundle) -> None: ...

    def bundleBuilt(self, __a0: ghidra.app.plugin.core.osgi.GhidraBundle, __a1: unicode) -> None: ...

    def bundleEnablementChange(self, __a0: ghidra.app.plugin.core.osgi.GhidraBundle, __a1: bool) -> None: ...

    def bundleException(self, __a0: ghidra.app.plugin.core.osgi.GhidraBundleException) -> None: ...

    def bundleRemoved(self, __a0: ghidra.app.plugin.core.osgi.GhidraBundle) -> None: ...

    def bundlesAdded(self, __a0: java.util.Collection) -> None: ...

    def bundlesRemoved(self, __a0: java.util.Collection) -> None: ...

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