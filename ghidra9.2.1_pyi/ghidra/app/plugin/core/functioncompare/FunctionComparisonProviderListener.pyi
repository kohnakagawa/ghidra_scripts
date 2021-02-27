import ghidra.app.plugin.core.functioncompare
import java.lang


class FunctionComparisonProviderListener(object):








    def equals(self, __a0: object) -> bool: ...

    def getClass(self) -> java.lang.Class: ...

    def hashCode(self) -> int: ...

    def notify(self) -> None: ...

    def notifyAll(self) -> None: ...

    def providerClosed(self, __a0: ghidra.app.plugin.core.functioncompare.FunctionComparisonProvider) -> None: ...

    def providerOpened(self, __a0: ghidra.app.plugin.core.functioncompare.FunctionComparisonProvider) -> None: ...

    def toString(self) -> unicode: ...

    @overload
    def wait(self) -> None: ...

    @overload
    def wait(self, __a0: long) -> None: ...

    @overload
    def wait(self, __a0: long, __a1: int) -> None: ...
