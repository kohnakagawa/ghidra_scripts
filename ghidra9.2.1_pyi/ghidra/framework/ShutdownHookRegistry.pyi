import ghidra.framework
import ghidra.framework.ShutdownHookRegistry
import java.lang


class ShutdownHookRegistry(object):





    class ShutdownHook(object, java.lang.Comparable):








        @overload
        def compareTo(self, __a0: ghidra.framework.ShutdownHookRegistry.ShutdownHook) -> int: ...

        @overload
        def compareTo(self, __a0: object) -> int: ...

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



    def __init__(self): ...



    @staticmethod
    def addShutdownHook(r: java.lang.Runnable, priority: ghidra.framework.ShutdownPriority) -> ghidra.framework.ShutdownHookRegistry.ShutdownHook:
        """
        Install a shutdown hook at the specified priority.  If the hook has no specific
         priority or sensitivity to when it runs, the standard Java Runtime shutdown hook
         mechanism should be used.
         Hooks with a higher priority value will run first
        @param r shutdown hook runnable
        @param priority relative priority
        """
        ...

    def equals(self, __a0: object) -> bool: ...

    def getClass(self) -> java.lang.Class: ...

    def hashCode(self) -> int: ...

    def notify(self) -> None: ...

    def notifyAll(self) -> None: ...

    @staticmethod
    def removeShutdownHook(hook: ghidra.framework.ShutdownHookRegistry.ShutdownHook) -> None:
        """
        Remove a shutdown hook previously registered.
         Hooks with a higher priority value will run first
        @param hook shutdown hook
        """
        ...

    def toString(self) -> unicode: ...

    @overload
    def wait(self) -> None: ...

    @overload
    def wait(self, __a0: long) -> None: ...

    @overload
    def wait(self, __a0: long, __a1: int) -> None: ...
