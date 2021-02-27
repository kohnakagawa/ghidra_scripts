import ghidra.graph.job
import java.lang


class GraphJobRunner(object, ghidra.graph.job.GraphJobListener):
    """
    A class to run GraphJobs.  This class will queue jobs and will run them
     in the Swing thread.  Job implementations may be multi-threaded, as they choose, by managing
     threads themselves.    This is different than a typical job runner, which is usually
     itself threaded.

     A job is considered finished when #jobFinished(GraphJob)
     is called on this class.  After this callback, the next job will be run.

     #setFinalJob(GraphJob) sets a job to be run last, after all jobs in the queue
     have finished.

     When a job is added via #schedule(GraphJob), any currently running job will
     be told to finish immediately, if it's GraphJob#canShortcut() returns true.  If it
     cannot be shortcut, then it will be allowed to finish.  Further, this logic will be applied
     to each job in the queue.  So, if there are multiple jobs in the queue, which all return
     true for GraphJob#canShortcut(), then they will each be shortcut (allowing them
     to complete) before running the newly scheduled job.

     This class is thread-safe in that you can #schedule(GraphJob) jobs from any
     thread.

     Synchronization Policy:  the methods that mutate fields of this class or read them
     must be synchronized.
    """





    def __init__(self): ...



    def dispose(self) -> None:
        """
        Clears any pending jobs, stops the currently running job ungracefully and updates this
         class so that any new jobs added will be ignored.
        """
        ...

    def equals(self, __a0: object) -> bool: ...

    def finishAllJobs(self) -> None:
        """
        Causes all jobs to be finished as quickly as possible, calling {@link GraphJob#shortcut()}
         on each job.

         <P>Note: some jobs are not shortcut-able and will finish on their own time.  Any jobs
         queued behind a non-shortcut-able job will <b>not</b> be shortcut.
        @see #dispose()
        """
        ...

    def getClass(self) -> java.lang.Class: ...

    def hashCode(self) -> int: ...

    def isBusy(self) -> bool: ...

    def jobFinished(self, job: ghidra.graph.job.GraphJob) -> None: ...

    def notify(self) -> None: ...

    def notifyAll(self) -> None: ...

    def schedule(self, job: ghidra.graph.job.GraphJob) -> None: ...

    def setFinalJob(self, job: ghidra.graph.job.GraphJob) -> None:
        """
        Sets a job to run after all currently running and queued jobs.  If a final job was already
         set, then that job will be replaced with the given job.
        @param job the job to run
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

    @property
    def finalJob(self) -> None: ...  # No getter available.

    @finalJob.setter
    def finalJob(self, value: ghidra.graph.job.GraphJob) -> None: ...
