import ghidra.app.util.demangler
import java.lang


class Demangled(object):
    """
    A unifying top-level interface for all DemangledObjects and DemangledTypes

     This class and its children have many overlapping concepts that we wish to refine at a
     future date.  Below is a listing of known uses:


     			MethodDescription



     			#getName()


     			A 'safe' name that is the #getDemangledName(), but with some characters
     			changed to be valid for use within Ghidra.




     			#getDemangledName()


     			The unmodified name that was set upon this object.




     			#getNamespaceName()


     			The 'safe' name of this object when it is used as a namespace name.   This usually has
     			parameter and template information.  Further, some characters within templates and
     			function signatures are replaced, such as spaces and namespace separators.

     			Given this full demangled string: , this method will return
     			.




     			#getNamespaceString()


     			This returns the unmodified name of this item, along with any unmodified parent
     			namespace names, all separated by a namespace delimiter.  Unlike
     			#getNamespaceName(), the spaces and internal namespace tokens will not be
     			replaced.

     			Given this full demangled string: , this method will return
     			.




     			#getSignature()


     			Returns the complete string form of this object, with most known attributes.  For
     			functions, this will be a complete signature.




     			#getOriginalDemangled()


     			The original unmodified demangled string.  This is the full demangled string returned
              from the demangling service.



    """









    def equals(self, __a0: object) -> bool: ...

    def getClass(self) -> java.lang.Class: ...

    def getDemangledName(self) -> unicode:
        """
        Returns the unmodified demangled name of this object. This name may contain whitespace
         and other characters not supported for symbol or data type creation.  See {@link #getName()}
         for the same name modified for use within Ghidra.
        @return name of this DemangledObject
        """
        ...

    def getMangledString(self) -> unicode:
        """
        Returns the original mangled string
        @return the string
        """
        ...

    def getName(self) -> unicode:
        """
        Returns the demangled name of this object.
         NOTE: unsupported symbol characters, like whitespace, will be converted to an underscore.
        @return name of this DemangledObject with unsupported characters converted to underscore
        @see #getDemangledName()
        """
        ...

    def getNamespace(self) -> ghidra.app.util.demangler.Demangled:
        """
        Returns the namespace containing this demangled object
        @return the namespace containing this demangled object
        """
        ...

    def getNamespaceName(self) -> unicode:
        """
        Returns this object's namespace name without the fully-qualified parent path. The
         value returned here may have had some special characters replaced, such as ' ' replaced
         with '_' and '::' replaced with '--'.
        @return the name
        """
        ...

    def getNamespaceString(self) -> unicode:
        """
        Returns a representation of this object as fully-qualified namespace.  The
         value returned here may have had some special characters replaced, such as ' ' replaced
         with '_' and '::' replaced with '--'.
        @return the full namespace
        """
        ...

    def getOriginalDemangled(self) -> unicode:
        """
        Returns the original demangled string returned by the demangling service
        @return the original demangled string
        """
        ...

    def getSignature(self) -> unicode:
        """
        Generates a complete representation of this object to include all know attributes of this
         object
        @return the signature
        """
        ...

    def hashCode(self) -> int: ...

    def notify(self) -> None: ...

    def notifyAll(self) -> None: ...

    def setName(self, name: unicode) -> None:
        """
        Sets the name for this object
        @param name the name
        """
        ...

    def setNamespace(self, ns: ghidra.app.util.demangler.Demangled) -> None:
        """
        Sets the namespace of this demangled object
        @param ns the namespace
        """
        ...

    def toString(self) -> unicode: ...

    @overload
    def wait(self) -> None: ...

    @overload
    def wait(self, __a0: long) -> None: ...

    @overload
    def wait(self, __a0: long, __a1: int) -> None: ...

    @property
    def demangledName(self) -> unicode: ...

    @property
    def mangledString(self) -> unicode: ...

    @property
    def name(self) -> unicode: ...

    @name.setter
    def name(self, value: unicode) -> None: ...

    @property
    def namespace(self) -> ghidra.app.util.demangler.Demangled: ...

    @namespace.setter
    def namespace(self, value: ghidra.app.util.demangler.Demangled) -> None: ...

    @property
    def namespaceName(self) -> unicode: ...

    @property
    def namespaceString(self) -> unicode: ...

    @property
    def originalDemangled(self) -> unicode: ...

    @property
    def signature(self) -> unicode: ...
