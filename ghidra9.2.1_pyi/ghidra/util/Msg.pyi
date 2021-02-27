import ghidra.util
import java.awt
import java.lang


class Msg(object):
    """
    Class with static methods to report errors as either a short message or a
     more detailed message (e.g., stacktrace).

     The 'message' parameter for these calls is typically a String.  However, it can also
     be a log4j Message object as well.   (See log4j2 for details.)
    """









    @overload
    @staticmethod
    def debug(originator: object, message: object) -> None:
        """
        Used to record a debug message to the log file.
        @param originator a Logger instance, "this", or YourClass.class
        @param message the details of the message
        """
        ...

    @overload
    @staticmethod
    def debug(originator: object, message: object, throwable: java.lang.Throwable) -> None:
        """
        Used to record a debug message to the log file.  This may be used to document an exception
         without elevating that exception to error or warning status
        @param originator a Logger instance, "this", or YourClass.class
        @param message the details of the message
        @param throwable the Throwable that describes the cause of the error
        """
        ...

    def equals(self, __a0: object) -> bool: ...

    @overload
    @staticmethod
    def error(originator: object, message: object) -> None:
        """
        Used to display an error message with no available Throwable to the user
         via the console (no GUI). Also records the message to the logging system.
         If you have a Throwable, please use the other error(...) method.
        @param originator a Logger instance, "this", or YourClass.class
        @param message the details of the message
        """
        ...

    @overload
    @staticmethod
    def error(originator: object, message: object, throwable: java.lang.Throwable) -> None:
        """
        Used to display an error message with a Throwable (for stack trace) to
         the user via the console (no GUI). Also records the message to the
         logging system.
        @param originator a Logger instance, "this", or YourClass.class
        @param message the details of the message
        @param throwable the Throwable that describes the cause of the error
        """
        ...

    def getClass(self) -> java.lang.Class: ...

    def hashCode(self) -> int: ...

    @overload
    @staticmethod
    def info(originator: object, message: object) -> None:
        """
        Used to display an informational message to the user via the console (no
         GUI). Also records the message to the logging system.
        @param originator a Logger instance, "this", or YourClass.class
        @param message the details of the message
        """
        ...

    @overload
    @staticmethod
    def info(originator: object, message: object, throwable: java.lang.Throwable) -> None:
        """
        Used to display an informational message to the user via the console (no
         GUI). Also records the message to the logging system.  This may be used to
         document an exception without elevating that exception to error or warning status.
        @param originator a Logger instance, "this", or YourClass.class
        @param message the details of the message
        @param throwable the Throwable that describes the cause of the error
        """
        ...

    def notify(self) -> None: ...

    def notifyAll(self) -> None: ...

    @staticmethod
    def out(message: object) -> None:
        """
        Useful for printing temporary messages without any logging markup.  This is meant to be
         a replacement for System.out.
        @param message the message to print
        """
        ...

    @staticmethod
    def setErrorDisplay(errDisplay: ghidra.util.ErrorDisplay) -> None:
        """
        Sets the error display (by default it's console)
        @param errDisplay the error display
        """
        ...

    @staticmethod
    def setErrorLogger(errLogger: ghidra.util.ErrorLogger) -> None:
        """
        Sets the error logger (by default it's a DefaultErrorLogger).
        @param errLogger the error logger
        """
        ...

    @overload
    @staticmethod
    def showError(originator: object, parent: java.awt.Component, title: unicode, message: object) -> None:
        """
        Used to display an error message with no available Throwable to the user
         with a pop-up GUI dialog. Also records the message to the logging system.
         If you have a Throwable, please use the other error(...) method.
        @param originator a Logger instance, "this", or YourClass.class
        @param parent a parent component used to center the dialog (or null if you
                    don't have one)
        @param title the title of the pop-up dialog (main subject of message)
        @param message the details of the message
        """
        ...

    @overload
    @staticmethod
    def showError(originator: object, parent: java.awt.Component, title: unicode, message: object, throwable: java.lang.Throwable) -> None:
        """
        Used to display an error message with a Throwable (for stack trace) to
         the user with a pop-up GUI dialog. Also records the message to the
         logging system.
        @param originator a Logger instance, "this", or YourClass.class
        @param parent a parent component used to center the dialog (or null if you
                    don't have one)
        @param title the title of the pop-up dialog (main subject of message)
        @param message the details of the message
        @param throwable the Throwable that describes the cause of the error
        """
        ...

    @staticmethod
    def showInfo(originator: object, parent: java.awt.Component, title: unicode, message: object) -> None:
        """
        Used to display an informational message to the user
         with a pop-up GUI dialog. Also records the message to the logging system.
        @param originator a Logger instance, "this", or YourClass.class
        @param parent a parent component used to center the dialog (or null if you
                    don't have one)
        @param title the title of the pop-up dialog (main subject of message)
        @param message the details of the message
        """
        ...

    @staticmethod
    def showWarn(originator: object, parent: java.awt.Component, title: unicode, message: object) -> None:
        """
        Used to display a warning message to the user with a pop-up GUI dialog.
         Also records the message to the logging system.
        @param originator a Logger instance, "this", or YourClass.class
        @param parent a parent component used to center the dialog (or null if you
                    don't have one)
        @param title the title of the pop-up dialog (main subject of message)
        @param message the details of the message
        """
        ...

    def toString(self) -> unicode: ...

    @overload
    @staticmethod
    def trace(originator: object, message: object) -> None:
        """
        Used to record a trace message to the log file. All calls to this method
         outside of main methods and JUnit tests will be removed before a
         production release.
        @param originator a Logger instance, "this", or YourClass.class
        @param message the details of the message
        """
        ...

    @overload
    @staticmethod
    def trace(originator: object, message: object, throwable: java.lang.Throwable) -> None:
        """
        Used to record a trace message to the log file. All calls to this method
         outside of main methods and JUnit tests will be removed before a
         production release. This may be used to document an exception
         without elevating that exception to error or warning status.
        @param originator a Logger instance, "this", or YourClass.class
        @param message the details of the message
        @param throwable the Throwable that describes the cause of the error
        """
        ...

    @overload
    def wait(self) -> None: ...

    @overload
    def wait(self, __a0: long) -> None: ...

    @overload
    def wait(self, __a0: long, __a1: int) -> None: ...

    @overload
    @staticmethod
    def warn(originator: object, message: object) -> None:
        """
        Used to display a warning message to the user via the console (no GUI).
         Also records the message to the logging system.
        @param originator a Logger instance, "this", or YourClass.class
        @param message the details of the message
        """
        ...

    @overload
    @staticmethod
    def warn(originator: object, message: object, throwable: java.lang.Throwable) -> None:
        """
        Used to display a warning message to the user via the console (no GUI).
         Also records the message to the logging system.
        @param originator a Logger instance, "this", or YourClass.class
        @param message the details of the message
        @param throwable a Throwable for printing a stack trace
        """
        ...
