from wasmer import engine, Store, Module, Instance
from wasmer import wat2wasm, wasm2wat, Type, ImportObject
from wasmer import Function, Global, Memory, Table
from wasmer import FunctionType, GlobalType
from wasmer_compiler_cranelift import Compiler
# cranelift was chosen as it is has fast compilation times and fast execution times
import unittest
import loguru
import pathlib

I32 = Type.I32
I64 = Type.I64
F32 = Type.F32
F64 = Type.F64
V128 = Type.V128
EXTERN_REF = Type.EXTERN_REF
FUNC_REF = Type.FUNC_REF

types = lambda *types: list(types)
result = lambda *result: list(result)

def main():
    unittest.main(verbosity=2)

def load_bytes_module(store, wasm_bytes, import_object=None):
    module = Module(store, wasm_bytes)
    instance = Instance(module)
    return instance.exports

def wat_module(path, import_object=None):
    store = Store
    wasm_bytes = wat2wasm(open(path, 'r').read())
    exported = load_bytes_module(store, wasm_bytes)
    return exported

def wasm_module(path, import_object=None):
    store = Store(engine.JIT(Compiler))
    wasm_bytes = open(path, 'rb').read()
    exported = load_bytes_module(store, wasm_bytes)
    return exported

class WasmiteCase(unittest.TestCase):
    """Wasmite Extension of unittest.TestCase"""
    def assertTypes(self, func, types):
        assert func.type.params == types
    
    def assertResult(self, func, result):
        assert func.type.results == result

class TestWasm(WasmiteCase):
    pass

class TestWat(WasmiteCase):
    pass