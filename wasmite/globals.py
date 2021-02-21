import unittest
from typing import NamedTuple, List, Type

from wasmer import Instance, ImportObject
from wasmer import Type
from loguru import logger

I32 = Type.I32
I64 = Type.I64
F32 = Type.F32
F64 = Type.F64
V128 = Type.V128
EXTERN_REF = Type.EXTERN_REF
FUNC_REF = Type.FUNC_REF

get_types = lambda x: list(map(lambda x: Type(x).name, x))


class FunctionTypes(NamedTuple):
    """ FuncType: holds the param types and results type. """

    params: List[Type]
    result: List[Type]


class BaseModule:
    IMPORT_FLAG = False
    TYPE = None

    def __init__(self, path):
        self.path = path
        self.logger = logger
        self._import_module()

    def _import_module(self):
        """ import a module: implemented in subclasses """
        raise NotImplementedError()

    def run_main(self):
        """ run main function: only implemented in wasi subclass """
        raise NotImplementedError()

    def register(self, name, namespace):
        """ register and import python functions into the module """
        if not self.TYPE == "WASI":
            self.import_object = ImportObject()
            self.import_object.register(name, namespace)
            self._IMPORT_FLAG = True

    def get_exports(self):
        """ start module and export functions """
        if self._IMPORT_FLAG:
            instance = Instance(self.module, self.import_object)
        else:
            instance = Instance(self.module)
        self.exports = instance.exports
        return instance.exports


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
        msg = """\n\nTypes Differ (on {}):\nWebAssembly Function: {}\nUnittest FunctionTypes: {}""".format(
            msg, first, second
        )
        assertion_func(first, second, msg=msg)


class WasmiteCase(unittest.TestCase, CheckFunction):
    """Wasmite Extension of unittest.TestCase"""

    def assertTypes(self, func, func_type):
        """ Check the static types of the param(s) and return of WebAssembly Function """
        self._assertFuncType(func.type.params, func_type.params, "params")
        self._assertFuncType(func.type.results, func_type.result, "return")


def main():
    unittest.main(verbosity=2)
