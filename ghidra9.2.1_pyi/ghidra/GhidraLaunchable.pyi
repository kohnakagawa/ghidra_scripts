from typing import List
import ghidra
import java.lang


class GhidraLaunchable(object):
    """
    Something intended to be launched by the GhidraLauncher.
    """









    def equals(self, __a0: object) -> bool: ...

    def getClass(self) -> java.lang.Class: ...

    def hashCode(self) -> int: ...

    def launch(self, layout: ghidra.GhidraApplicationLayout, args: List[unicode]) -> None:
        """
        Launches the launchable.
        @param layout The application layout to use for the launch.
        @param args The arguments passed through by the {@link GhidraLauncher}.
        @throws Exception if there was a problem with the launch.
        """
        ...

    def notify(self) -> None: ...

    def notifyAll(self) -> None: ...

    def toString(self) -> unicode: ...

    @overload
    def wait(self) -> None: ...

    @overload
    def wait(self, __a0: long) -> None: ...

    @overload
    def wait(self, __a0: long, __a1: int) -> None: ...
