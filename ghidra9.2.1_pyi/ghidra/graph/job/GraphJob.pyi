import ghidra.graph.job
import java.lang


class GraphJob(object):
    """
    A graph job is an item of work that needs to be performed.
    """









    def canShortcut(self) -> bool:
        """
        Returns true if the job can be told to stop running, but to still perform any final
         work before being done.
        @return true if the job can be shortcut
        """
        ...

    def dispose(self) -> None:
        """
        Call to immediately stop this job, ignoring any exceptions or state issues that arise.
        """
        ...

    def equals(self, __a0: object) -> bool: ...

    def execute(self, listener: ghidra.graph.job.GraphJobListener) -> None:
        """
        Tells this job to do its work.  This call will be on the Swing thread.  It is required
         that the given listener be called on the Swing thread when the job is finished.
        @param listener the listener this job is expected to call when its work is finished
        """
        ...

    def getClass(self) -> java.lang.Class: ...

    def hashCode(self) -> int: ...

    def isFinished(self) -> bool:
        """
        Returns true if this job has finished its work
        @return true if this job has finished its work
        """
        ...

    def notify(self) -> None: ...

    def notifyAll(self) -> None: ...

    def shortcut(self) -> None:
        """
        Tells this job to stop running, but to still perform any final work before being done.

         <P>Note: if your job is multi-threaded, then you must make sure to end your thread and
         work before returning from this method.  If that cannot be done in a timely manner, then
         your {@link #canShortcut()} should return false.
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
    def finished(self) -> bool: ...
