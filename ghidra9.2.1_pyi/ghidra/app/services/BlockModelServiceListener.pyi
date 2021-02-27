import java.lang


class BlockModelServiceListener(object):
    """
    Listener interface for BlockModelService.
    """









    def equals(self, __a0: object) -> bool: ...

    def getClass(self) -> java.lang.Class: ...

    def hashCode(self) -> int: ...

    def modelAdded(self, modeName: unicode, modelType: int) -> None:
        """
        Provides notification when a model is added.
        @param modeName name of the block model that was added
        @param modelType type of block model that was added
        """
        ...

    def modelRemoved(self, modeName: unicode, modelType: int) -> None:
        """
        Provides notifiication when a model is removed.
        @param modeName name of the block model that was removed
        @param modelType type of block model that was removed
        """
        ...

    def notify(self) -> None: ...

    def notifyAll(self) -> None: ...

    def toString(self) -> unicode: ...

    @overload
    def wait(self) -> None: ...

    @overload
    def wait(self, __a0: long) -> None: ...

    @overload
    def wait(self, __a0: long, __a1: int) -> None: ...
