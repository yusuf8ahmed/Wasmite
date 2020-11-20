<p align="center">
  <img src="images/logo.svg"/>
</p> 

### What is the Wasmite project
As Wasm is the future is the future of the web. I decide to create Wasmite a python package for unit-testing your wasm or wat code. Wasmite is based on standard library package **unittest** and its documentation can be found here: [documentation for unittest](https://docs.python.org/3/library/unittest.html).

Wasmite looks for tests in python files whose names start with test_\*.py and runs every test_\* function it discovers. The testing folder has more examples.

Here is a simple example of :
```python
#in testing/test_wasm.py
import wasmite
from wasmite import types, result
from wasmite import I32, I64

# create a Test class the inherits wasmite.TestWasm
class Test(wasmite.TestWasm):
    # create a variable the hold all the functions from a specific wasm file.
    exports = wasmite.wasm_module("test.wasm")
    # create any amount of function that test you codes functionality
    def test_add(self):
        # test the add function in test.wasm
        result = self.exports.add(1,2)
        self.assertEqual(result, 3) 
        
    def test_sub(self):
        # test the add function in test.wasm
        result = self.exports.sub(2,2) # 2-2 = 0 != -1
        self.assertEqual(result, -1) 

    def test_args_add(self):
        # check that the param types of the function add is I32, I32
        add_function = self.exports.add
        self.assertTypes(add_function, types(I32, I32))
        
    def test_result_add(self):
      # check that the return types of the function add is I32
        add_function = self.exports.add
        self.assertResult(add_function, result(I32))
```
Then you can then run this test like so:
```bash
# make sure you are in /testing

$ python -m unittest test_wasm.py

.F
======================================================================
FAIL: test_sub (test_wasm.Test)
----------------------------------------------------------------------
Traceback (most recent call last):
  File "/.../Wasmite/testing/test_wasm.py", line 14, in test_sub
    self.assertEqual(result, -1)
AssertionError: 0 != -1

----------------------------------------------------------------------
Ran 2 tests in 0.001s

FAILED (failures=1)
```

**This project was formerly extension of my Rust/Python Web framework Wasp and some section of the code my refer to it's earlier name Native** 