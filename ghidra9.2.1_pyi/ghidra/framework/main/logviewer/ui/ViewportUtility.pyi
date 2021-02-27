import ghidra.framework.main.logviewer.model
import ghidra.framework.main.logviewer.ui
import java.lang
import java.util
import javax.swing


class ViewportUtility(object, java.util.Observer):
    """
    Utility class for managing the viewport in the FVTable. This viewport must be
     adjusted manually whenever Chunk objects are added to or removed from to the view,
     or whenever the FVSlider is moved.
    """





    def __init__(self, eventListener: ghidra.framework.main.logviewer.event.FVEventListener): ...



    def equals(self, __a0: object) -> bool: ...

    def getClass(self) -> java.lang.Class: ...

    def getHeight(self) -> int:
        """
        Returns the height (in pixels) of the viewport.
        @return
        """
        ...

    def getNumRowsInViewport(self) -> int:
        """
        Returns the number of rows that are visible in the viewport.
        @return
        """
        ...

    def getViewportPositionAsRow(self) -> int:
        """
        Returns the table row associated with the top of the viewport.
        @return
        """
        ...

    def hashCode(self) -> int: ...

    def isInViewport(self, row: int) -> bool:
        """
        Returns true if the given row is in the viewport.
        @param row
        @return
        """
        ...

    def moveViewportDown(self, rows: int, selection: bool) -> None:
        """
        Moves the viewport down the number of rows specified. If moving down puts he view below
         the bounds of the first-visible chunk, load the next chunk.
        @param rows
        @param selection
        """
        ...

    def moveViewportToBottom(self) -> None:
        """
        Snaps the viewport to the bottom of the table.
        """
        ...

    def moveViewportToTop(self) -> None:
        """
        Snaps the viewport to the top of the table.
        """
        ...

    def moveViewportUp(self, rows: int, selection: bool) -> None:
        """
        Moves the viewport up the number of rows specified. If moving up puts he view above
         the bounds of the first-visible chunk, load a previous chunk.
        @param rows
        @param selection
        """
        ...

    def notify(self) -> None: ...

    def notifyAll(self) -> None: ...

    def scrollViewportTo(self, row: int) -> None:
        """
        Moves the viewport (top) to the given row in the current view.
        @param row
        """
        ...

    def setModel(self, model: ghidra.framework.main.logviewer.model.ChunkModel) -> None:
        """
        @param model
        """
        ...

    def setReader(self, reader: ghidra.framework.main.logviewer.model.ChunkReader) -> None:
        """
        @param reader
        """
        ...

    def setTable(self, table: ghidra.framework.main.logviewer.ui.FVTable) -> None:
        """
        @param table
        """
        ...

    def setViewport(self, viewport: javax.swing.JViewport) -> None:
        """
        @param viewport
        """
        ...

    def toString(self) -> unicode: ...

    def update(self, o: java.util.Observable, arg: object) -> None:
        """
        @param o
        @param arg
        """
        ...

    @overload
    def wait(self) -> None: ...

    @overload
    def wait(self, __a0: long) -> None: ...

    @overload
    def wait(self, __a0: long, __a1: int) -> None: ...

    @property
    def height(self) -> int: ...

    @property
    def model(self) -> None: ...  # No getter available.

    @model.setter
    def model(self, value: ghidra.framework.main.logviewer.model.ChunkModel) -> None: ...

    @property
    def numRowsInViewport(self) -> int: ...

    @property
    def reader(self) -> None: ...  # No getter available.

    @reader.setter
    def reader(self, value: ghidra.framework.main.logviewer.model.ChunkReader) -> None: ...

    @property
    def table(self) -> None: ...  # No getter available.

    @table.setter
    def table(self, value: ghidra.framework.main.logviewer.ui.FVTable) -> None: ...

    @property
    def viewport(self) -> None: ...  # No getter available.

    @viewport.setter
    def viewport(self, value: javax.swing.JViewport) -> None: ...

    @property
    def viewportPositionAsRow(self) -> int: ...
