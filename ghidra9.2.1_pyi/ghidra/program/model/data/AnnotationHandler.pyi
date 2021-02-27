from typing import List
import ghidra.program.model.data
import ghidra.util.classfinder
import java.lang


class AnnotationHandler(ghidra.util.classfinder.ExtensionPoint, object):
    """
    NOTE:  ALL AnnotationHandler CLASSES MUST END IN "AnnotationHandler".  If not,
     the ClassSearcher will not find them.

     AnnotationHandlers provide prefix/suffix information for various datatypes
     for specific C-like languages.
    """









    def equals(self, __a0: object) -> bool: ...

    def getClass(self) -> java.lang.Class: ...

    def getDescription(self) -> unicode:
        """
        Returns the description of the specific handler
        @return the description of the specific handler
        """
        ...

    def getFileExtensions(self) -> List[unicode]:
        """
        Returns an array of known extensions for the output file type.  If no extensions are
         preferred, the an empty array should be returned.
        @return an array of known extensions for the output file type.
        """
        ...

    def getLanguageName(self) -> unicode:
        """
        Returns the name of the C-like language that this handler supports
        @return the name of the C-like language that this handler supports
        """
        ...

    @overload
    def getPrefix(self, e: ghidra.program.model.data.Enum, member: unicode) -> unicode:
        """
        Returns the prefix for type Enum
        @param e the Enum datatype
        @param member the name of the member of the Enum
        @return the prefix for type Enum
        """
        ...

    @overload
    def getPrefix(self, c: ghidra.program.model.data.Composite, dtc: ghidra.program.model.data.DataTypeComponent) -> unicode:
        """
        Returns the prefix for type Composite
        @param c the Composite datatype
        @param dtc the name of the member of the Composite
        @return the prefix for type Composite
        """
        ...

    @overload
    def getSuffix(self, e: ghidra.program.model.data.Enum, member: unicode) -> unicode:
        """
        Returns the suffix for type Enum
        @param e the Enum datatype
        @param member the name of the member of the Enum
        @return the suffix for type Enum
        """
        ...

    @overload
    def getSuffix(self, c: ghidra.program.model.data.Composite, dtc: ghidra.program.model.data.DataTypeComponent) -> unicode:
        """
        Returns the suffix for type Composite
        @param c the Composite datatype
        @param dtc the name of the member of the Composite
        @return the suffix for type Composite
        """
        ...

    def hashCode(self) -> int: ...

    def notify(self) -> None: ...

    def notifyAll(self) -> None: ...

    def toString(self) -> unicode:
        """
        Returns a string description of this handler.
        @return a string description of this handler
        """
        ...

    @overload
    def wait(self) -> None: ...

    @overload
    def wait(self, __a0: long) -> None: ...

    @overload
    def wait(self, __a0: long, __a1: int) -> None: ...

    @property
    def description(self) -> unicode: ...

    @property
    def fileExtensions(self) -> List[unicode]: ...

    @property
    def languageName(self) -> unicode: ...
