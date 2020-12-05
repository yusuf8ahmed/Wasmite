from wasmer import engine, Store, Module, Instance
from wasmer import wat2wasm, wasm2wat, ImportObject
from wasmer import Type as WType
from wasmer import Function, Global, Memory, Table
from wasmer import FunctionType, GlobalType
from wasmer_compiler_cranelift import Compiler
from typing import NamedTuple, List, Type
from .func_type import CheckFunction, get_types
# cranelift was chosen as it is has fastest compilation times and fast execution times
import unittest
import loguru
import pathlib
import traceback

def main():
    unittest.main(verbosity=2)

def load_bytes_module(store, wasm_bytes):
    module = Module(store, wasm_bytes)
    instance = Instance(module)
    return instance.exports

def wat_module(path):
    store = Store
    wasm_bytes = wat2wasm(open(path, 'r').read())
    exported = load_bytes_module(store, wasm_bytes)
    return exported

def wasm_module(path):    
    store = Store(engine.JIT(Compiler))
    wasm_bytes = open(path, 'rb').read()
    exported = load_bytes_module(store, wasm_bytes)
    return exported

class FuncType(NamedTuple):
    """ FuncType: holds the param types and results type. """
    params: List[Type]
    result: List[Type]

class WasmiteCase(unittest.TestCase, CheckFunction):
    """Wasmite Extension of unittest.TestCase"""
    
    def checkFunctionTypes(self, func, func_type):
        """ Check the static types of the param(s) and return of WebAssembly Function """
        self._assertFuncType(func.type.params, func_type.params, "params")
        self._assertFuncType(func.type.results, func_type.result, "return")

class TestWasm(WasmiteCase):
    pass

class TestWat(WasmiteCase):
    pass