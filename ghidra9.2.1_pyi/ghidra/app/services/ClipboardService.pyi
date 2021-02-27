import ghidra.app.services
import java.lang


class ClipboardService(object):








    def deRegisterClipboardContentProvider(self, service: ghidra.app.services.ClipboardContentProviderService) -> None: ...

    def equals(self, __a0: object) -> bool: ...

    def getClass(self) -> java.lang.Class: ...

    def hashCode(self) -> int: ...

    def notify(self) -> None: ...

    def notifyAll(self) -> None: ...

    def registerClipboardContentProvider(self, service: ghidra.app.services.ClipboardContentProviderService) -> None: ...

    def toString(self) -> unicode: ...

    @overload
    def wait(self) -> None: ...

    @overload
    def wait(self, __a0: long) -> None: ...

    @overload
    def wait(self, __a0: long, __a1: int) -> None: ...
