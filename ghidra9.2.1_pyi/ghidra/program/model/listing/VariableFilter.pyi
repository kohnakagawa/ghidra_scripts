import ghidra.program.model.listing
import java.lang


class VariableFilter(object):
    COMPOUND_STACK_VARIABLE_FILTER: ghidra.program.model.listing.VariableFilter = ghidra.program.model.listing.VariableFilter$CompoundStackVariableFilter@626f2c30
    LOCAL_VARIABLE_FILTER: ghidra.program.model.listing.VariableFilter = ghidra.program.model.listing.VariableFilter$LocalVariableFilter@26ae3cc7
    MEMORY_VARIABLE_FILTER: ghidra.program.model.listing.VariableFilter = ghidra.program.model.listing.VariableFilter$MemoryVariableFilter@59db9b1c
    NONAUTO_PARAMETER_FILTER: ghidra.program.model.listing.VariableFilter = ghidra.program.model.listing.VariableFilter$ParameterFilter@314dd066
    PARAMETER_FILTER: ghidra.program.model.listing.VariableFilter = ghidra.program.model.listing.VariableFilter$ParameterFilter@1c378e69
    REGISTER_VARIABLE_FILTER: ghidra.program.model.listing.VariableFilter = ghidra.program.model.listing.VariableFilter$RegisterVariableFilter@7d6d7f3a
    STACK_VARIABLE_FILTER: ghidra.program.model.listing.VariableFilter = ghidra.program.model.listing.VariableFilter$StackVariableFilter@50086097
    UNIQUE_VARIABLE_FILTER: ghidra.program.model.listing.VariableFilter = ghidra.program.model.listing.VariableFilter$UniqueVariableFilter@669ce389




    class LocalVariableFilter(object, ghidra.program.model.listing.VariableFilter):
        COMPOUND_STACK_VARIABLE_FILTER: ghidra.program.model.listing.VariableFilter = ghidra.program.model.listing.VariableFilter$CompoundStackVariableFilter@626f2c30
        LOCAL_VARIABLE_FILTER: ghidra.program.model.listing.VariableFilter = ghidra.program.model.listing.VariableFilter$LocalVariableFilter@26ae3cc7
        MEMORY_VARIABLE_FILTER: ghidra.program.model.listing.VariableFilter = ghidra.program.model.listing.VariableFilter$MemoryVariableFilter@59db9b1c
        NONAUTO_PARAMETER_FILTER: ghidra.program.model.listing.VariableFilter = ghidra.program.model.listing.VariableFilter$ParameterFilter@314dd066
        PARAMETER_FILTER: ghidra.program.model.listing.VariableFilter = ghidra.program.model.listing.VariableFilter$ParameterFilter@1c378e69
        REGISTER_VARIABLE_FILTER: ghidra.program.model.listing.VariableFilter = ghidra.program.model.listing.VariableFilter$RegisterVariableFilter@7d6d7f3a
        STACK_VARIABLE_FILTER: ghidra.program.model.listing.VariableFilter = ghidra.program.model.listing.VariableFilter$StackVariableFilter@50086097
        UNIQUE_VARIABLE_FILTER: ghidra.program.model.listing.VariableFilter = ghidra.program.model.listing.VariableFilter$UniqueVariableFilter@669ce389



        def __init__(self): ...



        def equals(self, __a0: object) -> bool: ...

        def getClass(self) -> java.lang.Class: ...

        def hashCode(self) -> int: ...

        def matches(self, __a0: ghidra.program.model.listing.Variable) -> bool: ...

        def notify(self) -> None: ...

        def notifyAll(self) -> None: ...

        def toString(self) -> unicode: ...

        @overload
        def wait(self) -> None: ...

        @overload
        def wait(self, __a0: long) -> None: ...

        @overload
        def wait(self, __a0: long, __a1: int) -> None: ...






    class ParameterFilter(object, ghidra.program.model.listing.VariableFilter):
        COMPOUND_STACK_VARIABLE_FILTER: ghidra.program.model.listing.VariableFilter = ghidra.program.model.listing.VariableFilter$CompoundStackVariableFilter@626f2c30
        LOCAL_VARIABLE_FILTER: ghidra.program.model.listing.VariableFilter = ghidra.program.model.listing.VariableFilter$LocalVariableFilter@26ae3cc7
        MEMORY_VARIABLE_FILTER: ghidra.program.model.listing.VariableFilter = ghidra.program.model.listing.VariableFilter$MemoryVariableFilter@59db9b1c
        NONAUTO_PARAMETER_FILTER: ghidra.program.model.listing.VariableFilter = ghidra.program.model.listing.VariableFilter$ParameterFilter@314dd066
        PARAMETER_FILTER: ghidra.program.model.listing.VariableFilter = ghidra.program.model.listing.VariableFilter$ParameterFilter@1c378e69
        REGISTER_VARIABLE_FILTER: ghidra.program.model.listing.VariableFilter = ghidra.program.model.listing.VariableFilter$RegisterVariableFilter@7d6d7f3a
        STACK_VARIABLE_FILTER: ghidra.program.model.listing.VariableFilter = ghidra.program.model.listing.VariableFilter$StackVariableFilter@50086097
        UNIQUE_VARIABLE_FILTER: ghidra.program.model.listing.VariableFilter = ghidra.program.model.listing.VariableFilter$UniqueVariableFilter@669ce389



        def __init__(self, __a0: bool): ...



        def equals(self, __a0: object) -> bool: ...

        def getClass(self) -> java.lang.Class: ...

        def hashCode(self) -> int: ...

        def matches(self, __a0: ghidra.program.model.listing.Variable) -> bool: ...

        def notify(self) -> None: ...

        def notifyAll(self) -> None: ...

        def toString(self) -> unicode: ...

        @overload
        def wait(self) -> None: ...

        @overload
        def wait(self, __a0: long) -> None: ...

        @overload
        def wait(self, __a0: long, __a1: int) -> None: ...






    class CompoundStackVariableFilter(object, ghidra.program.model.listing.VariableFilter):
        COMPOUND_STACK_VARIABLE_FILTER: ghidra.program.model.listing.VariableFilter = ghidra.program.model.listing.VariableFilter$CompoundStackVariableFilter@626f2c30
        LOCAL_VARIABLE_FILTER: ghidra.program.model.listing.VariableFilter = ghidra.program.model.listing.VariableFilter$LocalVariableFilter@26ae3cc7
        MEMORY_VARIABLE_FILTER: ghidra.program.model.listing.VariableFilter = ghidra.program.model.listing.VariableFilter$MemoryVariableFilter@59db9b1c
        NONAUTO_PARAMETER_FILTER: ghidra.program.model.listing.VariableFilter = ghidra.program.model.listing.VariableFilter$ParameterFilter@314dd066
        PARAMETER_FILTER: ghidra.program.model.listing.VariableFilter = ghidra.program.model.listing.VariableFilter$ParameterFilter@1c378e69
        REGISTER_VARIABLE_FILTER: ghidra.program.model.listing.VariableFilter = ghidra.program.model.listing.VariableFilter$RegisterVariableFilter@7d6d7f3a
        STACK_VARIABLE_FILTER: ghidra.program.model.listing.VariableFilter = ghidra.program.model.listing.VariableFilter$StackVariableFilter@50086097
        UNIQUE_VARIABLE_FILTER: ghidra.program.model.listing.VariableFilter = ghidra.program.model.listing.VariableFilter$UniqueVariableFilter@669ce389



        def __init__(self): ...



        def equals(self, __a0: object) -> bool: ...

        def getClass(self) -> java.lang.Class: ...

        def hashCode(self) -> int: ...

        def matches(self, __a0: ghidra.program.model.listing.Variable) -> bool: ...

        def notify(self) -> None: ...

        def notifyAll(self) -> None: ...

        def toString(self) -> unicode: ...

        @overload
        def wait(self) -> None: ...

        @overload
        def wait(self, __a0: long) -> None: ...

        @overload
        def wait(self, __a0: long, __a1: int) -> None: ...






    class StackVariableFilter(object, ghidra.program.model.listing.VariableFilter):
        COMPOUND_STACK_VARIABLE_FILTER: ghidra.program.model.listing.VariableFilter = ghidra.program.model.listing.VariableFilter$CompoundStackVariableFilter@626f2c30
        LOCAL_VARIABLE_FILTER: ghidra.program.model.listing.VariableFilter = ghidra.program.model.listing.VariableFilter$LocalVariableFilter@26ae3cc7
        MEMORY_VARIABLE_FILTER: ghidra.program.model.listing.VariableFilter = ghidra.program.model.listing.VariableFilter$MemoryVariableFilter@59db9b1c
        NONAUTO_PARAMETER_FILTER: ghidra.program.model.listing.VariableFilter = ghidra.program.model.listing.VariableFilter$ParameterFilter@314dd066
        PARAMETER_FILTER: ghidra.program.model.listing.VariableFilter = ghidra.program.model.listing.VariableFilter$ParameterFilter@1c378e69
        REGISTER_VARIABLE_FILTER: ghidra.program.model.listing.VariableFilter = ghidra.program.model.listing.VariableFilter$RegisterVariableFilter@7d6d7f3a
        STACK_VARIABLE_FILTER: ghidra.program.model.listing.VariableFilter = ghidra.program.model.listing.VariableFilter$StackVariableFilter@50086097
        UNIQUE_VARIABLE_FILTER: ghidra.program.model.listing.VariableFilter = ghidra.program.model.listing.VariableFilter$UniqueVariableFilter@669ce389



        def __init__(self): ...



        def equals(self, __a0: object) -> bool: ...

        def getClass(self) -> java.lang.Class: ...

        def hashCode(self) -> int: ...

        def matches(self, __a0: ghidra.program.model.listing.Variable) -> bool: ...

        def notify(self) -> None: ...

        def notifyAll(self) -> None: ...

        def toString(self) -> unicode: ...

        @overload
        def wait(self) -> None: ...

        @overload
        def wait(self, __a0: long) -> None: ...

        @overload
        def wait(self, __a0: long, __a1: int) -> None: ...






    class UniqueVariableFilter(object, ghidra.program.model.listing.VariableFilter):
        COMPOUND_STACK_VARIABLE_FILTER: ghidra.program.model.listing.VariableFilter = ghidra.program.model.listing.VariableFilter$CompoundStackVariableFilter@626f2c30
        LOCAL_VARIABLE_FILTER: ghidra.program.model.listing.VariableFilter = ghidra.program.model.listing.VariableFilter$LocalVariableFilter@26ae3cc7
        MEMORY_VARIABLE_FILTER: ghidra.program.model.listing.VariableFilter = ghidra.program.model.listing.VariableFilter$MemoryVariableFilter@59db9b1c
        NONAUTO_PARAMETER_FILTER: ghidra.program.model.listing.VariableFilter = ghidra.program.model.listing.VariableFilter$ParameterFilter@314dd066
        PARAMETER_FILTER: ghidra.program.model.listing.VariableFilter = ghidra.program.model.listing.VariableFilter$ParameterFilter@1c378e69
        REGISTER_VARIABLE_FILTER: ghidra.program.model.listing.VariableFilter = ghidra.program.model.listing.VariableFilter$RegisterVariableFilter@7d6d7f3a
        STACK_VARIABLE_FILTER: ghidra.program.model.listing.VariableFilter = ghidra.program.model.listing.VariableFilter$StackVariableFilter@50086097
        UNIQUE_VARIABLE_FILTER: ghidra.program.model.listing.VariableFilter = ghidra.program.model.listing.VariableFilter$UniqueVariableFilter@669ce389



        def __init__(self): ...



        def equals(self, __a0: object) -> bool: ...

        def getClass(self) -> java.lang.Class: ...

        def hashCode(self) -> int: ...

        def matches(self, __a0: ghidra.program.model.listing.Variable) -> bool: ...

        def notify(self) -> None: ...

        def notifyAll(self) -> None: ...

        def toString(self) -> unicode: ...

        @overload
        def wait(self) -> None: ...

        @overload
        def wait(self, __a0: long) -> None: ...

        @overload
        def wait(self, __a0: long, __a1: int) -> None: ...






    class MemoryVariableFilter(object, ghidra.program.model.listing.VariableFilter):
        COMPOUND_STACK_VARIABLE_FILTER: ghidra.program.model.listing.VariableFilter = ghidra.program.model.listing.VariableFilter$CompoundStackVariableFilter@626f2c30
        LOCAL_VARIABLE_FILTER: ghidra.program.model.listing.VariableFilter = ghidra.program.model.listing.VariableFilter$LocalVariableFilter@26ae3cc7
        MEMORY_VARIABLE_FILTER: ghidra.program.model.listing.VariableFilter = ghidra.program.model.listing.VariableFilter$MemoryVariableFilter@59db9b1c
        NONAUTO_PARAMETER_FILTER: ghidra.program.model.listing.VariableFilter = ghidra.program.model.listing.VariableFilter$ParameterFilter@314dd066
        PARAMETER_FILTER: ghidra.program.model.listing.VariableFilter = ghidra.program.model.listing.VariableFilter$ParameterFilter@1c378e69
        REGISTER_VARIABLE_FILTER: ghidra.program.model.listing.VariableFilter = ghidra.program.model.listing.VariableFilter$RegisterVariableFilter@7d6d7f3a
        STACK_VARIABLE_FILTER: ghidra.program.model.listing.VariableFilter = ghidra.program.model.listing.VariableFilter$StackVariableFilter@50086097
        UNIQUE_VARIABLE_FILTER: ghidra.program.model.listing.VariableFilter = ghidra.program.model.listing.VariableFilter$UniqueVariableFilter@669ce389



        def __init__(self): ...



        def equals(self, __a0: object) -> bool: ...

        def getClass(self) -> java.lang.Class: ...

        def hashCode(self) -> int: ...

        def matches(self, __a0: ghidra.program.model.listing.Variable) -> bool: ...

        def notify(self) -> None: ...

        def notifyAll(self) -> None: ...

        def toString(self) -> unicode: ...

        @overload
        def wait(self) -> None: ...

        @overload
        def wait(self, __a0: long) -> None: ...

        @overload
        def wait(self, __a0: long, __a1: int) -> None: ...






    class RegisterVariableFilter(object, ghidra.program.model.listing.VariableFilter):
        COMPOUND_STACK_VARIABLE_FILTER: ghidra.program.model.listing.VariableFilter = ghidra.program.model.listing.VariableFilter$CompoundStackVariableFilter@626f2c30
        LOCAL_VARIABLE_FILTER: ghidra.program.model.listing.VariableFilter = ghidra.program.model.listing.VariableFilter$LocalVariableFilter@26ae3cc7
        MEMORY_VARIABLE_FILTER: ghidra.program.model.listing.VariableFilter = ghidra.program.model.listing.VariableFilter$MemoryVariableFilter@59db9b1c
        NONAUTO_PARAMETER_FILTER: ghidra.program.model.listing.VariableFilter = ghidra.program.model.listing.VariableFilter$ParameterFilter@314dd066
        PARAMETER_FILTER: ghidra.program.model.listing.VariableFilter = ghidra.program.model.listing.VariableFilter$ParameterFilter@1c378e69
        REGISTER_VARIABLE_FILTER: ghidra.program.model.listing.VariableFilter = ghidra.program.model.listing.VariableFilter$RegisterVariableFilter@7d6d7f3a
        STACK_VARIABLE_FILTER: ghidra.program.model.listing.VariableFilter = ghidra.program.model.listing.VariableFilter$StackVariableFilter@50086097
        UNIQUE_VARIABLE_FILTER: ghidra.program.model.listing.VariableFilter = ghidra.program.model.listing.VariableFilter$UniqueVariableFilter@669ce389



        def __init__(self): ...



        def equals(self, __a0: object) -> bool: ...

        def getClass(self) -> java.lang.Class: ...

        def hashCode(self) -> int: ...

        def matches(self, __a0: ghidra.program.model.listing.Variable) -> bool: ...

        def notify(self) -> None: ...

        def notifyAll(self) -> None: ...

        def toString(self) -> unicode: ...

        @overload
        def wait(self) -> None: ...

        @overload
        def wait(self, __a0: long) -> None: ...

        @overload
        def wait(self, __a0: long, __a1: int) -> None: ...







    def equals(self, __a0: object) -> bool: ...

    def getClass(self) -> java.lang.Class: ...

    def hashCode(self) -> int: ...

    def matches(self, variable: ghidra.program.model.listing.Variable) -> bool:
        """
        Determine if the specified variable matches this filter criteria
        @param variable
        @return true if variable satisfies the criteria of this filter
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
