<p align="center">
  <img src="images/logo.svg"/>
</p> 

### What is the Wasmite project
Welcome! Wasmite is a python package for unit-testing your wasm or wat code. Wasmite is based on standard library package **unittest** and its documentation can be found here: [documentation for unittest](https://docs.python.org/3/library/unittest.html).

wasmite looks for tests in python files whose names start with test_* and runs every test_* function it discovers. The testing folder has more examples.

Here is a simple example of :
```python
#in testing/test_wasm.py
import wasmite

# create a Test class the inherits wasmite.TestWasm
class Test(wasmite.TestWasm):
    # create a variable the hold all the functions from a specific wasm file.
    exports = wasmite.wasm_module("test.wasm")
    # create any amount of function that test you codes functionality
    def test_add(self):
        result = self.exports.add(1,2)
        self.assertEqual(result, 3) 
        
    def test_sub(self):
        result = self.exports.sub(2,2) # 2-2 = 0 != -1
        self.assertEqual(result, -1) 
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