import java.lang


class BackgroundThreadTaskLauncher(object):
    """
    Helper class to launch the given task in a background thread  This helper will not
     show a task dialog.

     This class is useful when you want to run the task and use a monitor that is embedded
     in some other component.

     See TaskLauncher.
    """





    def __init__(self): ...



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
