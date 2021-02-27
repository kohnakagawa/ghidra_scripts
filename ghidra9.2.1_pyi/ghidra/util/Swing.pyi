import java.lang
import java.util.concurrent
import java.util.function


class Swing(object):
    """
    A utility class to handle running code on the AWT Event Dispatch Thread
    """

    GSWING_THREAD_POOL_NAME: unicode = u'GSwing Worker'







    @staticmethod
    def allowSwingToProcessEvents() -> None:
        """
        Wait until AWT event queue (Swing) has been flushed and no more (to a point) events
         are pending.
        """
        ...

    @staticmethod
    def assertSwingThread(errorMessage: unicode) -> bool:
        """
        Logs a stack trace if the current calling thread is not the Swing thread
        @param errorMessage The message to display when not on the Swing thread
        @return true if the calling thread is the Swing thread
        """
        ...

    def equals(self, __a0: object) -> bool: ...

    def getClass(self) -> java.lang.Class: ...

    def hashCode(self) -> int: ...

    @staticmethod
    def isSwingThread() -> bool:
        """
        Returns true if this is the event dispatch thread. Note that this method returns true in
         headless mode because any thread in headless mode can dispatch its own events. In swing
         environments, the swing thread is usually used to dispatch events.
        @return true if this is the event dispatch thread -OR- is in headless mode.
        """
        ...

    def notify(self) -> None: ...

    def notifyAll(self) -> None: ...

    @staticmethod
    def runIfSwingOrRunLater(r: java.lang.Runnable) -> None:
        """
        Runs the given runnable now if the caller is on the Swing thread.  Otherwise, the
         runnable will be posted later.
        @param r the runnable
        """
        ...

    @staticmethod
    def runLater(r: java.lang.Runnable) -> None:
        """
        Calls the given runnable on the Swing thread in the future by putting the request on
         the back of the event queue.
        @param r the runnable
        """
        ...

    @overload
    @staticmethod
    def runNow(r: java.lang.Runnable) -> None:
        """
        Calls the given runnable on the Swing thread
        @param r the runnable
        @see #runNow(Supplier) if you need to return a value from the Swing thread.
        """
        ...

    @overload
    @staticmethod
    def runNow(s: java.util.function.Supplier) -> object:
        """
        Calls the given suppler on the Swing thread, blocking with a
         {@link SwingUtilities#invokeAndWait(Runnable)} if not on the Swing thread.

         <p>Use this method when you are not on the Swing thread and you need to get a value
         that is managed/synchronized by the Swing thread.

         <pre>{@literal
         		String value = runNow(() -> label.getText());
         }</pre>
        @param s the supplier that will be called on the Swing thread
        @return the result of the supplier
        @see #runNow(Runnable)
        """
        ...

    @overload
    @staticmethod
    def runNow(r: java.lang.Runnable, timeout: long, unit: java.util.concurrent.TimeUnit) -> None:
        """
        Calls the given runnable on the Swing thread

         <p>This method will throw an exception if the Swing thread is not available within the
         given timeout.  This method is useful for preventing deadlocks.
        @param r the runnable
        @param timeout the timeout value
        @param unit the time unit of the timeout value
        @throws UnableToSwingException if the timeout was reach waiting for the Swing thread
        @see #runNow(Supplier) if you need to return a value from the Swing thread.
        """
        ...

    def toString(self) -> unicode: ...

    @overload
    def wait(self) -> None: ...

    @overload
    def wait(self, __a0: long) -> None: ...

    @overload
    def wait(self, __a0: long, __a1: int) -> None: ...
