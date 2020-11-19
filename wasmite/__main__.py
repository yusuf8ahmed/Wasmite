from wasmer import engine, Store, Module, Instance
from wasmer import wat2wasm, wasm2wat, Type 
from wasmer import Function, Global, Memory, Table
from wasmer import FunctionType, GlobalType
from wasmer_compiler_cranelift import Compiler
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

def wat_module(path):
    wat_content = open(path, 'r').read()
    wasm_bytes = wat2wasm(wat_content)
    instance = Instance(Module(Store(), wasm_bytes))
    exported = instance.exports
    return exported

def wasm_module(path):
    store = Store(engine.JIT(Compiler))
    module = Module(store, open(path, 'rb').read())
    instance = Instance(module)
    exported = instance.exports
    return exported

class WasmiteCase(unittest.TestCase):
    """Wasmite Extension of unittest.TestCase"""
    pass

class TestWasm(WasmiteCase):
    pass

class TestWat(WasmiteCase):
    pass
    
    