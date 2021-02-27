from typing import Iterator
from typing import List
import generic.concurrent
import ghidra.app.decompiler.parallel
import ghidra.program.model.address
import ghidra.program.model.listing
import ghidra.util.task
import java.lang
import java.util
import java.util.function


class ParallelDecompiler(object):








    @staticmethod
    def createChunkingParallelDecompiler(callback: generic.concurrent.QCallback, monitor: ghidra.util.task.TaskMonitor) -> ghidra.app.decompiler.parallel.ChunkingParallelDecompiler:
        """
        Creates an object that can be used to perform decompilation of a limited number of
         functions at a time, as opposed to working over an entire range of functions at once.
         {@link #decompileFunctions(QCallback, Program, AddressSetView, TaskMonitor)} will create
         and tear down concurrent data structures on each use, making repeated calls less efficient.
         You would use this method when you wish to perform periodic work as results are returned
         <b>and when using the callback mechanism is not sufficient</b> such as when ordering of
         results is required.
        @param callback the callback required to perform work.
        @param monitor the monitor used to report progress and to cancel
        @return the parallel decompiler used for decompiling.
        """
        ...

    @overload
    @staticmethod
    def decompileFunctions(callback: generic.concurrent.QCallback, functions: java.util.Collection, monitor: ghidra.util.task.TaskMonitor) -> List[R]:
        """
        Decompile the given functions using multiple decompilers
        @param callback the callback to be called for each that is processed
        @param functions the functions to decompile
        @param monitor the task monitor
        @return the list of client results
        @throws InterruptedException if interrupted
        @throws Exception if any other exception occurs
        """
        ...

    @overload
    @staticmethod
    def decompileFunctions(callback: generic.concurrent.QCallback, program: ghidra.program.model.listing.Program, addresses: ghidra.program.model.address.AddressSetView, monitor: ghidra.util.task.TaskMonitor) -> List[R]:
        """
        Decompile the given functions using multiple decompilers
        @param callback the callback to be called for each that is processed
        @param program the program
        @param addresses the addresses restricting which functions to decompile
        @param monitor the task monitor
        @return the list of client results
        @throws InterruptedException if interrupted
        @throws Exception if any other exception occurs
        """
        ...

    @overload
    @staticmethod
    def decompileFunctions(callback: generic.concurrent.QCallback, program: ghidra.program.model.listing.Program, functions: Iterator[ghidra.program.model.listing.Function], resultsConsumer: java.util.function.Consumer, monitor: ghidra.util.task.TaskMonitor) -> None:
        """
        Decompile the given functions using multiple decompilers.

         <p>Results will be passed to the given consumer as they are produced.  Calling this
         method allows you to handle results as they are discovered.

         <p><strong>This method will wait for all processing before returning.</strong>
        @param callback the callback to be called for each that is processed
        @param program the program
        @param functions the functions to decompile
        @param resultsConsumer the consumer to which results will be passed
        @param monitor the task monitor
        @throws InterruptedException if interrupted
        @throws Exception if any other exception occurs
        """
        ...

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
