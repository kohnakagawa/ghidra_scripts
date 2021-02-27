from typing import List
import java.awt
import java.io
import java.lang
import java.util.function


class SystemUtilities(object):
    """
    General purpose class to provide convenience methods for doing "System" type
     stuff, e.g., find resources, date/time, etc. All methods in this class are
     static.
    """

    FONT_SIZE_OVERRIDE_PROPERTY_NAME: unicode = u'font.size.override'
    HEADLESS_PROPERTY: unicode = u'SystemUtilities.isHeadless'
    SINGLE_JAR_MODE_PROPERTY: unicode = u'SystemUtilities.isSingleJarMode'
    TESTING_BATCH_PROPERTY: unicode = u'ghidra.test.property.batch.mode'
    TESTING_PROPERTY: unicode = u'SystemUtilities.isTesting'



    def __init__(self): ...



    @staticmethod
    def adjustForFontSizeOverride(font: java.awt.Font) -> java.awt.Font:
        """
        Checks to see if the font size override setting is enabled and adjusts
         the given font as necessary to match the override setting. If the setting
         is not enabled, then <code>font</code> is returned.
        @param font The current font to adjust, if necessary.
        @return a font object with the proper size.
        """
        ...

    @staticmethod
    def assertThisIsTheSwingThread(errorMessage: unicode) -> None:
        """
        A development/testing time method to make sure the current thread is the swing thread.
        @param errorMessage The message to display when the assert fails
        """
        ...

    @staticmethod
    def assertTrue(booleanValue: bool, string: unicode) -> None: ...

    @staticmethod
    def compareTo(__a0: java.lang.Comparable, __a1: java.lang.Comparable) -> int: ...

    def equals(self, __a0: object) -> bool: ...

    @staticmethod
    def getBooleanProperty(name: unicode, defaultValue: bool) -> bool:
        """
        Gets the boolean value of the  system property by the given name.  If the property is
         not set, the defaultValue is returned.   If the value is set, then it will be passed
         into {@link Boolean#parseBoolean(String)}.
        @param name the property name to check
        @param defaultValue the default value
        @return true if the property is set and has a value of 'true', ignoring case
        """
        ...

    def getClass(self) -> java.lang.Class: ...

    @staticmethod
    def getDefaultThreadPoolSize() -> int:
        """
        Returns the default size (in number of threads) for a <b>CPU processing bound</b>
         thread pool.
        @return the default pool size.
        """
        ...

    @staticmethod
    def getFontSizeOverrideValue() -> int:
        """
        Returns a non-null value if the system property is set that triggers the
         font override setting, which makes all Java and Ghidra component fonts
         the same size.
        @return a non-null value if the system property is set that triggers the
                 font override setting, which makes all Java and Ghidra component
                 fonts the same size.
        @see #FONT_SIZE_OVERRIDE_PROPERTY_NAME
        """
        ...

    @staticmethod
    def getSourceLocationForClass(classObject: java.lang.Class) -> java.io.File:
        """
        Returns a file that contains the given class. If the class is in a jar file, then
         the jar file will be returned. If the file is in a .class file, then the directory
         containing the package root will be returned (i.e. the "bin" directory).
        @param classObject the class for which to get the location
        @return the containing location
        """
        ...

    @staticmethod
    def getUserName() -> unicode:
        """
        Get the user that is running the ghidra application
        @return the user name
        """
        ...

    def hashCode(self) -> int: ...

    @staticmethod
    def isArrayEqual(array1: List[object], array2: List[object]) -> bool: ...

    @staticmethod
    def isEqual(o1: object, o2: object) -> bool:
        """
        Returns whether or not the two indicated objects are equal. It allows
         either or both of the specified objects to be null.
        @param o1 the first object or null
        @param o2 the second object or null
        @return true if the objects are equal.
        """
        ...

    @staticmethod
    def isEventDispatchThread() -> bool:
        """
        Returns true if this is the event dispatch thread. Note that this method returns true in
         headless mode because any thread in headless mode can dispatch its own events. In swing
         environments, the swing thread is usually used to dispatch events.
        @return true if this is the event dispatch thread -OR- is in headless mode.
        """
        ...

    @staticmethod
    def isInDevelopmentMode() -> bool:
        """
        Returns true if we are running in development mode. The assumption is
         that if this class is in a jar file, then we are in production mode.
        @return true if we are running in development mode
        """
        ...

    @staticmethod
    def isInHeadlessMode() -> bool:
        """
        Returns true if the system is running without a GUI.
        @return true if the system is running without a GUI.
        """
        ...

    @staticmethod
    def isInReleaseMode() -> bool:
        """
        Returns true if the application is a release and not in development or testing
        @return true if the application is a release and not in development or testing
        """
        ...

    @staticmethod
    def isInTestingBatchMode() -> bool:
        """
        Returns true if the system is running during a batch, automated test.
        @return true if the system is running during a batch, automated test.
        """
        ...

    @staticmethod
    def isInTestingMode() -> bool:
        """
        Returns true if the system is running during a test.
        @return true if the system is running during a test.
        """
        ...

    def notify(self) -> None: ...

    def notifyAll(self) -> None: ...

    @staticmethod
    def printString(string: unicode, printStream: java.io.PrintStream) -> bool:
        """
        A debugging utility that allows you to create a conditional breakpoint in Eclipse that
         will print items for you while it is performing its tests.  This method always returns
         false.  This means to use it you will have to OR (||) your conditional breakpoint
         expressions if you want them to pass.  Otherwise, you can make this method be the
         only breakpoint expression and it will never stop on the breakpoint, but will still
         print your debug.
         <p>
         This method is useful to print values of code that you cannot edit while debugging.
         <p>
         Example, inside of your conditional breakpoint for a method on a Sun Java file you
         can put something like: <code>printString("Value of first arg: " + arg0, System.err)</code>
         <p>
         Note: Don't remove this method simply because no code is referencing it, as it is used
         by conditional breakpoints.
        @param string The string to print
        @param printStream The stream to print to (System.our or err)
        @return The string passed in so that you can use this method in an evaluation
        """
        ...

    @staticmethod
    def runIfSwingOrPostSwingLater(r: java.lang.Runnable) -> None: ...

    @staticmethod
    def runSwingLater(r: java.lang.Runnable) -> None:
        """
        Calls the given runnable on the Swing thread in the future by putting the request on
         the back of the event queue.
        @param r the runnable
        """
        ...

    @overload
    @staticmethod
    def runSwingNow(r: java.lang.Runnable) -> None:
        """
        Calls the given runnable on the Swing thread.
        @param r the runnable
        @see #runSwingNow(Supplier) if you need to return a value from the Swing thread.
        """
        ...

    @overload
    @staticmethod
    def runSwingNow(s: java.util.function.Supplier) -> object:
        """
        Calls the given suppler on the Swing thread, blocking with a
         {@link SwingUtilities#invokeAndWait(Runnable)}.  Use this method when you need to get
         a value while being on the Swing thread.

         <pre>{@literal
         		String value = runSwingNow(() -> label.getText());
         }</pre>
        @param s the supplier that will be called on the Swing thread
        @return the result of the supplier
        @see #runSwingNow(Runnable)
        """
        ...

    def toString(self) -> unicode: ...

    @overload
    def wait(self) -> None: ...

    @overload
    def wait(self, __a0: long) -> None: ...

    @overload
    def wait(self, __a0: long, __a1: int) -> None: ...
