from typing import List
import ghidra.xml
import java.lang


class ThreadedXmlPullParserImpl(ghidra.xml.AbstractXmlPullParser):
    """
    Constructs a new XML parser. This is class is designed for reading XML files.
     It is built on top of a ContentHandler. However, instead of being a "push"
     pattern, it has been translated into a "pull" pattern. That is, the user of
     this class can process the elements as needed. As well as skipping elements
     as needed.
    """





    def __init__(self): ...



    @overload
    def discardSubTree(self) -> int: ...

    @overload
    def discardSubTree(self, elementName: unicode) -> int: ...

    @overload
    def discardSubTree(self, element: ghidra.xml.XmlElement) -> int: ...

    def dispose(self) -> None:
        """
        Disposes this XML parser. No more elements may be read after dispose is
         called.
        """
        ...

    @overload
    def end(self) -> ghidra.xml.XmlElement: ...

    @overload
    def end(self, element: ghidra.xml.XmlElement) -> ghidra.xml.XmlElement: ...

    def equals(self, __a0: object) -> bool: ...

    def getClass(self) -> java.lang.Class: ...

    def getColumnNumber(self) -> int: ...

    def getCurrentLevel(self) -> int: ...

    def getLineNumber(self) -> int: ...

    def getName(self) -> unicode: ...

    def getProcessingInstruction(self, piName: unicode, attribute: unicode) -> unicode:
        """
        Returns the value of the attribute of the processing instruction. For
         example, <code>&lt;?program_dtd version="1"?&gt;</code>
        @param piName the name of the processing instruction
        @param attribute the name of the attribute
        @return the value of the attribute of the processing instruction
        """
        ...

    def hasNext(self) -> bool:
        """
        Returns true if the parser has more elements to read.
        @return true if the parser has more elements to read
        """
        ...

    def hashCode(self) -> int: ...

    def isPullingContent(self) -> bool: ...

    def next(self) -> ghidra.xml.XmlElement:
        """
        Returns the next element to be read and increments the iterator.
        @return the next element to be read and increments the iterator
        """
        ...

    def notify(self) -> None: ...

    def notifyAll(self) -> None: ...

    def peek(self) -> ghidra.xml.XmlElement:
        """
        Returns the next element to be read, but does not increment the iterator.
        @return the next element to be read, but does not increment the iterator
        """
        ...

    def setPullingContent(self, pullingContent: bool) -> None: ...

    def softStart(self, names: List[unicode]) -> ghidra.xml.XmlElement: ...

    def start(self, names: List[unicode]) -> ghidra.xml.XmlElement: ...

    def toString(self) -> unicode: ...

    @overload
    def wait(self) -> None: ...

    @overload
    def wait(self, __a0: long) -> None: ...

    @overload
    def wait(self, __a0: long, __a1: int) -> None: ...
