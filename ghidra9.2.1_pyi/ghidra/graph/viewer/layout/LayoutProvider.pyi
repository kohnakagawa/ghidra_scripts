import ghidra.graph
import ghidra.graph.viewer.layout
import ghidra.util.classfinder
import ghidra.util.task
import java.lang
import javax.swing


class LayoutProvider(ghidra.util.classfinder.ExtensionPoint, object):
    """
    A layout provider creates VisualGraphLayout instances.  This class provides a name
     and icon for use in a UI.  These features can be used to create a menu of layouts that may
     be applied.

     The pattern of usage for this class is for it to create the layout that it represents and
     then to apply the locations of that layout to the vertices (and edges, in the case of
     articulating edges) of the graph before returning the new layout.
    """









    def equals(self, __a0: object) -> bool: ...

    def getActionIcon(self) -> javax.swing.Icon:
        """
        Returns an icon that can be used to show the provider a menu or toolbar.  This may
         return null, as an icon is not a requirement.
        @return an icon that can be used to show the provider a menu or toolbar
        """
        ...

    def getClass(self) -> java.lang.Class: ...

    def getLayout(self, __a0: ghidra.graph.VisualGraph, __a1: ghidra.util.task.TaskMonitor) -> ghidra.graph.viewer.layout.VisualGraphLayout: ...

    def getLayoutName(self) -> unicode:
        """
        Returns the name of this layout
        @return the name of this layout
        """
        ...

    def getPriorityLevel(self) -> int:
        """
        Returns an arbitrary value that is relative to other LayoutProviders.  The higher the
         value the more preferred the provider will be over other providers.
        @return the priority
        """
        ...

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
    def actionIcon(self) -> javax.swing.Icon: ...

    @property
    def layoutName(self) -> unicode: ...

    @property
    def priorityLevel(self) -> int: ...
