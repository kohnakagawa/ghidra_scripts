from typing import List
import ghidra.docking.settings
import ghidra.util.exception
import ghidra.util.table.column
import ghidra.util.table.column.GColumnRenderer
import java.awt
import java.lang
import javax.swing
import javax.swing.table


class GColumnRenderer(javax.swing.table.TableCellRenderer, object):
    """
    An interface for the DynamicTableColumn.  This allows the filtering system to stay
     in sync with the rendering system by using the display text to filter.

     Table filtering in GTables typically works with the following setup:

     	The table has a text field that allows for quick filtering across all visible
          columns.  The specifics of how the text filter works are defined by the
          RowFilterTransformer, which is controlled by the user via the button at the right
          of the filter field.  (In the absence of this button, filters are typically a 'contains'
          filter.)

          The default transformer turns items to strings by, in order,:

          	checking the the column renderer's
          		#getFilterString(Object, Settings),if a column renderer is installed

          	checking to see if the column value is an instance of DisplayStringProvider

          	checking to see if the column value is a JLabel

          	calling toString() on the object




      	The table has the ability to perform advanced filtering based upon specific columns.  Each
      	column's type is used to find dynamically discovered ColumnConstraints.  These
      	constraints dictate how a given column can be filtered.  The user will create filters
      	using these constraints in the ColumnFilterDialog by pressing the
      	button at the far right of the filter text field.

      	The way the constraints are used in the filtering system, in conjunction with
      	   this renderer, is defined by the ColumnConstraintFilterMode via
      	   #getColumnConstraintFilterMode().


      	Any custom filters, defined by individual clients (this is outside the scope of the
      	default filtering system)



     Note: The default filtering behavior of this class is to only filter on the aforementioned
           filter text field.  That is, column constraints will not be enabled by default. To
           change this, change the value returned by #getColumnConstraintFilterMode().
    """






    class ColumnConstraintFilterMode(java.lang.Enum):
        ALLOW_ALL_FILTERS: ghidra.util.table.column.GColumnRenderer.ColumnConstraintFilterMode = ALLOW_ALL_FILTERS
        ALLOW_CONSTRAINTS_FILTER_ONLY: ghidra.util.table.column.GColumnRenderer.ColumnConstraintFilterMode = ALLOW_CONSTRAINTS_FILTER_ONLY
        ALLOW_RENDERER_STRING_FILTER_ONLY: ghidra.util.table.column.GColumnRenderer.ColumnConstraintFilterMode = ALLOW_RENDERER_STRING_FILTER_ONLY







        @overload
        def compareTo(self, __a0: java.lang.Enum) -> int: ...

        @overload
        def compareTo(self, __a0: object) -> int: ...

        def equals(self, __a0: object) -> bool: ...

        def getClass(self) -> java.lang.Class: ...

        def getDeclaringClass(self) -> java.lang.Class: ...

        def hashCode(self) -> int: ...

        def name(self) -> unicode: ...

        def notify(self) -> None: ...

        def notifyAll(self) -> None: ...

        def ordinal(self) -> int: ...

        def toString(self) -> unicode: ...

        @overload
        @staticmethod
        def valueOf(__a0: unicode) -> ghidra.util.table.column.GColumnRenderer.ColumnConstraintFilterMode: ...

        @overload
        @staticmethod
        def valueOf(__a0: java.lang.Class, __a1: unicode) -> java.lang.Enum: ...

        @staticmethod
        def values() -> List[ghidra.util.table.column.GColumnRenderer.ColumnConstraintFilterMode]: ...

        @overload
        def wait(self) -> None: ...

        @overload
        def wait(self, __a0: long) -> None: ...

        @overload
        def wait(self, __a0: long, __a1: int) -> None: ...







    def createWrapperTypeException(self) -> ghidra.util.exception.AssertException:
        """
        A convenience method for primitive-based/wrapper-based renderers to signal that they
         should not be using text to filter.

         <P>The basic wrapper types, like Number, and some others, like {@link Date}, have special
         built-in filtering capabilities.  Columns whose column type is one of the wrapper classes
         will not have their {@link #getFilterString(Object, Settings)} methods called.  They can
         stub out those methods by throwing the exception returned by this method.
        @return the new exception
        @see AbstractWrapperTypeColumnRenderer
        """
        ...

    def equals(self, __a0: object) -> bool: ...

    def getClass(self) -> java.lang.Class: ...

    def getColumnConstraintFilterMode(self) -> ghidra.util.table.column.GColumnRenderer.ColumnConstraintFilterMode:
        """
        Returns the current mode of how column constraints will be used to filter this column

         <P>This method is typically not overridden.  This is only needed in rare cases, such as
         when a column uses a renderer, but does *not* want this column to be filtered using
         a String column constraint.   Or, if a column uses a renderer and wants that text to
         be available as a filter, along with any other column constraints.
        @return the mode
        """
        ...

    def getFilterString(self, t: object, settings: ghidra.docking.settings.Settings) -> unicode:
        """
        Returns a string that is suitable for use when filtering.  The returned String should
         be an unformatted (e.g., no HTML markup, icons, etc) version of what is on the screen.
         If the String returned here does not match what the user sees (that which is rendered),
         then the filtering action may confuse the user.
        @param t the column type instance
        @param settings any settings the converter may need to convert the type
        @return the unformatted String version of what is rendered in the table cell on screen
        """
        ...

    def getTableCellRendererComponent(self, __a0: javax.swing.JTable, __a1: object, __a2: bool, __a3: bool, __a4: int, __a5: int) -> java.awt.Component: ...

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
    def columnConstraintFilterMode(self) -> ghidra.util.table.column.GColumnRenderer.ColumnConstraintFilterMode: ...
