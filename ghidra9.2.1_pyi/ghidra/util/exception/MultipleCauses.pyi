from typing import List
import ghidra.util.exception
import java.io
import java.lang
import java.util


class MultipleCauses(java.lang.Throwable):
    """
    Use an instance of this class as the cause when you need to record several causes of an
     exception.

     This paradigm would be necessary when multiple attempts can be made to complete a task, e.g.,
     traversing a list of plugins until one can handle a given condition. If all attempts fail, it is
     desirable to report on each attempt.

     This class acts as a wrapper allowing multiple causes to be recorded in place of one. The causes
     recorded in this wrapper actually apply to the throwable ("parent") which has this
     MultipleCauses exception as its cause.
    """






    class Util(object):




        def __init__(self): ...



        def equals(self, __a0: object) -> bool: ...

        def getClass(self) -> java.lang.Class: ...

        def hashCode(self) -> int: ...

        @staticmethod
        def iterCauses(__a0: java.lang.Throwable) -> java.lang.Iterable: ...

        def notify(self) -> None: ...

        def notifyAll(self) -> None: ...

        def toString(self) -> unicode: ...

        @overload
        def wait(self) -> None: ...

        @overload
        def wait(self, __a0: long) -> None: ...

        @overload
        def wait(self, __a0: long, __a1: int) -> None: ...



    @overload
    def __init__(self):
        """
        Constructs a new MultipleCauses wrapper with no causes
         NOTE: it is rude to leave this empty
        """
        ...

    @overload
    def __init__(self, causes: java.util.Collection):
        """
        Constructs a new MultipleCauses wrapper with the given causes
        @param causes
        """
        ...



    @overload
    def addAllCauses(self, that: ghidra.util.exception.MultipleCauses) -> None:
        """
        Add the causes from another MultipleCauses into this one
        @param that the source to copy from
        """
        ...

    @overload
    def addAllCauses(self, e: java.lang.Throwable) -> None:
        """
        Assuming a throwable has multiple causes, add them all to this MultipleCauses
        @param e the throwable having multiple causes

         This is useful for flattening causes into a common exception. For instance, if a method is
         collecting multiple causes for a potential WidgetException, and it catches a
         WidgetException, instead of collecting the caught WidgetException, it might instead copy
         its causes into its own collection.
        """
        ...

    def addCause(self, cause: java.lang.Throwable) -> None:
        """
        Add the cause to the collection of causes (for the "parent" throwable)
        @param cause the throwable to add as a cause
        """
        ...

    def addFlattenedIfMultiple(self, e: java.lang.Throwable) -> None:
        """
        If the throwable has multiple causes, collect its causes into this MultipleCauses.
         Otherwise, just add it as a cause.
        @param e
        """
        ...

    def addSuppressed(self, __a0: java.lang.Throwable) -> None: ...

    def equals(self, __a0: object) -> bool: ...

    def fillInStackTrace(self) -> java.lang.Throwable: ...

    def getCause(self) -> java.lang.Throwable:
        """
        Use getCauses instead
        @return null
        """
        ...

    def getCauses(self) -> java.util.Collection:
        """
        Returns the causes of the parent throwable (possibly an empty collection)
        @return the collection of causes of the parent throwable
         NOTE: it is rude to leave this empty. If the parent throwable has no cause, or the cause is
         unknown, leave its cause null.
        """
        ...

    def getClass(self) -> java.lang.Class: ...

    def getLocalizedMessage(self) -> unicode: ...

    def getMessage(self) -> unicode: ...

    def getStackTrace(self) -> List[java.lang.StackTraceElement]: ...

    def getSuppressed(self) -> List[java.lang.Throwable]: ...

    @staticmethod
    def hasMultiple(e: java.lang.Throwable) -> bool: ...

    def hashCode(self) -> int: ...

    def initCause(self, cause: java.lang.Throwable) -> java.lang.Throwable:
        """
        Use addCause instead
        """
        ...

    def isEmpty(self) -> bool: ...

    def notify(self) -> None: ...

    def notifyAll(self) -> None: ...

    @overload
    def printStackTrace(self) -> None: ...

    @overload
    def printStackTrace(self, __a0: java.io.PrintStream) -> None: ...

    @overload
    def printStackTrace(self, __a0: java.io.PrintWriter) -> None: ...

    @overload
    @staticmethod
    def printTree(out: java.io.PrintStream, e: java.lang.Throwable) -> None: ...

    @overload
    @staticmethod
    def printTree(out: java.io.PrintStream, prefix: unicode, e: java.lang.Throwable) -> None: ...

    def setStackTrace(self, __a0: List[java.lang.StackTraceElement]) -> None: ...

    def toString(self) -> unicode: ...

    @overload
    def wait(self) -> None: ...

    @overload
    def wait(self, __a0: long) -> None: ...

    @overload
    def wait(self, __a0: long, __a1: int) -> None: ...

    @property
    def cause(self) -> java.lang.Throwable: ...

    @property
    def causes(self) -> java.util.Collection: ...

    @property
    def empty(self) -> bool: ...
