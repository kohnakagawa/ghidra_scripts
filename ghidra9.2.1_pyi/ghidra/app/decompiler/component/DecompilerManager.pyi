import java.lang


class DecompilerManager(object):
    """
    Manages the threading involved with dealing with the decompiler. It uses a simpler approach
     than previous versions.  Currently, there is only one Runnable ever scheduled to the RunManager.
     If a new Decompile request comes in while a decompile is in progress, the new request is
     first checked to see if it going to result in the same function being decompile. If so, then the
     location is updated and the current decompile is allowed to continue.  If the new request is
     a new function or the "forceDecompile" option is on, then the current decompile is stopped
     and a new one is scheduled.  A SwingUpdateManger is used to prevent lots of decompile requests
     from coming to quickly.
    """





    def __init__(self, decompilerController: ghidra.app.decompiler.component.DecompilerController, options: ghidra.app.decompiler.DecompileOptions): ...



    def cancelAll(self) -> None: ...

    def dispose(self) -> None: ...

    def equals(self, __a0: object) -> bool: ...

    def getClass(self) -> java.lang.Class: ...

    def hashCode(self) -> int: ...

    def isBusy(self) -> bool: ...

    def notify(self) -> None: ...

    def notifyAll(self) -> None: ...

    def resetDecompiler(self) -> None:
        """
        Resets the native decompiler process.  Call this method when the decompiler's view
         of a program has been invalidated, such as when a new overlay space has been added.
        """
        ...

    def toString(self) -> unicode: ...

    @overload
    def wait(self) -> None: ...

    @overload
    def wait(self, __a0: long) -> None: ...

    @overload
    def wait(self, __a0: long, __a1: int) -> None: ...

    @property
    def busy(self) -> bool: ...
