import ghidra.framework.plugintool
import ghidra.framework.plugintool.util
import java.lang


class DiffServiceProvider(object, ghidra.framework.plugintool.ServiceProvider):








    def addServiceListener(self, __a0: ghidra.framework.plugintool.util.ServiceListener) -> None: ...

    def equals(self, __a0: object) -> bool: ...

    def getClass(self) -> java.lang.Class: ...

    def getService(self, __a0: java.lang.Class) -> object: ...

    def hashCode(self) -> int: ...

    def notify(self) -> None: ...

    def notifyAll(self) -> None: ...

    def removeServiceListener(self, __a0: ghidra.framework.plugintool.util.ServiceListener) -> None: ...

    def toString(self) -> unicode: ...

    @overload
    def wait(self) -> None: ...

    @overload
    def wait(self, __a0: long) -> None: ...

    @overload
    def wait(self, __a0: long, __a1: int) -> None: ...
