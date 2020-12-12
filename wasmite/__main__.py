from wasmer import engine, Store, Instance
from wasmer import wat2wasm, wasm2wat, ImportObject
from wasmer import Function, Global, Memory, Table
from wasmer import Value
from wasmer import Type as WType, Module as WModule,
from wasmer_compiler_cranelift import Compiler
from typing import NamedTuple, List, Type
from .extension import CheckFunction, get_types
# cranelift was chosen as it is has fast compilation times and fast execution times
import unittest
import loguru
import pathlib
import traceback

class Module:
    IMPORT_FLAG = False
    
    def __init__(self, path, wat=False):
        self.path = path
        if wat:
            self._import_wat_module()
        else:
            self._import_module()

    def _import_wat_module(self):
        """ import a WAT module """
        self.store = Store()
        self.wasm_bytes = wat2wasm(open(self.path, 'r').read())
        
    def _import_module(self):
        """ import a WASM module """
        self.store = Store(engine.JIT(Compiler))
        self.wasm_bytes = open(self.path, 'rb').read()    
        
    def register(self, name, namespace):
        """ register and import python functions into the module """
        self.import_object = ImportObject()
        self.import_object.register(
            name,
            namespace
        )
        self._IMPORT_FLAG = True
        
    def start(self):
        """ start module and export functions """
        # WAModule is 'Module' from the wasmer library
        module = WModule(self.store, self.wasm_bytes)
        if self._IMPORT_FLAG:
            instance = Instance(module, self.import_object)
        else:
            instance = Instance(module)
        self.exports = instance.exports
        
class FuncType(NamedTuple):
    """ FuncType: holds the param types and results type. """
    params: List[Type]
    result: List[Type]

class _WasmiteCase(unittest.TestCase, CheckFunction):
    """Wasmite Extension of unittest.TestCase"""
    
    def checkFunctionTypes(self, func, func_type):
        """ Check the static types of the param(s) and return of WebAssembly Function """
        self._assertFuncType(func.type.params, func_type.params, "params")
        self._assertFuncType(func.type.results, func_type.result, "return")

class WasmiteCase(_WasmiteCase):
    pass

def main():
    unittest.main(verbosity=2)