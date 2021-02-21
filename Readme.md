<p align="center">
  <img src="images/logo.svg"/>
</p> 

### What is the Wasmite project
Since WebAssembly is the future of the web. I decide to create Wasmite, a python package for unit-testing your wasm or wat code. Wasmite is based on **[wasmer](https://wasmerio.github.io/wasmer-python/api/wasmer/)** and the python standard library package **[unittest](https://docs.python.org/3/library/unittest.html)**. Documentation for can be found here: [documentation for unittest](https://docs.python.org/3/library/unittest.html) and [documentation for wasmer](https://wasmerio.github.io/wasmer-python/api/wasmer/)

**This project was formerly an extension of my Rust/Python Web framework Wasp, so some section of the code may refer to it's earlier name (Native)** 

Wasmite looks for tests in python files whose names start with test_\*.py and runs every test_\* function it discovers. The testing folder has more examples.

**Having any problems or questions create a [issue](https://github.com/yusuf8ahmed/Wasmite/issues/new), i will be happy to help :)**

### Installation

This project requires python 3 and doesn't support 3.9
```bash
pip install wasmite
```

### Project Goals:

- [x] Import wasm or wat module successfully
- [x] Access functions within module 
- [x] Type checking of parameters and the result of functions
- [x] Release to **PyPi** for public to use
- [x] Allow Wasmite ... 
    - [x] Export Python functions
    - [x] Export Global Instances
    - [x] Export Memory Instances
- [x] More complex examples in testing folder
- [ ] Receive community on how to improve

Examples:

* [c++](https://github.com/yusuf8ahmed/Wasmite/tree/master/examples/c%2B%2B)
* [c](https://github.com/yusuf8ahmed/Wasmite/tree/master/examples/c)
* [wasm](https://github.com/yusuf8ahmed/Wasmite/tree/examples/testing/wasm)
* [wat](https://github.com/yusuf8ahmed/Wasmite/tree/examples/testing/wat)


```python
from wasmite import WasmiteCase, WasmModule
from wasmite import FunctionTypes, Function, Global, Value, main
from wasmite import I32

def sum(x: int, y: int) -> int:
    """ python function to be imported into WASM  """
    return x + y

class Test(WasmiteCase):
    # create a variable the hold all the functions from a specific wasm file.
    module = WasmModule("test_wasm.wasm")
    # import python function into WASM 
    # type annotations on the function is necessary 
    module.register("math", {
        "sum": Function(module.store, sum),
        "seven": Global(module.store, Value.i32(7), mutable=True)
    })
    # start up the module and return the exports (this is mandatory)
    exports = module.get_exports()
    
    def test_add(self):
        # test add function
        result = self.exports.add(1,2)
        self.assertEqual(result, 3) 
        
    def test_sub(self):
        # test the sub function
        result = self.exports.sub(2,2)
        self.assertEqual(result, 0)

    def test_args_add(self):
        # check the types for results and parameter of the function "add"
        # param is I32, I32 and result is I32
        add_function = self.exports.add
        self.assertTypes(add_function, FunctionTypes([I32, I32], [I32])) # result will fail
        
    def test_import_sum(self):
        # test the imported python function sum.
        sum_function = self.exports.addsum(5,2)
        self.assertEqual(sum_function, 7)
        
    def test_global_read(self):
        # test reading value of global
        read_seven = self.exports.read_global()
        self.assertEqual(read_seven, 7) 
        
    def test_global_write(self):
        # test writing value of global
        self.exports.write_global(5)
        read_seven = self.exports.read_global()
        self.assertEqual(read_seven, 5) 
        
# Hi don't forget to add me         
if __name__ == "__main__":
    main()
``` 
-->

Then you can then run this test like so:
```bash
# make sure you are in examples/wasm
$ python test_wasm.py

test_add (__main__.Test) ... ok
test_args_add (__main__.Test) ... ok
test_global_read (__main__.Test) ... ok
test_global_write (__main__.Test) ... ok
test_import_sum (__main__.Test) ... ok
test_sub (__main__.Test) ... ok

----------------------------------------------------------------------
Ran 6 tests in 0.001s

OK
``` 
