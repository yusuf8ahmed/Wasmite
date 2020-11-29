<p align="center">
  <img src="images/logo.svg"/>
</p> 

### What is the Wasmite project
As WebAssembly is the future of the web. I decide to create Wasmite a python package for unit-testing your wasm or wat code. Wasmite is based on **[wasmer](https://wasmerio.github.io/wasmer-python/api/wasmer/)** and the python standard library package **[unittest](https://docs.python.org/3/library/unittest.html)**. Documentation for can be found here: [documentation for unittest](https://docs.python.org/3/library/unittest.html) and [documentation for wasmer](https://wasmerio.github.io/wasmer-python/api/wasmer/)

**This project was formerly an extension of my Rust/Python Web framework Wasp and some section of the code may refer to it's earlier name Native** 

Wasmite looks for tests in python files whose names start with test_\*.py and runs every test_\* function it discovers. The testing folder has more examples.

### Installation

This project requires python 3 and doesn't support 3.9
```bash
pip install wasmite
```

### project goals:

- [x] import wasm or wat module successfully
- [x] access functions within module 
- [x] type checking of parameters and the result of functions
- [ ] allow WebAssembly to import and use 
    - Python functions
    - Global Instances
    - Memory Instances
- [ ] release to **PyPi** for public to use
- [ ] more complex examples in testing folder
- [ ] receive community on how to improve


Here is a simple example of :
```python
#in testing/test_wasm.py
import wasmite
from wasmite import types, result
from wasmite import I32, I64

# create a Test class the inherits wasmite.TestWasm
class Test(wasmite.TestWasm):
    # create a variable the hold all the module from a specific wasm file.
    exports = wasmite.wasm_module("test.wasm")
    # create any amount of function that test you functionality
    def test_add(self):
        # test the "add" function in test.wasm
        result = self.exports.add(1,2)
        self.assertEqual(result, 3) 
        
    def test_sub(self):
        # test the "sub" function in test.wasm
        result = self.exports.sub(2,2) # 2-2 = 0 == -1 => False
        self.assertEqual(result, -1)

    def test_sub_notequal(self):
        # test the "sub" function in test.wasm using assertNotEqual
        result = self.exports.sub(5,2) # 5-2 = 3 != -1 => True
        self.assertNotEqual(result, -1)

    def test_args_add(self):
        # check that the param types of the function "add" is I32, I32
        add_function = self.exports.add
        self.assertTypes(add_function, types(I32, I32))

    def test_result_add(self):
        # check that the return types of the function "add" is I32
        add_function = self.exports.add
        self.assertResult(add_function, result(I32))
        
if __name__ == "__main__":
    wasmite.main()
```
Then you can then run this test like so:
```bash
# make sure you are in /testing

$ python test_wasm.py

test_add (__main__.Test) ... ok
test_args_add (__main__.Test) ... ok
test_result_add (__main__.Test) ... ok
test_sub (__main__.Test) ... FAIL
test_sub_notequal (__main__.Test) ... ok

======================================================================
FAIL: test_sub (__main__.Test)
----------------------------------------------------------------------
Traceback (most recent call last):
  File "test_wasm.py", line 18, in test_sub
    self.assertEqual(result, -1)
AssertionError: 0 != -1

----------------------------------------------------------------------
Ran 5 tests in 0.001s

FAILED (failures=1)
```

