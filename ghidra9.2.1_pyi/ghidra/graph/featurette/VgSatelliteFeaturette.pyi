import docking
import ghidra.framework.options
import ghidra.graph
import ghidra.graph.featurette
import java.lang


class VgSatelliteFeaturette(object, ghidra.graph.featurette.VisualGraphFeaturette):
    """
    A sub-feature that provides a satellite viewer to VisualGraphComponentProviders

     Note: this class installs actions to manipulate the satellite view.  For these to be
     correctly enabled, you must produce VgActionContext objects in your
     VisualGraphComponentProvider#getActionContext(MouseEvent) method.  Specifically,
     the context returned must be a type of VgActionContext, with the
     VgActionContext#shouldShowSatelliteActions() returning true.
    """





    def __init__(self): ...



    def equals(self, __a0: object) -> bool: ...

    def getClass(self) -> java.lang.Class: ...

    def getSatelliteProvider(self) -> docking.ComponentProvider: ...

    def hashCode(self) -> int: ...

    def init(self, provider: ghidra.graph.VisualGraphComponentProvider) -> None: ...

    def notify(self) -> None: ...

    def notifyAll(self) -> None: ...

    def providerClosed(self, provider: ghidra.graph.VisualGraphComponentProvider) -> None: ...

    def providerOpened(self, provider: ghidra.graph.VisualGraphComponentProvider) -> None: ...

    def readConfigState(self, saveState: ghidra.framework.options.SaveState) -> None: ...

    def remove(self) -> None: ...

    def toString(self) -> unicode: ...

    @overload
    def wait(self) -> None: ...

    @overload
    def wait(self, __a0: long) -> None: ...

    @overload
    def wait(self, __a0: long, __a1: int) -> None: ...

    def writeConfigState(self, saveState: ghidra.framework.options.SaveState) -> None: ...

    @property
    def satelliteProvider(self) -> docking.ComponentProvider: ...
