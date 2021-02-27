import docking
import ghidra.service.graph
import java.awt
import java.awt.event
import java.lang
import java.util


class VertexGraphActionContext(ghidra.service.graph.GraphActionContext):
    """
    GraphActionContext for when user invokes a popup action on a graph vertex.
    """





    def __init__(self, componentProvider: docking.ComponentProvider, graph: ghidra.service.graph.AttributedGraph, selectedVertices: java.util.Set, locatedVertex: ghidra.service.graph.AttributedVertex, clickedVertex: ghidra.service.graph.AttributedVertex): ...



    def equals(self, __a0: object) -> bool: ...

    def getClass(self) -> java.lang.Class: ...

    def getClickedVertex(self) -> ghidra.service.graph.AttributedVertex:
        """
        Returns the vertex from where the popup menu was launched
        @return the vertex from where the popup menu was launched
        """
        ...

    def getComponentProvider(self) -> docking.ComponentProvider:
        """
        Returns the {@link ComponentProvider} that generated this ActionContext
        @return the provider
        """
        ...

    def getContextObject(self) -> object:
        """
        Returns the object that was included by the ComponentProvider when this context was created.
        @return the object that was included by the ComponentProvider when this context was created.
        """
        ...

    def getFocusedVertex(self) -> ghidra.service.graph.AttributedVertex:
        """
        Returns the focused vertex (similar concept to the cursor in a text document)
        @return the focused vertex
        """
        ...

    def getGlobalContext(self) -> docking.ActionContext:
        """
        Returns the global action context for the tool.  The global context is the context of
         the default focused component, instead of the normal action context which is the current
         focused component.
        @return the global action context for the tool
        """
        ...

    def getGraph(self) -> ghidra.service.graph.AttributedGraph:
        """
        Returns the graph
        @return the graph
        """
        ...

    def getMouseEvent(self) -> java.awt.event.MouseEvent:
        """
        Returns the context's mouse event.  Contexts that are based upon key events will have no
         mouse event.
        @return the mouse event that triggered this context; null implies a key event-based context
        """
        ...

    def getSelectedVertices(self) -> java.util.Set:
        """
        Returns the set of selectedVertices in the graph
        @return the set of selectedVertices in the graph
        """
        ...

    def getSourceComponent(self) -> java.awt.Component:
        """
        Returns the component that is the target of this context.   This value should not change
         whether the context is triggered by a key binding or mouse event.
        @return the component; may be null
        """
        ...

    def getSourceObject(self) -> object:
        """
        Returns the sourceObject from the actionEvent that triggered this context to be generated.
        @return the sourceObject from the actionEvent that triggered this context to be generated.
        """
        ...

    def hashCode(self) -> int: ...

    def notify(self) -> None: ...

    def notifyAll(self) -> None: ...

    def setContextObject(self, contextObject: object) -> docking.ActionContext:
        """
        Sets the context object for this context.  This can be any object of the creator's
         choosing that can be provided for later retrieval.
        @param contextObject Sets the context object for this context.
        @return this context
        """
        ...

    def setMouseEvent(self, e: java.awt.event.MouseEvent) -> docking.ActionContext:
        """
        Updates the context's mouse event.  Contexts that are based upon key events will have no
         mouse event.   This method is really for the framework to use.  Client calls to this
         method will be overridden by the framework when menu items are clicked.
        @param e the event that triggered this context.
        @return this context
        """
        ...

    def setSourceObject(self, sourceObject: object) -> docking.ActionContext:
        """
        Sets the sourceObject for this ActionContext.  This method is used internally by the
         DockingWindowManager. ComponentProvider and action developers should only use this
         method for testing.
        @param sourceObject the source object
        @return this context
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
    def clickedVertex(self) -> ghidra.service.graph.AttributedVertex: ...
