from wasmer import Type

I32 = Type.I32
I64 = Type.I64
F32 = Type.F32
F64 = Type.F64
V128 = Type.V128
EXTERN_REF = Type.EXTERN_REF
FUNC_REF = Type.FUNC_REF

get_types = lambda x: list(map(lambda x: Type(x).name, x))

class CheckFunction:
    def _baseAssertFuncType(self, first, second, msg=None):
        """ The default assertEqual implementation, not type specific. """
        if not first == second:
            msg = self._formatMessage(msg, "Types Differ")
            raise self.failureException(msg)   
     
    def assertSequenceEqual(self, seq1, seq2, msg=None, seq_type=None):
        """ The implementation of assertEqual. """
        if not (seq1 == seq2):
            msg = self._formatMessage(msg, "Types Differ")
            raise self.failureException(msg)   
               
    def _getAssertFuncType(self, first, second):
        if type(first) is type(second):
            asserter = self._type_equality_funcs.get(type(first))
            if asserter is not None:
                if isinstance(asserter, str):
                    asserter = getattr(self, asserter)
                return asserter
        return self._baseAssertFuncType

    def _assertFuncType(self, first, second, msg):
        first, second = get_types(first), get_types(second)
        assertion_func = self._getAssertFuncType(first, second)
        msg = """\n\nTypes Differ (on {}):\nWebAssembly Function: {}\nUnittest FunctionTypes: {}""".format(msg, first, second)
        assertion_func(first, second, msg=msg)