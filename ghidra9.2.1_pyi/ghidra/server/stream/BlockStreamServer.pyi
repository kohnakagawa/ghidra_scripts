from typing import List
import db.buffers
import ghidra.server.stream
import java.lang
import java.net
import java.util


class BlockStreamServer(java.lang.Thread):








    @staticmethod
    def activeCount() -> int: ...

    def checkAccess(self) -> None: ...

    def countStackFrames(self) -> int: ...

    @staticmethod
    def currentThread() -> java.lang.Thread: ...

    @staticmethod
    def dumpStack() -> None: ...

    @staticmethod
    def enumerate(__a0: List[java.lang.Thread]) -> int: ...

    def equals(self, __a0: object) -> bool: ...

    @staticmethod
    def getAllStackTraces() -> java.util.Map: ...

    @staticmethod
    def getBlockStreamServer() -> ghidra.server.stream.BlockStreamServer: ...

    def getClass(self) -> java.lang.Class: ...

    def getContextClassLoader(self) -> java.lang.ClassLoader: ...

    @staticmethod
    def getDefaultUncaughtExceptionHandler() -> java.lang.Thread.UncaughtExceptionHandler: ...

    def getId(self) -> long: ...

    def getName(self) -> unicode: ...

    def getNextStreamID(self) -> long: ...

    def getPriority(self) -> int: ...

    def getServerHostname(self) -> unicode: ...

    def getServerPort(self) -> int: ...

    def getStackTrace(self) -> List[java.lang.StackTraceElement]: ...

    def getState(self) -> java.lang.Thread.State: ...

    def getThreadGroup(self) -> java.lang.ThreadGroup: ...

    def getUncaughtExceptionHandler(self) -> java.lang.Thread.UncaughtExceptionHandler: ...

    def hashCode(self) -> int: ...

    @staticmethod
    def holdsLock(__a0: object) -> bool: ...

    def interrupt(self) -> None: ...

    @staticmethod
    def interrupted() -> bool: ...

    def isAlive(self) -> bool: ...

    def isDaemon(self) -> bool: ...

    def isInterrupted(self) -> bool: ...

    def isRunning(self) -> bool: ...

    @overload
    def join(self) -> None: ...

    @overload
    def join(self, __a0: long) -> None: ...

    @overload
    def join(self, __a0: long, __a1: int) -> None: ...

    def notify(self) -> None: ...

    def notifyAll(self) -> None: ...

    @staticmethod
    def onSpinWait() -> None: ...

    def registerBlockStream(self, __a0: ghidra.server.stream.RemoteBlockStreamHandle, __a1: db.buffers.BlockStream) -> bool: ...

    def resume(self) -> None: ...

    def run(self) -> None: ...

    def setContextClassLoader(self, __a0: java.lang.ClassLoader) -> None: ...

    def setDaemon(self, __a0: bool) -> None: ...

    @staticmethod
    def setDefaultUncaughtExceptionHandler(__a0: java.lang.Thread.UncaughtExceptionHandler) -> None: ...

    def setName(self, __a0: unicode) -> None: ...

    def setPriority(self, __a0: int) -> None: ...

    def setUncaughtExceptionHandler(self, __a0: java.lang.Thread.UncaughtExceptionHandler) -> None: ...

    @overload
    @staticmethod
    def sleep(__a0: long) -> None: ...

    @overload
    @staticmethod
    def sleep(__a0: long, __a1: int) -> None: ...

    def start(self) -> None: ...

    def startServer(self, __a0: java.net.ServerSocket, __a1: unicode) -> None: ...

    def stop(self) -> None: ...

    def stopServer(self) -> None: ...

    def suspend(self) -> None: ...

    def toString(self) -> unicode: ...

    @overload
    def wait(self) -> None: ...

    @overload
    def wait(self, __a0: long) -> None: ...

    @overload
    def wait(self, __a0: long, __a1: int) -> None: ...

    @staticmethod
    def yield() -> None: ...

    @property
    def nextStreamID(self) -> long: ...

    @property
    def running(self) -> bool: ...

    @property
    def serverHostname(self) -> unicode: ...

    @property
    def serverPort(self) -> int: ...
