from typing import List
import docking.widgets.fieldpanel.field
import ghidra.app.plugin.processors.sleigh.template
import ghidra.program.model.address
import ghidra.program.model.listing
import ghidra.program.model.pcode
import java.awt
import java.lang


class PcodeFormatter(object):




    def __init__(self):
        """
        Constructor
        """
        ...



    def equals(self, __a0: object) -> bool: ...

    def getClass(self) -> java.lang.Class: ...

    def getPcodeOpTemplates(self, addrFactory: ghidra.program.model.address.AddressFactory, pcodeOps: List[ghidra.program.model.pcode.PcodeOp]) -> List[ghidra.app.plugin.processors.sleigh.template.OpTpl]:
        """
        Convert flattened PcodeOp's into pcode operation templates.
        @param addrFactory
        @param pcodeOps
        @return pcode operation templates
        """
        ...

    def hashCode(self) -> int: ...

    def notify(self) -> None: ...

    def notifyAll(self) -> None: ...

    def setColor(self, addressColor: java.awt.Color, registerColor: java.awt.Color, scalarColor: java.awt.Color, localColor: java.awt.Color) -> None:
        """
        Set color options for AttributedString objects
        @param addressColor
        @param registerColor
        @param scalarColor
        @param localColor
        """
        ...

    def setFontMetrics(self, metrics: java.awt.FontMetrics) -> None:
        """
        Set font metrics for AttributedString objects
        @param metrics
        """
        ...

    def setOptions(self, maxDisplayLines: int, displayRawPcode: bool) -> None:
        """
        Set general formatting options
        @param maxDisplayLines
        @param displayRawPcode
        """
        ...

    @overload
    def toAttributedStrings(self, program: ghidra.program.model.listing.Program, pcodeOpTemplates: List[ghidra.app.plugin.processors.sleigh.template.OpTpl]) -> List[docking.widgets.fieldpanel.field.AttributedString]:
        """
        Format an array of pcode OpTpl objects as a list of AttributedString objects.
         The returned list contains a separate element for each row of the pcode listing.
        @param program
        @param pcodeOpTemplates
        @return pcode listing as a two-dimensional list of AttributedString objects
        """
        ...

    @overload
    def toAttributedStrings(self, program: ghidra.program.model.listing.Program, pcodeOps: List[ghidra.program.model.pcode.PcodeOp]) -> List[docking.widgets.fieldpanel.field.AttributedString]:
        """
        Format an array of PcodeOp objects as a two-dimensional list of AttributedString objects.
         The returned list contains a separate element for each row of the pcode listing.
        @param program
        @param pcodeOps
        @return pcode listing as a two-dimensional list of AttributedString objects
        """
        ...

    @overload
    def toString(self) -> unicode: ...

    @overload
    def toString(self, program: ghidra.program.model.listing.Program, pcodeOpTemplates: List[ghidra.app.plugin.processors.sleigh.template.OpTpl]) -> unicode:
        """
        Format an array of pcode OpTpl objects as a multi-line String
        @param program
        @param pcodeOpTemplates
        @return pcode listing as a String
        """
        ...

    @overload
    def toString(self, program: ghidra.program.model.listing.Program, pcodeOps: List[ghidra.program.model.pcode.PcodeOp]) -> unicode:
        """
        Format an array of PcodeOp objects as a multi-line String
        @return pcode listing as a String
        """
        ...

    @overload
    def wait(self) -> None: ...

    @overload
    def wait(self, __a0: long) -> None: ...

    @overload
    def wait(self, __a0: long, __a1: int) -> None: ...

    @property
    def fontMetrics(self) -> None: ...  # No getter available.

    @fontMetrics.setter
    def fontMetrics(self, value: java.awt.FontMetrics) -> None: ...
