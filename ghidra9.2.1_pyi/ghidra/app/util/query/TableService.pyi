import ghidra.app.nav
import ghidra.app.plugin.core.table
import ghidra.app.tablechooser
import ghidra.program.model.listing
import ghidra.util.table
import java.awt
import java.lang
import javax.swing


class TableService(object):
    """
    Service to show a component that has a JTable given a table model
     that builds up its data dynamically (a ThreadedTableModel).
    """









    @overload
    def createTableChooserDialog(self, executor: ghidra.app.tablechooser.TableChooserExecutor, program: ghidra.program.model.listing.Program, name: unicode, navigatable: ghidra.app.nav.Navigatable) -> ghidra.app.tablechooser.TableChooserDialog: ...

    @overload
    def createTableChooserDialog(self, executor: ghidra.app.tablechooser.TableChooserExecutor, program: ghidra.program.model.listing.Program, name: unicode, navigatable: ghidra.app.nav.Navigatable, isModal: bool) -> ghidra.app.tablechooser.TableChooserDialog: ...

    def equals(self, __a0: object) -> bool: ...

    def getClass(self) -> java.lang.Class: ...

    def hashCode(self) -> int: ...

    def notify(self) -> None: ...

    def notifyAll(self) -> None: ...

    def showTable(self, componentProviderTitle: unicode, tableTypeName: unicode, model: ghidra.util.table.GhidraProgramTableModel, windowSubMenu: unicode, navigatable: ghidra.app.nav.Navigatable) -> ghidra.app.plugin.core.table.TableComponentProvider:
        """
        Creates a table view using the given model. This version does not create markers.
        @param componentProviderTitle The title of the view
        @param tableTypeName The name of the table's type.  This is used to group like tables
                together
        @param model the data model
        @param windowSubMenu the name of a sub-menu to use in the "windows" menu.
        @param navigatable the component to navigate.  If null, the "connected" components will
                navigate.
        @return a provider to show a visible component for the data
        """
        ...

    def showTableWithMarkers(self, componentProviderTitle: unicode, tableTypeName: unicode, model: ghidra.util.table.GhidraProgramTableModel, markerColor: java.awt.Color, markerIcon: javax.swing.ImageIcon, windowSubMenu: unicode, navigatable: ghidra.app.nav.Navigatable) -> ghidra.app.plugin.core.table.TableComponentProvider:
        """
        Creates a table view using the given model. This version creates markers.
        @param componentProviderTitle The title of the view
        @param tableTypeName The name of the table's type.  This is used to group like tables
                together
        @param model the data model
        @param markerColor the color to use for the marker
        @param markerIcon the icon to associate with the marker set.
        @param windowSubMenu the name of a sub-menu to use in the "windows" menu.
        @param navigatable the component to navigate.  If null, the "connected" components will
                navigate.
        @return a provider to show a visible component for the data
        """
        ...

    def toString(self) -> unicode: ...

    @overload
    def wait(self) -> None: ...

    @overload
    def wait(self, __a0: long) -> None: ...

    @overload
    def wait(self, __a0: long, __a1: int) -> None: ...
