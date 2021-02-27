import ghidra.framework.cmd
import ghidra.framework.model
import ghidra.program.model.symbol
import java.lang


class CreateNamespacesCmd(object, ghidra.framework.cmd.Command):
    """
    This class attempts to create a namespace for each token in the provided
     string.  Thus, when providing a namespace string, do not include the name
     of anything other than namespaces, such as the name of a symbol.


     Example strings:

         globalNamespace#DELIMITERchild1Namespace#DELIMITERchild2
         child1



     To view the assumptions for creating namespaces from a path string, see
     the NamespaceUtils class.
    """





    @overload
    def __init__(self, namespacesString: unicode, source: ghidra.program.model.symbol.SourceType):
        """
        Takes a namespace string that will be parsed and the results of which
         will be used for creating the namespaces if they do not exist.
         <p>
         Calling this constructor is equivalent to calling:
         <pre>
         Command command = new CreateNamespacesCmd( namespaceString, null );
         </pre>
        @param namespacesString The string to be parsed.
        @param source the source of the namespace
        @see <a href="#examples">example format</a>
        @see <a href="#assumptions">assumptions</a>
        """
        ...

    @overload
    def __init__(self, namespacesString: unicode, parentNamespace: ghidra.program.model.symbol.Namespace, source: ghidra.program.model.symbol.SourceType):
        """
        Takes a namespace string that will be parsed and the results of which
         will be used for creating the namespaces if they do not exist.
        @param namespacesString The string to be parsed.
        @param parentNamespace The namespace to be used as the starting parent
                of the namespaces that will be created.
        @param source the source of the namespace
        @throws NullPointerException if <code>namespaceString</code> is <code>null</code>.
        @see <a href="#examples">example format</a>
        @see <a href="#assumptions">assumptions</a>
        """
        ...



    def applyTo(self, obj: ghidra.framework.model.DomainObject) -> bool:
        """
        @see ghidra.framework.cmd.Command#applyTo(ghidra.framework.model.DomainObject)
        """
        ...

    def equals(self, __a0: object) -> bool: ...

    def getClass(self) -> java.lang.Class: ...

    def getName(self) -> unicode: ...

    def getNamespace(self) -> ghidra.program.model.symbol.Namespace:
        """
        Returns the newly created namespace or null if one was not created.
        @return the newly created namespace or null if one was not created.
        """
        ...

    def getStatusMsg(self) -> unicode: ...

    def hashCode(self) -> int: ...

    def notify(self) -> None: ...

    def notifyAll(self) -> None: ...

    def toString(self) -> unicode: ...

    @overload
    def wait(self) -> None: ...

    @overload
    def wait(self, __a0: long) -> None: ...

    @overload
    def wait(self, __a0: long, __a1: int) -> None: ...

    @property
    def name(self) -> unicode: ...

    @property
    def namespace(self) -> ghidra.program.model.symbol.Namespace: ...

    @property
    def statusMsg(self) -> unicode: ...
