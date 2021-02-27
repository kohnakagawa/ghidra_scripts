import ghidra.util.task
import java.io
import java.lang


class PythonUtils(object):
    """
    Python utility method class.
    """

    PYTHON_CACHEDIR: unicode = u'jython_cachedir'
    PYTHON_NAME: unicode = u'jython-2.7.2'
    PYTHON_SRC: unicode = u'python-src'



    def __init__(self): ...



    def equals(self, __a0: object) -> bool: ...

    def getClass(self) -> java.lang.Class: ...

    def hashCode(self) -> int: ...

    def notify(self) -> None: ...

    def notifyAll(self) -> None: ...

    @staticmethod
    def setupPythonCacheDir(monitor: ghidra.util.task.TaskMonitor) -> java.io.File:
        """
        Sets up the python cache directory.  This is a temporary space that python source files
         get compiled to and cached.  It should NOT be in the Ghidra installation directory, because
         some installations will not have the appropriate directory permissions to create new files in.
        @param monitor A monitor to use during the cache directory setup.
        @return The python cache directory.
        @throws IOException If there was a disk-related problem setting up the cache directory.
        @throws CancelledException If the user cancelled the setup.
        """
        ...

    @staticmethod
    def setupPythonHomeDir() -> java.io.File:
        """
        Sets up the python home directory.  This is the directory that has the "Lib" directory in it.
        @return The python home directory.
        @throws IOException If there was a disk-related problem setting up the home directory.
        """
        ...

    def toString(self) -> unicode: ...

    @overload
    def wait(self) -> None: ...

    @overload
    def wait(self, __a0: long) -> None: ...

    @overload
    def wait(self, __a0: long, __a1: int) -> None: ...
