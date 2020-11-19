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
        result = self.exports.sub(2,2)
        self.assertEqual(result, -1)
        
        
        