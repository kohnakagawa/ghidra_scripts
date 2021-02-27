from typing import List
import ghidra.program.model.data
import java.lang


class CategoryPath(object, java.lang.Comparable):
    """
    A category path is the full path to a particular data type
    """

    DELIMITER_CHAR: int = '/'
    DELIMITER_STRING: unicode = u'/'
    ESCAPED_DELIMITER_STRING: unicode = u'\\/'
    ROOT: ghidra.program.model.data.CategoryPath = /



    @overload
    def __init__(self, path: unicode):
        """
        Creates a category path given a forward-slash-delimited string (e.g., {@code "/aa/bb"}).
         If an individual path component has one or more '/' characters in it, then it can be
         <I><B>escaped</B></I> using the {@link #escapeString(String)} utility method.  The
         {@link #unescapeString(String)} method can be used to unescape an individual component.
         <P>
         <B>Refrain</B> from using this constructor in production code, and instead use one of the
         other constructors that does not require escaping.  Situations where using this constructor
         is OK is in simple cases where a literal is passed in, such as in testing methods or in
         scripts.
        @param path category path string, delimited with '/' characters where individual components
         may have '/' characters escaped.  Must start with the '/' character.
        """
        ...

    @overload
    def __init__(self, parent: ghidra.program.model.data.CategoryPath, subPathElements: List[unicode]):
        """
        Construct a CategoryPath from a parent and a hierarchical array of strings where each
         string is the name of a category in the category path.
        @param parent the parent CategoryPath.  Choose {@code ROOT} if needed.
        @param subPathElements the array of names of sub-categories of the parent.
        @throws IllegalArgumentException if the given array is null or empty.
        """
        ...

    @overload
    def __init__(self, __a0: ghidra.program.model.data.CategoryPath, __a1: List[object]): ...



    def asArray(self) -> List[unicode]:
        """
        Returns a hierarchical array of names of the categories in the category path, starting with
         the name just below the {@code ROOT} category.
        @return a hierarchical array of names of the categories in the category path.
        """
        ...

    def asList(self) -> List[unicode]:
        """
        Returns a hierarchical list of names of the categories in the category path, starting with
         the name just below the {@code ROOT} category.
        @return a hierarchical list of names of the category in the category path.
        """
        ...

    @overload
    def compareTo(self, other: ghidra.program.model.data.CategoryPath) -> int: ...

    @overload
    def compareTo(self, __a0: object) -> int: ...

    def equals(self, obj: object) -> bool: ...

    @staticmethod
    def escapeString(nonEscapedString: unicode) -> unicode:
        """
        Converts a non-escaped String into an escaped string suitable for being passed in as a
         component of a single category path string to the constructor that takes a single
         escaped category path string.  The user is responsible for constructing the single
         category path string from the escaped components.
        @param nonEscapedString String that might need escaping for characters used for delimiting
        @return escaped String
        @see #unescapeString(String)
        """
        ...

    def getClass(self) -> java.lang.Class: ...

    def getName(self) -> unicode:
        """
        Return the terminating name of this category path.
        @return the name
        """
        ...

    def getParent(self) -> ghidra.program.model.data.CategoryPath:
        """
        Return the parent category path.
        @return the parent
        """
        ...

    def getPath(self) -> unicode:
        """
        Return the {@link String} representation of this category path including the category name,
         where components are delimited with a forward slash.  Any component that contains a forward
         slash will be have the forward slash characters escaped.
        @return the full category path
        """
        ...

    def getPathElements(self) -> List[unicode]:
        """
        Returns array of names in category path.
        @return array of names
        """
        ...

    def hashCode(self) -> int: ...

    def isAncestorOrSelf(self, candidateAncestorPath: ghidra.program.model.data.CategoryPath) -> bool:
        """
        Tests if the specified categoryPath is the same as, or an ancestor of, this category path.
        @param candidateAncestorPath the category path to be checked.
        @return true if the given path is the same as, or an ancestor of, this category path.
        """
        ...

    def isRoot(self) -> bool:
        """
        Determine if this category path corresponds to the root category
        @return true if this is a root category path
        """
        ...

    def notify(self) -> None: ...

    def notifyAll(self) -> None: ...

    def toString(self) -> unicode: ...

    @staticmethod
    def unescapeString(escapedString: unicode) -> unicode:
        """
        Converts an escaped String suitable for being passed in as a component of a single category
         path string into an non-escaped string.
        @param escapedString String that might need unescaping for characters used for delimiting
        @return non-escaped String
        @see #escapeString(String)
        """
        ...

    @overload
    def wait(self) -> None: ...

    @overload
    def wait(self, __a0: long) -> None: ...

    @overload
    def wait(self, __a0: long, __a1: int) -> None: ...

    @property
    def name(self) -> unicode: ...

    @property
    def parent(self) -> ghidra.program.model.data.CategoryPath: ...

    @property
    def path(self) -> unicode: ...

    @property
    def pathElements(self) -> List[unicode]: ...

    @property
    def root(self) -> bool: ...
