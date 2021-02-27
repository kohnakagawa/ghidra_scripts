import java.lang
import java.util.concurrent


class CountLatch(object):
    """
    Latch that has a count that can be incremented and decremented.  Threads that call await() will
     block until the count is 0.
    """





    def __init__(self): ...



    @overload
    def await(self) -> None:
        """
        Causes the current thread to wait until the latch count is
         zero, unless the thread is {@linkplain Thread#interrupt interrupted}.

         <p>If the current count is zero then this method returns immediately.

         <p>If the current count is greater than zero then the current
         thread becomes disabled for thread scheduling purposes and lies
         dormant until one of two things happen:
         <ul>
         <li>The count reaches zero due to invocations of the
         {@link #decrement} method; or
         <li>Some other thread {@linkplain Thread#interrupt interrupts}
         the current thread.
         </ul>

         <p>If the current thread:
         <ul>
         <li>has its interrupted status set on entry to this method; or
         <li>is {@linkplain Thread#interrupt interrupted} while waiting,
         </ul>
         then {@link InterruptedException} is thrown and the current thread's
         interrupted status is cleared.
        @throws InterruptedException if the current thread is interrupted
                 while waiting
        """
        ...

    @overload
    def await(self, timeout: long, unit: java.util.concurrent.TimeUnit) -> bool:
        """
        Causes the current thread to wait until the latch count is
         zero, unless the thread is {@linkplain Thread#interrupt interrupted},
         or the specified waiting time elapses.

         <p>If the current count is zero then this method returns immediately
         with the value {@code true}.

         <p>If the current count is greater than zero then the current
         thread becomes disabled for thread scheduling purposes and lies
         dormant until one of three things happen:
         <ul>
         <li>The count reaches zero due to invocations of the
         {@link #decrement} method; or
         <li>Some other thread {@linkplain Thread#interrupt interrupts}
         the current thread; or
         <li>The specified waiting time elapses.
         </ul>

         <p>If the count reaches zero then the method returns with the
         value {@code true}.

         <p>If the current thread:
         <ul>
         <li>has its interrupted status set on entry to this method; or
         <li>is {@linkplain Thread#interrupt interrupted} while waiting,
         </ul>
         then {@link InterruptedException} is thrown and the current thread's
         interrupted status is cleared.

         <p>If the specified waiting time elapses then the value {@code false}
         is returned.  If the time is less than or equal to zero, the method
         will not wait at all.
        @param timeout the maximum time to wait
        @param unit the time unit of the {@code timeout} argument
        @return {@code true} if the count reached zero and {@code false}
                 if the waiting time elapsed before the count reached zero
        @throws InterruptedException if the current thread is interrupted
                 while waiting
        """
        ...

    def decrement(self) -> None:
        """
        Decrements the latch count and releases any waiting threads when the count reaches 0.
        """
        ...

    def equals(self, __a0: object) -> bool: ...

    def getClass(self) -> java.lang.Class: ...

    def getCount(self) -> int: ...

    def hashCode(self) -> int: ...

    def increment(self) -> None:
        """
        Increments the latch count.
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

    @property
    def count(self) -> int: ...
