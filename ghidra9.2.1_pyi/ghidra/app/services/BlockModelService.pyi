from typing import List
import ghidra.app.services
import ghidra.program.model.block
import ghidra.program.model.listing
import java.lang


class BlockModelService(object):
    """
    Service for providing block models.
    """

    BASIC_MODEL: int = 1
    DEFAULT_BLOCK_MODEL_NAME: unicode = u'Simple Block'
    DEFAULT_SUBROUTINE_MODEL_NAME: unicode = u'Multiple Entry'
    ISOLATED_ENTRY_SUBROUTINE_MODEL_NAME: unicode = u'Isolated Entry'
    MULTI_ENTRY_SUBROUTINE_MODEL_NAME: unicode = u'Multiple Entry'
    OVERLAPPED_SUBROUTINE_MODEL_NAME: unicode = u'Overlapped Code'
    PARTITIONED_SUBROUTINE_MODEL_NAME: unicode = u'Partitioned Code'
    SIMPLE_BLOCK_MODEL_NAME: unicode = u'Simple Block'
    SUBROUTINE_MODEL: int = 2







    def addListener(self, listener: ghidra.app.services.BlockModelServiceListener) -> None:
        """
        Add service listener.
        @param listener listener to add
        """
        ...

    def equals(self, __a0: object) -> bool: ...

    @overload
    def getActiveBlockModel(self) -> ghidra.program.model.block.CodeBlockModel:
        """
        Get new instance of the active Basic Block model for the current program.
        @return new Basic Block model instance or null if program is not open.
        @deprecated use getActiveBlockModel(Program) instead
        """
        ...

    @overload
    def getActiveBlockModel(self, includeExternals: bool) -> ghidra.program.model.block.CodeBlockModel:
        """
        Get new instance of the active Basic Block model for the current program.
        @param includeExternals externals are included if true
        @return new Basic Block model instance or null if program is not open.
        @deprecated use getActiveBlockModel(Program, boolean) instead
        """
        ...

    @overload
    def getActiveBlockModel(self, program: ghidra.program.model.listing.Program) -> ghidra.program.model.block.CodeBlockModel:
        """
        Get new instance of the active Basic Block model.
        @param program program to associate with the block model
        @return new Basic Block model instance or null if program is null
        """
        ...

    @overload
    def getActiveBlockModel(self, program: ghidra.program.model.listing.Program, includeExternals: bool) -> ghidra.program.model.block.CodeBlockModel:
        """
        Get new instance of the active Basic Block model.
        @param program program to associate with the block model
        @param includeExternals externals are included if true
        @return new Basic Block model instance or null if program is null
        """
        ...

    def getActiveBlockModelName(self) -> unicode:
        """
        Get the name of the active Basic Block model.
        @return active block model name
        """
        ...

    @overload
    def getActiveSubroutineModel(self) -> ghidra.program.model.block.CodeBlockModel:
        """
        Get new instance of the active Subroutine Block model for the current program.
        @return new Subroutine Block model instance or null if program is not open
        @deprecated use getActiveSubroutineModel(Program) instead
        """
        ...

    @overload
    def getActiveSubroutineModel(self, includeExternals: bool) -> ghidra.program.model.block.CodeBlockModel:
        """
        Get new instance of the active Subroutine Block model for the current program.
        @param includeExternals externals are included if true
        @return new Subroutine Block model instance or null if program is not open
        @deprecated use getActiveSubroutineModel(Program) instead
        """
        ...

    @overload
    def getActiveSubroutineModel(self, program: ghidra.program.model.listing.Program) -> ghidra.program.model.block.CodeBlockModel:
        """
        Get new instance of the active Subroutine Block model.
        @param program program associated with the block model.
        @return new Subroutine Block model instance or null if program is null
        """
        ...

    @overload
    def getActiveSubroutineModel(self, program: ghidra.program.model.listing.Program, includeExternals: bool) -> ghidra.program.model.block.CodeBlockModel:
        """
        Get new instance of the active Subroutine Block model.
        @param program program associated with the block model.
        @param includeExternals externals are included if true
        @return new Subroutine Block model instance or null if program is null
        """
        ...

    def getActiveSubroutineModelName(self) -> unicode:
        """
        Get the name of the active Subroutine model.
        @return active subroutine model name
        """
        ...

    def getAvailableModelNames(self, modelType: int) -> List[unicode]:
        """
        Get list of registered block models of the specified type.
         A modelType of ANY_BLOCK will return all models registered.
         List ordering is based upon the registration order.
         It is important to recognize that the list of returned names
         could change as models are registered and unregistered.
        @param modelType type of model (ANY_MODEL, BASIC_MODEL or SUBROUTINE_MODEL)
        @return array of model names
        """
        ...

    def getClass(self) -> java.lang.Class: ...

    @overload
    def getNewModelByName(self, modelName: unicode) -> ghidra.program.model.block.CodeBlockModel:
        """
        Get new instance of the specified block model.
        @param modelName name of registered block model
        @return new model instance or null if program is not open.
        @throws NotFoundException if specified model is not registered
        @deprecated use getNewModelByName(String, Program) instead
        """
        ...

    @overload
    def getNewModelByName(self, modelName: unicode, includeExternals: bool) -> ghidra.program.model.block.CodeBlockModel:
        """
        Get new instance of the specified block model.
        @param modelName name of registered block model
        @param includeExternals externals are included if true
        @return new model instance or null if program is not open.
        @throws NotFoundException if specified model is not registered
        @deprecated use getNewModelByName(String, Program, boolean) instead
        """
        ...

    @overload
    def getNewModelByName(self, modelName: unicode, program: ghidra.program.model.listing.Program) -> ghidra.program.model.block.CodeBlockModel:
        """
        Get new instance of the specified block model.
        @param modelName name of registered block model
        @param program program associated with the model
        @return new model instance or null if program is null
        @throws NotFoundException if specified model is not registered
        """
        ...

    @overload
    def getNewModelByName(self, modelName: unicode, program: ghidra.program.model.listing.Program, includeExternals: bool) -> ghidra.program.model.block.CodeBlockModel:
        """
        Get new instance of the specified block model.
        @param modelName name of registered block model
        @param program program associated with the model
        @param includeExternals externals are included if true
        @return new model instance or null if program is null
        @throws NotFoundException if specified model is not registered
        """
        ...

    def hashCode(self) -> int: ...

    def notify(self) -> None: ...

    def notifyAll(self) -> None: ...

    def registerModel(self, modelClass: java.lang.Class, modelName: unicode) -> None:
        """
        Register a new model.
        @param modelClass code block model class.
         Subroutine models must implement the SubroutineBlockMode interface - all other models
         are assumed to be basic block models.
        @param modelName name of model
        """
        ...

    def removeListener(self, listener: ghidra.app.services.BlockModelServiceListener) -> None:
        """
        Remove service listener.
        @param listener to remove
        """
        ...

    def toString(self) -> unicode: ...

    def unregisterModel(self, modelClass: java.lang.Class) -> None:
        """
        Deregister a model.
        @param modelClass code block model class.
        """
        ...

    @overload
    def wait(self) -> None: ...

    @overload
    def wait(self, __a0: long) -> None: ...

    @overload
    def wait(self, __a0: long, __a1: int) -> None: ...

    @property
    def activeBlockModel(self) -> ghidra.program.model.block.CodeBlockModel: ...

    @property
    def activeBlockModelName(self) -> unicode: ...

    @property
    def activeSubroutineModel(self) -> ghidra.program.model.block.CodeBlockModel: ...

    @property
    def activeSubroutineModelName(self) -> unicode: ...
