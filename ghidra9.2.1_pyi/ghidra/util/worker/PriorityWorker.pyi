import ghidra.util.task
import ghidra.util.worker
import java.lang


class PriorityWorker(ghidra.util.worker.AbstractWorker):
    """
    Executes a single job at a time in priority order.
    """





    @overload
    def __init__(self, name: unicode, monitor: ghidra.util.task.TaskMonitor):
        """
        Creates a PriorityWorker that will use a <b>shared</b> thread pool to process jobs.
         Also, threads created using this constructor are not persistent.
        @param name the name of the shared thread pool.
        @param monitor the monitor used to cancel jobs.
        """
        ...

    @overload
    def __init__(self, name: unicode, isPersistentThread: bool, useSharedThreadPool: bool, monitor: ghidra.util.task.TaskMonitor):
        """
        This constructor allows you to change persistence and shared thread pool usage.
        @param name the name of the shared thread pool.
        @param isPersistentThread if true, the worker thread will stay around when idle;
                     false means that the thread will go away if not needed. Should be true for
                     high frequency usage.
        @param useSharedThreadPool true signals to use the given name to find/create a thread pool
                     that can be shared throughout the system.
        @param monitor the monitor used to cancel jobs.
        """
        ...



    def clearAllJobs(self) -> None:
        """
        Clears any pending jobs and cancels any currently executing job.
        """
        ...

    def clearAllJobsWithInterrupt_IKnowTheRisks(self) -> None:
        """
        Clears any pending jobs and cancels any currently executing job.
          <p>
          <b>Warning: Calling this method may leave the program in a bad
          state.  Thus, it is recommended that you only do so when you known that any job that
          could possibly be scheduled does not manipulate sensitive parts of the program; for
          example, opening file handles that should be closed before finishing.</b>
          <p><b>
          If you are unsure
          about whether your jobs handle interrupt correctly, then don't use this method.
          </b>
        """
        ...

    def clearPendingJobs(self) -> None:
        """
        Clears any jobs from the queue <b>that have not yet been run</b>.  This does not cancel
         the currently running job.
        """
        ...

    def dispose(self) -> None:
        """
        Disposes this worker and terminates its thread.
        """
        ...

    def equals(self, __a0: object) -> bool: ...

    def getClass(self) -> java.lang.Class: ...

    def hashCode(self) -> int: ...

    def isBusy(self) -> bool: ...

    def isDisposed(self) -> bool: ...

    def notify(self) -> None: ...

    def notifyAll(self) -> None: ...

    @overload
    def schedule(self, job: ghidra.util.worker.PriorityJob) -> None: ...

    @overload
    def schedule(self, __a0: ghidra.util.worker.Job) -> None: ...

    def setBusyListener(self, listener: ghidra.util.task.BusyListener) -> None: ...

    def setTaskMonitor(self, monitor: ghidra.util.task.TaskMonitor) -> None: ...

    def toString(self) -> unicode: ...

    @overload
    def wait(self) -> None: ...

    @overload
    def wait(self, __a0: long) -> None: ...

    @overload
    def wait(self, __a0: long, __a1: int) -> None: ...

    def waitUntilNoJobsScheduled(self, maxWait: int) -> None:
        """
        This method will block until there are no scheduled jobs in this worker. This
         method assumes that all jobs have a priority less than Long.MAX_VALUE.
         <p>
         For a non-priority
         queue, this call will not wait for jobs that are scheduled after this call was made.
        """
        ...
