import java.lang


class DWARFExpressionResult(object):
    """
    The result of executing a DWARFExpression with a DWARFExpressionEvaluator.

     Currently only holds the stack results, but future improvements should
     migrate result values (ie. stuff like DWARFExpressionEvaluator#isDeref())
     from DWARFExpressionEvaluator to here.
    """





    def __init__(self, stack: java.util.ArrayDeque): ...



    def equals(self, __a0: object) -> bool: ...

    def getClass(self) -> java.lang.Class: ...

    def hashCode(self) -> int: ...

    def notify(self) -> None: ...

    def notifyAll(self) -> None: ...

    def pop(self) -> long: ...

    def toString(self) -> unicode: ...

    @overload
    def wait(self) -> None: ...

    @overload
    def wait(self, __a0: long) -> None: ...

    @overload
    def wait(self, __a0: long, __a1: int) -> None: ...
