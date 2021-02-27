import ghidra.util.task
import ghidra.util.worker
import java.lang


class AbstractWorker(object):
    """
    Class that uses a single thread to execute scheduled jobs.

     Subclasses provide the BlockingQueue implementation, which allows for controlling
     how jobs get scheduled (e.g., FIFO or priority-based).
    """









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

    @property
    def busy(self) -> bool: ...

    @property
    def busyListener(self) -> None: ...  # No getter available.

    @busyListener.setter
    def busyListener(self, value: ghidra.util.task.BusyListener) -> None: ...

    @property
    def disposed(self) -> bool: ...

    @property
    def taskMonitor(self) -> None: ...  # No getter available.

    @taskMonitor.setter
    def taskMonitor(self, value: ghidra.util.task.TaskMonitor) -> None: ...
