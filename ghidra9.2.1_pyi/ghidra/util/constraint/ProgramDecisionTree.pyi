import generic.constraint
import generic.jar
import java.io
import java.lang


class ProgramDecisionTree(generic.constraint.DecisionTree):




    def __init__(self): ...



    def equals(self, __a0: object) -> bool: ...

    def getClass(self) -> java.lang.Class: ...

    def getDecisionsSet(self, testObject: object, propertyName: unicode) -> generic.constraint.DecisionSet:
        """
        Searches the decision tree for values of given property name that match the constraints
         within this tree.
        @param testObject the object that the constraints are test against.
        @param propertyName the name of the property whose values are being collected.
        @return a DecisionSet containing all the values of the given property whose path in the
         tree matched all the constraints for the given test object.
        """
        ...

    def hashCode(self) -> int: ...

    @overload
    def loadConstraints(self, file: generic.jar.ResourceFile) -> None:
        """
        Loads the tree from an xml constraint file. Note: this method can be called multiple times,
         with each call appending to the existing tree.
        @param file the file that contains the xml for the constraint.
        @throws IOException if an I/O problem occurs reading from the stream.
        @throws XmlParseException if the XML is not property formatted or a tag that is not
         a constraint name or property name is encountered.
        """
        ...

    @overload
    def loadConstraints(self, name: unicode, stream: java.io.InputStream) -> None:
        """
        Loads the tree from an xml data contained within an input stream. Note: this method can be
         called multiple times, with each call appending to the existing tree.
        @param name the name of the input source so that decisions can be traced back to
         the appropriate xml constraints source.
        @param stream the InputStream from which to read an xml constraints specification.
        @throws IOException if an I/O problem occurs reading from the stream.
        @throws XmlParseException if the XML is not property formatted or a tag that is not
         a constraint name or property name is encountered.
        """
        ...

    def notify(self) -> None: ...

    def notifyAll(self) -> None: ...

    def registerConstraintType(self, name: unicode, constraintClass: java.lang.Class) -> None:
        """
        Registers a constraint class to be recognized from an xml constraint specification file.
        @param name the name of the constraint which is also the xml tag value.
        @param constraintClass the constraint type which will be initialized from the xml constraint
         specification file.
        """
        ...

    def registerPropertyName(self, propertyName: unicode) -> None:
        """
        Registers a property name.  Every tag in an xml constraint file (except the root tag which
         is unused) must be either a constraint name or a property name.
        @param propertyName the name of a valid property to be expected in an xml constraints file.
        """
        ...

    def toString(self) -> unicode: ...

    @overload
    def wait(self) -> None: ...

    @overload
    def wait(self, __a0: long) -> None: ...

    @overload
    def wait(self, __a0: long, __a1: int) -> None: ...
