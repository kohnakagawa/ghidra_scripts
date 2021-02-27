import ghidra.framework.protocol.ghidra
import java.lang


class TransientProjectManager(object):








    def dispose(self) -> None:
        """
        Force disposal of all transient projects associated with remote Ghidra URL
         connections. WARNING: This method intended for testing only.
        """
        ...

    def equals(self, __a0: object) -> bool: ...

    def getActiveProjectCount(self) -> int:
        """
        Get the number of active transient project data instances
        @return number of active transient project data instances
        """
        ...

    def getClass(self) -> java.lang.Class: ...

    @staticmethod
    def getTransientProjectManager() -> ghidra.framework.protocol.ghidra.TransientProjectManager:
        """
        Get the <code>TransientProjectManager</code> singleton instance for the JVM
        @return <code>TransientProjectManager</code> singleton instance
        """
        ...

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
    def activeProjectCount(self) -> int: ...
