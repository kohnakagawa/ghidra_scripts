from typing import List
import ghidra.util.classfinder
import ghidra.util.task
import java.lang
import java.util.function
import javax.swing.event


class ClassSearcher(object):
    """
    This class is a collection of static methods used to discover classes that implement a
     particular interface or extend a particular base class.

     Warning: Using the search feature of this class will trigger other classes to be loaded.
     Thus, clients should not make calls to this class inside of static initializer blocks

     Note: if your application is not using a module structure for its release build, then
     your application must create the following file, with the required entries,
     in order to find extension points:

     	install dir/data/ExtensionPoint.manifest

    """

    SEARCH_ALL_JARS_PROPERTY: unicode = u'class.searcher.search.all.jars'







    @staticmethod
    def addChangeListener(l: javax.swing.event.ChangeListener) -> None:
        """
        Add a change listener that will be notified when the classpath
         is searched for new classes.
         <p><strong>Note:</strong> The listener list is implemented
         using WeakReferences. Therefore, the caller must maintain a handle to
         the listener being added, or else it will be garbage collected and
         never called.</p>
        @param l the listener to add
        """
        ...

    def equals(self, __a0: object) -> bool: ...

    def getClass(self) -> java.lang.Class: ...

    @overload
    @staticmethod
    def getClasses(c: java.lang.Class) -> List[java.lang.Class]:
        """
        Get {@link ExtensionPointProperties#priority() priority-sorted} classes that implement or
         derive from the given class
        @param c the filter class
        @return set of classes that implement or extend T
        """
        ...

    @overload
    @staticmethod
    def getClasses(c: java.lang.Class, classFilter: java.util.function.Predicate) -> List[java.lang.Class]:
        """
        Get {@link ExtensionPointProperties#priority() priority-sorted} classes that
         implement or derive from the given class
        @param c the filter class
        @param classFilter A Predicate that tests class objects (that are already of type T)
         			for further filtering, <code>null</code> is equivalent to "return true"
        @return {@link ExtensionPointProperties#priority() priority-sorted} list of
         			classes that implement or extend T and pass the filtering test performed by the
         			predicate
        """
        ...

    @overload
    @staticmethod
    def getInstances(c: java.lang.Class) -> List[object]: ...

    @overload
    @staticmethod
    def getInstances(c: java.lang.Class, filter: ghidra.util.classfinder.ClassFilter) -> List[object]:
        """
        Get {@link ExtensionPointProperties#priority() priority-sorted} classes
         instances that implement or derive from the given class
        @param c the filter class
        @param filter A Predicate that tests class objects (that are already of type T)
         			for further filtering, <code>null</code> is equivalent to "return true"
        @return {@link ExtensionPointProperties#priority() priority-sorted} list of
         			classes instances that implement or extend T and pass the filtering test performed by
                  the predicate
        """
        ...

    def hashCode(self) -> int: ...

    def notify(self) -> None: ...

    def notifyAll(self) -> None: ...

    @staticmethod
    def removeChangeListener(l: javax.swing.event.ChangeListener) -> None:
        """
        Remove the change listener
        @param l the listener to remove
        """
        ...

    @staticmethod
    def search(forceRefresh: bool, monitor: ghidra.util.task.TaskMonitor) -> None:
        """
        Searches the classpath and updates the list of available classes which
         satisfy the class filter.  Classes which
         data types, and language providers. When the search completes and was
         not cancelled, the change listeners are notified.
        @param forceRefresh if true the class cache is ignored and the search is performed
         		  from scratch.
        @param monitor the progress monitor for the search.
        @throws CancelledException if the operation is cancelled
        """
        ...

    def toString(self) -> unicode: ...

    @overload
    def wait(self) -> None: ...

    @overload
    def wait(self, __a0: long) -> None: ...

    @overload
    def wait(self, __a0: long, __a1: int) -> None: ...
