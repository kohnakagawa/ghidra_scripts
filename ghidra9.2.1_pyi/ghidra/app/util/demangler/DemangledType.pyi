import ghidra.app.util.demangler
import java.lang


class DemangledType(object, ghidra.app.util.demangler.Demangled):
    """
    Represents a demangled string.  This class is really just a placeholder for demangled
     information.  See DemangledObject for a class that represents software concepts that
     can be applied to a program.   The DemangledObject may use instances of this class
     to compose its internal state for namespace information, return types and parameters.
    """





    def __init__(self, mangled: unicode, originaDemangled: unicode, name: unicode): ...



    def equals(self, __a0: object) -> bool: ...

    def getClass(self) -> java.lang.Class: ...

    def getDemangledName(self) -> unicode: ...

    def getMangledString(self) -> unicode: ...

    def getName(self) -> unicode: ...

    def getNamespace(self) -> ghidra.app.util.demangler.Demangled: ...

    def getNamespaceName(self) -> unicode: ...

    def getNamespaceString(self) -> unicode: ...

    def getOriginalDemangled(self) -> unicode: ...

    def getSignature(self) -> unicode: ...

    def getTemplate(self) -> ghidra.app.util.demangler.DemangledTemplate: ...

    def hashCode(self) -> int: ...

    def isConst(self) -> bool: ...

    def isVolatile(self) -> bool: ...

    def notify(self) -> None: ...

    def notifyAll(self) -> None: ...

    def setConst(self) -> None: ...

    def setName(self, name: unicode) -> None: ...

    def setNamespace(self, namespace: ghidra.app.util.demangler.Demangled) -> None: ...

    def setTemplate(self, template: ghidra.app.util.demangler.DemangledTemplate) -> None: ...

    def setVolatile(self) -> None: ...

    def toString(self) -> unicode: ...

    @overload
    def wait(self) -> None: ...

    @overload
    def wait(self, __a0: long) -> None: ...

    @overload
    def wait(self, __a0: long, __a1: int) -> None: ...

    @property
    def const(self) -> bool: ...

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

    @property
    def template(self) -> ghidra.app.util.demangler.DemangledTemplate: ...

    @template.setter
    def template(self, value: ghidra.app.util.demangler.DemangledTemplate) -> None: ...

    @property
    def volatile(self) -> bool: ...
