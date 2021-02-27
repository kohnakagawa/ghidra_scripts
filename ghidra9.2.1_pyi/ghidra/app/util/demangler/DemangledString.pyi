import ghidra.app.util.demangler
import ghidra.program.model.address
import ghidra.program.model.listing
import ghidra.program.model.symbol
import ghidra.util.task
import java.lang


class DemangledString(ghidra.app.util.demangler.DemangledObject):




    def __init__(self, mangled: unicode, originalDemangled: unicode, name: unicode, string: unicode, length: int, unicode: bool):
        """
        Construct demangled string.
        @param mangled the source mangled string
        @param originalDemangled the original demangled string
        @param name name associated with this object
        @param string string text associated with this object or null.  This is used to establish
         label and plate comment if specified.  If null, name will be used as symbol name.
        @param length length of string or -1.  Actual string data type applied currently
         assumes null terminated string.
        @param unicode true if string is a Unicode string.
        """
        ...



    def applyPlateCommentOnly(self, program: ghidra.program.model.listing.Program, address: ghidra.program.model.address.Address) -> bool:
        """
        @param program The program for which to apply the comment
        @param address The address for the comment
        @return {@code true} if a comment was applied
        """
        ...

    def applyTo(self, program: ghidra.program.model.listing.Program, address: ghidra.program.model.address.Address, options: ghidra.app.util.demangler.DemanglerOptions, monitor: ghidra.util.task.TaskMonitor) -> bool: ...

    @staticmethod
    def createNamespace(program: ghidra.program.model.listing.Program, typeNamespace: ghidra.app.util.demangler.Demangled, parentNamespace: ghidra.program.model.symbol.Namespace, functionPermitted: bool) -> ghidra.program.model.symbol.Namespace:
        """
        Get or create the specified typeNamespace.  The returned namespace may only be a partial
         namespace if errors occurred.  The caller should check the returned namespace and adjust
         any symbol creation accordingly.
        @param program the program
        @param typeNamespace demangled namespace
        @param parentNamespace root namespace to be used (e.g., library, global, etc.)
        @param functionPermitted if true an existing function may be used as a namespace
        @return namespace or partial namespace if error occurs
        """
        ...

    def equals(self, __a0: object) -> bool: ...

    def getBasedName(self) -> unicode: ...

    def getClass(self) -> java.lang.Class: ...

    def getDemangledName(self) -> unicode: ...

    def getLength(self) -> int:
        """
        Returns the length in bytes of the demangled string.
        @return the length in bytes of the demangled string
        """
        ...

    def getMangledString(self) -> unicode: ...

    def getMemberScope(self) -> unicode: ...

    def getName(self) -> unicode: ...

    def getNamespace(self) -> ghidra.app.util.demangler.Demangled: ...

    def getNamespaceName(self) -> unicode: ...

    def getNamespaceString(self) -> unicode: ...

    def getOriginalDemangled(self) -> unicode: ...

    @overload
    def getSignature(self) -> unicode: ...

    @overload
    def getSignature(self, format: bool) -> unicode: ...

    def getSpecialPrefix(self) -> unicode: ...

    def getStorageClass(self) -> unicode: ...

    def getString(self) -> unicode:
        """
        Returns the demangled string.
        @return the demangled string
        """
        ...

    def getVisibility(self) -> unicode: ...

    def hashCode(self) -> int: ...

    def isConst(self) -> bool: ...

    def isPointer64(self) -> bool: ...

    def isRestrict(self) -> bool: ...

    def isStatic(self) -> bool: ...

    def isThunk(self) -> bool: ...

    def isUnaligned(self) -> bool: ...

    def isUnicode(self) -> bool:
        """
        Returns true if the demangled string is unicode.
        @return true if the demangled string is unicode
        """
        ...

    def isVirtual(self) -> bool: ...

    def isVolatile(self) -> bool: ...

    def notify(self) -> None: ...

    def notifyAll(self) -> None: ...

    def setBasedName(self, basedName: unicode) -> None: ...

    def setConst(self, isConst: bool) -> None: ...

    def setMemberScope(self, memberScope: unicode) -> None: ...

    def setName(self, name: unicode) -> None:
        """
        Sets the name of the demangled object
        @param name the new name
        """
        ...

    def setNamespace(self, namespace: ghidra.app.util.demangler.Demangled) -> None: ...

    def setPointer64(self, isPointer64: bool) -> None: ...

    def setRestrict(self) -> None: ...

    def setSignature(self, signature: unicode) -> None:
        """
        Sets the signature. Calling this method will
         override the auto-generated signature.
        @param signature the signature
        """
        ...

    def setSpecialPrefix(self, special: unicode) -> None: ...

    def setStatic(self, isStatic: bool) -> None: ...

    def setStorageClass(self, storageClass: unicode) -> None: ...

    def setThunk(self, isThunk: bool) -> None: ...

    def setUnaligned(self) -> None: ...

    def setVirtual(self, isVirtual: bool) -> None: ...

    def setVisibilty(self, visibility: unicode) -> None: ...

    def setVolatile(self, isVolatile: bool) -> None: ...

    def toString(self) -> unicode: ...

    @overload
    def wait(self) -> None: ...

    @overload
    def wait(self, __a0: long) -> None: ...

    @overload
    def wait(self, __a0: long, __a1: int) -> None: ...

    @property
    def length(self) -> int: ...

    @property
    def string(self) -> unicode: ...

    @property
    def unicode(self) -> bool: ...