from typing import List
import generic.jar
import java.lang


class GhidraLauncher(object):
    """
    Class to build the Ghidra classpath, add it to the GhidraClassLoader, and start the
     desired GhidraLaunchable that's passed in as a command line argument.
    """





    def __init__(self): ...



    def equals(self, __a0: object) -> bool: ...

    @staticmethod
    def findJarsInDir(dir: generic.jar.ResourceFile) -> List[unicode]:
        """
        Searches the given directory (non-recursively) for jars and returns their paths in a list.
        @param dir The directory to search for jars in.
        @return A list of discovered jar paths.
        """
        ...

    def getClass(self) -> java.lang.Class: ...

    def hashCode(self) -> int: ...

    @staticmethod
    def main(args: List[unicode]) -> None:
        """
        Launches the given {@link GhidraLaunchable}, passing through the args to it.
        @param args The first argument is the name of the class to launch.  The remaining args
             get passed through to the class's {@link GhidraLaunchable#launch} method.
        @throws Exception If there was a problem launching.  See the exception's message for more
             details on what went wrong.
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
